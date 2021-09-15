class Queue:
    
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enqueue(self,data):
        self.items.append(data)

    def dequeue(self):
        if len(self.items) <= 0:
            return "the Queue is Empty"
        else:
            return self.items.pop(0)

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return -1

    def clear(self):
        self.items = []

nor,mir = input("Enter Input (Normal, Mirror) : ").split()

normal_q = Queue()
mirror_q = Queue()
temp_q = Queue()
output_q = Queue()

defuser = []

for x in nor:
    normal_q.enqueue(x)
for x in mir[::-1]:
    mirror_q.enqueue(x)

while True:
    pop = False
    while mirror_q.size() > 0 or temp_q.size() > 0:
        if temp_q.size() < 3 and mirror_q.size() > 0:
            temp_q.enqueue(mirror_q.peek())
            mirror_q.dequeue()
        elif all(element == temp_q.items[0] for element in temp_q.items) and temp_q.size() == 3:
            defuser.append(temp_q.peek())
            for j in range(3):
                temp_q.dequeue()
            pop = True
            for i in mirror_q.items:
                output_q.enqueue(i)
            mirror_q.clear()
            for i in output_q.items:
                mirror_q.enqueue(i)
            output_q.clear()
            break
        else:
            output_q.enqueue(temp_q.peek())
            temp_q.dequeue()

    if not pop:
        if temp_q.size() > 0:
            for i in range(temp_q.size()):
                output_q.enqueue(temp_q.peek())
                temp_q.dequeue()
        break
for i in output_q.items:
    mirror_q.enqueue(i)

output_q.clear()
mir_pop = len(defuser)
fail = 0
nor_pop = 0
while True:
    pop = False
    while normal_q.size() > 0 or temp_q.size() > 0:
        if temp_q.size() < 3 and normal_q.size() > 0:
            temp_q.enqueue(normal_q.peek())
            normal_q.dequeue()
        elif temp_q.size() >= 3 and len(defuser) > 0:
            if all(element == temp_q.items[0] for element in temp_q.items) and temp_q.size() >= 3:
                temp_q.items.insert(2, defuser[0])
                defuser.pop(0)
                pop = True
                if temp_q.items[0] == temp_q.items[1] == temp_q.items[2]:
                    for j in range(3):
                        temp_q.dequeue()
                    fail += 1
                    break
                else:
                    for j in range(temp_q.size()):
                        output_q.enqueue(temp_q.peek())
                        temp_q.dequeue()
                    break
            else:
                output_q.enqueue(temp_q.peek())
                temp_q.dequeue()
        else:
            if all(element == temp_q.items[0] for element in temp_q.items) and temp_q.size() == 3:
                pop = True
                for j in range(3):
                    temp_q.dequeue()
                nor_pop += 1
                for i in normal_q.items:
                    output_q.enqueue(i)
                normal_q.clear()
                for i in output_q.items:
                    normal_q.enqueue(i)
                output_q.clear()
            else:
                output_q.enqueue(temp_q.peek())
                temp_q.dequeue()
    if not pop:
        if temp_q.size() > 0:
            for i in range(temp_q.size()):
                print(output_q.items)
                output_q.enqueue(temp_q.peek())
                temp_q.dequeue()
        break
for i in output_q.items:
    normal_q.enqueue(i)
output_q.clear()
print("NORMAL :")
print(normal_q.size())
if normal_q.size() == 0:
    print("Empty")
else:
    print(*(e for e in normal_q.items[::-1]),sep='')
print(nor_pop,"Explosive(s) ! ! ! (NORMAL)")
if fail > 0:
    print("Failed Interrupted",fail,"Bomb(s)")
print("------------MIRROR------------")
print(": RORRIM")
print(mirror_q.size())
if mirror_q.size() == 0:
    print("ytpmE")
else:
    print(*(e for e in mirror_q.items[::-1]),sep='')
print("(RORRIM) ! ! ! (s)evisolpxE",mir_pop)