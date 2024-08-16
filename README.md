Road-Crossing Game
This Python project is a simple arcade-style game where a player controls a turtle trying to cross a busy road. The player must navigate the turtle from the bottom to the top of the screen while avoiding incoming cars. Each time the turtle successfully crosses the road, the game level increases, making the cars move faster and increasing the challenge.

*Features
Player Movement: The turtle moves forward with the "Up" key, trying to reach the top of the screen.
Car Generation: Cars are randomly generated along the y-axis and move from left to right across the screen.
Collision Detection: If the turtle collides with a car, the game ends, and a "Game Over" message is displayed.
Leveling Up: Each time the turtle reaches the top of the screen, the level increases, and the speed of the cars increases.
Scoreboard: A scoreboard keeps track of the current level.

*How to Play
Use the "Up" arrow key to move the turtle forward.
Avoid the cars as they move across the screen.
Successfully reach the top of the screen to level up.

*Files
player.py: Contains the Player class that controls the turtle's movement.
car_manager.py: Contains the CarManager class that handles car generation and movement.
scoreboard.py: Contains the Scoreboard class to track and display the game level and end-game message.
