from queue import Queue

str_init = input("Enter Input : ").split("/")

str_oper = str_init[1].split(",")
bs = Queue()

list(map(bs.put,str(str_init[0]).split()))

for i in range(len(str_oper)):
    if str_oper[i][0] == "E":
        bs.put((str_oper[i][2:]))
    elif str_oper[i][0] == "D":
        bs.get()

if any(list(bs.queue).count(x) > 1 for x in list(bs.queue)):
    print("Duplicate")
else:
    print("NO Duplicate")