# Match the Bearcat
## CS 110 Final Project
### Fall, 2018

[Link to repository](https://github.com/binghamtonuniversity-cs110/final-project-fall18-team-snakes)

[Link to demo presentation slides](https://docs.google.com/presentation/d/15Kt6HpzVCmHykP6S2Nbe6jo3G0eQsLWsuvhgI8KlOdk/edit#slide=id.p)

### Team:
#### Team Names
Dyandra Allen, Nickolas De Dios, Aoife McManus, Christian Torres
***

## Project Description

“Match the Bearcat” is a matching game in which the player controls the cursor to match all the cards with their corresponding number. Each card will have a certain number and an exact pair. The player is given a layout of cards which are hidden over white rectangles for the player to know the locations of each number. Then, the player must choose a card and pick the card that corresponds with the same number. The player is given three minutes to solve the whole puzzle. However, if the person picks the wrong match, five seconds are deducted by the timer. The game is over when every pair is matched or if the timer reaches zero. The game does have a high score mechanic based on how many turns it took the player to finish the game.
***    

## User Interface Design


* Main Menu Start Screen
  * The main menu start screen will have a background image, along with a "Start Game" link and a link to the instructions        screen. 
<img src = "https://github.com/binghamtonuniversity-cs110/final-project-fall18-team-snakes/blob/master/projPhotos/firstStart.jpg"  width = "250" height = "250" /> 
  

* Instructions Screen
   * There will a background image with the instructions listed. 
   * Exit link back to main menu.
<img src = "https://github.com/binghamtonuniversity-cs110/final-project-fall18-team-snakes/blob/master/projPhotos/firstInstruction.jpg" width = "250" height = "250" /> 

* Game Screen
   * Where the game takes place.
   * Cards dispersed across screen. 
   * There will be a score tracker (the number of turns) and a timer. 
   * The game is exited when all the cards have been matched or the timer is done. 
   * If user clicks on two non-matching cards, the numbers on the card disappears and the game continues.
   * There is a "give up" button that goes to the Game Over Screen in case the player wants to end the game early.
<img src = "https://github.com/binghamtonuniversity-cs110/final-project-fall18-team-snakes/blob/master/projPhotos/firstGameScreen.jpg" width = "250" height = "250" /> 

* Game Over Screen
   * This screen appears when the timer reaches zero. 
   * From here, you have the option to play the game again by clicking "play again", return to the start screen by clicking "main menu", or exit out of the game by clicking "quit". 
<img src = "https://github.com/binghamtonuniversity-cs110/final-project-fall18-team-snakes/blob/master/projPhotos/firstGameOver.jpg" width = "250" height = "250" /> 


* Final GUI interface
<img src = "https://github.com/binghamtonuniversity-cs110/final-project-fall18-team-snakes/blob/master/projPhotos/mainmenuscreen.JPG"/> 

<img src = "https://github.com/binghamtonuniversity-cs110/final-project-fall18-team-snakes/blob/master/projPhotos/instructionscreen.JPG"/> 

<img src = "https://github.com/binghamtonuniversity-cs110/final-project-fall18-team-snakes/blob/master/projPhotos/gamescreen.JPG"/> 

<img src = "https://github.com/binghamtonuniversity-cs110/final-project-fall18-team-snakes/blob/master/projPhotos/winscreen.JPG"/> 

<img src = "https://github.com/binghamtonuniversity-cs110/final-project-fall18-team-snakes/blob/master/projPhotos/gameoverscreen.JPG"/> 

***        

## Program Design

### Non-Standard Libraries and Modules Used
* **Pygame** (https://www.pygame.org/)-  A module set incorporating many common game development functions into python, developed by Pete Shinners and Pygame Community. Includes crucial graphical elements as well as a musical playback functionality.	

### Class and File Relationships (Flowchart)

<img src = "https://github.com/binghamtonuniversity-cs110/final-project-fall18-team-snakes/blob/master/projPhotos/class%20flow%20chart%20(2).jpg" width = "700" height = "550" /> 
    
### List of Classes
* Card - A class that defines the cards within the game - white rectangular shapes. It contains functions such as the location of each card, the placement of numbers for each card and the placement for white rectangles. 
* Timer - A class that defines the timer within the game screen - sets the timer when called in the game screen function. It contains functions that determine whether or not the timer should stop or pause or when time should be deducted if a player got a pair wrong.
* Controller - A class that defines the rules of the game - it is used to establish the timer, the score (turns), the sounds, and the window. The refresh page is established here, and so each of the prior classes and their UI elements reload in this class.

***

## Tasks and Responsibilities

### Software Lead - [Aoife McManus]

The Software Lead supported both the Front End Specialist and Back End Specialists through integrating separate classes into the Controller class, allowing for a smooth MVC format which was runned through a single file. She worked hand-in-hand with the Back End Specialists to make the timer functions into a separate class as well as programming the Card class. More importantly, she was aware of the testing process and made sure that the game ran without any major problems. She also incorporated some code for pygame and the back end classes.

### Front End Specialist - [Dyandra Allen]

The Front End Specialist conducted independent research into the functionality of Pygame in order to create visual aspects such as buttons and on-screen text. She used this knowledge to design and program a consistent GUI that allowed easy access for the player to navigate the main screen, instruction page, and game over screen. Moreover, she worked with the rest of the team to incorporate the classes into the ccontroller as well as sound effects and music coverage.

### Back End Specialist - [Nickolas De Dios, Christian Torres]

The Back End Specialists helped with the "Model" portion of MATCH THE BEARCAT by writing the major classes that would be used in the game like the cards and timer functions, that would be a part of the main game. In addition, they also implemented major pygame functionality into the classes. They worked on the way the cards would reveal numbers and time deduction methods as well. They also collaborated with the Front End Specialist for the implementation of the classes into the Controller file.

## Testing

### Menu Testing
To begin, we run Controller() and make certain that the main menu of the game opens. The music begins to play and the two buttons labeled "Start Game" and "Instructions" are fully functional. Before beginning, we click the Instructions button to confirm that the Instructions menu opens along with the continuation of the background music score. The Instructions screen will have a button labeled "Main Menu". When pressed, it brings the user to the previous screen, the main menu, as it should. Lastly, we test the "Start Game" button on the main menu to make sure that the user is brought to the Game screen without any issues.

### Game Testing
When the Game screen appears, we ensure that a grid of 20 cards appears and the timer automatically begins ticking down from 3:00 minutes. Displayed towards the top of the screen is "Turns:" beginning at zero. A "Give Up" button is also provided on the right side of the screen. When pressed, we are brought to the Game Over screen. Because the arrow keys are not required, we ensure that a single click of the mouse button reveals a single number on a specific card. If two numbers are matched correctly, they will turn green and remain visible until the game is over. If two numbers are picked incorrectly, they will turn red, become invisible once again shortly after, and five seconds will be deducted from the timer. Other than the cards and the Give Up button, nothing else on the Game screen should be interactable.

Moving on from this, we perform a playtest to make sure that the numbered cards react smoothly with each click and the number of tries increase by one every time two cards are clicked. A number only appears when its corresponding card is clicked; otherwise, they are hidden. The music will continue throughout the entire game until either the time runs out or all cards are matched.

Finally, we attempt to reach both a win state and fail state. To reach a win state, all cards are matched before the timer runs out. Doing this takes us to the Win screen. The game's music score comes to a pause at this point. The Win screen will display two buttons, one saying "Play Again?" and the other "Main Menu". As stated, one button will start the game over again if desired and the other brings the user back to the main menu. The Win screen also shows the user how many turns it took to reach the win state and plays a cheer sound effect lasting a few seconds. The words "Hooray? You Won!" are displayed as well. As for the fail state, we will purposefully match cards incorrectly until the timer reaches 0:00. This will take us to the End screen, where the same "Play Again?" and "Main Menu" buttons as before are displayed and the game's music score comes to a pause. These buttons will perform the same functions when pressed as they do on the Win Screen. Along with this, the End Screen also includes the words "GAME OVER" with a boom sound effect which lasts for one to two seconds. Once these are all checked, we will close the entire game window by clicking the X button on the top right corner. This concludes the testing procedure.

### ATP Copy

| Step | Procedure | Expected Result | Actual Result | Pass |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| 1 | Run Controller() | 1) Main menu page opens normally 2) Music begins playing in the background 3) Start Game Button and Instructions Screen Button appear |  |  |
| 2 | Click Instructions Button | 1) Instructions for the game should appear on screen 2) A button appears that takes you to the main menu for the game 3) The music from the main menu continues playing |  |  |
| 3 | Click Start Game Button | 1) A screen appears with various cards distributed across the page 2) There will be a timer that appears near the bottom of the screen that counts down from 3 minutes 3) The music from the main menu screen continues playing 4) There will be also a turns counter that appears on the side of the screen 5) A give up button will appear |  |  |
| 4 | Click Card | 1) A number should appear on the card in black |  |  |
| 5 | Click Matching Card | 1) If a matching card is selected, both the cards should turn green and appear with the numbers on them in green for the rest of the game 2) The turn accumulator will increase by one |  |  |
| 6 | Click Non-Matching Card | 1) If you select a card that does not match a card that has already been clicked, both cards will appear red and turn white again 2) Five seconds will be subtracted from the timer 3) The turn accumulator will increase by one |  |  |
| 7 | Click Give Up Button | 1) Numbers of turns you used appears 2) A play again button and a main menu button appear 3) Music from the game stops 4) "Game over" sound plays | | |
| 8 | General Playtesting | 1) Cards appear on the screen as expected 2) Same matching and non-matching card test |  |  |
| 9 | Force Fail Test | 1) There is no time left on the timer or turns exceeds thirty 2) Game over screen appears 4) A play again  button and a main menu button appear 5) Number of turns used appears 6) "Game over" sound plays 7) A play again button and a main menu button appear |  |  |
| 10 | Force Win Test | 1) A play again button and a main menu button appear 2) A personal high score appears based on your number of turns 3) Applause sound comes on |  |  |
| 11 | Click Play Again Button | 1) Returns to the Start Game Screen | | | 



