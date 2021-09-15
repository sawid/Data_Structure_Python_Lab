from queue import Queue

queue = Queue()

str_queue = input("Enter Input : ").split(',')
# print(str_wood)
for i in range(len(str_queue)):
    if str_queue[i][0] == "E":
        queue.put((str_queue[i][2:]))
        print("Add ", int(str_queue[i][2:]), " index is ", queue.qsize() - 1,sep="")
    elif str_queue[i][0] == "D":
        if queue.empty():
            print(-1)
        else:
            print("Pop ", queue.get(), " size in queue is ", queue.qsize(),sep="")
if queue.empty():
    print("Empty")
else:
    print("Number in Queue is :  ",list(queue.queue),sep="", end="")
