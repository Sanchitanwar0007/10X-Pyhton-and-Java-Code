class Circle:
	def __init__(self,num):
		self.num=num
		
	def getArea(self):
		are=0
		if(self.num>=0):
			are=3.14*self.num**2
		return are
	def getCircumference(self):
		val=0
		if(self.num>=0):
			val="{:.2f}".format(2*3.14*self.num)
		return val
		
if __name__ == "__main__":
    one_circle = Circle(float(input()))
    print(float(one_circle.getArea()))
    print(float(one_circle.getCircumference()))