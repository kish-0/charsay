
def makestring(inpt):
    s=""
    for j in inpt:
        if inpt.index(j) < 100:
            s+=j
        else:
            break

    s = s.split()
    s = " ".join(s)
    return s

def bart(inp):
    s = makestring(inp)
    print(rf"""             
    |\/\/\/|   
    |      |   
    |      |     |{s}|
    | (o)(o)      /
    C      _)    /
    | ,___| ____/
    |   /    
   /____\    
  /      \ """)
    
def homer(inp):
    s = makestring(inp)
    print(rf"""
     __&__      
    /     \     
    |       |    |{s}|
    |  (o)(o)    /
    C   .---_)  / 
    | |.___| __/    
    |  \__/     
   /_____\     
  /_____/ \    
 /         \ """)

def marge(inp):
    s = makestring(inp)
    print(rf"""
            
       oooo
     ooooooooo
    oooooooooooo
    ooooooooooooo
     oooooooooooooo
     oooooooooooooo
     ooooooOOOOOOOO
      oooooooooooooo
      oooooooooooooo
      oooooooooooooo
      oooooooooooooo
       oooooooooooooo
       oooooooooooooo
       ooooo \_| \_|o
       oooo \/  \/  \
       oooo (o   )o  )
       O/c   \__/ --.     |{s}|  
       O\_   ,     -'     /
        O|  '\_______)   /
         |       _)  ___/
         oooooooo
        /        \ """)
    
def lisa(inp):
    s = makestring(inp)
    print(rf"""
          
          /\  /\
      ___/  \/  \___
     |             /
     |            /_
     /     \_| \_| /
    /     \/  \/  \/
    \     (o   )o  )     |{s}|
     \ /c  \__/ --.      /
     | \_  ,     -'     /
     |_ | '\_______) __/
       ||      _)
        |     |
        ooooooo
       /       \ """)
    
def maggie(inp):
    s = makestring(inp)
    print(rf"""
       /\
 .----/  \----.
  \          /
.--\ (o)(o) /__.  |*slurp* ga ga ga|
 \     ()     /   /
  >   (C_)   < __/
 /___\____/___\
    /|    |\
   /        \ """)
    



def main():
    s = "Hello, world!"
    maggie(s)
    
if __name__ == "__main__":
    main()
