print("Welcome to Treasure Island, your mission is to find the treasure")
leftOrRight = input("Do you want to go left or right?").lower()
print(leftOrRight)

if leftOrRight == "left" :
  swimOrWait = input("Do you want to swim or wait?").lower() 
  
  if swimOrWait == "wait":
    pickColor = input("What color would you pick for a door?").lower()
  
    if pickColor == "red":
      print("You got burned by fire, game over")
    elif pickColor == "yellow" :
      print("You win")
    elif pickColor =="blue" :
      print("You got eaten by a monster")
    else:
      print("Game Over")
  else:
    print("You didn't make it to shore, game over")
else :
  print("Fall in a hole, game over")
