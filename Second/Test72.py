try:
    f = open('d:/ file','r')
    print(1,end=' ')
except IOError as error:
    print(error.errno)
    print(2)
else:
    f.close()
    print(3,end=' ')