file = open('write.txt','w+')
file.write('i am the first line\n')
file.writelines([
    'second line\n'
    'third line\n'
    'fourth'
])
file.seek(6)
print(file.read())

file.close()