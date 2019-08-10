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
            paths.append(path)
        else:
            print('File:', path, 'is not found!')

if len(paths) != 0:
    fname = input('Input filename: ')
    fname = 'None.py' if fname == '' else fname
    fname += '.py'if fname[-3:] != '.py' else ''
    with open(fname, 'wb') as script_file:
        script_file.write(bytes("file_names = [", encoding="utf-8"))
        for path in paths:
            script_file.write(bytes('"' + path + '", ', encoding="utf-8"))
        script_file.write(bytes("]\n\n", encoding="utf-8"))
        script_file.write(bytes("byte_files = [", encoding="utf-8"))
        for file in paths:
            bytes_of_file = []
            with open(file, 'rb') as file_in_bytes:
                for byte in file_in_bytes:
                    bytes_of_file.append(byte)
            script_file.write(bytes(str(bytes_of_file) + ", ", encoding="utf-8"))

        script_file.write(bytes("]\n\n", encoding="utf-8"))
        script_file.write(bytes("for i in range(len(file_names)):\n", encoding="utf-8"))
        script_file.write(bytes("    with open(file_names[i], 'wb') as new_file:\n", encoding="utf-8"))
        script_file.write(bytes("        for byte_file in byte_files[i]:\n", encoding="utf-8"))
        script_file.write(bytes("            new_file.write(byte_file)\n", encoding="utf-8"))
