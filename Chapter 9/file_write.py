st = "You should also learn C++."

f = open("Chapter 9/myfile.txt", "w")
f.write(st)
f.close()


f = open("file.txt", "w")

lines = ["Hello\n", "Python\n", "File I/O\n"]

f.writelines(lines)

f.close()