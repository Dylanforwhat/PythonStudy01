from Test34 import my_str

my_set = {"heima","itheima","itcast","python","heima"}
print(my_set)
print({type(my_set)})

my_set.add("qiuweili")
my_set.add("heima")
print(my_set)

my_set.remove("itcast")
print(my_set)

x = my_set.pop() # 没有下标，随机取
print(x)

my_set.clear()
print(my_set) # set() 空集合

set1 = {1,2,3}
set2 = {1,5,6}
# set3 = set1.difference(set2)
# print(set3)

set1.difference_update(set2)#  在集合1内删除与集合2相同的元素
print(set1) # 修改已有集合
print(set2)

set4 = set1.union(set2)
print(set4)