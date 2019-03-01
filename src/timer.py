import pygame
import time

class Timer:
    """
        Intializes the timer
        args: None
        return: None
    """
    def __init__(self):
        self.timer=pygame.time.Clock()
        self.time=180500

    """
        Controls the countdown of the clock
        args: self
        return: None
    """
    def Countdown(self):
        x = self.timer
        self.time -= x.tick()
        self.visible_time = self.time/1000
        self.t1 = self.visible_time//60
        self.t2 = self.visible_time%60
        self.temp = ""
        if self.t2 < 10:
            self.temp = '0'
        self.visible_time = "%i:%s%i" % (self.t1,self.temp,self.t2)

    """
        Deducts time if player guesses incorrectly
        args: self
        return: None
    """
    def TimePenalty(self):
        self.time = self.time - 5000
        return self.time

    """
        Returns the minute
        args: self
        return: str(self.t1)
    """
    def gett1(self):
        return self.t1

    """
        Returns the time
        args: self
        return: str(self.visible_time)
    """
    def getTime(self):
        return self.visible_time
