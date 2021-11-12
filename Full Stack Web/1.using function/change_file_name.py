import os
file_list = os.listdir(r'D:\Workspace\Full Stack Web\1.using function\prank')
print(file_list)
for file_name in file_list:
    os.rename(file_name,file_name.translate(None,"0123456789"))
file_list = os.listdir(r'D:\Workspace\Full Stack Web\1.using function\prank')
print(file_list)