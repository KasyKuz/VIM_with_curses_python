from __future__ import annotations
from abc import ABC, abstractmethod

#from MyString import MyString as MyString

from  test_curses import *

class Observer:
    def __init__(self):
        self.who_obs = []
        

    def add_obs(self, subj):
        self.who_obs.append(subj)
       

    def news(self, buf_c, buf):
        for s in self.who_obs:
            s.special_method()


class Lib_Builder():
    

    def __init__(self) -> None:
        self. variant = " "
      

    def give_graph_lib(self, s: str) :
        if (s == "curses"):
            return curses_implementation()
        else:
            print("no such implemetation, try again")
            return None
        

    
class Controller(ABC):
    @abstractmethod
    def return_new_state(self):
        pass




class MyController_command (Controller):
    def __init__(self):
        self.window_n = 1
        

    def add_cur_win(self, view):
        pass
    def return_new_state(self):
        pass

class MyController_help  (Controller):
    def __init__(self):
        self.window_n = 2
        self.Views = []

    def add_view(self, view):
        self.Views.append(view)       

    def return_new_state(self):
        pass

class MyController_text (Controller):
    def __init__(self):
        self.window_n = 0
        self.Views = []

    def add_view(self, view):
        self.Views.append(view)       

    def return_new_state(self):
        pass
      
        
    
    def return_new_state(self):
        while (True):
            if (self.window_n == 1):
                key = curses_implementation.find_key(self.MyModel.win_text)
                if (key == "\x1b"): self.window_n = (self.window_n+1) % 3
                elif (key == 'l'): self.MyModel.curs_left(self.window_n)             
                
                elif (key == 'h'): self.MyModel.curs_right(self.window_n)
                elif (key == 'k'): self.MyModel.curs_up(self.window_n) #up                
                    
                elif (key == 'j'): self.MyModel.curs_down(self.window_n) #down
                else:
                    return
            elif (self.window_n == 2):
                return
            elif (self.window_n == 3):
                return
            else:
                print("error - unexpected state")
                exit(0)
        



class View (ABC):

    @abstractmethod 
    def win_inition(self, y,x, y_begin, x_begin ):
        pass        
    @abstractmethod
    def return_win(self):
       pass
    @abstractmethod
    def update(self, data) :
        """
        Получить обновление от субъекта.
        """
        pass

class MyView_command (View):
    def __init__(self, lib):
        self.lib = lib
        self.cur_win = None
 
     
    def win_inition(self, y,x, y_begin, x_begin ):
        self.cur_win = self.lib.new_win(y,x, y_begin, x_begin)
        
    def return_win(self):
        return self.cur_win
    def update(self, data) :
        pass
        

class MyView_help (View):
    def __init__(self,lib):
        self.lib = lib
        self.cur_win = None

    def win_inition(self, y,x, y_begin, x_begin ):
        self.cur_win = self.lib.new_win(y,x, y_begin, x_begin)
        
    def return_win(self):
        return self.cur_win
    def update(self, data) :
        pass
    def update(self, data) :
        pass
        

class MyView_text (View):
    def __init__(self, lib):
 
        self.lib = lib
        self.cur_win = None
       
     
    def win_inition(self, y,x, y_begin, x_begin ):
        self.cur_win = self.lib.new_win(y,x, y_begin, x_begin)

    def return_win(self):
        return self.cur_win
    

    def write_all_text(self, text, win):
        x,y = 0,0
        for i in range(len(text)):
            curses_implementation.write_line(win, text, [x,y,])
    def set_curs_win(self):
        self.write_all_text(text)
        curses_implementation.set_curs_on(screen, text,x,y)

    def update(self, some_data): #будут какие-то данные
        pass
        

class MyModel_command ():
   
    def __init__(self):
        self.SIZE = [6,4]

class MyModel_help ():
   
    def __init__(self):
        self.SIZE = [6,4]

