from random import randrange
critter_names = ["JOHN CENA", "Shrek", "A Troll", "Maymay", "Ur mum", "A Pink guy", "A Roman bust", "A Rampant AI", "A NSA operative", "A Klu Klux Klan Member",
                 "An iPhone user","A Mac user", "Someone wearing a snapback", "Someone wearing an Unknown Pleasures T-shirt who hasn't even listened to the album",
                 "Larry Page","Someone who illegitimately won the NCSS", "A Lad", "An Illuminatus"]
character = {"name": "YUNG LEAN", "armour_name": "Boardies", "armour_rating": 1, "weapon_name": "Meaty fists", "weapon_rating" : 10, "hp": 100}

size = input("How big do you want the map? (recomended between 10 and 20): ")
char_xy = [0,0]
critter_list = {}
door = [randrange(0, int(size)), randrange(0, int(size))]
new_level = True
player_in_range = False
level = 0
def attack(name):
    critter_list[name][2] = critter_list[name][2] - character["weapon_rating"]
def defend(name):
    character["hp"] = character["hp"] - (critter_list[name][3]/character["armour_rating"])
def critter_gen():
    for i in critter_names:
        if randrange(1, 6) == 3:
            critter_list[i] = [randrange(0, int(size)), randrange(0, int(size)), randrange(1, 100), randrange(1, 25)] #[xpos, ypos, hp, attack]
def player_input():
    move = input("It's your move! ")
    if move == "w" and char_xy[0] > 0:
        char_xy[0] -= 1
    elif move == "a" and char_xy[1] > 0:
        char_xy[1] -= 1
    elif move == "s" and char_xy[0] < int(size) - 1:
        char_xy[0] += 1
    elif move == "d" and char_xy[1] < int(size) - 1:
        char_xy[1] += 1
    elif move == "e":
        if door[0] == char_xy[0] and door[1] == char_xy[1]:
            new_level = True
    elif move == "f":
        for i in critter_list:
            if critter_list[i][0] == char_xy[0] and critter_list[i][1] == char_xy[1]:
                attack(i)
                defend(i)
            elif critter_list[i][0] == char_xy[0] + 1 and critter_list[i][1] == char_xy[1] + 1:
                attack(i)
            elif critter_list[i][0] == char_xy[0] - 1 and critter_list[i][1] == char_xy[1] + 1:
                attack(i)
            elif critter_list[i][0] == char_xy[0] + 1 and critter_list[i][1] == char_xy[1] - 1:
                attack(i)
            elif critter_list[i][0] == char_xy[0] - 1 and critter_list[i][1] == char_xy[1] - 1:
                attack(i)
            elif critter_list[i][0] == char_xy[0] and critter_list[i][1] == char_xy[1] + 1:
                attack(i)
            elif critter_list[i][0] == char_xy[0] and critter_list[i][1] == char_xy[1] - 1:
                attack(i)
            elif critter_list[i][0] == char_xy[0] + 1 and critter_list[i][1] == char_xy[1]:
                attack(i)
            elif critter_list[i][0] == char_xy[0] - 1 and critter_list[i][1] == char_xy[1]:
                attack(i)
    else:
        print("That is not a valid move")
def map_gen():
    asc = '-'
    gen = [int(size)*[asc] for i in range(int(size))]
    gen[char_xy[0]][char_xy[1]] = '@'
    for i in critter_list:
        if critter_list[i][2] > 0:
            gen[critter_list[i][0]][critter_list[i][1]] = "M"
        else:
            gen[critter_list[i][0]][critter_list[i][1]] = "X"
    gen[door[0]][door[1]] = "D"
    print('\n'.join(' '.join(row) for row in gen))
def ai():
    for i in critter_list:
        if critter_list[i][2] > 0:
            if critter_list[i][0] == char_xy[0] and critter_list[i][1] == char_xy[1]:
                attack(i)
                defend(i)
                player_in_range = True
            elif critter_list[i][0] == char_xy[0] + 1 and critter_list[i][1] == char_xy[1] + 1:
                defend(i)
                player_in_range = True
            elif critter_list[i][0] == char_xy[0] - 1 and critter_list[i][1] == char_xy[1] + 1:
                defend(i)
                player_in_range = True
            elif critter_list[i][0] == char_xy[0] + 1 and critter_list[i][1] == char_xy[1] - 1:
                defend(i)
                player_in_range = True
            elif critter_list[i][0] == char_xy[0] - 1 and critter_list[i][1] == char_xy[1] - 1:
                defend(i)
                player_in_range = True
            elif critter_list[i][0] == char_xy[0] and critter_list[i][1] == char_xy[1] + 1:
                defend(i)
                player_in_range = True
            elif critter_list[i][0] == char_xy[0] and critter_list[i][1] == char_xy[1] - 1:
                defend(i)
                player_in_range = True
            elif critter_list[i][0] == char_xy[0] + 1 and critter_list[i][1] == char_xy[1]:
                defend(i)
                player_in_range = True
            elif critter_list[i][0] == char_xy[0] - 1 and critter_list[i][1] == char_xy[1]:
                defend(i)
                player_in_range = True
            else:
                player_in_range = False
            if player_in_range == False:
                c_move = randrange(1, 6)
                if c_move == 1 and critter_list[i][0] < int(size) - 1:
                    critter_list[i][0] += 1
                elif c_move == 2 and critter_list[i][1] < int(size) - 1:
                    critter_list[i][1] += 1
                elif c_move == 4 and critter_list[i][0] > 0:
                    critter_list[i][0] -= 1
                elif c_move == 5 and critter_list[i][1] > 0:
                    critter_list[i][1] -= 1
while character["hp"] > 0:
    if new_level == True:
        door = [randrange(0, int(size)), randrange(0, int(size))]
        critter_list = {}
        critter_gen()
        map_gen()
        level += 1
        new_level = False
    elif new_level == False:
        print("N A M E:  " + character["name"])
        print("H E A L T H:  " + str(character["hp"]))
        print("W E A P O N:  " + str(character["weapon_rating"]) + "     " + character["weapon_name"])
        print("A R M O U R:  " + str(character["armour_rating"]) + "     " + character["armour_name"])
        for i in critter_list:
            print("E N E M Y:  " + str(i) + "     " + "H P: " + str(critter_list[i][2]) + "     " + "A T K: " + str(critter_list[i][3]))
        player_input()
        ai()
        map_gen()
        if door[0] == char_xy[0] and door[1] == char_xy[1]:
            new_level = True

print()
print()
print(" ________________________________________________")
print("|    G    A    M    E        O    V    E    R    |")
print(" IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
print()
print("            You Reached L E V E L: " + str(level))