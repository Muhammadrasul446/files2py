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
        script_file.write("file_names = [".encode())
        for path in paths:
            while path.find('/') != -1:
                path = path[path.find('/') + 1:]
            script_file.write(('"' + path + '", ').encode())
        script_file.write("]\n\n".encode())
        script_file.write("byte_files = [".encode())
        for file in paths:
            bytes_of_file = []
            with open(file, 'rb') as file_in_bytes:
                for byte in file_in_bytes:
                    bytes_of_file.append(byte)
            script_file.write((str(bytes_of_file) + ", ").encode())

        script_file.write("]\n\n".encode("utf-8"))
        script_file.write("for i in range(len(file_names)):\n".encode())
        script_file.write("    with open(file_names[i], 'wb') as new_file:\n".encode())
        script_file.write("        for byte_file in byte_files[i]:\n".encode())
        script_file.write("            new_file.write(byte_file)\n".encode())
else:
    print('No path was given!')
input('Press Enter to finish script...')
