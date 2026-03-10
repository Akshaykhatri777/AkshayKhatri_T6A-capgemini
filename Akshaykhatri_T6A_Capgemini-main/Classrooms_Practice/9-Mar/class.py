class College:
    c_name='JECRC'
    loc='Jaipur'
    type='Private'
s1=College()     #s1,s2,s3 are objects
s2=College()
s3=College()
print(s3)
# print(College)
s1.name = 'akshay'
s2.name = 'om'

s1.age = 21
s2.age = 22

s1.comp = 'capg'
s2.comp = 'lti'

print(s1.c_name,s1.loc,s1.name,s1.age,s1.comp,sep='  ')
print(s2.c_name,s2.loc,s2.name,s2.age,s2.comp,sep='  ')