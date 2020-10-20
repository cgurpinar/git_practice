def write_file(filename, lst):
	with open(f"{filename}.txt", "w") as f:
		print(*lst, sep="\n", file=f)		
		f.close()
		print("\nProcess Completed.\n")

def read_file(filename):
	with open(f"{filename}.txt", "r") as f:
		if f.readable():
			r = f.readlines()
			for line in r:
				print(line.rstrip("\n"))
			print()
		else:
			print("File not found.")
		f.close()

def read_files_x_y(filename, x, y):
	with open(f"{filename}.txt", "r") as f:
		if f.readable():
			r = f.readlines()
			x = x - 1
			while x <= y - 1:
				print(r[x].strip("\n"))
				x += 1
			print()
		else:
			print("File not found.")
		f.close()


exit_ = False

while not exit_:
	print("1. Write the file ('w')\n2. Read the file ('r')\n/exit")
	u_choice = input("> ")

	if u_choice != '':
		if u_choice == "/exit":
			print("\nBye!")
			exit_ = True
		elif u_choice == "1":
			print("\n#	Write the file 		#")
			file_name = input("Enter a filename: ")
			print()
			data_count = abs(int(input("How many processes do?: ")))

			tmp_list = []
			for i in range(data_count):
				strings = input("Enter {}. line: ".format(i + 1))
				tmp_list.append(strings)
			write_file(file_name, tmp_list)

		elif u_choice == "2":
			print("\n# 	Read the file 	#")
			print("1. Read the whole file\n2. Read x to y lines\n/exit")
			u_choice = input("> ")

			if u_choice == "/exit":
				print()
				exit_ = True
			elif u_choice == "1":
				print("\n#	Read the whole file 	#")
				file_name = input("Enter a filename: ")
				print()
				read_file(file_name)	
			elif u_choice == "2":
				print("\n#	Read x to y lines 	#")
				file_name = input("Enter a filename: ")
				x = abs(int(input("Enter the line start: ")))
				y = abs(int(input("Enter the line end: ")))
				print()
				read_files_x_y(file_name, x, y)
			else:
				print("Invalid Assignment!")
		else:
			print("Invalid Assignment!")
