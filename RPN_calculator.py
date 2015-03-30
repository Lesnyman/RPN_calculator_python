from reportlab.lib.validators import isNumber
class Calculator:
    rpn = []
    stack = []
    operations = {"+":lambda x,y: x + y,
                  "-":lambda x,y: x - y,
                  "*":lambda x,y: x * y,
                  "/":lambda x,y: x / y,
                  "^":lambda x,y: pow(x, y)
                  }
    
    def showInputString(self, data):
        print(data)
        #for d in data:
        #    print (d)
        return
    
    def showAsConventional(self, data):
        conventional = []
        for d in data:
            if isNumber(d):
                conventional.append(d)
            else:
                temp1=conventional.pop()
                temp2=conventional.pop()
                pass
                
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
                temp1=self.stack.pop()
                temp2=self.stack.pop()
                result = self.operations[calc](temp2,temp1)
                #print(result)
                self.stack.append(result)
        return
        
        
        
    
calculator = Calculator()
#calculator.rpn = [19, 2.14, "+" , 4.5, 2, 4.3, "/", "-", "*"] #85
calculator.rpn = [12, 2, 3, 4, "*", 10, 5, "/", "+", "*", "+"] #40
calculator.showAsConventional(calculator.rpn)
calculator.showInputString(calculator.rpn)
calculator.calculate(calculator.rpn)
print (calculator.stack)

