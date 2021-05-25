# pip install secure_delete
from secure_delete import secure_delete
from os.path import isdir, isfile 

directory = input("Enter directory or file path: ")
print(directory)

if isdir(directory) or isfile(directory):
    print("Exists")
    delete = input("Delete directory/file? Press y = yes (remove another letter): ")
    if delete == "y":
        secure_delete.secure_random_seed_init()
        secure_delete.secure_delete(directory)
        print("Removed")
    else:
        print("Not removed")       
    
else:
    print("Does not exist")  
