# variables
wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_damage = 150
elf_damage = 100
human_damage = 20


dragon_hp = 300
dragon_damage = 50

#infinite while loop to handle player choices
while True:
    print("1. Wizard")
    print("2. Elf")
    print("3. Human")
    user_choice = input("Choose your character: ")

    if user_choice == "1": # user input
        character = wizard
        my_hp = wizard_hp # declared variable
        my_damage = wizard_damage #declared variable
        break
    if user_choice == "2": 
        character = elf
        my_hp = elf_hp # declared variable
        my_damage = elf_damage #declared variable
        break
    if user_choice == "3": 
        character = human
        my_hp = human_hp # declared variable
        my_damage = human_damage #declared variable
        break
    else:
        print ("Unknown character")

#indent
print("character", "my_hp", "my_damage")
print("You have chosen the character: " + character)
print("Health: " , my_hp)
print("Damage: " , my_damage)

#    (Battle)
while True:
    dragon_hp = dragon_hp - my_damage
    print("The", character, "damaged the Dragon!")
    print("The Dragons's hitpoints are now:",dragon_hp)
    if dragon_hp <= 0:
        print("The Dragon has lost the battle")
        break
    #dragon attack 
    my_hp = my_hp - dragon_damage
    print("The Dragon strikes back at", character)
    print("The", character, "hitpoints are now:", my_hp)
    if my_hp <= 0:
        print("The", character, "has lost the battle.")
        break
