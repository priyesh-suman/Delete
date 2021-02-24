
fh = open('Try1.txt','a')
for i in range (10):
    fh.writelines("This is us %d\n" %i)
    
fh.close()

