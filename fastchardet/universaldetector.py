######################## BEGIN LICENSE BLOCK ########################
# The Original Code is Mozilla Universal charset detector code.
#
# The Initial Developer of the Original Code is
# Netscape Communications Corporation.
# Portions created by the Initial Developer are Copyright (C) 2001
# the Initial Developer. All Rights Reserved.
#
# Contributor(s):
#   Matt Basta - slimming and efficiefying
#   Mark Pilgrim - port to Python
#   Shy Shalom - original C code
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# 
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
# 02110-1301  USA
######################### END LICENSE BLOCK #########################

import constants, sys
from latin1prober import Latin1Prober # windows-1252
from utf8prober import UTF8Prober # utf-8
import re

MINIMUM_THRESHOLD = 0.20
ePureAscii = 0
eEscAscii = 1
eHighbyte = 2

class UniversalDetector:
    def __init__(self):
        self._highBitDetector = re.compile(r'[\x80-\xFF]')
        self._escDetector = re.compile(r'(\033|~{)')
        self._mEscCharSetProber = None
        self._mCharSetProbers = []
        self.reset()

    def reset(self):
        self.result = {'encoding': None, 'confidence': 0.0}
        self.done = constants.False
        self._mStart = constants.True
        self._mGotData = constants.False
        self._mInputState = ePureAscii
        self._mLastChar = ''
        for prober in self._mCharSetProbers:
            prober.reset()

    def feed(self, aBuf):
        if isinstance(aBuf, unicode):
            self.result = {'encoding': "unicode", 'confidence': 0.0}
            self.done = constants.True
            return
        
        if self.done: return

        aLen = len(aBuf)
        if not aLen: return
        
        if not self._mGotData:
            # If the data starts with BOM, we know it is UTF
            if aBuf[:3] == '\xEF\xBB\xBF':
                # EF BB BF  UTF-8 with BOM
                self.result = {'encoding': "utf_8", 'confidence': 1.0}
            elif aBuf[:4] in ('\xFF\xFE\x00\x00',
                              '\x00\x00\xFE\xFF',
                              '\xFE\xFF\x00\x00',
                              '\x00\x00\xFF\xFE') or \
                 aBuf[:2] in ('\xFF\xFE', '\xFE\xFF'):
                self.result = {'encoding': "utf_n", 'confidence': 1.0}

        self._mGotData = constants.True
        if self.result['encoding'] and (self.result['confidence'] > 0.0):
            self.done = constants.True
            return

        if self._mInputState == ePureAscii:
            if self._highBitDetector.search(aBuf):
                self._mInputState = eHighbyte
            elif self._escDetector.search(self._mLastChar + aBuf):
                self._mInputState = eEscAscii

        self._mLastChar = aBuf[-1]

        if self._mInputState == eEscAscii:
            self.result = {'encoding': "escaped",
                           'confidence': 1.0}
            self.done = constants.True
        elif self._mInputState == eHighbyte:
            if not self._mCharSetProbers:
                self._mCharSetProbers = [UTF8Prober(), Latin1Prober()]
            for prober in self._mCharSetProbers:
                if prober.feed(aBuf) == constants.eFoundIt:
                    self.result = {'encoding': prober.get_charset_name(),
                                   'confidence': prober.get_confidence()}
                    self.done = constants.True
                    break

    def close(self):
        if self.done: return
        if not self._mGotData:
            if constants._debug:
                sys.stderr.write('no data received!\n')
            return
        self.done = constants.True
        
        if self._mInputState == ePureAscii:
            self.result = {'encoding': 'ascii', 'confidence': 1.0}
            return self.result

        if self._mInputState == eHighbyte:
            proberConfidence = None
            maxProberConfidence = 0.0
            maxProber = None
            for prober in self._mCharSetProbers:
                if not prober: continue
                proberConfidence = prober.get_confidence()
                if proberConfidence > maxProberConfidence:
                    maxProberConfidence = proberConfidence
                    maxProber = prober
            if maxProber and (maxProberConfidence > MINIMUM_THRESHOLD):
                self.result = {'encoding': maxProber.get_charset_name(),
                               'confidence': maxProber.get_confidence()}
                return self.result

        if constants._debug:
            sys.stderr.write('no probers hit minimum threshhold\n')
            for prober in self._mCharSetProbers[0].mProbers:
                if not prober: continue
                sys.stderr.write('%s confidence = %s\n' % \
                                 (prober.get_charset_name(), \
                                  prober.get_confidence()))
