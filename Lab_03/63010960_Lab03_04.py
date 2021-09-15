class StackCalc():
    def __init__(self):
        self.items = []
    def run(self,*args):
        for i, val in enumerate(args):
            if str(val).isnumeric():
                self.items.append(int(val))
            elif val == "DUP":
                self.items.append(int(self.items[-1]))
            elif val == "POP":
                self.items.pop()
            elif val == "PSH":
                self.items.append(int(self.items[i + 1]))
            elif val == "+":
                self.items.append(self.items.pop() + self.items.pop())
            elif val == "-":
                self.items.append(self.items.pop() - self.items.pop())
            elif val == "*":
                self.items.append(self.items.pop() * self.items.pop())
            elif val == "/":
                self.items.append(int(self.items.pop() / self.items.pop()))
            else:
                self.items.append("Invalid instruction: " + val)
                break
    def getValue(self):
        if self.items == []:
            return 0;
        else:
            return self.items[-1]
        

print("* Stack Calculator *")
arg = input("Enter arguments : ").split()
machine = StackCalc()
machine.run(*arg)
print(machine.getValue())