## dumps(): Encryption
## loads(): Decryption

'''
1. JSON,
2. pickle,
'''

import json

file = open('temp.txt', 'a+')

data = {
    'fullname': 'John Doe',
    'userID': 93847140,
    'password': '*****',
}
# print(f'Original Data: {data}')
# print(f'Type of Original Data: {type(data)}')
# print()


enc_data = json.dumps(data)
file.write(enc_data )

file.seek(0)

enc_data = file.read()
print(type(enc_data))

ori_data = json.loads(enc_data)
print(ori_data, type(ori_data))

# print(f'Encrypted Data: {enc_data}')
# print(f'Type of Encrypted Data: {type(enc_data)}')
# print()

# dec_data = json.loads(enc_data)
# print(f'Decrypted Data: {dec_data}')
# print(f'Type of Decrypted Data: {type(dec_data)}')


file.close()