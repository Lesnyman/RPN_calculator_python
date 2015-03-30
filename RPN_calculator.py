from reportlab.lib.validators import isNumber
import sys
class Calculator:
    rpn = []
    stack = []
    operations = {"+":lambda x,y: x + y,
                  "-":lambda x,y: x - y,
                  "*":lambda x,y: x * y,
                  "/":lambda x,y: x / y,
                  "^":lambda x,y: pow(x, y)
                  }
    
    def showInputString(self):
        #print(data)
        sys.stdout.write("Input data is: ")
        for d in self.rpn:
            sys.stdout.write("%s, " % d)
        print("")
            
        return
    
    def showAsConventional(self): 
        conventional = []
        for d in self.rpn:
            if isNumber(d):
                conventional.append(d)
            else:
                temp1=conventional.pop()
                temp2=conventional.pop()
                temp3 = "(%s %s %s)" % (temp2, d,temp1)
                conventional.append(temp3)    
        print("infix notation: %s" % conventional[-1])  
        return
    
    def isNumber(self, n):
        try:
            float(n)
            return True
        except ValueError:
            return False
    
    def addNumbers(self,a,b):
        return a+b;
    
    def calculate(self, calculator):
        for calc in calculator:
            if isNumber(calc):
                self.stack.append(calc)
            else:
                try:
                    temp1=self.stack.pop()
                    temp2=self.stack.pop()
                    result = self.operations[calc](temp2,temp1)
                    #print(result)
                    self.stack.append(result)
                except IndexError:
                    print("Index Error - check postfix statement!!")
                    return

        print("Result = %f" % self.stack[-1])

            
        return
        
        
        
    
calculator = Calculator()
calculator.rpn = [19, 2.14, "+" , 4.5, 2, 4.3, "/", "-", "*"] #85.297442
#calculator.rpn = [12, 2, 3, 4, "*", 10, 5, "/", "+", "*", "+"] #40

calculator.showInputString()
calculator.showAsConventional()
calculator.calculate(calculator.rpn)


