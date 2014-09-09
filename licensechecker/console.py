#!/usr/bin/env python3
#
# The MIT License (MIT)
#
# Copyright (c) 2014 ChangZhuo Chen (陳昌倬) <czchen@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import argparse
import os

import licensechecker

_BUF_LEN = 1024

def get_args():
    parser = argparse.ArgumentParser(description=licensechecker.__description__)

    parser.add_argument('path', nargs='+', help='source code path')

    return parser.parse_args()


def generate_file_list(path):
    file_list = []

    for item in path:
        if os.path.isfile(item):
            file_list.append(item)
        elif os.path.isdir(item):

            for (dirpath, dirnames, filenames) in os.walk(item):
                file_list.extend(map(lambda x: os.path.join(dirpath, x), filenames))

    return file_list


def output(file_, copyright, license):
    print('Files: {}'.format(file_))

    print('Copyright:')
    for item in copyright:
        print(' {}'.format(item))

    license = list(license)
    license = ' or '.join(license)
    print('License: {}'.format(license))

    print('')


def main():
    args = get_args()

    file_list = generate_file_list(args.path)

    for file_ in file_list:
        with open(file_, 'r') as fd:
            buf = fd.read(_BUF_LEN)
            copyright = licensechecker.get_copyright(buf)
            license = licensechecker.get_license(buf)

            output(file_=file_, copyright=copyright, license=license)


if __name__ == '__main__':
    main()
