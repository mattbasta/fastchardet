######################## BEGIN LICENSE BLOCK ########################
# The Original Code is mozilla.org code.
#
# The Initial Developer of the Original Code is
# Netscape Communications Corporation.
# Portions created by the Initial Developer are Copyright (C) 1998
# the Initial Developer. All Rights Reserved.
#
# Contributor(s):
#   Mark Pilgrim - port to Python
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

from constants import eStart, eError, eItsMe

# UTF-8

UTF8_cls = ( \
    1,1,1,1,1,1,1,1,  # 00 - 07  #allow 0x00 as a legal value
    1,1,1,1,1,1,0,0,  # 08 - 0f 
    1,1,1,1,1,1,1,1,  # 10 - 17 
    1,1,1,0,1,1,1,1,  # 18 - 1f 
    1,1,1,1,1,1,1,1,  # 20 - 27 
    1,1,1,1,1,1,1,1,  # 28 - 2f 
    1,1,1,1,1,1,1,1,  # 30 - 37 
    1,1,1,1,1,1,1,1,  # 38 - 3f 
    1,1,1,1,1,1,1,1,  # 40 - 47 
    1,1,1,1,1,1,1,1,  # 48 - 4f 
    1,1,1,1,1,1,1,1,  # 50 - 57 
    1,1,1,1,1,1,1,1,  # 58 - 5f 
    1,1,1,1,1,1,1,1,  # 60 - 67 
    1,1,1,1,1,1,1,1,  # 68 - 6f 
    1,1,1,1,1,1,1,1,  # 70 - 77 
    1,1,1,1,1,1,1,1,  # 78 - 7f 
    2,2,2,2,3,3,3,3,  # 80 - 87 
    4,4,4,4,4,4,4,4,  # 88 - 8f 
    4,4,4,4,4,4,4,4,  # 90 - 97 
    4,4,4,4,4,4,4,4,  # 98 - 9f 
    5,5,5,5,5,5,5,5,  # a0 - a7 
    5,5,5,5,5,5,5,5,  # a8 - af 
    5,5,5,5,5,5,5,5,  # b0 - b7 
    5,5,5,5,5,5,5,5,  # b8 - bf 
    0,0,6,6,6,6,6,6,  # c0 - c7 
    6,6,6,6,6,6,6,6,  # c8 - cf 
    6,6,6,6,6,6,6,6,  # d0 - d7 
    6,6,6,6,6,6,6,6,  # d8 - df 
    7,8,8,8,8,8,8,8,  # e0 - e7 
    8,8,8,8,8,9,8,8,  # e8 - ef 
    10,11,11,11,11,11,11,11,  # f0 - f7 
    12,13,13,13,14,15,0,0)   # f8 - ff 

UTF8_st = ( \
    eError,eStart,eError,eError,eError,eError,     12,   10,#00-07 
         9,     11,     8,     7,     6,     5,     4,    3,#08-0f 
    eError,eError,eError,eError,eError,eError,eError,eError,#10-17 
    eError,eError,eError,eError,eError,eError,eError,eError,#18-1f 
    eItsMe,eItsMe,eItsMe,eItsMe,eItsMe,eItsMe,eItsMe,eItsMe,#20-27 
    eItsMe,eItsMe,eItsMe,eItsMe,eItsMe,eItsMe,eItsMe,eItsMe,#28-2f 
    eError,eError,     5,     5,     5,     5,eError,eError,#30-37 
    eError,eError,eError,eError,eError,eError,eError,eError,#38-3f 
    eError,eError,eError,     5,     5,     5,eError,eError,#40-47 
    eError,eError,eError,eError,eError,eError,eError,eError,#48-4f 
    eError,eError,     7,     7,     7,     7,eError,eError,#50-57 
    eError,eError,eError,eError,eError,eError,eError,eError,#58-5f 
    eError,eError,eError,eError,     7,     7,eError,eError,#60-67 
    eError,eError,eError,eError,eError,eError,eError,eError,#68-6f 
    eError,eError,     9,     9,     9,     9,eError,eError,#70-77 
    eError,eError,eError,eError,eError,eError,eError,eError,#78-7f 
    eError,eError,eError,eError,eError,     9,eError,eError,#80-87 
    eError,eError,eError,eError,eError,eError,eError,eError,#88-8f 
    eError,eError,    12,    12,    12,    12,eError,eError,#90-97 
    eError,eError,eError,eError,eError,eError,eError,eError,#98-9f 
    eError,eError,eError,eError,eError,    12,eError,eError,#a0-a7 
    eError,eError,eError,eError,eError,eError,eError,eError,#a8-af 
    eError,eError,    12,    12,    12,eError,eError,eError,#b0-b7 
    eError,eError,eError,eError,eError,eError,eError,eError,#b8-bf 
    eError,eError,eStart,eStart,eStart,eStart,eError,eError,#c0-c7 
    eError,eError,eError,eError,eError,eError,eError,eError)#c8-cf 

UTF8CharLenTable = (0, 1, 0, 0, 0, 0, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6)

UTF8SMModel = {'classTable': UTF8_cls,
               'classFactor': 16,
               'stateTable': UTF8_st,
               'charLenTable': UTF8CharLenTable,
               'name': 'UTF-8'}
