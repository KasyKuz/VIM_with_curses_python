from MVC import *
from mainModule import *
from views import *
from test_curses import *
from MyString import MyString as MyString

class MyController_mode1 (Controller):
    def __init__(self):
        self.view = None
    def set_view(self,view):
        self.view = view

   
    def run(self, model:MainModel, key):
        model.set_mode("command")
        model.return_observer().news(model.return_inf(), model.return_coordinates(),model.return_filename(), model.get_mode())
        while (True):
            key = self.view.get_key_w()
            if (key == "\x1b"):
                break
           
            command = ""
            while (key != '\n' and key != "\x1b"):
                command+=key
                key = self.view.get_key_w()
            command = command.split(" ")
            print(command)
            ##заглушка
            #command[1] = "help.txt"
            if (command[0] == "o" and len(command)==2):
                model.write_in_buf(command[1])
            elif (command[0] == "x" and len(command)==1):
                model.file_x()
            elif (command[0] == "w" and len(command)==1):
                model.file_w()
            elif (command[0] == 'w'  and len(command)==2):
                model.write_in_file(command[1])
                self.view.clear()
                return model
            elif (command[0] == "q" and len(command[0])==1):
                model.file_q()
            elif (len(command[0])==2 and command[0][0]+command[0][1] == "q!" ):
                model.file_q_n()
            elif (len(command[0])==3 and command[0][0]+command[0][1]+command[0][2] == "wq!"):
                model.file_x()
            elif (command[0] == "h" and len(command)==1):
                model.help()
            elif (command[0].isdigit() == True and len(command)==1):
                model.curs_number(int(command[0]))
           
            self.view.clear()
            model.return_observer().news(model.return_inf(), model.return_coordinates(), model.return_filename(), model.get_mode())
            
        self.view.clear()
        model.return_observer().news(model.return_inf(), model.return_coordinates(),model.return_filename(), model.get_mode())
        return model
            

           
  
class MyController_mode2 (Controller):
    def __init__(self):
         self.view = None
    def set_view(self,view):
        self.view = view
    def do_action(self,Model:MainModel):
        key = self.view.get_key_w()
        while (key != "\x1b"):
            self.dop_ac(Model,key)
            Model.return_observer().news(Model.return_inf(), Model.return_coordinates(),Model.return_filename(),Model.get_mode())
            key = self.view.get_key_w()
        return Model
    def dop_ac(self,Model:MainModel, key):
       
        if key == '/':
        
            key = self.view.get_key_w()
            buf = ""
            while (key != '\n'):
                buf += key
                key = self.view.get_key_w()
            Model. search_right(buf)
        elif key == '?':
            key = self.view.get_key_w()
            buf = ""
            while (key != '\n'):
                buf += key
                key = self.view.get_key_w()
            Model.search_left(buf)
        elif key == 'n':                       # НЕ РАБОТАЕТ
            key = self.view.get_key_w()
            if (key == '\n'):
                Model.second_search_n()
                print("second_search_n()")
        elif key == 'N':                       # НЕ РАБОТАЕТ
            key = self.view.get_key_w()
            if (key == '\n'):
                Model.second_search_N()
        self.view.clear()
        return Model
    def run(self, Model:MainModel, key):        
        self.view.write_0(key)
        Model.set_mode("search")
        Model.return_observer().news(Model.return_inf(), Model.return_coordinates(),Model.return_filename(),Model.get_mode())
        Model = self.dop_ac(Model,key)
       
        Model.return_observer().news(Model.return_inf(), Model.return_coordinates(),Model.return_filename(), Model.get_mode())
        Model = self.do_action(Model)
        self.view.clear()
        return Model
                

