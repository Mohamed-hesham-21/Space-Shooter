
# Space Shooter Game

## Introduction

Welcome to **Space Shooter**,my first GUI game project and first game provided in [Clear Code](https://www.youtube.com/watch?v=8OMghdHP-zs&t=11585s)'s video that built using Python and Pygame! This game puts you in the role of a space pilot tasked with shooting down meteors while avoiding collisions. With a simple yet engaging gameplay loop, this project helped me gain hands-on experience in software/game development.

## Game Overview

**Space Shooter** is a 2D arcade-style shooter game where the player controls a spaceship and must shoot down falling meteors to score points. The player can move the spaceship around the screen and fire lasers at incoming meteors. The game ends if a meteor collides with the player's spaceship.

## Features

- **Player Movement**: The player can move the spaceship up, down, left, or right using the arrow keys.
- **Shooting Mechanic**: Pressing the spacebar fires lasers that destroy meteors.
- **Meteors**: Randomly falling meteors with varying speeds and rotations.
- **Score System**: Score increases every time a meteor is destroyed.
- **Background Music**: Continuous background music enhances the gaming experience.
- **Explosion Animation**: An animation plays when a meteor is destroyed.
- **Game Over**: The game ends when a meteor collides with the spaceship.

## How to Play

1. **Move**: Use the arrow keys to move the spaceship around the screen.
2. **Shoot**: Press the spacebar to fire lasers.
3. **Avoid**: Steer clear of meteors to prevent losing the game.

## Installation

To run **Space Shooter** on your local machine, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/space-shooter.git
   cd space-shooter
   ```

2. **Install Dependencies**:
   Ensure you have Python and Pygame installed. You can install Pygame using pip:
   ```bash
   pip install pygame
   ```

3. **Run the Game**:
   Execute the game script using Python:
   ```bash
   python space_shooter.py
   ```

## Code Structure

The game code is organized into the following main components:

- **Player**: Handles the player's spaceship, movement, shooting mechanics, and laser cooldown.
- **Star**: Represents background stars to enhance visual appeal.
- **Laser**: Manages laser projectiles fired by the player.
- **Meteor**: Controls falling meteors with random speed and rotation.
- **Explosion_Animation**: Displays an explosion animation when meteors are destroyed.
- **Display_Score**: Renders the current score on the screen.
- **Collisions**: Checks for collisions between lasers, meteors, and the player.

## What I Learned

Working on this game has been a valuable learning experience. Here are some key takeaways:

- **Game Mechanics**: Implementing core game mechanics such as movement, shooting, and collision detection.
- **Pygame**: Gaining hands-on experience with Pygame for creating 2D games, including handling sprites, events, and animations.
- **Design Patterns**: Using object-oriented programming to structure game components effectively.
- **Timing and Delta Time**: Managing frame-independent movement and actions with delta time.
- **Sound Management**: Incorporating sound effects and background music to enhance the game experience.
- **Debugging**: Troubleshooting and debugging game logic to ensure smooth gameplay.

## Future Improvements

There are several enhancements I plan to add in future updates if time allows:

- **Levels**: Introduce multiple levels with increasing difficulty.
- **Power-Ups**: Add power-ups to give players temporary advantages.
- **High Scores**: Implement a high score system to track and display the best scores.
- **Graphics**: Improve graphics and animations for a more polished look.
- **Menu System**: Add a start menu, pause menu, and game over screen.

## Acknowledgments

### Special Thanks

I would like to extend my heartfelt thanks to:
- **[Clear Code](https://www.youtube.com/@ClearCode)**: For their invaluable support and guidance throughout this project. Your insights and encouragement were crucial in bringing this game to life.

### Learning Resources

I am grateful for the following resources that helped me during the development of this game:

- **[Pygame Documentation](https://www.pygame.org/docs/)**: For providing comprehensive information on how to use Pygame effectively.
- **[Real Python](https://realpython.com/)**: For tutorials and articles on Python programming and game development.
- **YouTube Tutorials by [Clear Code](https://www.youtube.com/@ClearCode)**: For practical, hands-on video tutorials that guided me through Pygame basics and advanced concepts.
- **[nevoprojects](nevonprojects.com)**: For Project idea that helped me to develop this project.



## Acknowledgments

- **Pygame**: For providing the tools to create this game.
- **OpenGameArt**: For the assets used in this game.
