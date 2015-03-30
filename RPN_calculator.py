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
        try:
            self.rpn[-1]
        except IndexError:
            print("Nothing to evaluate")
            return
        
        for d in self.rpn:
            if self.isNumber(d):
                conventional.append(d)
            elif d in ("+","-","^","/","*"):
                try:
                    temp1=conventional.pop()
                    temp2=conventional.pop()
                except IndexError:
                    print("Index Error - check postfix statement!!")
                    return
                temp3 = "(%s %s %s)" % (temp2, d,temp1)
                conventional.append(temp3)
            else:
                print("Incorrect operator or operand!!")
                return    
        print("Infix notation: %s" % conventional[-1])  
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
            if self.isNumber(calc):
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
                except KeyError:
                    print("Operator error! - check postfix statement!!")
                    return
                     
        try:
            self.rpn[-1]
        except IndexError:
            print("Nothing to evaluate")
            return
        if len(self.stack) > 1:
            print("Missing operator")
            return
        print("Result = %s" % self.stack[-1])
        return
    
    
    def userRpnInput(self):
        userInput = True 
        while(userInput):
            tmp = raw_input("Please enter another number or operator. Type 'end' to end input. Type 'del' to delete last. Type 'quit' to quit.\nYour input : %s\n" % self.rpn)
            if self.isNumber(tmp):
                tmp = float(tmp)
            elif tmp == "end":
                self.showAsConventional()
                self.calculate(self.rpn)
                raw_input("Press enter to continue...")
                continue
            elif tmp == "del":
                try:
                    self.rpn.pop()
                except IndexError:
                    print("Your statement is already empty!")
                    raw_input("Press enter to continue...")
                continue
            elif tmp == "quit":
                return
            self.rpn.append(tmp)
            tmp=""
        return
        
        
    
calculator = Calculator()
#test rpn statements
#calculator.rpn = [19, 2.14, "+" , 4.5, 2, 4.3, "/", "-", "*"] #85.297442
#calculator.rpn = [12, 2, 3, 4, "*", 10, 5, "/", "+", "*", "+"] #40
calculator.userRpnInput()
#calculator.showInputString()
#calculator.showAsConventional()
#calculator.calculate(calculator.rpn)

