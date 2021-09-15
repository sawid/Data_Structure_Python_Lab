class intothewood():
    def __init__(self):
        self.items = []
        self.counter = 0
    def a(self,num):
        self.items.append(int(num))
        # print(self.items)
    def b(self):
        if self.items == []:
            return 0
        # print(self.items)
        temp = self.items
        
        len_temp = len(temp)
        i = 1
        while i < len_temp:
            if len(self.items) == 2:
                temp = self.items
                break
            elif temp[i] > temp[i - 1]:
                del temp[i - 1]
                len_temp = len(temp)
                i = 1
                # print(self.items, "slice")
            
            i+=1
        # print(temp)
                  
        max_num = max(temp)
        max_index = temp.index(max_num)
        if len(temp) > 1 and max_index != 0:
            if max_num == temp[max_index - 1]:
                temp = temp[(max_index + 1):]
            else:
                temp = temp[(max_index):]
        elif len(temp) == 2:
            if temp[0] == temp[1]:
                temp = temp[:1]
        # print(temp)
        # print(max_num)
        # print(self.items)
        # print(temp)
            
        self.counter = len(temp)
        return self.counter
    def s(self):
        if self.items == []:
            return
        for index, i in enumerate(self.items):
            if (i%2) == 0:
                if i != 1:
                    self.items[index]-=1
            else:
                self.items[index]+=2
                
        

itw = intothewood()
str_wood = input("Enter Input : ").split(',')
# print(str_wood)
for i in range(len(str_wood)):
    if str_wood[i][0] == "A":
        itw.a(int(str_wood[i][2:]))
    elif str_wood[i][0] == "B":
        print(itw.b())
    elif str_wood[i][0] == "S":
        itw.s()