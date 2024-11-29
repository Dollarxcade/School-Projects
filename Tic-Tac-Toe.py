
while True:
  try:
    player1 = input("Pick a X or O (X goes first)").lower()
    turn = False
    if player1 == "x":
      turn = True
      player2 = "o"
    elif player1 == "o":
      player2 = "x"
    else:
      print("Please input one of the options")
      continue

    grid = [["*","*","*"],
            ["*","*","*"],
            ["*","*","*"]]
    while True:
      for i in range(3):
        print(grid[i])
      if turn:
        xcord = int(input("Enter the x coordinate (1-3)"))
        ycord = int(input("Enter the y coordinate (1-3)"))
        if grid[ycord-1][xcord-1] == "*":
          grid[ycord-1][xcord-1] = player1
          turn = False
        else:
          print("Pick a spot without *")
        #if((grid[0,0]=="X") and (grid[0,1] =="X") and grid[0,2]
          #print("You won")
          #break
        }
      elif not turn:
        xcord = int(input("Enter the x coordinate (1-3)"))
        ycord = int(input("Enter the y coordinate (1-3)"))
        if grid[ycord-1][xcord-1] == "*":
          grid[ycord-1][xcord-1] = player2
          turn = True
        else:
          print("Pick a spot without *")
      full = True
      for i in range(3):
        for j in range(3):
          if grid[i][j] == "*":
            full = False
            break
      if full:
        break

  except:
    print("Please input one of the options")

#Last updated ∽2023, October
