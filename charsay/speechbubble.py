import textwrap

def wrapup(t):                                                # Wraps up text to be no more than 'maxlength' characters horzontally by sending them to \n
    wrapper = textwrap.TextWrapper(width=maxlength)
    wl = wrapper.wrap(text=t)
    return wl

def say(ls, maxl):
    global maxlength                                              # Declaring global maximum horizontal char accomodation of speech box
    maxlength = maxl
    big = None
    length = len(ls)
    frontpadding = " "                                        # Padding preceding the bubble

    if length > 60:                                           # Check if wrapping is actually needed
        ls = wrapup(ls)
        big = True
    else:
        if length > 20:
            maxlength = length
        else:
            maxlength = 20
            ls += " " * (20 - length)                         # If string len < 20, we succeed the string with " " so as to make the bubble uniform and connected to cartoon character

    print(frontpadding + " " + "_" * maxlength)               # Header top line
    print(frontpadding + "0" + " " * maxlength + "0")         # Header top line - corners

    if big:                                                   # If wrapping is required, printed accordingly
        for x in ls:
            if len(x) == maxlength:
                print(frontpadding + "|" + x + "|")
            else:
                while len(x) < maxlength:
                    x = x + " "
                print(frontpadding + "|" + x + "|")
    else:
        print(frontpadding + "|" + ls + "|")                   # Normal printing for strings with < 60 chars
    

    print(frontpadding + "0" + "_" * maxlength + "0", end="")  # Last closing line

def main():
    s = input("Input: ")
    say(s)
if __name__ == "__main__":
    main()