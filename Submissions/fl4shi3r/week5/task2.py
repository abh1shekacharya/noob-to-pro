import itertools
import zipfile

file_obj = zipfile.ZipFile('/home/shivendra/Downloads/locked.zip')

s = 'loabcdefghijkmnpqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'

length = int(input("Enter the length of the password : "))

comb = itertools.permutations(s,length)

for passwd in comb:
    passwd = (''.join(passwd))
    print(passwd)
    try:
        file_obj.extractall(pwd=passwd)
        print("Password :-" + passwd)
        break
    except Exception:
        pass
