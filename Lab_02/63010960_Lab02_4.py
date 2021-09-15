from typing import Sequence


def sumzero(arr, n):
    seq = []
    found = False
    if n < 3:
        return "Array Input Length Must More Than 2"
    for i in range(0, n-2):
     
        for j in range(i+1, n-1):
         
            for k in range(j+1, n):
             
                if (arr[i] + arr[j] + arr[k] == 0):
                    temp = []
                    temp.extend((arr[i], arr[j], arr[k]))
                    found = True
                    seq.append(temp)
    temp_seq = []
    for elem in seq:
        if elem not in temp_seq:
            temp_seq.append(elem)
    seq = temp_seq
    return seq

arr = list(map(int,input("Enter Your List : ").split()))
n = len(arr)
print(sumzero(arr, n))