import os

address = "/Users/samuelevans/Documents/Repos/myrepos/leetcode-solutions/python"

for file in os.listdir(address):
    
    my_split = file.split(" ")
    head, tail = my_split[0], "".join(my_split[1:])
    
    if len(head) < 4:
        head = "0" + head
        
        # os.rename(src, dst) : 
        # src is source address of file to be renamed and dst is destination with the new name.
        src = address + "/" + file
        dst = address + "/" + head + " " + tail
        
        os.rename(src,dst)
        

print(os.listdir(address))