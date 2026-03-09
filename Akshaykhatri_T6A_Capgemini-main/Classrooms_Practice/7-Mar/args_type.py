# def form(name,mail,ph,age):               #these are positional arguments
#     print(name,mail,ph,age,sep="\n")
# form('Akshay','aks@gmail','98765',21)



# def form(name,mail,ph,age=21,alt_ph=91912323):  #default arg must be present at last like age
#     print(name,mail,ph,age,alt_ph,sep="\n")
# form('Akshay','aks@gmail','98765',21,91232323)


# def form(name,mail,ph,age=None):               #there age is keyword arguments
#     print(name,mail,ph,age,sep="\n")
# form('Akshay','aks@gmail','98765',age=21)


# def form(*a):               #there a is variable length arguments with tuple
#     print('a is:',a,sep="\n")
#     print(type(a))
#     print(len(a))
# form('Akshay','aks@gmail','98765',21)


# def form2(**a):               #there a is variable length arguments with dictionary
#     print('a is:',a,sep="\n")
#     print(type(a))
# form2(a='Akshay',b='aks@gmail',c='98765',d=21)



def form(name,age=10,*a,ph=None):       #all argumnets in one function
    print(name)    #positional
    print(age)     #default
    print(a)       #variable length
    print(ph)      #keyword
form("akshay",20,'cricket','football',ph=9090909090)
