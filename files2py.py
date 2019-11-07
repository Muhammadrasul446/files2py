#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import codecs
from os.path import isfile as file_exists


paths = []
path = ''
print('Welcome to files2py!')
print('If you have done then input "done()"')
while True:
    path = input('File path: ')
    if path.lower() == 'done()':
        break
    else:
        if file_exists(path):
            if path not in paths:
                paths.append(path)
            else:
                print('File:', path, 'has already been given!')
        else:
            print('File:', path, 'is not found!')

if len(paths) != 0:
    fname = input('Input filename: ')
    fname = 'None.py' if fname == '' else fname
    fname += '.py'if fname[-3:] != '.py' else ''
    if file_exists(fname):
        if input("File: " + fname + " already exists. Do you want to rewrite it (y/n)?").lower() != 'y':
            exit()
    with open(fname, 'wb') as script_file:
        script_file.write("from os.path import isfile as file_exists\n".encode())
        script_file.write("from codecs import decode as codecs_decode\n".encode())
        script_file.write("from binascii import unhexlify as binascii_unhexlify\n\n".encode())
        script_file.write("file_names = [".encode())
        for path in paths:
            while path.find('/') != -1:
                path = path[path.find('/') + 1:]
            script_file.write(('"' + path + '", ').encode())
        script_file.write("]\n\n".encode())
        script_file.write("byte_files = [".encode())
        for file in paths:
            with open(file, 'rb') as reading_file:
                bytes_of_file = reading_file.read()
            bytes_of_file = codecs.encode(bytes_of_file, 'zip').hex()
            script_file.write(('"' + str(bytes_of_file) + '",\n').encode())

        script_file.write("]\n\n".encode("utf-8"))
        script_file.write("for i in range(len(file_names)):\n".encode())
        script_file.write("    if file_exists(file_names[i]):\n".encode())
        script_file.write("        if input('File: ' + file_names[i] + ' already exists. Do you want to rewrite it (y/n)?').lower() != 'y':\n".encode())
        script_file.write("            print('File: ' + file_names[i] + ' has been skipped!')\n".encode())
        script_file.write("            continue\n".encode())
        script_file.write("    with open(file_names[i], 'wb') as new_file:\n".encode())
        script_file.write("        bytes_of_file = codecs_decode(binascii_unhexlify(byte_files[i]), 'zip')\n".encode())
        script_file.write("        new_file.write(bytes_of_file )\n".encode())
else:
    print('No path was given!')
input('Press Enter to finish script...')
