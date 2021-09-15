n = input("Enter All Bid : ").split(" ")
for i in range(len(n)):
    n[i] = int(n[i])
if len(n) < 2:
    print("not enough bidder")
else:
    max_num = max(n)
    counter = 0
    for i in n:
        if i == max_num:
            counter += 1
    if counter > 1:
        print("error : have more than one highest bid")    
    else:
        n.sort()
        print("winner bid is ", max_num , " need to pay " , n[len(n) - 2] ,sep="")