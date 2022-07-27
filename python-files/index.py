my_file = open("hello-world.txt","a")
my_file.write("\nExample DEVF")
my_file.close()


my_file = open("hello-world.txt","r")
print(my_file.read())
my_file.close()