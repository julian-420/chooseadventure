import random
name = input("Hello user, welcome to my choose your own adventure! What is your name?")
choice = input("Well hello {}, which adventure would you like to try?\n\t1. Escaping the prison \n\t2. Robbing the bank \n\t3. Going to the moon ".format(name))
if choice == ("1"):
	inventory = []
	input("You chose 1: Escaping the prison.\nPress enter to continue")
	input("You got falsely accused of murder and they won. As you get escorted to your cell, you hear the prisoners shouting and banging on their cells.\nPress enter to continue")
	input("You promptly try to get some sleep.\nPress enter to continue")
	print("------------ DAY 1 --------------")
	choice1 = input("You get to the cafeteria and see someone get stabbed. Do you \nA. Start a riot\nB. Report him to the guards\nC.Do nothing")
	if choice1 == "a":
		input("When you try to start the riot, one of the prison gangs approach you.\nPress enter to continue")
		input("A newblood trying to start chaos, I like that. Would you like to join our gang?")
		gangchoice = input("Do you a: Join them or b: Decline.")
		if gangchoice == 'a':
			input("Great, welcome to the executioners.")
			print("But don't think that we will let you in that easy. You have to do a task for us.")
			task = input("Will you accept the task?\nA. Yes\B. No")
			if task == 'a':
				input('Ok, your task is to try to find a knife for us.\nPress enter for continue')
				input("You can either go pickpocket one of the guards, loot someone else's cell, or get materials to make one.")
				knifetask = input("Do you pick a, b, or c?")
				if knifetask == "a":
					input("You get one of the gang members to make a distraction, and you try to steal the knife.")
					number = random.randint(1, 10)
					attack = int(input("Please input a number 1-10."))
					if attack > number:
						input("Congratulations! You successfully pickpocket the guard and you retreat back to your base.\nPress enter to continue...")
						inventory.append("knife")
						print('Congratulations you got the knife!')
						print("{} are the items in your inventory.".format(inventory))
						input("Nice job kid. you're in.\nPress enter to continue...")
						print("---------- DAY 2 -----------")
					elif attack < number:
						print('"Hey! What do you think your doing?" The guard says.')
						input("You get sentenced to solitary confinement for the rest of your sentence..\nPress enter to continue...")
						print("GAME OVER.")
					else:
						print("Please input a valid answer. Exiting program.")
				if knifetask == "b":
					lootchoice = input("You try to find a cell to loot and you see an open drawer. Do you approach it?\nType y or n")
					if lootchoice == ("y"):
						attackoption = input("As you walk to the drawer, a prisoner approaches you. Hey! What do you think your doing! he says. Do you \n1. Use ")
						if attackoption == "1":
							attackchance = random.randint(1, 10)
							



		elif gangchoice == 'b':
			print("You don't want to join us? Well, we'll show you how it feel to be an outsider.")
			print("As they beat you to death, the last thing you see are the crazed smirks of the gang members.")
			print("--------- YOU DIED  -----------")
	elif choice1 == "b":
		input("You quickly report the unnamed inmate to the guards, and they thank you for your cooperation. But the other prisoners beg to differ..\nPress enter to continue...")




	elif choice1 == "c":
		print("Placeholder")
	else:
		print("Please enter a valid option. Exiting program...")
