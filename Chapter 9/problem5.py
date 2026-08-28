words = ["Donkey","Monkey","Cow"]

with open("Chapter 9/text2.txt") as f:
    content = f.read()
    
for word in words:
    content = content.replace(word, "#" * len(words))
    
with open("Chapter 9/text2.txt", "w") as f:
    f.write(content)
