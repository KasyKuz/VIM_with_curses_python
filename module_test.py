from MyString import MyString as MyString

class MyModel_text ():
   
    def __init__(self):
        
        self.state = 0
        self.Controllers = []
        self.coordinats =[1,1]          # координаты начала файла - 24] x  119] - y -x
       
        self.buf = []
        self.all_file = None
        self.text = None
        self.direction = -1             #0 = l, 1- r
        self.copy_str = None
        self.Views_observers = []

    def return_str_buf(self, n):
       
        if 1<=n and n<=len(self.buf):   return self.buf[n-1].c_str()
        return ""
    
    def set_coordinates(self, y,x):
      
        if ( y<=0 or y> len(self.buf) or x<=0 or x >= self.buf[y-1].length()-1):
            
            return    
        self.coordinats[0] = y
        self.coordinats[1] = x

    def return_coordinates(self):
        return self.coordinats
    def rewrite_buf(self):
        s2 = " "
        i=0
        
        s = self.all_file

        for c in s:
            s2+=c
                      
            if c == "\n":
                s2 = MyString(s2)
                self.buf.append(s2)
                s2 = ""
        s2+='\n'
        s2 = MyString(s2)
        self.buf.append(s2)
             

        

    def write_in_buf(self, filename):
        with open(filename) as f:
            s1=f.read()
        self.all_file = s1
        self.rewrite_buf()       
        #print(*self.buf,len(self.buf))
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
    def search_left(self, text):
        t= self.buf[self.coordinats[0]-1].c_str()[:self.coordinats[1]].rfind(text)
        
        if t != -1:
            self.coordinats[1] = 1
            self.state = 1 #тут obsever
            self.text = text
            self.direction = 1
            return
        for i in range (self.coordinats[0]-2,-1,-1):
            t= self.buf[i].c_str().rfind(text)
            if (t!=-1):
                self.coordinats[1] = 1
                self.coordinats[0] = i+1
                self.state = 1 #тут obsever
                self.text = text
                
        self.text = text
        self.direction = 0
        return
    def search_right(self,text):
      
        t = self.buf[self.coordinats[0]-1].find(text, self.coordinats[1]-1)
        if t !=-1:
            self.coordinats[1] = 1
            self.state = 1 #тут obsever
            self.text = text
            self.direction = 1
            return
        for i in range (self.coordinats[0],len(self.buf)):
            t = self.buf[i].find(text)
            if t !=-1:
                self.coordinats[1] = 1 # ????? check
                self.coordinats[0] = i+1 # ????? check
                self.state = 1 #тут obsever
                break
        self.text = text
        self.direction = 1
        return
    def second_search_n(self):
        if self.direction==0:
            self.search_left(self.text)
        elif self.direction==1:
            self.search_right(self.text)
        else:
            print("не бфыло поиска до этого")
    def second_search_N(self):
        if self.direction==1:
            self.search_left(self.text)
        elif self.direction==0:
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
        self.coordinats[1] = self.buf[len(self.buf)-1].length()
        self.coordinats[0] = len(self.buf)

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
      
    def update(self):
        pass
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
        #print(self.coordinats[0], self.coordinats[1])
        #print(self.buf[self.coordinats[0]-1].c_str()[self.coordinats[1]])
        ''' 
        print("curs_right",self.coordinats )
        if (len(self.buf[self.coordinats[0]-1].c_str())>0 and self.buf[self.coordinats[0]-1].c_str()[self.coordinats[1]]!= '\n '):            
            if (self.coordinats[1]+1 <= self.buf[self.coordinats[0]-1].length()-1):
                self.coordinats[1]+=1 # 0 1 2
            else:                
                if ( self.coordinats[0]+1 <= len(self.buf)):
                    self.coordinats[0] += 1
                    self.coordinats[1] = 0
        '''
        if ( self.coordinats[1]+1 < len (self.buf [self.coordinats[0]-1].c_str() )):
            self.coordinats[1]+=1 
  

       
    def curs_left(self):
        ''' 
        if (self.coordinats[1]-1!= 0):            
            if (self.coordinats[1]-1 > -1):
                self.coordinats[1]-=1 # 0 1 2
            else:                
                if ( self.coordinats[0]-1 <= len(self.buf)):
                    self.coordinats[0] += 1
                    self.coordinats[1] = 0
        '''
        if self.coordinats[1]-1 >=1:
            self.coordinats[1] -= 1
    def curs_up(self):
        if  self.coordinats[0] == 1:
            return
        self.coordinats[0] -=1
        
        
    def curs_down(self):
        if  self.coordinats[0] == len(self.buf):
            return
        self.coordinats[0]+= 1

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

    def curs_yw(self):
        t = self.buf[self.coordinats[0]-1].c_str().find(" ", self.coordinats[1]-1)+1
        t2 = self.buf[self.coordinats[0]-1].c_str()[:self.coordinats[1]].rfind(" ")+1
        s = self.buf[self.coordinats[0]-1].c_str()
        s = s[t2:t-1] 
        self.copy_str = s
    def curs_p(self):
        if self.copy_str == None:
            print("no copy text")
            return
        else:
            s = self.buf[self.coordinats[0]-1].c_str()[:self.coordinats[1]-1] + self.copy_str + self.buf[self.coordinats[0]-1].c_str()[self.coordinats[1]-1:]
            self.buf[self.coordinats[0]-1] = MyString(s)
