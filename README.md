python-unpack
=============

Recursively unarchive, decompress, and flatten all files in a given directory

Mike Jensen <jjensen.mike at gmail.com>

Distributed under the PSF License: http://www.python.org/psf/license/

Originally wrote for VAVE xml feed destructor (https://github.com/votinginfoproject/VAVE)

Requires Python rarfile (http://pypi.python.org/pypi/rarfile/2.2), python-magic (https://github.com/ahupp/python-magic), and python-filetype (https://github.com/jjensenmike/python-filetype)

Installation
============

Requires libraries listed above

Run:

python setup.py install

Examples
========

import unpack

unpack.unpack("folder_to_unpack", "unpack_location")

unpack.flatten_folder("unpack_location")

unpack.unpack("file_to_unpack.txt")

