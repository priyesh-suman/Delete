
fh = open('Try1.txt','a')
for i in range (20):
    fh.writelines("Hello World%d\n" %i)
    
fh.close()

