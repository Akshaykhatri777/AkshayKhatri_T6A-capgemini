class College:
    c_name='JECRC'
    loc='Jaipur'

    #creating constructor
    def __init__(self,name,id,age,state='Raj'):
        self.name=name
        self.id=id
        self.age=age
        self.state=state
        pass

    def display(self):       #object method
        # print(self.name,self.id,self.age,sep='\n')
        # print()
        self.loc='Jp to Vidhani'
        print(self.c_name,self.loc)

    @classmethod           #class method used to access through class
    def c_disp(cls,new):
        cls.loc='Vidhani'
        cls.c_name=new
        print(cls.c_name,cls.loc,sep='\n')

    @staticmethod
    def add(a,b):
        print(College.c_name)
        print(a+b)


s1 =College('akshay',25,21)     #s1 is object
s2 =College('tushar',115,21)
s1.c_disp('skit')
# print("\nAccesing class method using object")
# s1.c_disp()
# print("\nAccesing class method using class")
# College.c_disp('SKIT')
# print()
College.add(10,20)
s2.add(100,200)

