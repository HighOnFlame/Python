words = "Donkey"

with open("Chapter 9/text2.txt" , "r") as f:
    content = f.read()
    
contentnew = content.replace(words,"#######")
    
with open("Chapter 9/text2.txt", "w") as f:
    f.write(contentnew)
    
