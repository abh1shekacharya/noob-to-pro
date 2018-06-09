import zipfile
import itertools

file = zipfile.ZipFile('/home/amritesh/chai.zip')

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$&*.'
num = int(input('What is the length of password'))


permutation = itertools.permutations(letters, num)

for c in permutation:
    i = (''.join(c))
    print(i)
    try:
        file.extractall(pwd=i)
        print('Password is: ' + i)
        break
    except Exception:
        pass
