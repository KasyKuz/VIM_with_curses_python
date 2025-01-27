import curses
from curses import wrapper


from MyString import MyString as MyString
from base_lib_implementation import *


class curses_implementation (Base_implementation): #нужен родительский аьстрактный класс  ???управление окнами - может 2 класса
    def __init__(self):
        self.scr =None
        pass
    
    def clear_win(self,win):
        win.clear()
        
    def init_lib(self):
        #super().library_inition()
        self.scr = curses.initscr()
        
    def get_cursor(self, win):
        return win.getyx()

    def get_key(self,win,y,x):
   

        key = win.getkey(y,x)
       # win.delch(y,x)
        #self.cursor_0(win,y,x)
        
        return key
    def get_key2(self,win):
   

        key = win.getkey()
       # win.delch(y,x)
        #self.cursor_0(win,y,x)
        
        return key
    def get_size_win(self,win):
        return win.getmaxyx()
    def make_win_border(self,win):
        win.border()
    def find_key(self, win):
        return win.getkey()
    def win_clear(self, win):
        #win.clearok(True)
        win.clear()
    def refresh(self,win):
        win.refresh()
        return
    
    def new_win(self, y,x, y_begin, x_begin):
       
        scr = curses.newwin(y,x,y_begin,x_begin)
        scr.border()      
        return scr


    def cursor_0(self, win,y,x):
        win.move(y,x)

    def destroy_win(self, win):
        win.endwin()
        
   
   
    
    def write_line (self, screen, y,x, stri):
        screen.addstr(y,x,stri)


