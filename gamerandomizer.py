from tkinter import *
from random import randint
from shhh import secret_message


class startup():
  """Open GUI window with 3 options.

  Attributes:
    selected: An integer (1-3) that saves the option chosen.
"""

  selected = ""  # attribute

  def __init__(self) -> None:
      """Initialize windowSetup and run the GUI mainloop."""
      self.windowSetup()
      self.window.mainloop()
      pass

  def windowSetup(self) -> None:
      """Set up the window with three buttons."""
      self.window = Tk()
      self.window.title("What to play")
      self.window.geometry("300x150")

      self.b1 = Button(
          self.window,
          text="option 1",
          command=lambda: [self.selectionOne(),
                           self.window.destroy()])
      self.b1.pack()

      self.b2 = Button(
          self.window,
          text="option 2",
          command=lambda: [self.selectionTwo(),
                           self.window.destroy()])
      self.b2.pack()

      self.b3 = Button(
          self.window,
          text="option 3",
          command=lambda: [self.selectionThree(),
                           self.window.destroy()])
      self.b3.pack()

  def selectionOne(self):
      """Store variable selected as 1.
  
  Returns:
    self.selected
  """
      self.selected = 1
      return self.selected

  def selectionTwo(self):
      """Store variable selected as 2.
  
  Returns:
    self.selected
  """
      self.selected = 2
      return self.selected

  def selectionThree(self):
      """Store variable selected as 3.
  
  Returns:
    self.selected
  """
      self.selected = 3
      return self.selected


class allGames():
  game_lst = ["VALORANT", "TEAMFIGHT TACTICS", "LOL ARAM", "LOL SPECIALMODE", "LOL NORMALS", "mUCK","STARCRAFT2", "NEW GAME","uNrAiLED","Card Hunter","ROTMG","Overcooked! 2", "more coding c:","apex"]
  length = len(game_lst)
  
  def __init__(self) -> None:
    """Initialize windowSetup and run the GUI mainloop."""
    self.windowSetup()
    self.window.mainloop()
    pass

  def windowSetup(self) -> None:
    """Set up the window with three buttons."""
    self.window = Tk()
    self.window.title("All Games")
    self.window.geometry("300x100")

    def randomizer(self):
        index = randint(0, self.length - 1)
        self.game['text'] = self.game_lst[index]
        pass

    self.game = Label(self.window,
                      text="game",
                      fg='white',
                      bg='light blue',
                      font=('Courier', 18, 'bold'),
                      anchor=CENTER)
    self.game.pack()

    self.randomize = Button(self.window,
                            text="RANDOMIZE",
                            command=lambda: randomizer(self))
    self.randomize.pack()

class currentGames():
  game_lst = ["VALORANT", "TEAMFIGHT TACTICS", "LOL ARAM", "LOL SPECIALMODE","STARCRAFT2", "NEW GAME","Card Hunter", "more coding c:"]
  length = len(game_lst)
  
  def __init__(self) -> None:
    """Initialize windowSetup and run the GUI mainloop."""
    self.windowSetup()
    self.window.mainloop()
    pass

  def windowSetup(self) -> None:
    """Set up the window with three buttons."""
    self.window = Tk()
    self.window.title("Current Games")
    self.window.geometry("300x100")

    def randomizer(self):
        index = randint(0, self.length - 1)
        self.game['text'] = self.game_lst[index]
        pass

    self.game = Label(self.window,
                      text="game",
                      fg='white',
                      bg='purple',
                      font=('Courier', 18, 'bold'),
                      anchor=CENTER)
    self.game.pack()

    self.randomize = Button(self.window,
                            text="RANDOMIZE",
                            command=lambda: randomizer(self))
    self.randomize.pack()

class customized():
  game_lst = []
  length = len(game_lst)
  
  def __init__(self) -> None:
    """Initialize windowSetup and run the GUI mainloop."""
    self.windowSetup()
    self.window.mainloop()
    pass

  def windowSetup(self) -> None:
    """Set up the window with three buttons."""
    self.window = Tk()
    self.window.title("Custom")
    self.window.geometry("300x300")

    def randomizer(self):
      index = randint(0, self.length - 1)
      self.game['text'] = self.game_lst[index]
      pass
    
    def addGame(self):
      gameData = self.gameEntry.get()
      gameData = gameData.split(",")
      for x in gameData:
        self.game_lst.append(x)
      self.length = len(self.game_lst)
      pass

    def clearGame(self):
      self.game_lst = []
      self.gameEntry.delete(0,"end")
      self.gameEntry.insert(0, "game")
      self.length = len(self.game_lst)
      pass
      

    self.game = Label(self.window,
                      text="game",
                      fg='white',
                      bg='pink',
                      font=('Courier', 18, 'bold'),
                      anchor=CENTER)
    self.game.pack(padx=5, pady=15, side=TOP)

    self.randomize = Button(self.window,
                            text="RANDOMIZE",
                            command=lambda: randomizer(self))
    self.randomize.pack(padx=5, pady=15, side=TOP)
  
    self.enteredGame = StringVar(self.window,value="game",)
    self.gameEntry = Entry(self.window,textvar=self.enteredGame)
    self.gameEntry.pack(padx=5, pady=5, side=LEFT)
  
    self.add = Button(self.window,text="ADD",command= lambda:addGame(self))
    self.add.pack(padx=0, pady=5, side=LEFT)
  
    self.clear = Button(self.window, text="CLEAR", command = lambda:clearGame(self))
    self.clear.pack(padx=0, pady=5, side=LEFT)
    
if __name__ == '__main__':
  start = startup()
  selection = start.selected
  print(selection)

  if selection == 1:
      allGameWindow = allGames()
  if selection == 2:
      currentGameWindow = currentGames()
  if selection == 3:
      customizedWindow = customized()
    
  secret_message()

# To get a random integer from x to y -> randint(x, y)   *note* x and y will be included in the range
