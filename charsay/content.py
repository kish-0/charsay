
#CHARACTERS:

Bart = rf"""   
                 |          
    |\/\/\/|     |
    |      |     | 
    |      |     |
    | (o)(o)     |
    C      _)    |
    | ,___| ____/
    |   /    
   /____\    
  /      \ """

Homer =     rf""" 
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
 /         \ """ 

Marge = rf"""
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
"""

Lisa = rf"""
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
    """

Maggie = rf"""
       /\
 .----/  \----.    ________________
  \          /    0                0
.--\ (o)(o) /__.  |*slurp* ga ga ga|
 \     ()     /   0________________0 
  >   (C_)   < __/
 /___\____/___\
    /|    |\
   /        \ """









#LUCKY:
lucky_list = [
    "A new adventure awaits you.",
    "Believe in yourself and anything is possible.",
    "Better days are ahead.",
    "Change is coming, be ready.",
    "Chase your dreams with passion.",
    "Courage is the key to success.",
    "Dream big, work harder.",
    "Every cloud has a silver lining.",
    "Every day is a new chance.",
    "Faith can move mountains.",
    "Follow your heart, it knows best.",
    "Fortune favors the brave.",
    "Good things come to those who wait.",
    "Happiness is a choice.",
    "Hard work pays off in the end.",
    "Hope is the light in darkness.",
    "Innovation is the key to progress.",
    "Inspiration is everywhere, look closely.",
    "It's never too late to start.",
    "Keep moving forward, no matter what.",
    "Kindness goes a long way.",
    "Laughter is the best medicine.",
    "Life is full of surprises.",
    "Life is precious, cherish it.",
    "Love conquers all.",
    "Luck is what happens when preparation meets opportunity.",
    "Make every moment count.",
    "Never give up on your dreams.",
    "Never stop learning.",
    "New beginnings bring new opportunities.",
    "Opportunities are hidden in challenges.",
    "Patience is a virtue.",
    "Perseverance is the path to success.",
    "Positive thoughts attract positive outcomes.",
    "Smile often, it's contagious.",
    "Stay curious, stay wise.",
    "Success is not final, failure is not fatal.",
    "The best is yet to come.",
    "The future belongs to those who believe.",
    "The journey is just as important as the destination.",
    "The power is within you.",
    "The sky is the limit.",
    "There is beauty in simplicity.",
    "Think big, achieve bigger.",
    "Time is precious, use it wisely.",
    "Today is a new day.",
    "Tomorrow will be better.",
    "Trust your instincts.",
    "Vision is the art of seeing what is invisible.",
    "Wealth is not just about money.",
    "What goes around comes around.",
    "When life gives you lemons, make lemonade.",
    "Wisdom is the reward for experience.",
    "Worry less, live more.",
    "You are capable of more than you think.",
    "You are stronger than you seem.",
    "You are unique, celebrate it.",
    "You have the power to change your life.",
    "You will find your way.",
    "Your destiny awaits you.",
    "Your dreams are within reach.",
    "Your future is bright.",
    "Your heart knows the way.",
    "Your journey is special.",
    "Your life is a masterpiece.",
    "Your path is unique.",
    "Your potential is limitless.",
    "Your smile can change the world.",
    "Your story is still being written.",
    "Your voice matters.",
    "You're closer than you think.",
    "You're doing better than you think.",
    "You're stronger than yesterday.",
    "You're the architect of your life.",
    "You've got this.",
    "A beautiful day is coming.",
    "A chance encounter will change your life.",
    "A door is about to open for you.",
    "A fresh start is on the horizon.",
    "A great opportunity is coming your way.",
    "A hidden talent will soon be revealed.",
    "A journey of a thousand miles begins with one step.",
    "A little kindness can go a long way.",
    "A new chapter in your life is about to begin.",
    "A new friend is on the way.",
    "A path of discovery awaits you.",
    "A smile is the best accessory.",
    "A surprise is headed your way.",
    "A wonderful surprise awaits you.",
    "Abundance is coming into your life.",
    "Adventure calls, answer it.",
    "Always believe in yourself.",
    "Always keep a positive attitude.",
    "An exciting journey is ahead of you.",
    "An opportunity to shine is coming.",
    "Anything is possible if you believe.",
    "Be brave, be bold.",
    "Be open to new experiences.",
    "Be the change you wish to see.",
    "Be true to yourself.",
    "Believe in the impossible.",
    "Better things are coming.",
    "Blessings are on their way.",
    "Chase your fears, they will lead you to success.",
    "Choose happiness every day.",
    "Do what makes you happy.",
    "Dreams do come true.",
    "Every experience is a lesson.",
    "Every moment is a gift.",
    "Expect good things to happen.",
    "Faith will guide you through tough times.",
    "Focus on the positive.",
    "Good fortune is smiling upon you.",
    "Good things are coming your way.",
    "Great things are in store for you.",
    "Happiness is just around the corner.",
    "Hard work and determination will pay off.",
    "Have faith in yourself.",
    "Hope for the best.",
    "In every end, there is a new beginning.",
    "Innovation leads to success.",
    "Inspiration is all around you.",
    "It's okay to take risks.",
    "Keep shining your light.",
    "Kindness will bring you joy.",
    "Laughter heals the soul.",
    "Life is a beautiful adventure.",
    "Life is full of endless possibilities.",
    "Life's journey is precious, enjoy it.",
    "Look forward to a brighter tomorrow.",
    "Love is the answer to every question.",
    "Luck is on your side.",
    "Make today count.",
    "May your path be lit with joy.",
    "Miracles happen every day.",
    "New experiences await you.",
    "Never lose faith in yourself.",
    "Never underestimate your power.",
    " Opportunities are everywhere, seize them.",
    "Optimism is the key to success.",
    "Peace and happiness are within you.",
    "Positive energy attracts positive outcomes.",
    "Prosperity is on its way.",
    "Smile and the world smiles with you.",
    "Sometimes the best things in life are unexpected.",
    "Stay positive, stay strong.",
    "Success is just around the corner.",
    "The best days of your life are yet to come.",
    "The future is full of promise.",
    "The power of positivity is within you.",
    "The universe has your back.",
    "There is always hope.",
    "Think positively, act positively.",
    "Today is a gift, use it wisely.",
    "Tomorrow will bring new opportunities.",
    "Trust that everything will work out.",
    "Visionary ideas will lead you to success.",
    "Wealth and prosperity are coming your way.",
    "What you seek is seeking you.",
    "When you believe, anything is possible.",
    "Wisdom guides you through life's journey.",
    "Wonders await you on your journey.",
    "You are a shining star.",
    "You are capable of achieving greatness.",
    "You are destined for success.",
    "You are stronger than you think.",
    "You have the power to create your destiny.",
    "You will achieve your dreams.",
    "You will find your true path.",
    "Your dreams are within reach.",
    "Your future is filled with promise.",
    "Your heart is full of love and kindness.",
    "Your journey is unique and special.",
    "Your life is a masterpiece, keep creating.",
    "Your path is lit with success.",
    "Your potential is limitless, believe in it.",
    "Your smile can light up the world.",
    "Your story is one of triumph.",
    "Your voice is powerful, use it wisely.",
]
