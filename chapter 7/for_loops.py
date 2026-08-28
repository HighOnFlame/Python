for i in range(0, 40 , 4):
    if(i==8):
        break #  break from this iteration
    print(i)
    
for i in range(0, 40 , 4):
    if(i==8):
        continue   #skip this iteration
    print(i)


# For loops with lists and else
l = [1,994,454,67,643,534]
for i in l:
    print(i)
    
else:
    print("done")  
  
# output
# 1
# 994
# 454
# 67
# 643
# 534
# done


# For loops with tupples
t = (121,213,"Monu",323,43)
for i in t:
    print(i)    


# For loops with strings
s = "Monu"
for i in s:
    print(i)