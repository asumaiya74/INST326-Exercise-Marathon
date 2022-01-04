import players as pl

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
        bp = pl.BluePlayer(b)
        lst.append(bp)
    for i in range(3):
        r = "RedPlayer"+str(i+1)
        rp = pl.RedPlayer(r)
        lst.append(rp)
    
    while True:
        for item in lst:
            if item.position >=1000:
                counter =counter + 1
                tup = (item.name,counter)
                return tup
            else:
                item.walk()
                counter = counter + 1
                
if __name__ == "__main__":
    """
    Prints the winner of each game and the total turns
    """
    tup1 = play_game()
    tup2 = pl.play_game()

    print("\n----Marathon Champion----")
    print(f"Winner: {tup1[0]}")
    print(f"Total Turns: {tup1[1]}")

    print("\n-----Champion of small race (players.py)-----")
    print(f"Winner: {tup2[0]}")
    print(f"Total Turns: {tup2[1]}")
