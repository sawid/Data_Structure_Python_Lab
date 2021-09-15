class Stack():
        
    def __init__(self):    
        self.items = []
    def push(self,num):
        self.items.append(num)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
    def size(self):
        return len(self.items)         




print(" *** Stack implement by Python list***")

ls = [e for e in input("Enter data to stack : ").split()]

s = Stack()

for e in ls:

    s.push(e)

print(s.size(),"Data in stack : ",s.items)

while not s.isEmpty():

    s.pop()

print(s.size(),"Data in stack : ",s.items)