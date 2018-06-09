import zipfile

file = zipfile.ZipFile('/home/amritesh/test.zip')
dict = open('/home/amritesh/dict.txt')

for line in dict.readlines():
    password = line.strip('\n')
    try:
        file.extractall(pwd=password)
        print('Password is: ' + password)
    except Exception:
        pass
