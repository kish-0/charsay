from .speechbubble import say

def bart(inp):
    s = say(inp)
    print(rf"""   
                 |          
    |\/\/\/|     |
    |      |     | 
    |      |     |
    | (o)(o)     |
    C      _)    |
    | ,___| ____/
    |   /    
   /____\    
  /      \ """)
    
def homer(inp):
    s = say(inp)
    print(rf""" 
                |
     __&__      |
    /     \     |
    |       |   |  
    |  (o)(o)   |
    C   .---_)  | 
    | |.___| __/    
    |  \__/     
   /_____\     
  /_____/ \    
 /         \ """)

def marge(inp):
    s = say(inp)
    print(rf"""
 |         
 |              (####)
 |            (#######)
 |          (#########)
 |         (#########)
 |        (#########)
 |       (#########)
 |      (#########)
 |     (#########)
 |    (#########) 
 |     (o)(o)(##)
  \  ,_C     (##)
   \ /___,   (##)    
      \     (#) 
       |    |   
       OOOOOO  
      /      \
""")
    
def lisa(inp):
    s = say(inp)
    print(rf"""
 |          
 |   /\ /\  /\      
 |   | V  \/  \---. 
 |    \_        /   
 |     (o)(o)  <__. 
 |    _C         /  
  \_ /____,   )  \  
       \     /----' 
        ooooo       
       /     \
    """)
    
def maggie(inp):
    s = say(inp)
    print(rf"""
       /\
 .----/  \----.    ________________
  \          /    0                0
.--\ (o)(o) /__.  |*slurp* ga ga ga|
 \     ()     /   0________________0 
  >   (C_)   < __/
 /___\____/___\
    /|    |\
   /        \ """)
    



def main():
    s = "Hello, world!"
    maggie(s)
    
if __name__ == "__main__":
    main()
