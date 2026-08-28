with open("Chapter 9/poem.txt") as f:
    word = f.read()
    if("twinkle," in word):
        print("Yes")
    else:
        print("NO")