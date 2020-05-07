'''
r stands for read only
w stands for write aka write within
a stands for append can add info onto the end but can't change info
r+ is everything
'''


Name_file = open("NamesForReading.txt", "r")

#print(Name_file.readable())
for Name in Name_file.readlines():
    print(Name)
#print(Name_file.readline())


Name_file.close()