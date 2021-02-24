
fh = open('Try1.txt','a')
for i in range (20):
    fh.writelines("This is Not us %d\n" %i)
    
fh.close()

