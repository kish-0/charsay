import textwrap
# Declaring global maximum horizontal char accomodation of speech box
global maxlength
maxlength = 60

def wrapup(t):
    wrapper = textwrap.TextWrapper(width=maxlength)
    wl = wrapper.wrap(text=t)
    return wl

def say(ls):
    big = None
    length = len(ls)
    if length > 60:                          # Check if wrapping is actually needed
        ls = wrapup(ls)
        maxlength = 60
        big = True
    else:
        maxlength = length

    print("  " + "_" * maxlength)            # Header top line
    print(" " + "0" + " " * maxlength + "0") # Header top line - corners

    if big:                                  # If wrapping is required, printed accordingly
        for x in ls:
            if len(x) == maxlength:
                print(" " + "|" + x + "|")
            else:
                while len(x) < maxlength:
                    x = x + " "
                print(" " + "|" + x + "|")
    else:
        print(" " + "|" + ls + "|")          # Normal printing for strings with < 60 chars
    

    print(" " + "0" + "_" * maxlength + "0")  # Last closing line

def main():
    s = input("Input: ")
    say(s)
if __name__ == "__main__":
    main()