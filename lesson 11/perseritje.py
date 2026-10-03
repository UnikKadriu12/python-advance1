"""file = open("example.txt","r")

content + file.read()

print(content)
file.close()



"""

with open("example2.txt","r") as file:
    content = file.read()
    print(content)

#with open("example2.txt","w") as file:
 #   file.write("hello unik")


with open("example2.txt","w") as file:
    file.write("\nhello unik")


if os.path.exists("gg.txt"):
    print("file ekziston")
else:
    print("file nuk ekziston")