class MyController_mode3 (Controller):
    def __init__(self):
         self.view = None
    def set_view(self,view):
        self.view = view
    def do_action(self,Model:MainModel):
        key = self.view.get_key_no_w()
        while (key != "\x1b"):
           #вводим символы
            key = self.view.get_key_no_w()


    def run(self, Model:MainModel, key):
       
        if (key == 'o'):
            Model.set_mode("input")
            Model.return_observer().news(Model.return_inf(), Model.return_coordinates(),Model.return_filename(),Model.get_mode())
            key = self.view.get_key_no_w()
            
            if (key == 'I'): 
                key = self.view.get_key_no_w()
                if key !="\x1b":
                    Model.text_I(key) 
                    Model.return_observer().news(Model.return_inf(), Model.return_coordinates(),Model.return_filename(),Model.get_mode())
                while (key != "\x1b"):
                #вводим символы
                    key = self.view.get_key_no_w()
                    Model.text_i(key) 
                    Model.return_observer().news(Model.return_inf(), Model.return_coordinates(),Model.return_filename(),Model.get_mode())
                   
                 
            elif (key == 'i'):                       
                key = self.view.get_key_no_w()
              
                while (key != "\x1b"):
                #вводим символы
                    Model.text_i(key) 
                    Model.return_observer().news(Model.return_inf(), Model.return_coordinates(),Model.return_filename(),Model.get_mode())
                    key = self.view.get_key_no_w()
            
            elif (key == 'A'): 
                 # НЕ РАБОТАЕТ
                key = self.view.get_key_no_w()
                if key !="\x1b":
                    Model.text_A(key) 
                    Model.return_observer().news(Model.return_inf(), Model.return_coordinates(),Model.return_filename(),Model.get_mode())
                while (key != "\x1b"):
                #вводим символы
                    key = self.view.get_key_no_w()
                    Model.text_i(key) 
                   
                    Model.return_observer().news(Model.return_inf(), Model.return_coordinates(),Model.return_filename(),Model.get_mode())
                   
            elif (key == 'S'): 
                key = self.view.get_key_no_w()
                if key !="\x1b": 
                    Model.text_S(key)  
                    Model.return_observer().news(Model.return_inf(), Model.return_coordinates(),Model.return_filename(),Model.get_mode())
                key = self.view.get_key_no_w()
                while (key != "\x1b"):                    #вводим символы
                        
                        Model.text_i(key)                       
                        Model.return_observer().news(Model.return_inf(), Model.return_coordinates(),Model.return_filename(),Model.get_mode())
                        key = self.view.get_key_no_w()
            elif (key == 'r'):
                key = self.view.get_key_no_w()
                while (key != "\x1b"):
                    Model.text_r(key) 
                
                    Model.return_observer().news(Model.return_inf(), Model.return_coordinates(),Model.return_filename(),Model.get_mode())
                    key = self.view.get_key_no_w()
        return Model

        

      

class MyController_mode0 (Controller):
    def __init__(self):
      
        self.view = None     
        self.Model = None 
    

    def set_view(self, view:MyView_text):
        self.view = view

    def curs_right(self):


    def run(self, Model:MainModel, key):
        self.Model = Model
        Model.set_mode("navigation")
        Model.return_observer().news(Model.return_inf(), Model.return_coordinates(),Model.return_filename(),Model.get_mode())
        while (True):
            
            key = self.view.get_key_no_w()
            if (key == "o" or key == "i" or key == "I" or key == "A" or key == "S" or key == "r"): return 3,key, Model# это эскейп "\x1b"
            elif (key == ":"): return 1, ":", Model
            elif (key == "/" or key == "?" ): return 2, key,Model
            elif (key == 'l'): Model.curs_right()                   
            elif (key == 'h'): Model.curs_left()    
            elif (key == 'k'): Model.curs_up()            
            elif (key == 'j'): Model.curs_down()               
            elif (key == '0'): Model.curs_begin()  
            elif (key == '$'): Model.curs_end()  
            elif (key == 'w'): Model.curs_w()  
            elif (key == 'b'): Model.curs_b()
            elif (key.isdigit()==True): 
                num = int(key)
                while True:
                    key = self.view.get_key_no_w()
                    if key !='G':
                        num*=10
                        num+= int(key)
                                
                    else:
                        Model.curs_number(num)
                        break
                



            elif (key == 'G'): 
                print("G controller")
                Model.curs_G()  
         
            elif (key == 'g'):
                key = self.view.get_key_no_w()
                if (key == 'g'):    Model.curs_gg()  
         

            elif (key == 'x'):Model.curs_x()
            elif (key == 'd'):
                key = self.view.get_key_no_w()
                if (key == 'i'):   
                    key = self.view.get_key_no_w()
                    if (key == 'w'):    Model.curs_diw()  
                elif (key == 'd'):        Model.curs_dd()  
                    
            elif (key == 'y'):
                key = self.view.get_key_no_w()
                if (key == 'y'):   
                    Model.curs_yy()  
                elif (key == 'w'):    
                    Model.curs_yw()  
            elif (key == 'p'):Model.curs_p()
            
            else:
                return -1,"",Model
           
            Model.return_observer().news(Model.return_inf(), Model.return_coordinates(),Model.return_filename(),Model.get_mode())
            
        
      
