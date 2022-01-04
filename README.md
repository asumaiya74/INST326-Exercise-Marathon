# Background
For  this  exercise  we  are  going  to  create  a  simple  game.  This  game  will  have  players  that  will  race against each other.However, in order to make this game more interesting, we will create two kinds of players which will both move differently based on the functionality of its class.

# Instructions
- Write a script called **players.py**. This script should contain the following:
  - Write a class called **Player**
    - Write  an  **__init__()**  method.  This  method  should  have  two  parameters,  self  and  name. This method should to the following:
      - Create **name** and a position attributes. Position will be represented by a number. The position represents how many miles they are along a trail
  - Write  a  **RedPlayer**  class  and  a  **BluePlayer**  class.  Both  of  these  classes  should  be  subclasses of Player. These classes should do the following:
  - Write a play_game function. This function should not have any parameters but it should do the following:
  - Write docstrings for each method. (__init__() doesn’t need a docstring.)
  - Make an if __name__ == "__main__": statement in which you call the play_game() function.

- Write a script called **marathon.py**. This script should contain the following:
  - import **players.py**
  - Re-write the **play_game** function. The difference here is that that instead of checking if the position  of  any  instance  is  over  100,  we  will  check  if  the  position  of  any  instance  is  over 1000.
  - Make an **if __name__ == "__main__":** statement in which:
    - You call the **play_game()** function that is in this script and print the result.
    - You  call  the  **play_game()**  function  that  is  in  the  namespace  of  the  module  that  you imported (**players.py**) and print the result. 


# Note
Run the marathon script multiple times. Observe who the winners are when you run the simulation multiple times under the different conditions (pos >= 100 vs pos >= 1000).




