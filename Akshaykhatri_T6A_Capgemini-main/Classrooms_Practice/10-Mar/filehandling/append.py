file = open('jecrc.txt', 'a+')

# file.write('i am tushar')
# file.seek(0)
# file.write('from capg')

file.writelines([
    '\nHello,'
    'you\n'
    'tushar'

])

file.close()