def num_grid(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] != "#":
                lst[i][j] = 0
    for i in range(len(lst)):
        for j in range(len(lst[i])):
              if lst[i][j] == "#":
                if i == 0:
                      if j == 0:
                            if lst[i][j+1] != "#" : lst[i][j+1] += 1
                            if lst[i+1][j] != "#" : lst[i+1][j] += 1
                            if lst[i+1][j+1] != "#" : lst[i+1][j+1] += 1
                      elif j == 4:
                            if lst[i][j-1] != "#" : lst[i][j-1] += 1
                            if lst[i+1][j-1] != "#" : lst[i+1][j-1] += 1
                            if lst[i+1][j] != "#" : lst[i+1][j] += 1
                      else:
                            if lst[i][j-1] != "#" : lst[i][j-1] += 1
                            if lst[i][j+1] != "#" : lst[i][j+1] += 1
                            if lst[i+1][j] != "#" : lst[i+1][j] += 1
                            if lst[i+1][j-1] != "#" : lst[i+1][j-1] += 1
                            if lst[i+1][j+1] != "#" : lst[i+1][j+1] += 1
                elif i == 4:
                      if j == 0:
                            if lst[i-1][j] != "#" : lst[i-1][j] += 1
                            if lst[i][j+1] != "#" : lst[i][j+1] += 1
                            if lst[i-1][j+1] != "#" : lst[i-1][j+1] += 1
                      elif j == 4:
                            if lst[i-1][j] != "#" : lst[i-1][j] += 1
                            if lst[i][j-1] != "#" : lst[i][j-1] += 1
                            if lst[i-1][j-1] != "#" : lst[i-1][j-1] += 1
                      else:
                            if lst[i-1][j+1] != "#" : lst[i-1][j+1] += 1
                            if lst[i-1][j-1] != "#" : lst[i-1][j-1] += 1
                            if lst[i-1][j] != "#" : lst[i-1][j] += 1
                            if lst[i][j-1] != "#" : lst[i][j-1] += 1
                            if lst[i][j+1] != "#" : lst[i][j+1] += 1
                elif j == 0:
                      if lst[i-1][j] != "#" : lst[i-1][j] += 1
                      if lst[i][j+1] != "#" : lst[i][j+1] += 1
                      if lst[i+1][j] != "#" : lst[i+1][j] += 1
                      if lst[i-1][j+1] != "#" : lst[i-1][j+1] += 1
                      if lst[i+1][j+1] != "#" : lst[i+1][j+1] += 1
                elif j == 4:
                      if lst[i-1][j] != "#" : lst[i-1][j] += 1
                      if lst[i][j-1] != "#" : lst[i][j-1] += 1
                      if lst[i+1][j] != "#" : lst[i+1][j] += 1
                      if lst[i+1][j-1] != "#" : lst[i+1][j-1] += 1
                      if lst[i-1][j-1] != "#" : lst[i-1][j-1] += 1
                else:
                      if lst[i-1][j] != "#" : lst[i-1][j] += 1
                      if lst[i][j-1] != "#" : lst[i][j-1] += 1
                      if lst[i][j+1] != "#" : lst[i][j+1] += 1
                      if lst[i+1][j] != "#" : lst[i+1][j] += 1
                      if lst[i-1][j+1] != "#" : lst[i-1][j+1] += 1
                      if lst[i+1][j-1] != "#" : lst[i+1][j-1] += 1
                      if lst[i-1][j-1] != "#" : lst[i-1][j-1] += 1
                      if lst[i+1][j+1] != "#" : lst[i+1][j+1] += 1
    for i in range(len(lst)):
        for j in range(len(lst[i])):
          if lst[i][j] != "#":
            lst[i][j] = str(lst[i][j])            
    return lst



# lst_input = [

#     ["-","-","-","-","-"],

#     ["-","-","-","-","-"],

#     ["-","-","#","-","-"],

#     ["-","-","-","-","-"],

#     ["-","-","-","-","-"]

# ]

lst_input = []

input_list = input("*** Minesweeper ***\nEnter input(5x5) : ").split(",")

for e in input_list:

  lst_input.append([i for i in e.split()])

print("\n",*lst_input,sep = "\n")

print("\n",*num_grid(lst_input),sep = "\n")
