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

import os
import re

import yaml

_LICENSE = {}

def get_license(buf):
    ret = set()
    supersede = set()

    for license in _LICENSE:
        if license['name'] in supersede:
            continue

        for i in range(len(license['keywords'])):
            if license['keywords'][i].search(buf) is None:
                break
        else:
            ret.add(license['name'])
            ret = ret.difference(license['supersede'])
            supersede = supersede.union((license['supersede']))

    return ret


def get_keyword_regex(keyword):
    return re.compile(r'[\n\s*#]+'.join(keyword.split(' ')))


def load_license_config():
    global _LICENSE

    with open(os.path.join(os.path.dirname(__file__), 'data', 'license.yml'), 'r') as fd:
        _LICENSE = yaml.load(fd.read())

    for license in _LICENSE:
        for i in range(len(license['keywords'])):
            license['keywords'][i] = get_keyword_regex(license['keywords'][i])

        if 'supersede' in license:
            license['supersede'] = set(license['supersede'])
        else:
            license['supersede'] = set()

load_license_config()
