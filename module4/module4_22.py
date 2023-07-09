#Write a Python class named Rectangle constructed by a length and 
#width and a method which will compute the area of a rectangle

class Rectangle:

    def area(self,length,width):
        self.length = length
        self.width = width

        area = self.length * self.width
        print("Area Of Rectangle :",area)


r = Rectangle()

length = int(input("Enter Length Of Rectangle :"))
width = int(input("Enter The Width of Rectangle :"))

r.area(length,width)
