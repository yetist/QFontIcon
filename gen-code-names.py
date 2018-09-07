#! /usr/bin/env python
# -*- encoding:utf-8 -*-
# FileName: gen-meta-file.py

"This file is part of ____"
 
__author__   = "yetist"
__copyright__= "Copyright (C) 2018 yetist <yetist@yetibook>"
__license__  = """
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""
import os
import json
import requests

def load_awesome_names (path):
    out = {}
    if os.path.isfile(path):
        fp = open (path)
        out = json.load(fp)
    else:
        url = "https://github.com/FortAwesome/Font-Awesome/raw/master/advanced-options/metadata/icons.json"
        r = requests.get(url)
        if r.status_code == 200:
            out = r.json()
    return out

def write_meta_file(filename, data):
    fp = open(filename, "w+")
    json.dump(data, fp, indent = 2)
    fp.close()

def main():
    src = load_awesome_names ("icons.json")
    solid = {}
    brands = {}
    regular = {}
    for i in src.keys():
        if 'solid' in src[i]['svg']:
            solid[i] = int(src[i]['unicode'], 16)
        if 'brands' in src[i]['svg']:
            brands[i] = int(src[i]['unicode'], 16)
        if 'regular' in src[i]['svg']:
            regular[i] = int(src[i]['unicode'], 16)
    write_meta_file("solid-names.json", solid)
    write_meta_file("brands-names.json", brands)
    write_meta_file("regular-names.json", regular)

if __name__=="__main__":
    main()
