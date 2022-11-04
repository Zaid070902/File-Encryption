from cryptography.fernet import Fernet
import os

os.chdir('C:/Users/zaidf/OneDrive/Desktop/test-dir2')

directory = 'C:/Users/zaidf/OneDrive/Desktop/test-dir2'
list_dir = os.listdir()
print(list_dir)


def decrypt_file():
    key = b'Ez-gvzWq4Yd47uXSq0SLRQbGx_IyT2275quRpHx-4ZM='
    for file in os.scandir(directory):
        if file.is_file():
            file_in_dir = open(file, 'rb')
            data = file_in_dir.read()
            file_in_dir.close()

            fernet = Fernet(key)
            decrypted = fernet.decrypt(data)

            decrypted_file = open(file, 'wb')
            decrypted_file.write(decrypted)


decrypt_file()
