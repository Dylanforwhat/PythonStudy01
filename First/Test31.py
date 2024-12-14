mylist = ["itcast","itheima","pyhont"]
index = mylist.index("itheima")
print(index)

mylist[0] = "education"
print(mylist)

mylist.insert(1,"best")
print(mylist)

mylist.append("last")
print(mylist)

mylist = ["itcast","itheima","pyhont"]
del mylist[2]
print(mylist)

mylist = ["itcast","itheima","pyhont"]
a = mylist.pop(1)
print(mylist)
print(a)

mylist = ["itcast","itheima","pyhont"]
mylist.remove("itcast")
print(mylist)
