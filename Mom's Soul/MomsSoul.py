#!/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
                              MOM\'S SOUL 
===========================================================================
It was two nights ago...

Your house was attacked by some sort of monsters.

Aliens?

Super natural?

  You don't know and you don't care. You just know the attack left your 
mom in the hospital. She seems awake, her eyes are open and shes 
breathing, but she can not move or speak. The doctors have not found any 
known medical causes.

  Assuming the doctors won't believe you about the monsters, and knowing 
the monsters hold the key to your mothers health, You return to the 
house. You stick the first key in the top lock, and turn it. Then the 
second key in the bottom lock, as you turn the key, you slowly push open 
the door. AS you step into the Hall...

WWWWHHHHAAAAACCCCKKKKK!!!!

  You wake up several hours later, in your basement. You quickly check 
your pockets....

Empty!!!!

  You remember that your dad got you a real sword to hang on your wall, 
last year at the Renaissance Festival. If you can get that, you figure
you might stand a chance against these creatures, get your keys back and 
save your mom.

===========================================================================
Commands:

  go [direction]
  get [item]
  
  --Explore the house using the caommands (go [north,east,west,south])--
  --To use stairs use commands (go [up,down])--
  --Pick up items with command (get[item\'s name])--
  
  Watch out for the monsters if you dont have a weapon!!!
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
rooms = {

            'Hall' : { 
                  'south' : 'Stairs',
                  'east' : 'Dining Room'
                },

            'Kitchen' : {
                  'north' : 'Dining Room',
                  'west' : 'Stairs',
                  'item' : 'monster',
                  'item2' : 'key1'
                },
                
            'Dining Room' : {
                  'west' : 'Hall',
                  'south' : 'Kitchen'
                },
                
            'Stairs'  : {
                  'east' : 'Kitchen',
                  'north' : 'Hall',
                  'up' : '2F Stairs',
                  'down' : 'B1 Stairs'
                },
                
            '2F Stairs' : {
                  'down' : 'Stairs',
                  'north' : '2F Hall',
                  'east' : 'Kid\'s Room'
                },
                
            '2F Hall' : {
                  'south' : '2F Stairs',
                  'east': 'Master Bedroom'
                },
            
            'Kid\'s Room' : {
                  'west' : '2F Stairs',
                  'item' : 'sword'
                },
                
            'Master Bedroom' : {
                  'west' : '2F Hall',
                  'item2' : 'soul',
                  'item' : 'monster'
                },
                
            'B1 Stairs' : {
                  'up' : 'Stairs',
                  'north' : 'B1 North West Corner',
                  'east' : 'B1 South East Corner'
                },
            
            'B1 North West Corner' : {
                  'south' : 'B1 Stairs',
                  'east' : 'B1 North East Corner',
                  'item' : 'monster',
                  'item2' : 'key2'
                },
            
            'B1 North East Corner' : {
                  'west' : 'B1 North West Corner',
                  'south' : 'B1 South East Corner'
                },
            
            'B1 South East Corner' : {
                  'north' : 'B1 North East Corner',
                  'west' : 'B1 Stairs'
                }
         }

#start the player in the Hall
currentRoom = 'B1 South East Corner'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':  
    move = input('>')
    
  move = move.lower().split()

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
  if "item" in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    if 'sword' in inventory:
      del rooms[currentRoom]['item']
      rooms[currentRoom]['item']= rooms[currentRoom]['item2']
      print('''You used your sword to kill the monster!!!!
      ''')
      
      print('''The monster dropped something!!!
      ''')

  
    else :
      print('''AHHHH!!! A MONSTER!!!
---------------------------
 GAME OVER!  GAME OVER!  GAME OVER!''')
      break

  if currentRoom == 'Hall' and 'key1' in inventory and 'key2' in inventory:
    if 'soul' in inventory:
      print('''Congratulations
You escaped the house and returned your mom's soul to her.
      ''')
      
      print('YOU WIN!!!')
      break
    