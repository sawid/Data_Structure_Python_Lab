str = input("*** Reading E-Book ***\nText , Highlight : ")
str_list = []
str_list = str.split(",")
string = []
string = str_list[1]
for i in str_list[0]:
    if i == str_list[1]:
        print("[",i,"]",sep="",end="")
    else:
        print(i,end="")
        
    #โฟกโหดเกิน
    #หวัดดีโฟค 