class MyModel_text ():
   
    def __init__(self):
        
        self.state = 0
        self.Controllers = []
        
       
        self.buf = []
        self.Views_observers = []
        self.filename = "D:\\Documents\\ооп\\лаб4\\test.txt"

    def write_in_buf(self):
        with open(self.filename) as f:
            s=f.read(118)
            self.buf.append(s)
    # работа с файлом

    def return_win(self,number):
        if (number == 1):
            return self.win_text
        elif (number == 1):
            return self.win_command
        elif (number == 1):
            return self.win_help
        else:
            print("can't find this type of window")
    def search_left(self):
        pass
    def search_right(self):
        pass
        
    def curs_right(self):
        if (self.coord[self.state*2]+1 < self.borders[self.state][2]):
            self.coord[self.state*2]+=1 # 0 1 2
                                    # 0 0  0 0  0 0
            self.result+=1
        self.notify()
    def curs_left(self):
        if (self.coord[self.state*2]-1 >= self.borders[self.state][0]):
            self.coord[self.state*2]-=1 
            self.result+=1
        
    def curs_up(self):
        if (self.coord[self.state*2+1]+1 < self.borders[self.state][3]): # потом учесть, что надо пролиcтать файл
            self.coord[self.state*2+1]+=1
            self.result+=1
        
    def curs_down(self):
        if (self.coord[self.state*2+1]-1 >= self.borders[self.state][1]): # потом учесть, что надо пролиcтать файл
            self.coord[self.state*2+1]-=1
            self.result+=1
   

class Driver_class():
    def __init__(self):
        self.graph_lib = None
        self.views = []
        self.controllers = []
        self.models = []
    def start(self):
        #s = input ("enter lib, which you want to use: ")
        s= "curses"
        builder = Lib_Builder()
        self.graph_lib = builder.give_graph_lib(s)
        self.graph_lib.init_lib()

        Command_view = MyView_command(self.graph_lib)
        Text_view = MyView_text(self.graph_lib)
        Help_view = MyView_help(self.graph_lib)
        self.views.append(Command_view)
        self.views.append(Text_view)
        self.views.append(Help_view)

        Command_controller = MyController_command()
        Text_controller = MyController_text()
        Help_comtroller = MyController_help()
        self.controllers.append(Command_controller)
        self.controllers.append(Text_controller)
        self.controllers.append(Help_comtroller)       #сделать  Text_controller + интерфейс для переклбчения котроллеров
        

        Text_model = MyModel_text()
        Help_model = MyModel_help()
        Command_model = MyModel_command()

        self.models.append(Command_model)
        self.models.append(Text_model)
        self.models.append(Help_model)

    def inition_text_command_view(self ):

        self.views[0].win_inition( 5,120,25,0 )        
        self.graph_lib.refresh(self.views[0].return_win())

        self.views[1].win_inition( 25,120,0,0 )
        self.graph_lib.cursor_0(self.views[1].return_win(),1,1)
        self.graph_lib.refresh(self.views[1].return_win())
        ''' 
        key = self.graph_lib.find_key(self.views[1].return_win()) # потом убрать
        #self.graph_lib.make_win_border(self.views[1].return_win())
        self.graph_lib.win_clear(self.views[1].return_win())
        self.graph_lib.write_line(self.views[1].return_win(), "jfndjvdv sjvdkbvdkjv sjskvjb",[1,1,curses.A_BOLD])
        self.graph_lib.cursor_0(self.views[1].return_win(),1 , 5)
        
        self.graph_lib.make_win_border(self.views[1].return_win())
        self.graph_lib.refresh(self.views[1].return_win())
        key = self.graph_lib.find_key(self.views[1].return_win()) 
        '''
        ''' 
        self.views[2].win_inition( 2,12,26,2 )        
        self.graph_lib.refresh(self.views[2].return_win())
        key = self.graph_lib.find_key(self.views[2].return_win()) 
        self.graph_lib.destroy_win(self.views[1].return_win())
        key = self.graph_lib.find_key(self.views[2].return_win()) 
        '''







if __name__ == "__main__":
    # Клиентский код.
  
    ''' 
    curses.initscr()
    win_text =  curses.newwin(25,120,0,0)
        #scr = curses.newpad(y,x)
    win_text.border()
        #self.win_text.nodelay(True)
    win_text.getkey()
    win_text.getkey()
    win_command = curses.newwin(5,120,0,0)
    win_command.border()
     '''
    driver = Driver_class()
    driver.start()
    driver.inition_text_command_view()


    '''
    3 вьюшки, над ними менеджер на 3 контроллера - можно без сложной логики переключения
    
    обзервер в отдельный класс - модель должно быть легко изъять
    

    тесты над моделью

    конструктор для сбора всей инфрструктуры в паттерн билдер
    
    '''