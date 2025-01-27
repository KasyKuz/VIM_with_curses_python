from  test_curses import *

from MVC import *
from views import *
from controllers import *
from mainModule import *

class Lib_Builder():
    

    def __init__(self) -> None:
        self. variant = " "
      

    def give_graph_lib(self, s: str) :
        if (s == "curses"):
            return curses_implementation()
        else:
            print("no such implemetation, try again")
            return None
        
class Driver_class():
    def __init__(self):
        self.graph_lib = None
        self.views = []
        self.controllers = []
        self.models = []
        self.params =  [] #[25,5,120]                         # потом выбираем
    def start(self):
        #s = input ("enter lib, you want to use: ")
        s = "curses"
        builder = Lib_Builder()
        self.graph_lib = builder.give_graph_lib(s)
        self.graph_lib.init_lib()

        self.main_model = None

        
         #сделать  Text_controller + интерфейс для переклбчения котроллеров
        
                                                # + статус бар
        
    def inition_text_command_view(self ):
        self.views.append(MyView_command(self.graph_lib))
        self.views.append(MyView_text(self.graph_lib))
        self.views.append(MyView_bar(self.graph_lib))
    
        
        self.views[0].win_inition( self.params[1], self.params[2]-1,self.params[0],0)        
        self.graph_lib.refresh(self.views[0].return_win())   #сделать статус бар
       # self.graph_lib.cursor_0(self.views[0].return_win(),1,1)

       

        self.views[1].win_inition( self.params[0]-2, self.params[2]-1,1,0 )
        self.graph_lib.cursor_0(self.views[1].return_win(),1,1)
        self.graph_lib.refresh(self.views[1].return_win())

        self.views[2].win_inition( 1, self.params[2]-1,self.params[0]-1,0 )  
       # self.graph_lib.write_line(self.views[2].return_win(),0,0,"status_bar")
        self.graph_lib.refresh(self.views[2].return_win())   #сделать статус бар
        #self.graph_lib.get_key(self.views[2].return_win(),0,0)
   

       
        
        
    def init_obj(self):
        Controller_mode0 = MyController_mode0()
        Controller_mode1 = MyController_mode1()
        Controller_mode2 = MyController_mode2()
        Controller_mode3 = MyController_mode3()

        Controller_mode0.set_view(self.views[1])
        Controller_mode3.set_view(self.views[1])

        Controller_mode2.set_view(self.views[0])
        Controller_mode1.set_view(self.views[0])    #cnfnenc ,fh cbcntvf eghfktybz : устатус серч

        self.controllers.append(Controller_mode0)
        self.controllers.append(Controller_mode1)
        self.controllers.append(Controller_mode2)
        self.controllers.append(Controller_mode3)

        Model = MainModel()
        Model.set_observer(self.views[2])
        Model.set_observer(self.views[1])  # -  другие вьюхи тоже как-то надо
        ''' 
        Model.add_controller(Controller_mode0)
        Model.add_controller(Controller_mode1)
        Model.add_controller(Controller_mode2)
        Model.add_controller(Controller_mode3)
        '''
        self.main_model = Model


       
    def inition_params(self):

        #s = input ("enter proportions, multiply 30, of text window and command window you want to use (for example 5:1): ")
        #s = s.split(":")

        #s1 = int(s[0])
        #s2 = int(s[1])
        s1, s2 = 5, 1
        #g = input("enter length of Vim window: ")
        #g = int(g)

        g = 120

        const_len = 30

        self.params.append(const_len//(s1+s2)*s1)
        self.params.append(const_len//(s1+s2)*s2)
        self.params.append(g)

    def run(self):
        key = ""
        while True:
            result, key, model= self.controllers[0].run(self.main_model, key)
            self.main_model = model
            if result == 3:
                result = self.controllers[3].run(self.main_model, key)
                self.model = result
            elif result == 1:
                model = self.controllers[1].run(self.main_model, key)
                self.main_model = model
            elif result == 2:
                result = self.controllers[2].run(self.main_model,key)
                self.model = result
            elif result == -1:
                break

    """
    статус бар работает по-другому  !! переделать
    интерфейс между контр и моделью  + котр и вью

    переделать юмл , добавить, что возвращают классы

    
    """   
        

if __name__ == "__main__":
    # Клиентский код.
  
    driver = Driver_class()
    driver.start()
 
    driver.inition_params()
    driver.inition_text_command_view()
    driver.init_obj()
    driver.run()