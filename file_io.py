import os

def write_file(filename, lst):
	with open(f"{filename}.txt", "w") as f:
		print(*lst, sep="\n", file=f)		
		f.close()
		print("\nProcess Completed.\n")

def read_file(filename):
	if os.path.exists(f"{filename}.txt"):
		with open(f"{filename}.txt", "r") as f:
			r = f.readlines()
			for line in r:
				print(line.rstrip("\n"))
			print()
		f.close()
	else:
		print("File not found.\n")
		

def read_files_x_y(filename, x, y):
	if os.path.exists(f"{filename}.txt"):
		with open(f"{filename}.txt", "r") as f:
			r = f.readlines()
			x = x - 1
			while x <= y - 1:
				print(r[x].strip("\n"))
				x += 1
			print()
		f.close()
	else:
		print("File not found.\n")

def append_file(filename, lst):
	if os.path.exists(f"{filename}.txt"):
		with open(f"{filename}.txt", "a") as f:
			print(*lst, sep="\n", file=f)
			f.close()
			print("\nProcess Completed.\n")
	else:
		print("File not found.\n")

def check_file(filename):
	if os.path.exists(f"{filename}.txt"):
		print("\nFile exists.\n")
	else:
		print("File not found\n")

def delete_file(filename):
	if os.path.exists(f"{filename}.txt"):
		os.remove(f"{filename}.txt")
		print("\nProcess Completed.\n")
	else:
		print("File not found.\n")


exit_ = False

while not exit_:
	print("1. Write the file ('w')\n2. Read the file ('r')\n3. Append the file ('a')\n4. Check file\n0. Delete the file\n/exit")
	u_choice = input("> ")

	if u_choice != '':
		if u_choice == "/exit":
			print("\nBye!")
			exit_ = True
		elif u_choice == "1":		    # 1. Write the file ('w')
			print("\n#	Write the file 		#")
			file_name = input("Enter a filename: ")
			print()
			count = abs(int(input("How many processes do?: ")))

			tmp_list = []
			for i in range(count):
				strings = input("Enter {}. line: ".format(i + 1))
				tmp_list.append(strings)
			write_file(file_name, tmp_list)

		elif u_choice == "2":		    # 2. Read the file ('r')
			print("\n# 	Read the file 	#")
			print("1. Read the whole file\n2. Read x to y lines\n/exit")
			u_choice = input("> ")

			if u_choice == "/exit":
				print()
				exit_ = True
			elif u_choice == "1":	    # 2.1. Read the whole file
				print("\n#	Read the whole file 	#")
				file_name = input("Enter a filename: ")
				print()
				read_file(file_name)	
			elif u_choice == "2":	    # 2.2. Read x to y lines
				print("\n#	Read x to y lines 	#")
				file_name = input("Enter a filename: ")
				x = abs(int(input("Enter the line start: ")))
				y = abs(int(input("Enter the line end: ")))
				print()
				read_files_x_y(file_name, x, y)
			else:
				print("Invalid Assignment!")

		elif u_choice == "3":		    # 3. Append the file ('a')
			print("\n#	Append the file 	#\n")
			file_name = input("Enter a filename: ")
			print()
			count = abs(int(input("How many processes do?: ")))

			tmp_list = []
			for i in range(count):
				strings = input("Enter {}. line: ".format(i + 1))
				tmp_list.append(strings)

			append_file(file_name, tmp_list)

		elif u_choice == "4":		    # 4. Check file
			print("\n# 	Check the file 	#\n")
			file_name = input("Enter a filename: ")

			check_file(file_name)

		elif u_choice == "0":		    # 0. Delete the file
			print("\n# 	Check the file 	#\n")
			file_name = input("Enter a filename: ")
			
			delete_file(file_name)

		else:
			print("Invalid Assignment!")
