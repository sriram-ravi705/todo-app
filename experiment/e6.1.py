user_name = input("Add new member: ").strip() + "\n"

file = open('../files/user.txt', 'r')
read_file_list = file.readlines()
file.close()
file = open('../files/user.txt', 'w')
read_file_list.append(user_name)
file.writelines(read_file_list)
file.close()
