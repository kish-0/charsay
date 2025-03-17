import random
from .speechbubble import say
from .content import Homer, Bart, Marge, Lisa, Maggie
characters = ['homer', 'bart', 'marge', 'lisa', 'maggie']
from .content import lucky_list



class Charactersay:
    def __init__(self, horizontal_length=60):
        self.maxlength = horizontal_length
        self.string = "Hello, world!"
        self.internalcall = False

    def __str__(self):
        return("Character say!")
    
    
    def imfeelinglucky(self):                                # Generates a random character saying a random lucky-line from the content file
        x = random.choice(characters)
        self.internalcall = True                             # To indicate that the character funcs are being called internally
        say(random.choice(lucky_list), self.maxlength)
        match x:
            case 'homer':
                self.homer()
            case 'marge':
                self.marge()
            case 'bart' :
                self.bart()
            case 'lisa' :
                self.lisa()
            case 'maggie':
                self.maggie()
        self.internalcall = False

    def bart(self):
        if not self.internalcall:  
            say(self.string, self.maxlength)
        print(Bart)

    def homer(self):
        if not self.internalcall:                            # Should not say bcz, when its internally called, the random string musnt clash with given string
            say(self.string, self.maxlength)
        print(Homer)

    def marge(self):
        if not self.internalcall:  
            say(self.string, self.maxlength)
        print(Marge)
        
    def lisa(self):
        if not self.internalcall:  
            say(self.string, self.maxlength)
        print(Lisa)
        
    def maggie(self):
        if not self.internalcall:  
            say(self.string, self.maxlength)
        print(Maggie)


    @property
    def string(self):
        return self._string
    
    @string.setter
    def string(self, string):
        string = str(string)
        self._string = string


    @property
    def maxlength(self):
        return self._maxlength
    
    @maxlength.setter
    def maxlength(self, maxlength):
        try:
            maxlength = int(maxlength)
        except ValueError:
            raise ValueError("maxlength needs to be <class 'int'> or <class 'float'>")
        
        if maxlength < 15:
            raise ValueError("'maxlength' cannot be lower than 15")
        self._maxlength = maxlength
    







    

