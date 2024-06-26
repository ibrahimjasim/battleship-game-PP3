# Battleship game
![pp3 am i](https://github.com/ibrahimjasim/battleship-game-PP3/assets/127301769/b5b210a5-4b58-46cb-9152-d78dd587e927)
The game Battleship is a Python terminal game that revolves around two players trying to strategically guess and locate the positions of the opponent's ships while keeping the positions of ones own ships hidden. The game is typically played on a grid-based board in which each battleship occupies one cell on the grid. First player to sink all of the opponent's ships is declared winner of the game round. 
The Battleship game site is live, the link can be found [HERE](https://battleship-game-pp3-0cf9d51c9ddd.herokuapp.com/)

## UX
### Why playing the game 
 **Skill Development:**
-  It's a great way to practice strategic thinking and decision-making skills. Players need to guess the locations of ships, which requires logical reasoning and sometimes even pattern recognition.

**Learning Experience:** 
-  For those interested in programming, playing a game developed in Python can be inspiring. It demonstrates how coding skills can be used to create enjoyable, interactive experiences.

**Nostalgia and Fun:** 
-  Battleship has been a popular board game for generations. Playing a digital version can be a nostalgic experience for many, bringing back memories of playing the physical game.

**Convenience:** 
-  Unlike the traditional board game, this digital version doesn't require physical set-up or another person present to play. It's easily accessible and can be played anytime on a computer.

**Educational Tool:**  
-  For educators or parents, this game can be used as a fun way to introduce children to basic programming concepts and logic.

## How to play

**Gameplay:**

-  The game will prompt you to enter coordinates for your guesses. This typically involves specifying a row *(1-8)* and a column *(A-H)*.
-  Enter the coordinates where you think the computer's ships are located. For example, you might enter 1 for the row and A for the column.
-  The terminal will update you on whether your guess was a hit or a miss and display the game boards showing your guesses and the computer's guesses.
-  The game will also handle the computer's turn, making guesses against your ships.

![Screenshot 2024-01-20 114455](https://github.com/ibrahimjasim/battleship-game-PP3/assets/127301769/d88c6c7a-0f14-4a5a-b497-21b2de872ee9)





## Design
<br>

### Wireframe 
![Screenshot 2024-01-20 111233](https://github.com/ibrahimjasim/battleship-game-PP3/assets/127301769/c0dab7d8-e3f4-42ea-a78e-6276c4758d77)



## Features

-  **Grid-Based Gameplay:** The game is played on two 8x8 grids - one for the player and one for the computer. Each grid represents the ocean where ships are hidden.
-  **Ship Placement:** At the start of the game, ships are randomly placed on both the player's and computer's grids. The placement is hidden from the opponent.
-  **Turn-Based Guessing:** Players take turns guessing the location of the opponent's ships by specifying a row and a column (e.g., 1A, 3D).
-  **Hit and Miss Feedback:** After each guess, the game provides immediate feedback. A "hit" indicates a ship is located at the guessed spot, and a "miss" indicates an empty ocean square.
-  **Tracking Shots:** The game keeps track of each player's guesses, marking hits and misses on the grid so players can see their shot history and strategy.
-  ***Winning Condition:*** The objective is to sink all of the opponent's ships. The game ends when either the player or the computer sinks all of the other's ships.
-  **Randomized AI Behavior:** The computer's guesses are randomized, providing an unpredictable opponent.


![pp3](https://github.com/ibrahimjasim/battleship-game-PP3/assets/127301769/1e3615ba-dc5f-45a6-b6e9-076cac535ab1)

### End game 

-  A successful game round, that has been played out till the end, allows the user to view the opponents grid.
-  The score is also written out as well as a message congratulating/comisserating the player. 
-  A feuture allowing the game to be reset in order for the player to enjoy a new round is also presented as an option at the end of a game. 

![pp3 end game](https://github.com/ibrahimjasim/battleship-game-PP3/assets/127301769/3750b939-7059-4b29-ba4c-3d154d8bdc96)



## Testing

### Error Testing

| Verified |  Tested Variables | Description of output |
| ----------- | ----------- |----------- |
|:heavy_check_mark:  | Input random charachters/ space **once** instetad of accepted input data | Program replies with consistent *"Please enter a valid row"* |
|:heavy_check_mark:  | Input random charachters/ space **twice** instetad of accepted input data | Program reples with consistent *"Please enter a valid row"* |
|:heavy_check_mark:  | Input random charachters/ space **multiple times** instetad of accepted input data | Program replies with consistent *"Please enter a valid row"* |
|:heavy_check_mark:  | Correct cell is selected | Selecting **8-C** results in the selected cell to be hit. |
|:heavy_check_mark:  | Guessing same target twice | Selecting **8-C**  twice results in reply: *"You already guessed that"* |
|:heavy_check_mark:  | Guessing outside grid | Selecting **9-M** results in reply: *"Please enter a valid row"* |
|:heavy_check_mark:  | Computer waits for its turn | After finishing the 10 rounds as a player, the compiter had played 9 rounds. Game tied. |

### Validator testing
- **No errors detected from PEP8online.com**
![pep8](https://github.com/ibrahimjasim/battleship-game-PP3/assets/127301769/391d220a-de50-424e-b1e7-1b266f43c3c8)



### Perfomance Testing
- **Using Lighthouse to rate performance on a number of variables**
![Lighthousse pp3](https://github.com/ibrahimjasim/battleship-game-PP3/assets/127301769/00665314-4715-4d80-97c9-77e4efa2068f)


## Technologies Used
### Main Languages Used
- Python
### Frameworks, Libraries & Programs Used
* GitPod - to create my html files & styling sheet before pushing the project to Github.
* GitHub - to store my repository for submission.
* Heroku - to deploy the live version of the terminal.


## Deployment steps 
* Pushed the final project to GitHub
* Created a new Heroku app
* Set the port key in my configvars
* Set the buildpacks to `Python` and `NodeJS`, in that order 
* Connect GitHub as my Deployment method
* Then scroll down to Manual deploy then pressed the Deploy Bransh button

## Bugs
* Hitting enter for the first two inputs causes it to break
* Entering in two letters/numberss causes the game to crash
* Entering in a lower case is not acepted a second time round if the first column entry was invalid
* Game increments one of my turns when the computer plays
* Code get_ship_location() allows for users to enter "567" as a position and continue playing.

## Remaining Bugs
* No bugs remaining



## Credits
- CI material for the given project.
- Wikipedia for rules and logic behind the game.
- Used "copyassignment" as inspiration for functctions.
  
