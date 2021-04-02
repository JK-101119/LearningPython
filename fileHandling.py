# f = open('Mydata', 'r')
# print(f)
# print(f.read())
# print(f.readline())

# If the file we want to write does dot exists the Python will it for us.
# fw = open('Mydata2', 'w')
# fw.write("Hi from writing!")
#
# fw = open('Mydata2', 'w')
# fw.write("This is another line form write.")

# Where the 'w' command write new data after deleting there 'a' command append the new data without affecting old data.
# fw = open('Mydata2', 'a')
# fw.write("\nI am a new line.")

# Copying data from one file to another.
# f = open('Mydata', 'r')
# fw = open('Mydata2', 'a')
# for data in f:
#     fw.write(data)

# For reading images we have to use the binary command. The command 'wb' is able to read binary format of image.
# p = open('ImageName.format', 'wb')
