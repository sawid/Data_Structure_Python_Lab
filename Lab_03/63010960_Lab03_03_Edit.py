class Stack:
    
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False



inp = input('Enter Input : ').split()

S = Stack()

for j in inp:
    S.push(j)

counter = 0
marked = S.items[0]
combo = 0
i = 1
nested = False
len_size = S.size() - 1
while i < len_size:
    if ((S.items[i] == S.items[i + 1]) and ((S.items[i] == marked))):
        counter += 1
    else:
        marked = S.items[i + 1]
        counter = 1
    if counter == 3:
        del S.items[(i - 1):(i + 2)]
        len_size = S.size() - 1
        combo += 1
        i = 0
        counter = 1
    if i == len_size - 1:
        if counter <= 2:
            if nested == False:
                i = 0
                counter = 1
                nested = True
            else:
                break;
        else:
            counter = 1
            i = 0
    else:
        i+=1

print(S.size())
if "".join(S.items) == "":
    print("Empty")
else:
    text_p = "".join(S.items)
    print(text_p[::-1])
if combo > 1:
    print("Combo : ",combo," ! ! !",sep="")
