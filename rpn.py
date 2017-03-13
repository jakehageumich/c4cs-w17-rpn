def calculate(arg):
	stack = [];
	result = 0
	for i in arg:
		if str(i) == " ":
			continue
		if str(i) == "+":
			sum = 0
			while stack != []:
				sum += stack.pop()
			result = sum
			print(sum)
		elif str(i) == "-":
			difference = 0
			while stack != []:
				difference -= stack.pop()
			result = difference
			print(difference)
		elif str(i) == "*":
			product = 1                  
			while stack != []:
				product *= stack.pop()	
			result = product
			print(product)
		elif str(i) == "/":
			quotient = 0
			if stack != []:
				quotient = stack.pop()
			while stack != []:
				quotient /= stack.pop()
			result = quotient
			print(quotient)
		elif str(i) == "q":
			exit()
		else:
			stack.append(int(i))
def main():
	while True:
		calculate(input("rpn calc> "))
if __name__ == '__main__': # Note: that's "underscore underscore n a m e ..."
	main()
