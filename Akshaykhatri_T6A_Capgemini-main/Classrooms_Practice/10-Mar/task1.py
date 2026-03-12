class circle:
    def __init__(self,radius,c_name):
        self.radius = radius
        self.c_name = c_name
        pass

    def areaCirc(self):
        r = self.radius
        area=3.14*r*r
        print("Area of",self.c_name,"is:",area)

    def paraCirc(self):
        r = self.radius
        parameter=2*3.14*r
        print("Parameter of",self.c_name,"is:",parameter)
c1 = circle(5,"circle1")
c2 = circle(10,"circle2")
c1.areaCirc()
c2.paraCirc()