class Rectangle:
	def __init__(self,l,b):
		self.l=l
		self.b=b
	def rectangle_area(self):
		area=0
		if(self.l>0 and self.b>0):
			area=self.l*self.b
		return area
	def rectangle_perimeter(self):
		perimeter=0
		if(self.l>0 and self.b>0):
			perimeter=2*(self.l+self.b)
		return perimeter
if __name__ == "__main__":
    newRectangle = Rectangle(int(input()), int(input()))
    print(newRectangle.rectangle_area())
    print(newRectangle.rectangle_perimeter())