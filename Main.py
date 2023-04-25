email = []
name = []

while True:
	command_user = str(input("Enter 'q' to insert name and email , Enter 'w' to view', Enter 'qw' to exit : "))
	if command_user == "q":
		name_input = str(input("Enter name: "))
		email_input = str(input("Enter email: "))
		email.append(email_input)
		name.append(name_input)
	
	elif command_user == "w":
		"""for i in range(0,len(name)):
			print(name[i],"\n")
			print("\n")

		for i in range(0,len(email)):
			print(email[i],"\n")
			print("\n")"""

		for i in range(0,len(name)):
			for i in range(0,len(email)):
				print("\nEmail id:",email[i],"\nName:",name[i],"\n")

	elif command_user == "qw":
		break

	else:
		print("Wrong Message Try Again")