def test_module_test_set_cursor():
    filename = "D:\\Documents\\ооп\\лаб4\\test.txt"
    M = MyModel_text()
    M.write_in_buf(filename)

    #print(M.return_coordinates())
    assert M.return_coordinates() == [1,1], print("error in base coordinates")

    M.set_coordinates(1,3)
    #print(M.return_coordinates())
    assert M.return_coordinates() == [1,3], print("error in set coordinates")

    M.set_coordinates(0,3)
    #print(M.return_coordinates())
    assert M.return_coordinates() == [1,3], print("error in set coordinates")
    
    M.set_coordinates(1,0)
    #print(M.return_coordinates())
    assert M.return_coordinates() == [1,3], print("error in set coordinates")

    M.set_coordinates(1,41)
    #print(M.return_coordinates())
    assert M.return_coordinates() == [1,3], print("error in set coordinates")

    M.set_coordinates(3,0)
    #print(M.return_coordinates())
    assert M.return_coordinates() == [1,3], print("error in set coordinates")
    
def test_module_curs_move_test():
    filename = "D:\\Documents\\ооп\\лаб4\\test.txt"
    M = MyModel_text()
    M.write_in_buf(filename)

    M.curs_right()
    #print(M.return_coordinates())
    assert M.return_coordinates() == [1,2], print("error in set coordinates")

    M.curs_left()
    M.curs_left()
    #print(M.return_coordinates())  
    assert M.return_coordinates() == [1,1], print("error in set coordinates")


    M.curs_up()
    #print(M.return_coordinates())
    assert M.return_coordinates() == [1,1], print("error in set coordinates")

    M.curs_down()
    #print(M.return_coordinates())
    assert M.return_coordinates() == [2,1], print("error in set coordinates")

    M.curs_down()
    M.curs_down()
    #print(M.return_coordinates())
    assert M.return_coordinates() == [3,1], print("error in set coordinates")
def test_module_search_test():
    filename = "D:\\Documents\\ооп\\лаб4\\test.txt"
    M = MyModel_text()
    M.write_in_buf(filename)

    M.set_coordinates(2,4)
    M.curs_begin()
    #print(M.return_coordinates())
    assert M.return_coordinates() == [2,1], print("error in set coordinates")

    M.set_coordinates(2,4)
    M.curs_end()
    #print(M.return_coordinates())
    assert M.return_coordinates() == [2,47], print("error in set coordinates")

    M.curs_gg()
    #print(M.return_coordinates())
    assert M.return_coordinates() == [1,1], print("error in set coordinates")

    M.curs_G()
    #print(M.return_coordinates())
    assert M.return_coordinates() == [3,24], print("error in set coordinates")

    M.curs_NG(3)
    #print(M.return_coordinates())
    assert M.return_coordinates() == [3,1], print("error in set coordinates")

    M.curs_NG(4)
    #print(M.return_coordinates())
    assert M.return_coordinates() == [3,1], print("error in set coordinates")

    M.search_right("greka")
    #print(M.return_coordinates())
    assert M.return_coordinates() == [3,1], print("error in set coordinates")

    M.set_coordinates(1,1)
    M.search_right("reku")
    #print(M.return_coordinates())
    assert M.return_coordinates() == [2,1], print("error in set coordinates")
   
    M.search_left("po")
    #print(M.return_coordinates())
    assert M.return_coordinates() == [1,1], print("error in set coordinates")

    M.set_coordinates(2,8)
    M.curs_b()
    #print(M.return_coordinates())
    assert M.return_coordinates() == [2,6], print("error in set coordinates")

    M.set_coordinates(2,8)
    M.curs_w()
    #print(M.return_coordinates())
    assert M.return_coordinates() == [2,11], print("error in set coordinates")

    M.curs_w()
    #print(M.return_coordinates())
    assert M.return_coordinates() == [2,19], print("error in set coordinates")

    
def test_module_text_working_test():
    filename = "D:\\Documents\\ооп\\лаб4\\test.txt"
    M = MyModel_text()
    M.write_in_buf(filename)

    M.set_coordinates(3,9)
    M.curs_x()
    #print(M.return_str_buf(3))
    assert M.return_str_buf(3) == "sunul grka ruku v reku\n", print("error in set coordinates")

    M.curs_diw()
    #print(M.return_str_buf(3))
    assert M.return_str_buf(3) == "sunul ruku v reku\n", print("error in set coordinates")

    M.curs_dd()   
    assert M.return_str_buf(3) == "", print("error in set coordinates")

    M.curs_yy()
    #print(M.copy_return())
    assert M.copy_return() == "exal greka ch?erez reku vidit greka v reke rak\n", print("error in set coordinates")

    M.curs_yw()
    #print(M.copy_return())
    assert M.copy_return() == "exal", print("error in set coordinates")

    print(M.return_coordinates())
    M.set_coordinates(2,4)
    M.curs_p()
    #print((M.return_str_buf(2)))
    assert M.return_str_buf(2) == "exaexall greka ch?erez reku vidit greka v reke rak\n", print("error in set coordinates")

    

''' 
if __name__ == "__main__":
    module_test_set_cursor() 
    module_curs_move_test()
    module_search_test()
    module_text_working_test()

    #добавить тест на большой файл
   
'''