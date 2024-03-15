#Write a Python program to list only directories, files and all directories, files in a specified path.
import os

path = r'C:\Users\Hp\Desktop'

for i in os.listdir(path):
    if os.path.isdir(os.path.join(path,i)):
        print(i)
print('------------------------------------------------------------------\n')

for i in os.listdir(path):
    if not os.path.isdir(os.path.join(path,i)):
        print(i)

print('------------------------------------------------------------------\n')

for i in os.listdir(path):
    print(i)




#Write a Python program to check for access to a specified path. 
    #Test the existence, readability, writability and executability of the specified path
    


    import os
p=os.listdir(r'C:\Users\Hp\Desktop\pp2labs\Lab6\dir-and-files.py')

print('It exists: ', os.access(__file__, os.F_OK))
print('It is readable: ', os.access(__file__, os.R_OK))
print('It is writable: ', os.access(__file__, os.W_OK))
print('Its executable: ', os.access(__file__, os.X_OK))


#Write a Python program to test whether a given path exists or not. 
 #If the path exist find the filename and directory portion of the given path.

import os
p=(r'C:\Users\Hp\Desktop\pp2labs\Lab6\dir-and-files.py')

if os.path.exists(p):
    print("filename and directory portion of the given path")
    print(os.path.basename(p))
    print(os.path.dirname(p))
else:
    print("Doesnt exist")



#Write a Python program to count the number of lines in a text file.

a=open(r"C:\Users\Hp\Desktop\pp2labs\Lab6\atxt.txt")
cnt=0
for lines in a:
    cnt+=1
print(f"Lines: {cnt}")

#Write a Python program to write a list to a file.


p=open(r"C:\Users\Hp\Desktop\pp2labs\Lab6btxt.txt", "a")
a=["a", "b", "c"]
for i in a:
    p.write(i)



#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

for i in range(65, 65+26):
   filename = chr(i)+'.txt'
   with open(chr(i) + ".txt", "w") as file:
        file.writelines(chr(i))


#Write a Python program to copy the contents of a file to another file


with open('A.txt','r') as firstfile, open('B.txt','a') as secondfile:
    for line in firstfile:
             secondfile.write(line)



#Write a Python program to delete file by specified path. 
#Before deleting check for access and whether a given path exists or not.
             
import os

if os.path.exists('A.txt'):
    os.remove('A.txt')