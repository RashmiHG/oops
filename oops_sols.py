# 1) Create a Cricle class and intialize it with radius. Make two methods getArea and getCircumference inside this class

class circle:
    def __init__(self,radius):
        self.radius=radius
        print("creating a circle with radius: ",self.radius)
    def getarea(self):
        area=3.14*(self.radius**2)
        return area
    def getcircum(self):
        return 2*3.14*self.radius
if __name__=="__main__":
    r=eval(input("enter radius : "))
    c=circle(r)
    print("area of circle : ",c.getarea())
    print("circumference of circle is : ",c.getcircum())