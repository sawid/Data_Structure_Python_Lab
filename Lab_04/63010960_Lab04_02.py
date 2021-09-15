from queue import Queue

str_cashier = input("Enter people and time : ").split(" ")
cashier_list = list(str_cashier[0])
q = Queue()
q1 = Queue()
q2 = Queue()

list(map(q.put,cashier_list))

timer1 = 0
timer2 = 0

for i in range(1,int(str_cashier[1]) + 1):
    if (timer1 != 0) and (timer1%3 == 0) and (not q1.empty()):
        q1.get()
    if (timer2 != 0) and (timer2%2 == 0) and (not q2.empty()):
        q2.get()
    if (q1.qsize() < 5) and (not q.empty()):
        q1.put(q.get())
    elif q2.qsize() < 5 and (not q.empty()):
        q2.put(q.get())
    
    if q1.qsize() > 0:
        timer1 += 1
    elif q1.qsize() == 0:
        timer1 = 0
    if q2.qsize() > 0:
        timer2 += 1
    elif q2.qsize() == 0:
        timer2 = 0
    print(i, list(q.queue), list(q1.queue), list(q2.queue))