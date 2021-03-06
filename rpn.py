import readline
import subprocess

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
            return sum
        elif str(i) == "-":
            difference = 0
            while stack != []:
                difference -= stack.pop()
                result = difference
            return difference
        elif str(i) == "*":
            product = 1
            while stack != []:
                product *= stack.pop()
                result = product
            return product
        elif str(i) == "/":
            quotient = 0
            if stack != []:
                quotient = stack.pop()
                while stack != []:
                    quotient /= stack.pop()
                    result = quotient
                return quotient
        elif str(i) == "^":
            product = 0
            if len(stack) > 0:
                product = stack.pop()
            while len(stack) > 0:
                product **= stack.pop()
            return product
        elif str(i) == "q":
            exit()
        else:
            stack.append(int(i))
def main():
    while True:
        print(calculate(input("rpn calc> ")))
    subprocess.call(["coverage report -m"])
if __name__ == '__main__': # Note: that's "underscore underscore n a m e ..."
    main()
