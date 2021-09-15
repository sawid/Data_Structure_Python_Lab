class ManageStack():
    def __init__(self):
        self.items = []
    def A(self,num):
        self.items.append(num)
        return "Add = " + str(num)
    def P(self):
        if self.items == []:
            return -1;
        else:
            return "Pop = " + str(self.items.pop())
    def D(self,num):
        i = 0
        temp = ""
        len_list = len(self.items) - 1
        temp_list = []
        if self.items == []:
            print("-1")
        else:
            while i <= len_list:
                if self.items[i] == num:
                    print("Delete = " + str(num))
                    del self.items[i]
                    i = -1
                    len_list = len(self.items) - 1
                i+=1
                
        return temp;
    def LD(self,num):
        i = 0
        temp_num = []
        len_list = len(self.items) - 1
        if self.items == []:
            print("-1")
        else:
            while i <= len_list:
                if self.items[i] < num:
                    temp_num.append(self.items[i])
                i+=1
            temp_num.sort()
            for j in temp_num:
                len_self = len(self.items) - 1
                for k in range(len_self):
                    if j == self.items[k]:
                        print("Delete = " + str(self.items[k]) + " Because " + str(self.items[k]) + " is less than " + str(num))
                        del self.items[k]
                        len_self = len(self.items) - 1
    def MD(self,num):
        i = 0
        len_list = len(self.items) - 1
        if self.items == []:
            print("-1")
        else:
            while i <= len_list:
                if self.items[i] > num:
                    print("Delete = " + str(self.items[i]) + " Because " + str(self.items[i]) + " is more than " + str(num))
                    del self.items[i]
                    i = -1
                    len_list = len(self.items) - 1
                i+=1

ms = ManageStack()
S = input("Enter Input : ").split(',')

for i in range(len(S)):

    if S[i][0] == "A":
        print(ms.A(int(S[i][2:])),sep="")
    elif S[i][0] == "P":
	    print(ms.P())
    elif S[i][0] == "D":
	    ms.D(int(S[i][2:]))
    elif S[i][0:2] == "LD": 
        ms.LD(int(S[i][3:]))
    elif S[i][0:2] == "MD": 
        ms.MD(int(S[i][3:]))
print("Value in Stack =",ms.items)