import sys
import pygame
import random
import time
from src import Card
from src import timer

class Controller:
    """
        Intializes the icon, name, pygame, screen, font, score, buttons, images, and card lists
        args: self, (int)width , (int)height
        return: None
    """
    def __init__(self,width = 800, height = 600):
        # Creates icon and screen name
        ICON = pygame.image.load(("assets/card.jpg"))
        pygame.display.set_icon(ICON)
        pygame.display.set_caption("Match the Bearcat")

        # Intializing pygame
        pygame.init()
        pygame.font.init()


        # Create the screen
        self.screen = pygame.display.set_mode((width,height))
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()

        #Default font
        self.font = pygame.font.SysFont('Helvetica', 35, False)
        self.endFont = pygame.font.SysFont(None, 70, False)
        # Creates the buttons
        self.centerWidth = 300
        self.centerHeight = self.background.get_height()/2
        self.startBtn = pygame.Rect(55,450,200,100) #Start the game
        self.endBtn = pygame.Rect(600, 200, 150,50) #End the game
        self.instrBtn = pygame.Rect(550,450, 200,100) #Go to Instructions screen
        self.instrBtn2 = pygame.Rect(305,450, 200,100) #Go to the game screen
        self.mainBtn = pygame.Rect(280,405,200,100)
        self.play_again = pygame.Rect(280,280,200,100)

        # Music
        pygame.mixer.music.load("assets/music.mp3")
        pygame.mixer.music.play(-1)

        #Loads the images that we need
        self.baxterImg = pygame.image.load("assets/baxter.png")
        self.number_pic = pygame.image.load("assets/numbers.png")
        self.baxter_sitting = pygame.image.load("assets/baxter_sitting_.png")
        self.bubble = pygame .image.load("assets/bubble.png")
        self.confetti = pygame.image.load("assets/confetti.png")
        self.fire = pygame.image.load("assets/fire.jpg")
        self.gameover = pygame.image.load("assets/gameover.png")
        self.bear = pygame.image.load("assets/bearcat_1.png")
        #Intializes state of the game
        self.state = "GAME"

        #Creates the Score
        self.score=0

        #Creates variables that will be used when the user clicks two cards
        self.matched=[]
        self.exposed=[]
        self.wrong=[]

    """
        Starts and ends the game
    """
    def mainloop(self):
        while True:
            if(self.state == "GAME"):
                self.gameLoop()
            elif(self.state == "GAMEOVER"):
                self.setEndScreen()

    """
        This is the Main Loop of the Game
    """
    def gameLoop(self):
        """
            Sets up the start screen
            args: self
            return: None
        """
        def setStartScreen(self):
            #Background
            self.background.blit(self.number_pic, (0,0))

            #Game Title
            startFont = pygame.font.SysFont('Helvetica', 70, False)
            gameTitle = startFont.render('Match The Bearcat', True, (0,90,67))
            self.background.blit(gameTitle, (175,30)) #To be deleted

            #Start Button - Go To Game
            self.background.fill((106,10,0), rect = self.startBtn) #dark red, left
            startGameFont = self.font.render('Start Game', True, (255,255,255))
            self.background.blit(startGameFont, (80,470))

            #Instruction Button - Go to Instructions Screen
            self.background.fill((0,51,102), rect = self.instrBtn) #navy blue, right
            instructionsFont = self.font.render('Instructions', True, (255,255,255))
            self.background.blit(instructionsFont, (570,470))

            #Main screen Baxter image
            self.background.blit(self.baxterImg, (250,100))

        """
            Sets up the instruction screen
            args: self
            return: None
        """
        def setInstructionsScreen(self):
            #Background
            self.background.blit(self.number_pic, (0,0))
            self.background.blit(self.bear,(470,50))

            #Instruction Button - Return to main menu
            self.background.fill((238,44,44), rect = self.instrBtn2)
            startGameFont2 = self.font.render('Main Menu', True, (0,0,0))
            self.background.blit(startGameFont2, (330,472))

            self.instructionsList = ["Instructions: ", "This is a typical matching game.", "1. Click on the two matching cards","2. If the cards don't match, they disappear" ,"3. You will automatically lose once the timer reaches 0!", "Note: You lose 5 seconds for every wrong match","GOOD LUCK!!!"]
            self.lineY = 100
            for i in range(len(self.instructionsList)):
                self.instructions = self.font.render(self.instructionsList[i], True, (0,0,0))
                self.background.blit(self.instructions, (50,self.lineY))
                self.lineY += 50

        """
            Sets up the game over screen
            args: self
            return: None
        """
        def setEndScreen(self):
            #Background
           self.background.blit(self.fire, (0,0))
           self.background.blit(self.gameover, (500,180))

           #Game Over font
           gameOverFont = self.endFont.render('Game Over', True, (255,0,0))
           self.background.blit(gameOverFont, (250,50))

           #Failed to finish font
           finishFont2 = self.endFont.render("You didn't finish in time...", True, (255,0,0))
           self.background.blit(finishFont2, (130, 120))

           numturns = self.endFont.render("Number of turns:", True, (255,255,255))
           self.background.blit(numturns, (70, 180))
           turn = self.endFont.render(str(self.turns), True, (255,255,255))
           self.background.blit(turn, (490,180))


           #Play Again Button - Go to game screen
           self.background.fill((255,255,0), rect = self.play_again)
           play = self.font.render('Play Again?', True, (0,0,0))
           self.background.blit(play, (290,300))

           #Main Menu Button - Go to start menu
           self.background.fill((255,0,0,),rect = self.mainBtn)
           main = self.font.render('Main Menu', True, (0,0,0))
           self.background.blit(main, (295,430))

           #Stops the music
           pygame.mixer.music.pause()
           pygame.mixer.music.load("assets/boom.mp3")      #This is where to put music
           pygame.mixer.music.play()

           pygame.display.flip()

        """
            Sets up the "You Win" screen
            args: self
            return: None
        """
        def setWinScreen(self):
            #Background
            self.background.blit(self.confetti, (0,0))

            #Play Again Button - Go to game screen
            self.background.fill((255,255,0), rect = self.play_again)
            play = self.font.render('Play Again?', True, (0,0,0))
            self.background.blit(play, (290,300))

            #Main Menu Button - Go to main menu
            self.background.fill((255,0,0,),rect = self.mainBtn)
            main = self.font.render('Main Menu', True, (0,0,0))
            self.background.blit(main, (295,430))

            #You Won font
            endFont = pygame.font.SysFont(None, 70, False)
            self.winlist = ["Hooray! You Won!", "Can you beat your own record?",str(self.turns),"Thanks for playing!"]
            self.lineY = 20
            for i in range(len(self.winlist)):
                if i == 0 or i == 2:
                    self.win= endFont.render(self.winlist[i],True,(0,0,0))
                else:
                    #self.win = self.font.render(self.winlist[i], True, (250,0,0))
                    self.win = self.font.render(self.winlist[i], True, (0,0,0))
                self.background.blit(self.win, (50,self.lineY))
                self.lineY += 50
            self.background.blit(self.baxterImg, (480,120))
            #Stops the music and plays a new tune
            pygame.mixer.music.stop()        #Stops the music
            pygame.mixer.music.load("assets/applause3.mp3")      #This is where to put music
            pygame.mixer.music.play(1)

            pygame.display.flip()

        """
            Sets up the main game screen (where the user plays)
            args: self
            return: None
        """
        def setGameScreen(self):
            #unpauses music when game starts
            pygame.mixer.music.load("assets/music.mp3")      #This is where to put music
            pygame.mixer.music.play(-1)

            #Sets screen and local variable
            DISPLAY = pygame.display.set_mode((800,600))
            BLACK= (0,0,0)
            WHITE= (255,255,255)
            RED = (255,0,0)
            GREEN = (0, 255, 0)
            ARIAL_200 = pygame.font.SysFont("Arial", 200)
            ARIAL_50 = pygame.font.SysFont("Arial", 50)
            ARIAL_35 = pygame.font.SysFont("Arial", 35)
            ARIAL_20 = pygame.font.SysFont("Arial", 20)

            #Creates the card placeholders for the numbers and creates the timer
            deck = Card.Card.placeCards(self)

            global exposed
            exposed = []
            global matched
            matched = []
            global wrong
            wrong = []
            global turns
            self.turns = 0
            newTimer = timer.Timer()

            #Controls the cards being matched and give up button
            while len(matched) != 20:
                for event in pygame.event.get():
                    #Detect quit
                    breakPt = False
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if self.endBtn.collidepoint(pygame.mouse.get_pos()):
                            breakPt = True

                newTimer.Countdown()
                min = newTimer.gett1()

                if min < 0:
                     setEndScreen(self)
                     breakPt = True

                if breakPt:
                    setEndScreen(self)
                    break
                #Check for mouse click
                pressed = list(pygame.mouse.get_pressed())
                for i in range(len(pressed)):
                    if pressed[i]:
                        for i in range(self.ROWS):
                            for j in range(self.COLS):
                                mouse_pos = list(pygame.mouse.get_pos())
                                if mouse_pos[0] >= self.CARD_GRID[i][j].x and mouse_pos[1] >= self.CARD_GRID[i][j].y and mouse_pos[0] <= self.CARD_GRID[i][j].x + self.CARD_LEN and mouse_pos[1] <= self.CARD_GRID[i][j].y + self.CARD_LEN:
                                    global has_instance
                                    has_instance = False
                                    for k in range(len(exposed)):
                                        if exposed[k] == [i, j]:
                                            has_instance = True
                                    for k in range(len(matched)):
                                        if matched[k] == [i, j]:
                                            has_instance = True

                                    if has_instance == False:
                                        exposed.append([i, j])
                #When 2 clicks, adds 1 to turn
                if len(exposed) == 2:
                    self.turns += 1
                    if self.CARD_VAL_GRID[exposed[0][0]][exposed[0][1]] == self.CARD_VAL_GRID[exposed[1][0]][exposed[1][1]]:
                        matched.extend(exposed)
                        exposed.clear()

                    else:
                        wrong.extend(exposed)
                        exposed.clear()

                #Clear screen
                DISPLAY.fill((0,90,67)) #Pantone green

                #Baxter sitting image
                DISPLAY.blit(self.baxter_sitting, (520,400))
                DISPLAY.blit(self.bubble, (625,325))

                #Give Up Button - Goes to end screen
                DISPLAY.fill((255,255,255), rect = self.endBtn)
                giveup = self.font.render('Give Up', True, BLACK)
                DISPLAY.blit(giveup, (610,200))

                #Displays the timer
                timerfont = self.font.render("Timer:", True, WHITE)
                DISPLAY.blit(timerfont, (100,500))
                visTime = newTimer.getTime()
                timeFont = self.font.render(visTime, True, WHITE)
                DISPLAY.blit(timeFont, (220, 500))

                #Draw cards to display
                for i in range(self.ROWS):
                    for j in range(self.COLS):
                        pygame.draw.rect(DISPLAY, (255, 255, 255), self.CARD_GRID[i][j])

                #Draws numbers
                if exposed:
                    for i in exposed:
                        text = str(self.CARD_VAL_GRID[i[0]][i[1]])
                        render = ARIAL_50.render(text, True, BLACK)
                        DISPLAY.blit(render, (self.CARD_GRID[i[0]][i[1]].x + self.CARD_HOR_PAD, self.CARD_GRID[i[0]][i[1]].y + self.CARD_VER_PAD))

                #Checks if matched
                if matched:
                    for i in matched:
                        text = str(self.CARD_VAL_GRID[i[0]][i[1]])
                        render = ARIAL_50.render(text, True, GREEN)
                        DISPLAY.blit(render, (self.CARD_GRID[i[0]][i[1]].x + self.CARD_HOR_PAD, self.CARD_GRID[i[0]][i[1]].y + self.CARD_VER_PAD))

                #Checks if wrong
                if wrong:
                    for i in wrong:
                        text = str(self.CARD_VAL_GRID[i[0]][i[1]])
                        render = ARIAL_50.render(text, True, RED)
                        DISPLAY.blit(render, (self.CARD_GRID[i[0]][i[1]].x + self.CARD_HOR_PAD, self.CARD_GRID[i[0]][i[1]].y + self.CARD_VER_PAD))
                    visTime = newTimer.TimePenalty()
                #Displays turns and "Memory"
                title = ARIAL_35.render("Match the pairs!", True, WHITE )
                DISPLAY.blit(title, (570, 10))
                turn_text = ARIAL_20.render("Turns: " + str(self.turns), True, WHITE)
                DISPLAY.blit(turn_text, (580, 75))

                #Checks if all cards are matched
                if len(matched) == 20:
                    setWinScreen(self)

                pygame.display.flip()
                if wrong:
                    time.sleep(1)
                    wrong.clear()

        #Controls button events and sets the screen
        setStartScreen(self)
        while self.state == "GAME":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.startBtn.collidepoint(pygame.mouse.get_pos()) or self.play_again.collidepoint(pygame.mouse.get_pos()) :
                        setGameScreen(self)
                    elif self.instrBtn.collidepoint(pygame.mouse.get_pos()):
                        setInstructionsScreen(self) #white
                    elif self.endBtn.collidepoint(pygame.mouse.get_pos())  or self.mainBtn.collidepoint(pygame.mouse.get_pos()):
                        setStartScreen(self) #blue
                        pygame.mixer.music.load("assets/music.mp3")      #This is where to put music
                        pygame.mixer.music.play(-1)
                    elif self.instrBtn2.collidepoint(pygame.mouse.get_pos()):
                        setStartScreen(self)

            self.screen.blit(self.background, (0,0))
            pygame.display.flip()
