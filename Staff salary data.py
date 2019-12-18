filename = "data.txt"
r = open(filename,"r")
f = open("file.txt","a")
text = r.read().replace("\n"," ")
print(text)
text = r.read().replace("#"," ")
data = {"ID":[], "Name":[], "Position":[], "Salary":[]}
i = 0
while i < len(text):
    f.write(text[i])
    i += 1
f.close()
fr = open("file.txt","r")
for i in range(3,len(text), 3):
    data["ID"] = text[i]
print(fr.read())
print(data)