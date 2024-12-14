try:
    f = open('file','w')
    print(1,end=' ')
except IOError as error:
    print(error.errno,end=' ')
    print(2,end = ' ')
else:
    f.close()
    print(3)