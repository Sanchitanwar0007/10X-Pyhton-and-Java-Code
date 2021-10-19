class Flight:
		def __init__(self, upTime, downTime):
			self.upTime = upTime
			self.downTime = downTime

		def calculateFlight(self):
			hourup=""
			minup=""
			for i in range(len(self.upTime)):
				if(i==0 or i==1):
					hourup+=self.upTime[i]+""
				if(i==3 or i==4):
					minup+=self.upTime[i]+""
			hourup=int(hourup)
			minup=int(minup)
			hourUpTime=hourup*60
			
			up_in_min=hourUpTime+minup

			hourdown=""
			mindown=""
			for i in range(len(self.downTime)):
				if(i==0 or i==1):
					hourdown+=self.downTime[i]+""
				if(i==3 or i==4):
					mindown+=self.downTime[i]+""
			hourdown=int(hourdown)
			mindown=int(mindown)
			hourdowntime=hourdown*60
			down_in_min=hourdowntime+mindown
			return down_in_min-up_in_min
			



### DO NOT CHANGE ANYTHING BELOW THIS LINE

if __name__ == '__main__':
    
    t1 = input()
    t2 = input()

    f1 = Flight(t1, t2)
    print(f1.calculateFlight())