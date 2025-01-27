from MVC import *
from  test_curses import *

class MyView_command (View):
    def __init__(self, lib):
        self.lib = lib
        self.cur_win = None
        self.win_size = []

    def clear(self):
        y,x = self.lib.get_cursor(self.cur_win)
        print("clear y x", y,x)
        self.write_smth(" "*(x+3), 1,1)
        self.lib.cursor_0(self.cur_win,1,1)
        self.lib.refresh(self.cur_win)


    def write_0(self, ch):
        self.write_smth(ch,1,0)

    def write_smth(self, ch, z,z2):
        
        y,x = self.lib.get_size_win(self.cur_win)
        self.lib.write_line (self.cur_win, z2,z, ch) 

    def get_key_w(self):
        y, x = self.lib.get_cursor(self.cur_win)
        key = self.lib.get_key(self.cur_win, 0, x)    
        if (key =="\n" or key =="\x1b"):
            self.lib.clear_win(self.cur_win)
            self.lib.cursor_0(self.cur_win, 0,1)
        return key
  
    def win_inition(self, y,x, y_begin, x_begin ):
        self.cur_win = self.lib.new_win(y,x, y_begin, x_begin)
        s = self.lib.get_size_win(self.cur_win)
        self.win_size.append(s[0])
        self.win_size.append(s[1])
        self.lib.cursor_0(self.cur_win, 0,1)
        
    def return_win(self):
        return self.cur_win
    def update(self, data) :
        pass

class MyView_bar (View):
    def __init__(self, lib):
        self.lib = lib
        self.cur_win = None
        self.win_size = []
        self.filename = "None"
        
        self.coord = [0,0]
    def clear(self):
        pass
     
     
  
    def win_inition(self, y,x, y_begin, x_begin ):
        self.cur_win = self.lib.new_win(y,x, y_begin, x_begin)
        s = self.lib.get_size_win(self.cur_win)
        self.win_size.append(s[0])
        self.win_size.append(s[1])
        s = self.filename #+ "" + str(self.coord[0])+"/"+str(self.coord[1])
        self.lib.write_line(self.cur_win, 0, 0, s) 
        self.lib.refresh (self.cur_win)
    def return_win(self):
        return self.cur_win
    def clear_inf(self):
        self.coord = None
        self.filename=None
    def update(self,xx,coord,filename, mode) :
        self.lib.clear_win(self.cur_win)
       
        self.lib.refresh(self.cur_win)
        self.coord = coord
        c = 0
        if (self.filename == "None"):
            self.filename=filename
            c = coord[0]
        
            ''' 
        else:
            if (self.filename == filename and  self.coord == coord):
                return
        '''
        s = self.filename +"  "+str(c) +"/"+str(len(xx)) + " mode: "+ mode
        self.lib.write_line(self.cur_win, 0,1,s)
        self.lib.refresh(self.cur_win)

    """
    window.clrtobot()
Erase from cursor to the end of the window: all lines below the cursor are deleted, and then the equivalent of clrtoeol() is performed.
    """
        

