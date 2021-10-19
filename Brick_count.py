def calculate_total_price_of_bricks(dimensions, brick_count):
    if dimensions[0] == -1:              
		    width = 60                    
    else:
		    width = dimensions[0]
    if dimensions[1] == -1:
		    height = 40
    else:
		    height = dimensions[1]
    return calculate_price(brick_count*volume(length=100,width=width,height=height),price=0.00005)
### Do not change anything below this line
def volume(length=100,width=60,height=40):
	return length*width*height

def calculate_price(volume, price=0.00005):
	return round(volume*price)

if __name__ == "__main__":
    brick_count = int(input())          #O(1)
    dimensions = [int(i) for i in input().split(' ')]       #Space complexity O(2) ==>O(1)
    total_price = calculate_total_price_of_bricks(dimensions, brick_count)    #O(1)
    print(total_price)   # over all time and space complexity is O(1)