#a=eval(input('enter:'));
#print(a+500)
#11.	Check if number is a 3-digit number or not take user input.
num = int(input("Check if number is a 3-digit number or not: "))
if 100 <= num <= 999:
    print('yes, a 3-digit')
else:
    print('no, not a 3-digit')
#12.	Check if string length is greater than 5.
s1=input("Check if string length is greater than 5")
if(len(s1)>5):
    print("yes")
else:
    print('no')
#13.	Check if number is zero so print ‘zero’ otherwise print ‘Not Zero’.
n13=int(input('Check if number is zero so print ‘zero’: '))
if(n13==0):
    print('zero')
else:
    print('not zero')
#14.	Check if person can enter club (age + ID check). If yes, print ‘Eligible’.
print('14.	Check if person can enter club (age + ID check). If yes, print ‘Eligible’.')
age=int(input('Enter your age: '))
iid = input("Do you have id? (yes/no): ").lower()
if(age>=18 and iid=='yes'):
    print('Eligible')
else:
    print('ahh! Not eligible')
#15.	Check if number is within range 10–50 if yes print ‘In Range’ otherwise ‘Not in Range’.
n15=int(input('Check if number is within range 10–50, enter: '))
if(10<=n15<=50):
    print('In range')
else:
    print('Not in range')
#16.	Simple calculator (+ or -) take both number and operator symbol from user.
a=int(input('enter first num: '))
b=int(input('enter second num: '))
op=input('Enter the operation(+ or -): ')
elif op == '-':
    print(a - b)
else:
    print("Invalid operator")
#17.	Check if username and password are correct if yes, print ‘Login Successful’.
un="tushar vaishnaw"
pw='Password0'
print('username is: ',un,'\n')
print('password is: ',pw)
un1=input('enter username: ').lower()
pw1=input('enter password: ')
if(un1==un and pw1==pw):
    print('Login Successful')
else:
    print('Login Faild!!!')
#18.	Check if temperature is hot or cold.
temp=int(input('Enter the Temperature in °C: '))
if(temp<=15):
    print('it is cold outside')
else:
    print('it is hot outisde')
#19.	Check if number is palindrome (basic version) or not. If yes, print ‘Palindrome’ if no, print ‘Not Palindrome’.
num = int(input("Enter a number: "))
original = num
reverse = 0
# Reverse the number
while num > 0:
    digit = num % 10
    reverse = (reverse * 10) + digit
    num = num // 10
# Check and Print
if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
#20.	Check if number is greater than 100.
n20=int(input('enter a number: '))
if(n20<=100):
    print('not greater than 100')
else:
    print('greater than 100')
