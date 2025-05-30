# Dinosaur Runner Game

A simple endless runner game built with Python and Pygame. Control a dinosaur to jump over cactuses and dodge birds, just like the classic Chrome offline Dino game.

---

## 📋 Prerequisites

- **Python 3.7+**  
- **Pygame** library (version 2.0+ recommended)  
- A folder containing the image assets 

---

## 🚀 Installation

pip install pygame


## How It Works
**Player (Dinosaur) Class**

Handles running, jumping, and ducking animations.

Uses a step_index counter to cycle between two frames for running/ducking.

When jumping, vertical velocity is decreased over time to simulate gravity.

**Obstacle Classes**

SmallCactus and LargeCactus inherit from a base Obstacle class.

Each cactus type randomly selects one of three image variants.

Bird alternates between two frames to simulate flapping wings.

**Cloud Class**

Spawns off-screen to the right with a random y-position.

Moves left at the same speed as the ground, then respawns further right once off-screen.

**Game Loop (main() function)**

Initializes global variables: game_speed, x_pos_bg, y_pos_bg, points, and obstacle list.

Each frame:

Clear screen with white background.

Read keyboard input for jump/duck.

Update and draw the dinosaur.

Spawn/Update/Draw obstacles. Collision triggers game over.

Draw scrolling background (ground) by blitting two copies of Track.png.

Update and draw cloud.

Increment and render score; speed increases every 100 points.

Cap frame rate at 30 FPS using pygame.time.Clock().

**Menu & Restart**

On game over, display “Press any Key to Restart” and final score.

Wait for a keypress to call main() again.

