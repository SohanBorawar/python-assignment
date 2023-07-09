#Write a Python class named Circle constructed by a radius and two 
#methods which will compute the area and the perimeter of a circle

class circle:

    def area(self,radius):
        self.r = radius
        area = 3.14 * self.r**2
        print("Area Of Circle :",area)

    def perimeter(self,radius):
        self.r = radius
        perimeter = 2 * 3.14 * self.r
        print("Perimeter Of Circle :",perimeter)


c = circle()

radius = int(input("Enter The Radius Of Circle :"))

c.area(radius)
c.perimeter(radius)