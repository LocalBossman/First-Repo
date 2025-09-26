#Dictionary of Players stats
hero_stats = {
    "name" : "hero", # key : value (name -> key) : (hero -> value)
    "strength" : 7,
    "health" : 100.0,
}

hero_attacks = {
    "Cut" : 10, 
    "Slash" : 15,
    "Slam" : 50,
}

#Game ends
def quit ():
    print ("you chose to Flee\n")
    print ("Game over!")
    return False

#Lists Players stats
def player_stats ():
    for key, value in hero_stats.items():
        print(f"{key} : {value}")

def player_move():
    pass

def player_attack():
    pass


isPlaying = True

#Asks Player for their name
hero_stats["name"] = input ("what is your name?\n").lower()

#Displays Players stats after the player enters their name
player_stats()

#Plays different type of actions
while (isPlaying):

    action = input("\nSelect Action: Slop, Suck & twist\n").lower()

    print (f"Player Action: {action}")

    if(action == "suck"):
       isPlaying = quit()
    elif(action == "slop"):
        player_attack()
    elif(action == "twist"):
        player_move()
    else:
        print (f"{action} is an invalid action")

print ("End Of Loop")