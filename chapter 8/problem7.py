def remove(l,word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n


l = ["Rohan","Sohan","Ranjan","Ravi"]
print(remove(l,"an"))