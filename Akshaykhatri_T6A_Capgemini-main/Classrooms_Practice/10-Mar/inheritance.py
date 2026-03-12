class car:
    wheels = 4
class nano(car):
    @staticmethod
    def disp():
        print(car.wheels)
nano.disp()