
fh = open('Try2.txt','a')
for i in range (20):
    fh.writelines("Delete Test%d\n" %i)
    
fh.close()

