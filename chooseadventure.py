name = input("Hello user, welcome to my choose your own adventure! What is your name?")
choice = input("Well hello {}, which adventure would you like to try?\n\t1. Escaping the prison \n\t2. Robbing the bank \n\t3. Going to the moon ".format(name))
if choice == str(1):
	input("You chose 1: Escaping the prison.\nPress enter to continue")
	input("You got falsely accused of murder and they won. As you get escorted to your cell, you hear the prisoners shouting and banging on their cells.\nPress enter to continue")
	input("You promptly try to get some sleep.\nPress enter to continue")
	print("------------ DAY 1 --------------")
	choice1 = input("You get to the cafeteria and see someone get stabbed. Do you \nA. Start a riot\nB. Report him to the guards\nC.Do nothing")
	if choice1 == casefold("a"):
		input("When you try to start the riot, one of the prison gangs approach you.\nPress enter to continue")
		input("A newblood trying to start chaos, I like that. Would you like to join our gang?")
		gangchoice = input("Do you a: Join them or b: Decline.")
		if gangchoice == 'a':
			input("Great, welcome to the executioners.")
			print("But don't think that we will let you in that easy. You have to do a task for us.")
			task = input("Will you accept the task?\nA. Yes\B. No")
			if task == casefold('a')
				input('Ok, your task is to ')
		elif gangchoice == 'b':
			print("You don't want to join us? Well, we'll show you how it feel to be an outsider.")
			print("As they beat you to death, the last thing you see are the crazed smirks of the gang members.")
			print("--------- YOU DIED  -----------")
	elif choice == "b":
		print("PLaceholder")
	elif choice == "c":
		print("Placeholder")
	else:
		print("Please enter a valid option. Exiting program...")
