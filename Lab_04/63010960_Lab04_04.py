class linequeue():
    def __init__(self):
        self.items = []
    def get(self):
        for i in range(len(self.items)):
            if self.items[i] != []:
                return self.items[i].pop(0)
    def put(self, item, index):
        self.items.insert(index, item)
    def append(self, item):
        self.items.append(item)
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
    def size(self):
        return len(self.items)

str_init = input("Enter Input : ").split("/")

str_val = str_init[0].split(",")
str_oper = str_init[1].split(",")
q = linequeue()
q_depart = []
depart = []
id = []
for k in range(len(str_val)):
    depart.append(str_val[k][0])
    id.append(str_val[k][2:])

id_list = list(dict.fromkeys(depart))
for j in range(len(id_list)):
    q.append([])
# print(q.items)
for i in range(len(str_oper)):
    if str_oper[i][0] == "E":
        for j in id:
            if str(str_oper[i][2:]) == j:
                oper_id = id.index(j)
                o = 0
                # print(q.items)
                while o < (len(q.items) - 1):
                    if q.items[o] == [] and q.items[o + 1] != []:
                        q_depart.pop(o)
                        q.items.pop(o)
                        q.items.append([])
                        o = -1
                    o += 1
                # print(q.items)
                
                if depart[oper_id] not in q_depart:
                    q_depart.append(depart[oper_id])
                # print(q.items)
                # print(q_depart)
                oper_depart = int(q_depart.index((depart[oper_id])))
                break
        q.items[oper_depart].append(str_oper[i][2:])
    elif str_oper[i][0] == "D":
        # print(q.items)
        if q.items.count([]) == q.size():
            print("Empty")
        else:  
            print(q.get())