class MyView_text (View):
    def __init__(self, lib):
        self.lib = lib
        self.cur_win = None
        self.win_size = []

        self.data = []
        self.coord = [1,1]
        self.last_coord = [0,0]
        self.dir = 1
        self.realc = [1,1]
        self.last_text = []
        self.block = []
        self.save_start = 1
        self.end_or_begin = 1 #  1 - begin, 0 - end

    def clear(self):
        pass

    def get_key_no_w(self):
        y,x = self.lib.get_cursor(self.cur_win)
      
        #print("get_key_no_w 1 ",y, x)
        
        if (self.data == [] or self.data == None):
            s = " "
            ''' 
        elif ( self.data[y].c_str()=='\n'):
            s='\n'
            '''
        else:
            pass
            #print(self.data[y].c_str())
            #print("get_key_no_w 2",y,x)
            #print(self.coord[0]-1, self.coord[1]-1,  self.data[self.coord[0]-1].c_str())
            #s = self.data[self.coord[0]-1].c_str()[self.coord[1]-1]
        key = self.lib.get_key(self.cur_win, y, x)
        #self.lib.write_line(self.cur_win, y, x, s)
        self.lib.refresh(self.cur_win)
        
        self.lib.cursor_0(self.cur_win, y, x)
       

        return key
    
    
     
     
  
    def win_inition(self, y,x, y_begin, x_begin ):
        self.cur_win = self.lib.new_win(y,x, y_begin, x_begin)
        s = self.lib.get_size_win(self.cur_win)
        self.win_size.append(s[0]-1)
        self.win_size.append(s[1]-1)

    def clear_inf(self):
        self.data=None
        self.coord = None
    def return_win(self):
        return self.cur_win
    def return_inf(self):
        return self.coord
    
    def draw_from_begin(self, start):
        self.end_or_begin = 1
        start1 =1
        if start == 1:
            start1 = self.save_start
            self.save_start = start1
        else:
            start1 = self.coord[0]-1
            self.save_start = self.coord[0]-1
            
            
        ym,xm = self.lib.get_size_win(self.cur_win)
        y, x = 1,1

       
      
        data= self.data
        self.block = []
        self.lib.clear_win(self.cur_win)
        self.lib.refresh(self.cur_win)
        print("start_coord ",self.coord[0]-1)
        if (len(data)>0):
            for ii in range(start1,len(data)): # start1 = self.coord[0]-1
                i = data[ii]
                t1 = 0
                t2 = min(xm-1, len(i.c_str())) 
                #print(len(i.c_str()))
                while y<ym-1:
                   #print("was cikl")
                    self.lib.write_line(self.cur_win, y, x, i.c_str()[t1 : t2] )
                    self.lib.refresh(self.cur_win)
                    y+=1
                    self.block.append(i.c_str()[t1 : t2])
                    #print( ii, i.c_str()[t1 : t2])
                  
                    if (t2 ==  len(i.c_str())):
                    #    print("exit course")
                        break
                   
                    t1 = t2
                    t2 = min( t2 + xm-2,len(i.c_str()))
               # print(i.c_str()[t1 : t2] )
                if (self.coord[0] == ii):
                    print("realy was set")
                    realy = ii+1
        print("block len", len(self.block))
        if (len(self.block)>0): print(self.block[0])
        
        
    def draw_from_end(self, start):
        self.end_or_begin = 2
        start1 =1
        if start == 1:
            start1 = self.save_start
            self.save_start = start1
        else:
            start1 = self.coord[0]-1
            self.save_start = self.coord[0]-1
        ym,xm = self.lib.get_size_win(self.cur_win)
        y, x = 1,1
       
       
        data= self.data
        mas = []
        grand_mas = []
        if (len(data)>0):
            for ii in range(start1, -1,-1):  # start1 = self.coord[0]-1
                mas = []
                i = data[ii]                
                t1 = 0
                t2 = min(xm-1, len(i.c_str()))                
                while y<ym-1:               
                    mas.append(i.c_str()[t1 : t2])                   
                    y+=1           
                    if (t2 ==  len(i.c_str())):                    
                        break                   
                    t1 = t2
                    t2 = min( t2 + xm-2,len(i.c_str()))

                if (t2!= len(i.c_str())):
                    while True:
                        mas.append(i.c_str()[t1 : t2])
                        y+=1
                        if (t2 ==  len(i.c_str())):                      
                            break                    
                        t1 = t2
                        t2 = min( t2 + xm-2,len(i.c_str()))

                mas = mas[::-1]
                grand_mas.append(mas)
             
            
        y = ym - 2
        self.last_text = grand_mas
        self.dop_draw()
    def dop_draw(self):
        self.lib.clear_win(self.cur_win)
        self.lib.refresh(self.cur_win)
        y = self.win_size[0] -1
        x=1
        grand_mas = self.last_text
        self.block = []
        for masi in grand_mas:
            for slovo in masi:
                self.block.append(slovo)
                self.lib.write_line(self.cur_win, y, x, slovo )
                self.lib.refresh(self.cur_win)
                y-=1
                if (y== 0):
                    self.block = self.block[::-1]
                    return
                
    def draw_static(self):
        #self.lib.clear_win(self.cur_win)
        self.lib.refresh(self.cur_win)
        y = 1
        x=1
        grand_mas = self.block
        print("draw static test 1")
        print("block len", len(self.block))
        if (len(self.block)>0): print(self.block[0])
        self.block = []
        for slovo in grand_mas:
            self.block.append(slovo)
            self.lib.write_line(self.cur_win, y, x, slovo )
                #print("std ", slovo)
                #print("draw static test 2")
            self.lib.refresh(self.cur_win)
            y+=1
            if (y== self.win_size[0] ):                    
                return

    def choose_last_output(self):

        if self.end_or_begin == 1:
            self.draw_from_begin(1)
        elif self.end_or_begin == 2:
            self.draw_from_end(1)

