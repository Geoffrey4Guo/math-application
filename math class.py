
'Creates two variables called num1 and num2 and asks the user for integer inputs'

num1 = int(input("Please enter a number: "))

num2 = int(input("Please enter a second number: "))

 

'Creates a Math class that will take two variables and +,-,*,/ them'

class Math:

    'Declares a constructor to set the varibles to the class'

    def __init__(self, num1, num2):

        self.num1 = num1

        self.num2 = num2

    'Creates an add function'

    def add(self):

        return self.num1 + self.num2

    'Creates a subtract function'

    def subtract(self):

        return self.num1 - self.num2

    'Creates a multiply function'

    def multiply(self):

        return self.num1 * self.num2

    'Creates a divide function'

    def divide(self):
        'Uses an if statement to check if num2 is zero'
        'If true, it will print cannot be divided by zero'
        if (self.num2 == 0): 
            return "Cannot divide by zero"
        else:
            return self.num1 / self.num2
        
            
        
    

 

'Creates a Main class to run the above Math class with objects'

def main():

    'Creates an object called doing_math from the Math class'

    doing_math = Math(num1, num2)

    'Calls the functions and print the corresponding answers of the operations'

    print("The sum is", doing_math.add())

    print("The difference is", doing_math.subtract())

    print("The product is", doing_math.multiply())

    print("The quotient is", doing_math.divide())

 

 

'using the special variable __name__ to run the main program'

if __name__ == "__main__":

    main()


