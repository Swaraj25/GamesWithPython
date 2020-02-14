from IPython.display import clear_output

flag = True

def display(boat_side, m_on_right, c_on_right, m_on_left, c_on_left):
    if boat_side == 'right':
        print("{} {} |{}{}| {} {}".format('\U0001f482'*m_on_left, '\U0001f479'*c_on_left,'\U0001f30a'*4,'\U0001f6A2','\U0001f482'*m_on_right, '\U0001f479'*c_on_right))
    else:
        print("{} {} |{}{}| {} {}".format('\U0001f482'*m_on_left, '\U0001f479'*c_on_left,'\U0001f6A2','\U0001f30a'*4 ,'\U0001f482'*m_on_right, '\U0001f479'*c_on_right))


def play(boat_side, m_on_right, c_on_right, m_on_left, c_on_left):
    global flag
    right = {'missionaries':m_on_right,'cannibals':c_on_right}
    left = {'missionaries':m_on_left,'cannibals':c_on_left}
    boat = {'missionaries':0,'cannibals':0,'side':boat_side}
    while left['missionaries'] != 3 or left['cannibals'] !=3:
        boat ['missionaries']=0
        boat['cannibals']=0
        
        display(boat['side'], right['missionaries'], right['cannibals'], left['missionaries'], left['cannibals'])
        print("Missionaries to add on the boat : ",end='')
        boat['missionaries'] = int(input())

        print("Cannibals to add on the boat : ",end='')
        boat['cannibals'] = int(input())
        
        if not(0 < boat['missionaries'] + boat['cannibals'] <= 2):
            clear_output()
            print("Invalid move!!!! Capacity of boat is 2")
            continue
            
        
        if boat['side'] == 'right':
            if (boat['missionaries'] > right['missionaries'] or boat['cannibals'] > right['cannibals']):
                clear_output()
                print("Invalid Move!!! Missionaries on right side are: {} and Canibals on right side are: {}".format(right['missionaries'], right['cannibals']))
                continue
            
            else:
                right['missionaries'] -= boat['missionaries']
                right['cannibals'] -= boat['cannibals']
                left['missionaries'] += boat['missionaries']
                left['cannibals'] += boat['cannibals']
                boat['side'] = 'left'
                
        
        else:
            if (boat['missionaries'] > left['missionaries'] or boat['cannibals'] > left['cannibals']) :
                clear_output()
                print("Invalid Move!!! Missionaries on left side are: {} and Canibals on left side are: {}".format(left['missionaries'], left['cannibals']))
                continue
            else:
                left['missionaries'] -= boat['missionaries']
                left['cannibals'] -= boat['cannibals']
                right['missionaries'] += boat['missionaries']
                right['cannibals'] += boat['cannibals']
                boat['side'] = 'right'
                
        if ((left['cannibals'] > left['missionaries']) and (left['cannibals']!=0 and left['missionaries'] !=0)) or ((right['cannibals'] >right['missionaries']) and (right['cannibals']!=0 and right['missionaries'] !=0)):
            clear_output()
            display(boat['side'], right['missionaries'], right['cannibals'], left['missionaries'], left['cannibals'])
            print("Canibals ate Missionaries!!!!")
            flag = False
            break  
        clear_output()    
        
    
    
    if flag == True:
        display('side', right['missionaries'], right['cannibals'], left['missionaries'], left['cannibals'])
        print("Congratulations!!! You Won")
    else:
        print("Game Over")
        print("You Lose")
         

play('right',3,3,0,0)
        