##доработать ввод с перехродом на следующую строку снизу + переход вниз с j

##поработать над положением курсора при вводе слов
## настроить полпожение курсора от координаты модели
# отработать ввод в пустой блокнот                        +
#просмотреть мелкие баги
#еще раз убедиться что все ок с перескакиванием со строки на строку
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
## отработать искючения

## pytest
## uml
## отчет
## интерфейсы
                    

    def update(self, data,  coordinates,xx, mode) :
        self.data = []
        for i in data:
            #print(i.c_str())
            self.data.append(i)
        print("data size", len(self.data))
       
        self.coord = coordinates
        ''' 
        if (self.coord == self.last_coord): 
            self.lib.refresh(self.cur_win)
            return 
        '''
        if ( (self.coord[0]  - self.last_coord[0] != 0) and (self.coord[1]  - self.last_coord[1] != 0)):  
            self.realc[1] = self.coord[1] 
        print("cur: " ,self.coord)
        print("last: " ,self.last_coord)
        print("real y real x",self.realc[0], self.realc[1])
        if (self.coord[0]== 1 and self.coord[1]==1):                               #начальное положение курсора и текста
            self.draw_from_begin(2)
            self.lib.cursor_0(self.cur_win, 1, 1)

        elif ( self.coord[0]  - self.last_coord[0] == 0):   #обдумать движение по х
            print("running on x realy realx",self.realc[0], self.realc[1])
            if (self.coord[1]  - self.last_coord[1] > 0):
                
                if not (self.realc[1] +1 <  self.win_size[1]):
                    
                    self.realc[0] += 1
                #self.realc[0] += self.coord[1] // self.win_size[1] 
                self.realc [1] = self.coord[1] % self.win_size[1] 
                '''
                #self.check_block(self.realc[0], self.realc[1])
                if self.realc[1]+1 < self.win_size[1]:
                    self.realc[1] += 1
                    print("trarararar")
                    #добавить ограничения
                else:
                    print("trarararar2")
                    self.realc[1] =1
                    self.realc[0] +=1
                print( self.realc[0], self.realc[1])
                '''
                #self.draw_static()
                self.choose_last_output()
                self.lib.cursor_0(self.cur_win, self.realc[0], self.realc[1])
            elif (self.coord[1]  - self.last_coord[1] < 0):
               # self.check_block(self.realc[0], self.realc[1])
                if self.realc[1] < 1:
                    self.realc[1] =1
                #self.realc[0] -= 1 - self.coord[1] // self.win_size[1] 
                self.realc [1] = self.coord[1] % self.win_size[1]
                ''' 
                if self.realc[1] >= 1:
                    self.realc[1] -= 1
                    print("trarararar3")
                    #добавить ограничения 
                else:
                    self.realc[1] =1
                    self.realc[0] -=1   
                    print("trarararar")      
                ''' 
                
                #self.draw_static()
                self.choose_last_output()
                self.lib.cursor_0(self.cur_win, self.realc[0], self.realc[1])
            else:
                print("was draw from static")
                
                #self.draw_static()
                self.choose_last_output()
                self.lib.cursor_0(self.cur_win, self.realc[0], self.realc[1])

        elif ( self.coord[0]  - self.last_coord[0] == 1):
            if len(self.data)< self.coord[0]:
                self.choose_last_output()
                self.realc[0] += 1
                self.realc[1] = 1
                self.lib.cursor_0(self.cur_win, self.realc[0], self.realc[1])
            else: 
                cc = len(self.data[self.coord[0]-1].c_str()) % self.win_size[1]
                c = len(self.data[self.coord[0]-1].c_str()) // self.win_size[1]
                if cc!=0 and c>0:
                    c +=1
                elif c==0:
                    c=1

                cc2 = len(self.data[self.last_coord[0]-1].c_str()) % self.win_size[1]
                c2 = len(self.data[self.last_coord[0]-1].c_str()) // self.win_size[1] 
                ccc2 = self.last_coord[1]// self.win_size[1]
                if cc2!=0 and c2>0:
                    c2 +=1
                elif c2==0:
                    c2=1
                c2 -= ccc2
                #print("data:", self.data[self.last_coord[0]-1])
                #print("cursor j cc2 c2 len size: ",self.realc[0]+c2, cc2,c2, len(self.data[self.last_coord[0]-1].c_str()),self.win_size[1] )
                
                if self.realc[0]+c2 >= self.win_size[0]-1:
                    self.draw_from_end(2)
                    print("==1 draw end ")
                
                  
                    
                    self.realc[0] = self.win_size[0]-1-c  # self.realc[1] = 1
                    self.lib.cursor_0(self.cur_win, self.realc[0], self.realc[1])
                    #установка курсора
                else:
                    #установка курсора

                    # self.draw_from_begin()
        
                    print("==1 draw static ")
                    self.choose_last_output()
                    #self.draw_static()

                    self.realc[0]+= c2
                    #print(self.realc[0], self.realc[1])
                    self.lib.cursor_0(self.cur_win, self.realc[0], self.realc[1])

        elif ( self.coord[0]  - self.last_coord[0] > 1):
            self.draw_from_end(2)
            cc = len(self.data[self.coord[0]-1].c_str()) % self.win_size[1]
            c = len(self.data[self.coord[0]-1].c_str()) // self.win_size[1]
            if cc!=0 and c>0:
                c +=1
            elif c==0:
                c=1
                
            ccc = self.coord[1]//self.win_size[1]
            self.realc[0], self.realc[1] = self.win_size[0]+ccc-c, self.coord[1]%self.win_size[1]
            self.lib.cursor_0(self.cur_win, self.realc[0], self.realc[1])
            #установка курсора
        elif ( self.coord[0]  - self.last_coord[0] == -1):

            print("== -1")
            cc2 = len(self.data[self.coord[0]-1].c_str()) % self.win_size[1]
            c2 = len(self.data[self.coord[0]-1].c_str()) // self.win_size[1] 
            ccc2 = self.last_coord[1] // self.win_size[1] 
            if cc2!=0 and c2>0:
                c2 +=1
            elif c2==0:
                c2=1
            #print(self.realc[0] -c2-ccc2, c2, ccc2)
            if self.realc[0] -c2-ccc2 < 1:
                self.draw_from_begin(2)
                self.realc[0], self.realc[1] = 1,1
                self.lib.cursor_0(self.cur_win, self.realc[0], self.realc[1])
                #установка курсора
            else:
                #установка курсора
                
                #self.draw_static()
                self.choose_last_output()
                self.realc[0]-=c2+ ccc2
                self.lib.cursor_0(self.cur_win, self.realc[0], self.realc[1])
                
            
        elif ( self.coord[0]  - self.last_coord[0] < -1):
            self.draw_from_begin(2) 
            self.realc[0], self.realc[1] = 1,1
            self.lib.cursor_0(self.cur_win, self.realc[0], self.realc[1])

        self.lib.refresh(self.cur_win)
        self.last_coord[0] = self.coord[0]
        self.last_coord[1] = self.coord[1]
        
        print("set last: " ,self.last_coord)


   
# py -3.12 Drive.py