# encoding=utf8
def banner_bash( bannerstring ):

    length= len(bannerstring)
    i=0
    v_str=""
    
    while ( i < 6 ):
        j=0
        while (j < length):
        
            char = bannerstring[j].lower()

            if ( i == 0 ):
                if ( char == "0" ):v_str+="  ██████╗ "
                elif ( char == "1" ):v_str+="  ██╗"
                elif ( char == "2" ):v_str+=" ██████╗ "
                elif ( char == "3" ):v_str+=" ██████╗ "
                elif ( char == "4" ):v_str+=" ██╗  ██╗"
                elif ( char == "5" ):v_str+=" ███████╗"
                elif ( char == "6" ):v_str+="  ██████╗ "
                elif ( char == "7" ):v_str+=" ███████╗"
                elif ( char == "8" ):v_str+="  █████╗ "
                elif ( char == "9" ):v_str+="  █████╗ "

                elif ( char == "a" ):v_str+="  █████╗ "
                elif ( char == "b" ):v_str+=" ██████╗ "
                elif ( char == "c" ):v_str+="  █████╗ "
                elif ( char == "d" ):v_str+=" ██████╗ "
                elif ( char == "e" ):v_str+=" ███████╗"
                elif ( char == "f" ):v_str+=" ███████╗"
                elif ( char == "g" ):v_str+="  ██████╗ "
                elif ( char == "h" ):v_str+=" ██╗  ██╗"
                elif ( char == "i" ):v_str+=" ██╗"
                elif ( char == "j" ):v_str+="      ██╗"
                elif ( char == "k" ):v_str+=" ██╗  ██╗"
                elif ( char == "l" ):v_str+=" ██╗     "
                elif ( char == "m" ):v_str+=" ███╗   ███╗"
                elif ( char == "n" ):v_str+=" ███╗  ██╗"
                elif ( char == "o" ):v_str+="  █████╗ "
                elif ( char == "p" ):v_str+=" ██████╗ "
                elif ( char == "q" ):v_str+="  ██████╗ "
                elif ( char == "r" ):v_str+=" ██████╗ "
                elif ( char == "s" ):v_str+="  ██████╗"
                elif ( char == "t" ):v_str+=" ████████╗"
                elif ( char == "u" ):v_str+=" ██╗   ██╗"
                elif ( char == "v" ):v_str+=" ██╗   ██╗"
                elif ( char == "w" ):v_str+="  ██╗       ██╗"
                elif ( char == "x" ):v_str+=" ██╗  ██╗"
                elif ( char == "y" ):v_str+=" ██╗   ██╗"
                elif ( char == "z" ):v_str+=" ███████╗"

                elif ( char == "+" ):v_str+="        "
                elif ( char == "-" ):v_str+="       "
                elif ( char == "*" ):v_str+="         "
                elif ( char == "/" ):v_str+="     ██╗"
                elif ( char == "=" ):v_str+="        "
                elif ( char == "." ):v_str+="    "
                elif ( char == "<" ):v_str+="   ██╗"
                elif ( char == ">" ):v_str+=" ██╗  "
                elif ( char == "%" ):v_str+=" ██╗ ██╗"
                elif ( char == "^" ):v_str+="     ██    "

                elif ( char == "!" ):v_str+=" ██╗"             
                elif ( char == "?" ):v_str+="  █████╗ "
                elif ( char == ":" ):v_str+=" ██╗"
                elif ( char == "" ):v_str+=" ██╗"
                elif ( char == "$" ):v_str+="  ███████╗"
                elif ( char == "@" ):v_str+="   █████╗ "
                elif ( char == "," ):v_str+="    "
                elif ( char == "&" ):v_str+="  ╔██████╗ "
                elif ( char == "'" ):v_str+=" ██╗"
                elif ( char == "[" ):v_str+=" ████╗"
                elif ( char == "]" ):v_str+=" ████╗"
                elif ( char == "#" ):v_str+="    ██╗ ██╗ "
                elif ( char == " " ):v_str+="   "
                
            if ( i == 1 and j == 0 ):v_str+="\n"


            if ( i == 1 ):
                if ( char == "0" ):v_str+=" ██╔═████╗"
                elif ( char == "1" ):v_str+=" ███║"
                elif ( char == "2" ):v_str+=" ╚════██╗"
                elif ( char == "3" ):v_str+=" ╚════██╗"
                elif ( char == "4" ):v_str+=" ██║  ██║"
                elif ( char == "5" ):v_str+=" ██╔════╝"
                elif ( char == "6" ):v_str+=" ██╔════╝ "
                elif ( char == "7" ):v_str+=" ╚════██║"
                elif ( char == "8" ):v_str+=" ██╔══██╗"
                elif ( char == "9" ):v_str+=" ██╔══██╗"

                elif ( char == "a" ):v_str+=" ██╔══██╗"
                elif ( char == "b" ):v_str+=" ██╔══██╗"
                elif ( char == "c" ):v_str+=" ██╔══██╗"
                elif ( char == "d" ):v_str+=" ██╔══██╗"
                elif ( char == "e" ):v_str+=" ██╔════╝"
                elif ( char == "f" ):v_str+=" ██╔════╝"
                elif ( char == "g" ):v_str+=" ██╔════╝ "
                elif ( char == "h" ):v_str+=" ██║  ██║"
                elif ( char == "i" ):v_str+=" ██║"
                elif ( char == "j" ):v_str+="      ██║"
                elif ( char == "k" ):v_str+=" ██║ ██╔╝"
                elif ( char == "l" ):v_str+=" ██║     "
                elif ( char == "m" ):v_str+=" ████╗ ████║"
                elif ( char == "n" ):v_str+=" ████╗ ██║"
                elif ( char == "o" ):v_str+=" ██╔══██╗"
                elif ( char == "p" ):v_str+=" ██╔══██╗"
                elif ( char == "q" ):v_str+=" ██╔═══██╗"
                elif ( char == "r" ):v_str+=" ██╔══██╗"
                elif ( char == "s" ):v_str+=" ██╔════╝"
                elif ( char == "t" ):v_str+=" ╚══██╔══╝"
                elif ( char == "u" ):v_str+=" ██║   ██║"
                elif ( char == "v" ):v_str+=" ██║   ██║"
                elif ( char == "w" ):v_str+="  ██║  ██╗  ██║"
                elif ( char == "x" ):v_str+=" ╚██╗██╔╝"
                elif ( char == "y" ):v_str+=" ╚██╗ ██╔╝"
                elif ( char == "z" ):v_str+=" ╚════██║"

                elif ( char == "+" ):v_str+="   ██╗  "
                elif ( char == "-" ):v_str+="       "
                elif ( char == "*" ):v_str+=" ██    ██"
                elif ( char == "/" ):v_str+="    ██╔╝"
                elif ( char == "=" ):v_str+=" ██████╗"
                elif ( char == "." ):v_str+="    "
                elif ( char == "<" ):v_str+="  ██╔╝"
                elif ( char == ">" ):v_str+=" ╚██╗ "
                elif ( char == "%" ):v_str+=" ╚═╝██╔╝"
                elif ( char == "^" ):v_str+="   ██  ██  "

                elif ( char == "!" ):v_str+=" ██║"
                elif ( char == "?" ):v_str+=" ██╔══██╗"
                elif ( char == ":" ):v_str+=" ╚═╝"
                elif ( char == "" ):v_str+=" ╚═╝"
                elif ( char == "$" ):v_str+=" ██╔██╔══╝"
                elif ( char == "@" ):v_str+=" ██╔══█═██"
                elif ( char == "," ):v_str+="    "
                elif ( char == "&" ):v_str+="  █════██║ "
                elif ( char == "'" ):v_str+=" ╚█║"
                elif ( char == "[" ):v_str+=" ██╔═╝"
                elif ( char == "]" ):v_str+=" ╚═██║"
                elif ( char == "#" ):v_str+=" ██████████╗"   
                elif ( char == " " ):v_str+="   "
                
            if ( i == 2 and j == 0 ):v_str+="\n"


            if ( i == 2 ):
                if ( char == "0" ):v_str+=" ██║██╔██║"
                elif ( char == "1" ):v_str+=" ╚██║"
                elif ( char == "2" ):v_str+="  █████╔╝"
                elif ( char == "3" ):v_str+="  █████╔╝"
                elif ( char == "4" ):v_str+=" ███████║"
                elif ( char == "5" ):v_str+=" ███████╗"
                elif ( char == "6" ):v_str+=" ███████╗ "
                elif ( char == "7" ):v_str+="     ██╔╝"
                elif ( char == "8" ):v_str+=" ╚█████╔╝"
                elif ( char == "9" ):v_str+=" ╚██████║"

                elif ( char == "a" ):v_str+=" ███████║"
                elif ( char == "b" ):v_str+=" ██████╦╝"
                elif ( char == "c" ):v_str+=" ██║  ╚═╝"
                elif ( char == "d" ):v_str+=" ██║  ██║"
                elif ( char == "e" ):v_str+=" █████╗  "
                elif ( char == "f" ):v_str+=" █████╗  "
                elif ( char == "g" ):v_str+=" ██║  ██╗ "
                elif ( char == "h" ):v_str+=" ███████║"
                elif ( char == "i" ):v_str+=" ██║"
                elif ( char == "j" ):v_str+="      ██║"
                elif ( char == "k" ):v_str+=" █████═╝ "
                elif ( char == "l" ):v_str+=" ██║     "
                elif ( char == "m" ):v_str+=" ██╔████╔██║"
                elif ( char == "n" ):v_str+=" ██╔██╗██║"
                elif ( char == "o" ):v_str+=" ██║  ██║"
                elif ( char == "p" ):v_str+=" ██████╔╝"
                elif ( char == "q" ):v_str+=" ██║██╗██║"
                elif ( char == "r" ):v_str+=" ██████╔╝"
                elif ( char == "s" ):v_str+=" ╚█████╗ "
                elif ( char == "t" ):v_str+="    ██║   "
                elif ( char == "u" ):v_str+=" ██║   ██║"
                elif ( char == "v" ):v_str+=" ╚██╗ ██╔╝"
                elif ( char == "w" ):v_str+="  ╚██╗████╗██╔╝"
                elif ( char == "x" ):v_str+="  ╚███╔╝ "
                elif ( char == "y" ):v_str+="  ╚████╔╝ "
                elif ( char == "z" ):v_str+="   ███╔═╝"

                elif ( char == "+" ):v_str+=" ██████╗"
                elif ( char == "-" ):v_str+=" █████╗"
                elif ( char == "*" ):v_str+="   ████  "
                elif ( char == "/" ):v_str+="   ██╔╝ "
                elif ( char == "=" ):v_str+=" ╚═════╝"
                elif ( char == "." ):v_str+="    "
                elif ( char == "<" ):v_str+=" ██╔╝ "
                elif ( char == ">" ):v_str+="  ╚██╗"
                elif ( char == "%" ):v_str+="   ██╔╝ "
                elif ( char == "^" ):v_str+=" ██      ██"

                elif ( char == "!" ):v_str+=" ██║"
                elif ( char == "?" ):v_str+=" ╚═╝███╔╝"
                elif ( char == ":" ):v_str+="    "
                elif ( char == "" ):v_str+="    "
                elif ( char == "$" ):v_str+=" ╚██████╗ "
                elif ( char == "@" ):v_str+=" ██║  ████"
                elif ( char == "," ):v_str+="    "
                elif ( char == "&" ):v_str+="   ███  ╚╝ "
                elif ( char == "'" ):v_str+="  ╚╝"
                elif ( char == "[" ):v_str+=" ██║  "
                elif ( char == "]" ):v_str+="   ██║"
                elif ( char == "#" ):v_str+=" ╚═██╔═██╔═╝"
                elif ( char == " " ):v_str+="   "
                
            if ( i == 3 and j == 0 ):v_str+="\n"


            if ( i == 3 ):
                if ( char == "0" ):v_str+=" ████╔╝██║"
                elif ( char == "1" ):v_str+="  ██║"
                elif ( char == "2" ):v_str+=" ██╔═══╝ "
                elif ( char == "3" ):v_str+="  ╚═══██╗"
                elif ( char == "4" ):v_str+=" ╚════██║"
                elif ( char == "5" ):v_str+=" ╚════██║"
                elif ( char == "6" ):v_str+=" ██╔═══██╗"
                elif ( char == "7" ):v_str+="    ██╔╝ "
                elif ( char == "8" ):v_str+=" ██╔══██╗"
                elif ( char == "9" ):v_str+="  ╚═══██║"

                elif ( char == "a" ):v_str+=" ██╔══██║"
                elif ( char == "b" ):v_str+=" ██╔══██╗"
                elif ( char == "c" ):v_str+=" ██║  ██╗"
                elif ( char == "d" ):v_str+=" ██║  ██║"
                elif ( char == "e" ):v_str+=" ██╔══╝  "
                elif ( char == "f" ):v_str+=" ██╔══╝  "
                elif ( char == "g" ):v_str+=" ██║  ╚██╗"
                elif ( char == "h" ):v_str+=" ██╔══██║"
                elif ( char == "i" ):v_str+=" ██║"
                elif ( char == "j" ):v_str+=" ██╗  ██║"
                elif ( char == "k" ):v_str+=" ██╔═██╗ "
                elif ( char == "l" ):v_str+=" ██║     "
                elif ( char == "m" ):v_str+=" ██║╚██╔╝██║"
                elif ( char == "n" ):v_str+=" ██║╚████║"
                elif ( char == "o" ):v_str+=" ██║  ██║"
                elif ( char == "p" ):v_str+=" ██╔═══╝ "
                elif ( char == "q" ):v_str+=" ╚██████╔╝"
                elif ( char == "r" ):v_str+=" ██╔══██╗"
                elif ( char == "s" ):v_str+="  ╚═══██╗"
                elif ( char == "t" ):v_str+="    ██║   "
                elif ( char == "u" ):v_str+=" ██║   ██║"
                elif ( char == "v" ):v_str+="  ╚████╔╝ "
                elif ( char == "w" ):v_str+="   ████╔═████║ "
                elif ( char == "x" ):v_str+="  ██╔██╗ "
                elif ( char == "y" ):v_str+="   ╚██╔╝  "
                elif ( char == "z" ):v_str+=" ██╔══╝  "

                elif ( char == "+" ):v_str+=" ╚═██╔═╝"
                elif ( char == "-" ):v_str+=" ╚════╝"
                elif ( char == "*" ):v_str+="   ████  "
                elif ( char == "/" ):v_str+="  ██╔╝  "
                elif ( char == "=" ):v_str+=" ██████╗"
                elif ( char == "." ):v_str+="    "
                elif ( char == "<" ):v_str+=" ╚██╗ "
                elif ( char == ">" ):v_str+="  ██╔╝"
                elif ( char == "%" ):v_str+="  ██╔╝  "
                elif ( char == "^" ):v_str+="           "

                elif ( char == "!" ):v_str+=" ╚═╝"
                elif ( char == "?" ):v_str+="    ╚══╝ "
                elif ( char == ":" ):v_str+="    "
                elif ( char == "" ):v_str+=" ██╗"
                elif ( char == "$" ):v_str+="  ╚═██╔██╗"
                elif ( char == "@" ):v_str+=" ██╚════╝ "
                elif ( char == "," ):v_str+=" ██╗"
                elif ( char == "&" ):v_str+=" ██╔══██   "
                elif ( char == "'" ):v_str+="    "
                elif ( char == "[" ):v_str+=" ██║  "
                elif ( char == "]" ):v_str+="   ██║"
                elif ( char == "#" ):v_str+=" ██████████╗"
                elif ( char == " " ):v_str+="   "
                
            if ( i == 4 and j == 0 ):v_str+="\n"


            if ( i == 4 ):
                if ( char == "0" ):v_str+=" ╚██████╔╝"
                elif ( char == "1" ):v_str+="  ██║"
                elif ( char == "2" ):v_str+=" ███████╗"
                elif ( char == "3" ):v_str+=" ██████╔╝"
                elif ( char == "4" ):v_str+="      ██║"
                elif ( char == "5" ):v_str+=" ███████║"
                elif ( char == "6" ):v_str+=" ╚██████╔╝"
                elif ( char == "7" ):v_str+="    ██║  "
                elif ( char == "8" ):v_str+=" ╚█████╔╝"
                elif ( char == "9" ):v_str+="  █████╔╝"

                elif ( char == "a" ):v_str+=" ██║  ██║"
                elif ( char == "b" ):v_str+=" ██████╦╝"
                elif ( char == "c" ):v_str+=" ╚█████╔╝"
                elif ( char == "d" ):v_str+=" ██████╔╝"
                elif ( char == "e" ):v_str+=" ███████╗"
                elif ( char == "f" ):v_str+=" ██║     "
                elif ( char == "g" ):v_str+=" ╚██████╔╝"
                elif ( char == "h" ):v_str+=" ██║  ██║"
                elif ( char == "i" ):v_str+=" ██║"
                elif ( char == "j" ):v_str+=" ╚█████╔╝"
                elif ( char == "k" ):v_str+=" ██║ ╚██╗"
                elif ( char == "l" ):v_str+=" ███████╗"
                elif ( char == "m" ):v_str+=" ██║ ╚═╝ ██║"
                elif ( char == "n" ):v_str+=" ██║ ╚███║"
                elif ( char == "o" ):v_str+=" ╚█████╔╝"
                elif ( char == "p" ):v_str+=" ██║     "
                elif ( char == "q" ):v_str+="  ╚═██╔═╝ "
                elif ( char == "r" ):v_str+=" ██║  ██║"
                elif ( char == "s" ):v_str+=" ██████╔╝"
                elif ( char == "t" ):v_str+="    ██║   "
                elif ( char == "u" ):v_str+=" ╚██████╔╝"
                elif ( char == "v" ):v_str+="   ╚██╔╝  "
                elif ( char == "w" ):v_str+="   ╚██╔╝ ╚██╔╝ "
                elif ( char == "x" ):v_str+=" ██╔╝╚██╗"
                elif ( char == "y" ):v_str+="    ██║   "
                elif ( char == "z" ):v_str+=" ███████╗"

                elif ( char == "+" ):v_str+="   ╚═╝  "
                elif ( char == "-" ):v_str+="       "
                elif ( char == "*" ):v_str+=" ██    ██"
                elif ( char == "/" ):v_str+=" ██╔╝   "
                elif ( char == "=" ):v_str+=" ╚═════╝"
                elif ( char == "." ):v_str+=" ██╗"
                elif ( char == "<" ):v_str+="  ╚██╗"
                elif ( char == ">" ):v_str+=" ██╔╝ "
                elif ( char == "%" ):v_str+=" ██╔╝██╗"
                elif ( char == "^" ):v_str+="           "

                elif ( char == "!" ):v_str+=" ██╗"
                elif ( char == "?" ):v_str+="    ██╗  "
                elif ( char == ":" ):v_str+=" ██╗"
                elif ( char == "" ):v_str+=" ╚█║"
                elif ( char == "$" ):v_str+=" ███████╔╝"
                elif ( char == "@" ):v_str+=" ╚████████"
                elif ( char == "," ):v_str+=" ╚█║"
                elif ( char == "&" ):v_str+=" █████████╗"
                elif ( char == "'" ):v_str+="    "
                elif ( char == "[" ):v_str+=" ████╗"
                elif ( char == "]" ):v_str+=" ████║"
                elif ( char == "#" ):v_str+=" ╚██╔═██╔══╝"
                elif ( char == " " ):v_str+="   "
                
            if ( i == 5 and j == 0 ):v_str+="\n"


            if ( i == 5 ):
                if ( char == "0" ):v_str+="  ╚═════╝ "
                elif ( char == "1" ):v_str+="  ╚═╝"
                elif ( char == "2" ):v_str+=" ╚══════╝"
                elif ( char == "3" ):v_str+=" ╚═════╝ "
                elif ( char == "4" ):v_str+="      ╚═╝"
                elif ( char == "5" ):v_str+=" ╚══════╝"
                elif ( char == "6" ):v_str+="  ╚═════╝ "
                elif ( char == "7" ):v_str+="    ╚═╝  "
                elif ( char == "8" ):v_str+="  ╚════╝ "
                elif ( char == "9" ):v_str+="  ╚════╝ "

                elif ( char == "a" ):v_str+=" ╚═╝  ╚═╝"
                elif ( char == "b" ):v_str+=" ╚═════╝ "
                elif ( char == "c" ):v_str+="  ╚════╝ "
                elif ( char == "d" ):v_str+=" ╚═════╝ "
                elif ( char == "e" ):v_str+=" ╚══════╝"
                elif ( char == "f" ):v_str+=" ╚═╝     "
                elif ( char == "g" ):v_str+="  ╚═════╝ "
                elif ( char == "h" ):v_str+=" ╚═╝  ╚═╝"
                elif ( char == "i" ):v_str+=" ╚═╝"
                elif ( char == "j" ):v_str+="  ╚════╝ "
                elif ( char == "k" ):v_str+=" ╚═╝  ╚═╝"
                elif ( char == "l" ):v_str+=" ╚══════╝"
                elif ( char == "m" ):v_str+=" ╚═╝     ╚═╝"
                elif ( char == "n" ):v_str+=" ╚═╝  ╚══╝"
                elif ( char == "o" ):v_str+="  ╚════╝ "
                elif ( char == "p" ):v_str+=" ╚═╝     "
                elif ( char == "q" ):v_str+="    ╚═╝   "
                elif ( char == "r" ):v_str+=" ╚═╝  ╚═╝"
                elif ( char == "s" ):v_str+=" ╚═════╝ "
                elif ( char == "t" ):v_str+="    ╚═╝   "
                elif ( char == "u" ):v_str+="  ╚═════╝ "
                elif ( char == "v" ):v_str+="    ╚═╝   "
                elif ( char == "w" ):v_str+="    ╚═╝   ╚═╝  "
                elif ( char == "x" ):v_str+=" ╚═╝  ╚═╝"
                elif ( char == "y" ):v_str+="    ╚═╝   "
                elif ( char == "z" ):v_str+=" ╚══════╝"

                elif ( char == "+" ):v_str+="        "
                elif ( char == "-" ):v_str+="       "
                elif ( char == "*" ):v_str+="         "
                elif ( char == "/" ):v_str+=" ╚═╝    "
                elif ( char == "=" ):v_str+="        "
                elif ( char == "." ):v_str+=" ╚═╝"
                elif ( char == "<" ):v_str+="   ╚═╝"
                elif ( char == ">" ):v_str+=" ╚═╝  "
                elif ( char == "%" ):v_str+=" ╚═╝ ╚═╝"
                elif ( char == "^" ):v_str+="           "

                elif ( char == "!" ):v_str+=" ╚═╝"
                elif ( char == "?" ):v_str+="    ╚═╝  "
                elif ( char == ":" ):v_str+=" ╚═╝"
                elif ( char == "" ):v_str+="  ╚╝"
                elif ( char == "$" ):v_str+=" ╚══════╝ "
                elif ( char == "@" ):v_str+="  ╚══════╝"
                elif ( char == "," ):v_str+="  ╚╝"
                elif ( char == "&" ):v_str+=" ╚════════╝"
                elif ( char == "'" ):v_str+="    "
                elif ( char == "[" ):v_str+=" ╚═══╝"
                elif ( char == "]" ):v_str+=" ╚═══╝"
                elif ( char == "#" ):v_str+="  ╚═╝ ╚═╝   "
                elif ( char == " " ):v_str+="   "

            j+=1
        i+=1
    return v_str
#==============================================================
        
print(banner_bash("Hi Earth"))
