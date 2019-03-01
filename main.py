import pygame
from src import Controller
from src import Card

def main():

    pygame.init()

    #Create an instance on your controller object
    main_window = Controller.Controller()
    main_window.mainloop()


main()
