import random

# Random is going to be the attack thingy. :(
name = input("Hello user, welcome to my choose your own adventure! What is your name? ")
choice = input(
	"Well hello {}, which adventure would you like to try?\n\t1. Escaping the prison \n\t2. Robbing the bank \n\t3. Going to the moon ".format(
		name))
if choice == ("1"):
	inventory = []
	input("You chose 1: Escaping the prison.\nPress enter to continue")
	input(
		"You got falsely accused of murder and they won. As you get escorted to your cell, you hear the prisoners shouting and banging on their cells.\nPress enter to continue ")
	input("You promptly try to get some sleep.\nPress enter to continue")
	print("------------ DAY 1 --------------")
	choice1 = input(
		"You get to the cafeteria and see someone get stabbed. Do you \nA. Start a riot\nB. Report him to the guards\nC.Do nothing ")
	if choice1 == "a":
		input("When you try to start the riot, one of the prison gangs approach you.\nPress enter to continue ")
		input("A newblood trying to start chaos, I like that. Would you like to join our gang? ")
		gangchoice = input("Do you a: Join them or b: Decline. ")
		if gangchoice == 'a':
			input("Great, welcome to the executioners.")
			print("But don't think that we will let you in that easy. You have to do a task for us.")
			task = input("Will you accept the task?\nA. Yes\B. No")
			if task == 'a':
				input('Ok, your task is to try to find a knife for us.\nPress enter for continue')
				input(
					"You can either go pickpocket one of the guards, loot someone else's cell, or get materials to make one.")
				knifetask = input("Do you pick a, b, or c?")
				if knifetask == "a":
					input("You get one of the gang members to make a distraction, and you try to steal the knife.")
					number = random.randint(1, 10)
					attack = int(input("Please input a number 1-10."))
					if attack > number:
						input(
							"Congratulations! You successfully pickpocket the guard and you retreat back to your base.\nPress enter to continue...")
						inventory.append("knife")
						# This adds the knife to the list 'inventory' which is your inventory in the game.
						print('Congratulations you got the knife!')
						print("{} are the items in your inventory.".format(inventory))
						input("Nice job kid. you're in.\nPress enter to continue...")
						input("---------- DAY 2 -----------\nPress enter to continue...")
						input(
							"You wake up and one of the prisoners grab a knife and they try to stab you.\nPress enter to continue...")
						defensechance = input("Do you use something to defend yourself, or run away?\nPick a or b")
						if defensechance == "a":
							defenseanswer = random.randint(1, 10)
							defending_attack = int(input("Please pick a number 1-10"))
							if defending_attack > defenseanswer:
								input(
									"You stab him and he yells in pain. You feel like you have changed.\nYou don't feel anything as he slowly dies.")
								input(
									"Suddenly, everything fades to a bright white color. You hear an unknown voice.\nPress enter to continue...")
								input("Hello. You may be wondering what just happened.\nPress enter to continue...")
								input(
									"Well, we'll tell you. We have been studying you for the last view years, and you seemed like the right candidate for our test.\nUnfortunately, this test has revealed your true colors. We will now have to keep you for containment and study.\nPress enter to continue...")
								input("ENDING UNLOCKED: True Colors\nPress enter to continue...")
					elif attack < number:
						print('"Hey! What do you think your doing?" The guard says.')
						input(
							"You get sentenced to solitary confinement for the rest of your sentence..\nPress enter to continue...")
						print("GAME OVER.")
					else:
						input("Please input a valid answer. \nPress enter to exit.")
				if knifetask == "b":
					lootchoice = input(
						"You try to find a cell to loot and you see an open drawer. Do you approach it?\nType y or n")
					if lootchoice == ("y"):
						attackoption = input(
							"As you walk to the drawer, a prisoner approaches you. Hey! What do you think your doing! he says. Do you \n1. Use your fists or \n2. Run away in fear ")
						if attackoption == "1":
							attackchance = random.randint(1, 10)
							attackchance1 = int(input("Please pick a number from 1-10 in order to attack"))
							if attackchance1 > attackchance:
								input(
									"You successfully attack the prisoner and snatch his knife. After, you stab him repeatedly and flee the scene.")
								inventory.append("knife")
								print("The following items are in your inventory now.{}".format(inventory))
								knifechoice = input(
									"Do you \na: Take the knife for youreslf and try to murder the leader of the prison gang.\nnOr b: use the blood on the knife frame another prisoner and possibly be paroled.")
								if knifechoice == "a":
									input(
										'You go to the courtyard where your gang is staying. Everyone is looking at you, and they know you have a weapon.\nPress enter to continue...')
									killchoice = int(input(
										"Please input a number 1-10. You MUST get the exact number. Choose wisely..."))
									killchoicenumeral = random.randint(1, 10)
									if killchoice == killchoicenumeral:
										input(
											'You manage to stab the leader of the gang in the eye, and he dies shortly after.\nPress enter to continue...')
										input("You run away, but you drop your knife.")
										del inventory[0:1]
										print("These are now the items in your inventory.{}".format(inventory))
										finalchoice = input(
											"The whole gang is chasing you, and the guards are as well.\nDo you a: turn yourself in\n or b:break into the armory and go guns blazing")
										if finalchoice == "a":
											input(
												"In a last resort to stay alive, you go into the armory and get as many guns as you can. You start shooting"
												".You manaage to shoot some cops, but in the end you get gunned down.\nAchievement unlocked: GUNS BLAZING\nPress enter to exit")
									elif killchoice != killchoicenumeral:
										input(
											"You miss the attack, and the whole gang starts to beat you to death.\nAchievement unlocked: UNFORTUNATE\nPress enter to exit")
							elif attackchance1 < attackchance:
								input(
									"You miss the punch, and he promptly stabs you to death.\n------------ DIED ------------\nPress enter to exit. ")
							else:
								input("Please input a valid answer\nPress enter to exit. ")
				elif knifetask == "c":
					input("You go to the cafeteria and you get some of the straws.'This could make a handle' You think.\nPress enter to continue...")
					inventory.append("straw")
					input("These are now the items in your inventory : {}".format(inventory))
					material_choice = input("You can either\nA. Keep searching in the cafeteria, \nB. to the courtyard to find glass shards")
					if material_choice == "a":
						input("You keep searching in the cafeteria, but you find no materials\nPress enter to continue...")
						input("Suddenly, you spot a knife near the kitchen. You grab it.\nPress enter to continue...")
						inventory.append("knife")
						input("These are now the items in your inventory: {}".format(inventory))
						input('You report back to the gang and you get the knife\nPress enter to continue...')
						input('"Nice job kid, you\'re in"\nPress enter to continue')
						input('You live out the rest of your sentence with the gang, and you die with them.\nACHIEVEMENT UNLOCKED: EXECUTIONERS 4 LYFE\nPress enter to continue...')
					if material_choice == "b":
						input("You go to the courtyard and you see someone selling glass shards.\nPress enter to continue...")
						input("What do you have for trade?\nPress enter to continue.")
						input('All you have is a straw, so you say you have nothing.\nPress enter to continue...')
						input("He plunges the shard into your heart, and you have nobody to save you as you slowly bleed out.\nACHIEVEMENT UNLCOKED: 'BARGAINER'\nPress enter to exit")
		elif gangchoice == 'b':
			print("You don't want to join us? Well, we'll show you how it feel to be an outsider.")
			print("As they beat you to death, the last thing you see are the crazed smirks of the gang members.")
			input("--------- YOU DIED  -----------\nPress enter to exit.")
	elif choice1 == "b":
		input(
			"You quickly report the unnamed inmate to the guards, and they thank you for your cooperation. But the other prisoners beg to differ..\nPress enter to continue...")
		namechoice = input("Hey punk, what's your name? One of the prisoners ask you.")
		if namechoice != name:
			input(
				'Wow. Your name is not {0}, its {1}. I can see it on your uniform. You scared or what?\nPress Enter to continue...'.format(
					namechoice, name))
			fightflightchoice = input("Do you a. Run away from him or b. Get into a fistfight with him.")
			if fightflightchoice == "a":
				input("You start running but you trip, and the prisoner grabs you.\nPress enter to continue...")
				input(
					"Did you really think that you could run away? What an idiot. After he catches you, all the other prisoners start ganging up on you and you get killed.\nACHIVEMENT UNLOCKED: PANSY")
			if fightflightchoice == "b":
				flightflightanswer = random.randint(1, 10)
				flightflightquestion = int(input("Pick a number 1-10 for your attack."))
				if flightflightquestion < flightflightanswer:
					input(
						"You miss the punch and he punches you in the face. You yell in pain, and he beats you to death.\nPress enter to exit.")
				elif flightflightquestion > flightflightanswer:
					input("You punch him in the face and he runs away.\nPress enter to continue")
					input(
						"After that encounter, some of the prisoners so be very suspicious to you.\nPress enter to continue...")
					guardchoice = input(
						"The guards offer you a choice. You can either stay under their protection and be far away from the rest of the prisoners, or live out the rest of your sentence like normal?\nPick a or b")
					if guardchoice == "a":
						input(
							"The guards thank you for your trust in them and they take you to solitary confinement.'Wait! thats not what I meant! you try to say, but by then you've already been locked away forever.'\nACHIVEMENT UNLOCKED Teacher's pet\nPrese enter to exit")
					if guardchoice == "b":
						input(
							'You tell the guards that your not interested, and they reply saying: "Really? You think that you will last a second out there? Well dont come crying to us once the stab you to death."\nPress enter to continue')
						print("--------- DAY 2 --------")
						input(
							"You wake up and the guards lead to to the cafeteria. You get your lunch, but all of the other prisoners are looking at you with faces of disgust.\nPress enter to continue")
						input(
							"After lunch is done, you get 1 hour of free time to spend in the courtyard\nPress enter to continue")
						input(
							"When you are walking out of the prison, you hear a gunshot and it grazes right past your ear.\nPress enter to continue")
						input(
							"After the gun shoot another prisoner, all of the others start to scatter and make chaos. The guards try to defend the armory, but the sheer amount of prisoners topple them.\nPress enter to continue...")
						escape_choice = input("You have 2 options. You can either go with the prisoners to escape using guns from the armory, or go down to a tunnel system under the prison.\nInput 1/2")
						if escape_choice == '1':
							final_escape = input("You get to the the armory and you get a rifle. Almost all the guards are dead, but the remaining ones are staying to defend at the gate.\nDo you a. Rush the gate with your fellow inmates, or b. Find a differnt way to escape")
							if final_escape == "a":
								input("You and the others start to push the gate, and quickly you hear gunshots all around you. People are dying next to you, but the prisoners are still determined.\nPress enter to continue")
								detain_choice = int(input("A guard grabs you by your shirt and attemps to detain you.\nPick a number 1-10 in order to escape"))
								detain_number = random.randint(1,10)
								if detain_choice > detain_number:
									input("You manage to break free and you shoot him down.\nPress enter to continue...")
									input("One of the other prisoners got ther guard to open the gate, and you all escape.\nACHIEVEMENT UNLOCKED: ESCAPEE")
								elif detain_choice < detain_number:
									input("You try to break free from the guards grasp, but he still shoots you down.\nACHIEVEMENT UNLOCKED: So close")

			elif namechoice == name:
				input("Ok {}, do you know what happens to snitches around here?\nPress enter to continue...")
				input("They die out pretty quickly.\nPress enter to continue")
				life_choice = input("As the prisoners slowly creep up to you, you have 2 options. You can \nA. Run away from the prisoners\nB.Fight back")
				if life_choice == "a":
					input("You try to run away from the prisoners, but you fall and they catch you.\nACHIEVEMENT UNLOCKED: NARC\nPres enter to exit.")
				elif life_choice == "b":
					attackpick = int(input("Please input a number 1-10"))
					attackpickanswer = random.randint(1,10)
					if attackpick == attackpickanswer:
						input("You manage to attack one of them, but you were outnumbered.\nAchieved unlocked: What were you thinking?\nPress enter to exit.")
					else:
						input("You miss your attack and you die.")












	elif choice1 == "c":
		input("You decide to do nothing")
		input("ACHIEVEMENT UNLOCKED: Really?")
	else:
		input("Please enter a valid option.\nPress enter to exit.")
elif choice == '2':
	print("Placeholder")
elif choice == "3":
	print("placeholder")
else:
	input("Please input a valid answer.\nPress enter to exit.")
