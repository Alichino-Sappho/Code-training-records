# define 2 classes
class1=set()    # initialize class1
num1=int(input("input the number of class1: ")) 
for i in range(0,num1):
    name = input("input the name of student %d:" %(i+1))
    class1.add(name)    

class2=set()    # initialize class2
num2=int(input("input the number of class2: ")) 
for i in range(0,num2):
    name = input("input the name of student %d:" %(i+1))
    class2.add(name)

# difference=class2-class1
difference = class2.difference(class1)

print("The students in class2 but not class1 are: ")
for item in difference:
    print(item)
