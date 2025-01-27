from MVC import *
from  test_curses import *
import os
from MyString import MyString as MyString

class MainModel ():
   
    def __init__(self):
 
        
        self.state = 0
       
        self.coordinats =  [1,1]      
        self.borders = []                              #заполнить это поле !!!!!!
       
        self.buf = []
        self.buf_save = []
        self.all_file = None
        self.text = None
        self.direction = -1             #0 = l, 1- r
        self.copy_str = None
        self.observer = Observer()
        self.filename = "None"
        self.block = False                             ### использовать это потом
        self.search_coord = [1,1]
        self.mode = "navigation"
        self.last_command = "No"
    def get_mode(self):
        return self.mode
    def set_mode(self, mode):
        self.mode = mode
    def return_observer(self):
        return self.observer
    def return_inf(self):
        return self.buf
    def return_coordinates(self):
        return self.coordinats
    def return_filename(self):
        return self.filename
    def write_new_data(self, y,x, text):
        pass
    def curs_number(self, n):
        if (n>0 and n<=len(self.buf)):
            self.coordinats[0] = n

    def help(self):
        self.filename = "help.txt"
        self.block = True
        self.write_in_buf("help.txt")
      
    def set_observer(self, view):
        
        self.observer.add_obs(view)
    
    def return_str_buf(self, n):
       
        if 1<=n and n<=len(self.buf):   return self.buf[n-1].c_str()
        return ""
    
    def set_coordinates(self, y,x):
      
        if ( y<=0 or y> len(self.buf) or x<=0 or x >= self.buf[y-1].length()-1):
            
            return    
        self.coordinats[0] = y
        self.coordinats[1] = x

    

    def rewrite_buf(self):
        s2 = " "
        i=0
        
        s = self.all_file
      
        for c in s:
            s2+=c
                      
            if c == "\n":
                print(s2)
                s2 = MyString(s2)
                self.buf.append(s2)
                s2 = ""
        s2+='\n'
        s2 = MyString(s2)
        self.buf.append(s2)

    def file_x(self):
        self.file_w()
        exit(0)

    def file_q(self):
        if self.buf_save!=self.buf:
            pass
        else:exit(0)                    

    def file_q_n(self):
        print("end")
        exit(0)
  
    def file_w(self):
        if self.filename == "None":
            print("give no name for file")
            exit(0)
        try:
            os.remove(self.filename)
            self.write_in_file(self.filename)
        except:
            self.write_in_file(self.filename)
       

    def write_in_file (self, filename):
        
        f = open(filename, "a+")
        for i in self.buf:
            f.write(i.c_str())
        f.close()
        self.filename = "None"
        self.buf = []
        self.coordinats = [1,1]
       

    def write_in_buf(self, filename):
        self.filename = filename
        
        try:
            with open(filename) as f:
                s1=f.read()
            self.all_file = s1
            self.rewrite_buf()      
            print("--------------1",filename)
        except:
            print("-------------2",filename)
            pass
        self.buf_save = self.buf


         
        #print(*self.buf,len(self.buf))
    # работа с файлом

    def search_left(self, text):
        t= self.buf[self.coordinats[0]-1].c_str()[:self.coordinats[1]].rfind(text)
        
        if t != -1:
            self.coordinats[1] = 1
            self.state = 1 #тут obsever
            self.text = text
            self.direction = 1
            self.search_coord[0], self.search_coord[1] = self.coordinats[0], t+1
            return
        for i in range (self.coordinats[0]-2,-1,-1):
            t= self.buf[i].c_str().rfind(text)
            if (t!=-1):
                self.coordinats[1] = 1
                self.coordinats[0] = i+1
                self.state = 1 
                self.text = text
                self.search_coord[0], self.search_coord[1] = i+1, t+1
                
        self.text = text
        self.direction = 0
        print("after search left",self.coordinats, text)
        return
    def search_right(self,text):
        print("size: ", len(self.buf))
        t = self.buf[self.coordinats[0]-1].find(text, self.coordinats[1]-1)
        if t !=-1:
            self.coordinats[1] = 1
            self.state = 1
            self.text = text
            self.direction = 1
            self.search_coord[0], self.search_coord[1] = self.coordinats[0], t+1
            return
       
        for i in range (self.coordinats[0],len(self.buf)):
            t = self.buf[i].find(text)
            if t !=-1:
                self.coordinats[1] = 1 
                self.coordinats[0] = i+1
                self.state = 1 
                self.search_coord[0], self.search_coord[1] = i+1, t+1
                break
        self.text = text
        self.direction = 1
       
        print("after search right",self.coordinats, text)
        return
    def second_search_n(self):
        print("search n ", self.search_coord)
        if self.direction==0:
            self.coordinats[0], self.coordinats[1] = self.search_coord[0], self.search_coord[1]
            self.search_left(self.text)
        elif self.direction==1:
            self.coordinats[0], self.coordinats[1] = self.search_coord[0], self.search_coord[1]
            self.search_right(self.text)
            print("search coord", self.coordinats)
        else:
            print("не было поиска до этого")
    def second_search_N(self):
        if self.direction==1:
            self.coordinats[0], self.coordinats[1] = self.search_coord[0], self.search_coord[1]
            self.search_left(self.text)
        elif self.direction==0:
            self.coordinats[0], self.coordinats[1] = self.search_coord[0], self.search_coord[1]
            self.search_right(self.text)
        else:
            print("не бфыло поиска до этого")

    def curs_end(self):
        self.coordinats[1] = self.buf[self.coordinats[0]-1].length()       
        self.state = 1
        return
    def curs_begin(self):
        self.coordinats[1] = 1            
        self.state = 1
        return
    def curs_gg(self):
        self.coordinats[1] = 1
        self.coordinats[0] = 1
    def curs_G(self):
        print((" GGGGGGGGGGGGGGGGGGGGGGGGGGGG"))
        self.coordinats[1] = self.buf[len(self.buf)-1].length()
        self.coordinats[0] = len(self.buf)
        print("module print")
        print(self.buf[self.coordinats[0]-1].c_str())

    def curs_NG(self, N):
      
        if len(self.buf) >= N  and N>=1:
            self.coordinats[1] = 1
            self.coordinats[0] = N
       

    def curs_w(self):
       
        if (self.coordinats[1]+1 == self.buf[self.coordinats[0]-1].length()-1 or self.coordinats[1]==self.buf[self.coordinats[0]-1].length()-1):
            self.coordinats[1] = self.buf[self.coordinats[0]-1].length()
            return
        x = self.coordinats[1] +1
        y = self.coordinats[0] -1
        while (self.buf[y].c_str()[x]!=" " and x!=self.buf[self.coordinats[0]-1].length()):           
            x+=1
        self.coordinats[1] = x +1
        
        return
    
    def curs_b(self):
        if (self.coordinats[1]-1 == 1 or self.coordinats[1]-2 == 1 or self.coordinats[1]==1):
            self.coordinats[1] = 1
            return
        x = self.coordinats[1]-2
        y = self.coordinats[0] -1
        while (self.buf[y].c_str()[x]!=" " and x!=-1):           
            x-=1

        self.coordinats[1] = x+2        
        return
      
        
    def curs_right(self):
        
        if ( self.coordinats[1]+1 < len (self.buf [self.coordinats[0]-1].c_str() )):
            self.coordinats[1]+=1 
        
  

       
    def curs_left(self):
      
        if self.coordinats[1]-1 >=1:
            self.coordinats[1] -= 1
        
    def curs_up(self):
        if  self.coordinats[0] == 1:
            return
        self.coordinats[0] -=1
        if len(self.buf[self.coordinats[0]-1].c_str()) < self.coordinats[1]:
            self.coordinats[1] = len(self.buf[self.coordinats[0]-1].c_str())
        
        
    def curs_down(self):
        if  self.coordinats[0] == len(self.buf):
            return
        self.coordinats[0]+= 1
     
        if len(self.buf[self.coordinats[0]-1].c_str()) < self.coordinats[1]:
            self.coordinats[1] = len(self.buf[self.coordinats[0]-1].c_str())

    def curs_x(self):
        s = self.buf[self.coordinats[0]-1].c_str()
        s = s[:self.coordinats[1]-1] + s[self.coordinats[1]:]
        self.buf[self.coordinats[0]-1] = MyString(s)
        return
    
    def curs_diw(self):
        t = self.buf[self.coordinats[0]-1].c_str().find(" ", self.coordinats[1]-1)+1
        t2 = self.buf[self.coordinats[0]-1].c_str()[:self.coordinats[1]].rfind(" ")+1
        s = self.buf[self.coordinats[0]-1].c_str()
        s = s[:t2] + s[t:]
        self.buf[self.coordinats[0]-1] = MyString(s)
        return
    def curs_dd(self):
        self.buf.pop(self.coordinats[0]-1)
        self.coordinats[0] = self.coordinats[0]-1
        self.coordinats[1] = 1

    def copy_return(self):
        return self.copy_str
    def curs_yy(self):
        self.copy_str = self.buf[self.coordinats[0]-1].c_str()
        print("yy ", self.copy_str)

    def curs_yw(self):
        t = self.buf[self.coordinats[0]-1].c_str().find(" ", self.coordinats[1]-1)+1
        t2 = self.buf[self.coordinats[0]-1].c_str()[:self.coordinats[1]].rfind(" ")+1
        s = self.buf[self.coordinats[0]-1].c_str()
        s = s[t2:t-1] 
        self.copy_str = s
        print("yw ", self.copy_str)
    def curs_p(self):
        print("try to past")
        if self.copy_str == None:
            print("no copy text")
            return
        else:
            if self.copy_str[len(self.copy_str)-1] == '\n':
                self.buf.insert( self.coordinats[0]-1, MyString(self.copy_str) )
            else: 
                s = self.buf[self.coordinats[0]-1].c_str()[:self.coordinats[1]-1] + self.copy_str + self.buf[self.coordinats[0]-1].c_str()[self.coordinats[1]-1:]
                self.buf[self.coordinats[0]-1] = MyString(s)
            #print(s)

    #--------------------------------------------------------------------------
    def text_i(self,ch):
        
        if len(self.buf)< self.coordinats[0]:
            self.buf.append( MyString(ch))
            self.coordinats[1]+=1
        else: # len(self.buf)!=0:
            s = self.buf[self.coordinats[0]-1].c_str()
            s = s[:self.coordinats[1] - 1] + ch +s [self.coordinats[1] - 1:]
            self.buf[self.coordinats[0]-1] = MyString(s)
            self.coordinats[1]+=1
       
        if ch =='\n':
            self.coordinats[0]+=1
            self.coordinats[1] = 1
      


        
    def text_I(self,ch):
        self.coordinats[1] = 1
        self.text_i(ch)
        #self.coordinats[1]-=2
        
    def text_A(self,ch):
        self.coordinats[1] = len(self.buf[self.coordinats[0]-1].c_str())
        
    def text_S(self,ch):
        s = ""
        s+=ch
        self.buf[self.coordinats[0]-1] = MyString(s)
        self.coordinats[1] = 2
        

    def text_r(self,ch):
        s = self.buf[self.coordinats[0]-1].c_str()
        s = s[:self.coordinats[1] - 1] + ch +s [self.coordinats[1] :]
        self.buf[self.coordinats[0]-1] = MyString(s)