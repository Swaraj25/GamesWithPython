from IPython.display import clear_output
flag = False
green= ['E', 'E', 'E']
brown = ['3', '3', '3']
def is_green(frogs):
    if frogs == green:
        return True
    else:
        return False

def is_brown(frogs):
    if frogs == brown:
        return True
    else:
        return False

def display(frogs):
    for i in list(range(7)):
        print(' ',i,' ' ,end='')
    print()
    print(frogs)



def jump(frogs,frm_here,to_here):
    global green,brown
    
    if frogs[frm_here] in green:
        if frm_here < to_here and not (frogs[to_here] in brown or frogs[to_here] in green):
            frogs[to_here] = frogs[frm_here]
            frogs[frm_here] = '_'
            return True
        else:
            return False
    elif frogs[frm_here] in brown:
        if frm_here > to_here and not (frogs[to_here] in brown or frogs[to_here] in green):
            frogs[to_here] = frogs[frm_here]
            frogs[frm_here] = '_'
            return True
        else:
            return False
            
    

    
def play(frogs):
    global flag
    display(frogs)
    while not((is_brown(frogs[:3])) and (is_green(frogs[4:]))):
        print("Which frog should jump? : ",end='')
        frm = input()
        if frm == 'q' or frm == 'Q':
            break
        else:
            frm = int(frm)
        here = frogs.index('_')
        
        if  not ((0 <= frm <=6) and (0 <= here <=6) and (1<= abs(frm - here) <=2)):
            print("Invalid Positions!!!!")
            continue
        
        can_jump = jump(frogs,frm,here)
        
        if not can_jump:
            print('Invalid move!!!')
            continue
        clear_output()
        display(frogs)
        if (is_brown(frogs[:3])) and (is_green(frogs[4:])):
            flag = True
    if flag:
        print("Congratulations!!! You Won")
    else:
        print("Game Over!!!")

un = ['_']
frogs = green[0:] + un + brown[0:]
play(frogs)
