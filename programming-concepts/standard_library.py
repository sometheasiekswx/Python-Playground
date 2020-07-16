import zipfile
import math
import itertools

# Sorted
print('------ Sorted ------')
print(sorted('Somethea is the author'.split()))
print(sorted('Somethea is the author'.split(), key=str.lower))
print(sorted('Somethea is the author'.split(), key=str.upper))
people = [('Somethea', 'Siek', 12), ('Tom', 'Jerry', 123), ('Chris', 'Som', 50), ('Siek', 'Sopheany', 2)]
print(sorted(people, key=lambda x: x[0]))
print(sorted(people, key=lambda x: x[2]))

# Type
print('------ Type ------')
print(isinstance(people, list))

# Math
print('------ Math ------')
print(math.factorial(3))
print(math.factorial(10))
print(math.gcd(52, 8))
print(math.gcd(1000, 2))
print(math.gcd(234123452352352, 2342345235))

# Itertools
for i in itertools.count(100, 5):
    print(i)
    if i > 5000:
        break

for i in itertools.cycle('Somethea'):
    print(i)
    if i == 'a':
        break
for i in itertools.permutations(['Somethea', 'Sopheany', 'Apple']):
    print(i)

for i in itertools.combinations(['Somethea', 'Sopheany', 'Apple'], 2):
    print(i)

# File seeking
file = open('file_seeking.txt', 'r')
print(file.read(10))
file.close()
file = open('file_seeking.txt', 'r')
print(file.read(5))
print(file.read(5))
print(file.read(5))
file.close()
file = open('file_seeking.txt', 'r')
print(file.read(1))
file.close()
file = open('file_seeking.txt', 'r')
print(f'First line: {file.readline()}')
file.seek(0)
for line in file:
    print(line)

# Zip
zip_file = zipfile.ZipFile('Archive.zip', 'r')
print(zip_file.namelist())
for meta in zip_file.infolist():
    print(meta)
print(zip_file.getinfo('file_seeking.txt'))
print(zip_file.read('file_seeking.txt'))
with zip_file.open('file_seeking.txt') as f:
    print(f.readlines())
    print(f.read())
zip_file.extractall()
