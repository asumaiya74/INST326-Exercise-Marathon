import random

class Player:
    """
        A class to represent the Player playing the game. 
        It takes in name and position of the player.

        Args:
            name(str): number of the player
            position(int): represents how many miles they are along a trail; setting it to 0
        """
    #init method
    def __init__(self,name):
        self.name = name
        self.position = 0


class RedPlayer(Player):
    """
    A class that represents the RedPlayer playing the game. 
    It change the position of object steps randomly (1,10).

        Parameter: Red Player

        Returns: N/A
    """

    def __init__(self,name):
         Player.__init__(self,name)


    def walk(self):
        x = random.randint(1,10)
        self.position = self.position + x
   


class BluePlayer(Player):
    """
    A class that represents the BluePlayer playing the game. 
        It change the position of object steps randomly (4,8).

        Parameter: Blue Player

        Returns: N/A   
    """

    def __init__(self,name):
        Player.__init__(self,name)
  
        #walk method
    def walk(self):
        x = random.randint(4,8)
        self.position = self.position + x
    



def play_game():
    """
    Performs the way the players will move by making them walk
    A list that will contain 3 instances of BluePlayer and 
    3 instances of RedPlaye
    
    Returns: 
        tuple(list): The winner and the count of the game    
    """
    counter = 0
    lst = []
    for i in range(3):
        b = "BluePlayer"+str(i+1)
        bp = BluePlayer(b)
        lst.append(bp)
    for i in range(3):
        r = "RedPlayer"+str(i+1)
        rp = RedPlayer(r)
        lst.append(rp)
    
    while True:
        for item in lst:
            if item.position >=100:
                counter =counter + 1
                tup = (item.name,counter)
                return tup
            else:
                item.walk()
                counter = counter + 1


if __name__ == "__main__":
    """
    Prints the winner and the total turns
    """
    x = play_game()
    print(f"Winner: {x[0]}")
    print(f"Total Turns: {x[1]}")
