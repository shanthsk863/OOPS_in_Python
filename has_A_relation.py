class Car:
    def __init__(self,car_name,model,color):
        self.car_name=car_name
        self.model=model
        self.color=color
    def cor_info(self):
        print('The car name is: {},and model: {},and color: {}'.format(self.car_name,self.model,self.color
        ))    


class Employee:
    def __init__(self,ename,eno,car):
        self.ename=ename
        self.eno=eno
        self.car=car

    def getInfo(self):
        print('Employee Name:',self.ename)
        print('Employee Number:',self.eno)
        print('Employee Car Information :')
        self.car.cor_info()
car = Car('I20',2000,'Red',)
e = Employee('Shantesh',583,car) 
e.getInfo()
