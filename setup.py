from distutils.core import setup

# patch distutils if it can't cope with the "classifiers" or "download_url"
# keywords (prior to python 2.3.0).
from distutils.dist import DistributionMetadata
if not hasattr(DistributionMetadata, 'classifiers'):
    DistributionMetadata.classifiers = None
if not hasattr(DistributionMetadata, 'download_url'):
    DistributionMetadata.download_url = None
    
setup(
    name = "fastchardet",
    packages = ["fastchardet"],
    version = "0.1.1",
    license = "LGPL",
    platforms = ['POSIX', 'Windows'],
    description = "Fast universal encoding detector",
    author = "Matt Basta",
    author_email = "matt@serverboy.net",
    url = "http://github.com/mattbasta/fastchardet",
    keywords = ["encoding", "i18n", "xml", "l10n"],
    classifiers = [
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
        ],
    long_description = """\
Fast universal character encoding detector
-------------------------------------

Detects
 - ASCII
 - UTF-8
 - windows-1252 (English)
 - "None of the above"

Requires Python 2.1 or later
"""
    )
