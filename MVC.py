from __future__ import annotations
from abc import ABC, abstractmethod

#from MyString import MyString as MyString

from  test_curses import *

class Observer:
    def __init__(self):
        self.who_obs = []
        self.obs = []
        

    def add_obs(self, subj):
        self.who_obs.append(subj)

    def return_obs(self, n):
        return self.obs[n]
    


    def news(self,buf1,buf2,buf3, buf4):
        #print(buf2)
        for s in self.who_obs:
            s.update(buf1,buf2,buf3, buf4)


     

    
class Controller(ABC):
    @abstractmethod
    def run(self, model):
        pass
    @abstractmethod
    def set_view(self,view):
        pass
    @abstractmethod
    def run(self, model, key):
        pass



class View (ABC):

    @abstractmethod 
    def win_inition(self, y,x, y_begin, x_begin ):
        pass        
    @abstractmethod
    def return_win(self):
       pass
    @abstractmethod
    def update(self, ccord, data) :
        """
        Получить обновление от субъекта.
        """
        pass

    @abstractmethod
    def clear(self):
        pass




