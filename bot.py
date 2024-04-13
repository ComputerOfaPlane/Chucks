from random import randint

print('\n\n _____ _                _        ')
print('/  __ \\ |              | |       ')
print('| /  \\/ |__  _   _  ___| | _____         __')
print('| |   | \'_ \| | | |/ __| |/  __|     ___( o)>')
print('| \__/\\ | | | |_| | (__|   <\__ \\    \ <_. )')
print(' \\____/_| |_|\\__,_|\\___|_|\\_\\___/     `---\'  \n\n')

print('Ready for Toss?\n')

player = None
tosscall = None
simple = True

while tosscall not in ['odd','even','o','e']:
    tosscall = input('Enter Odd or Even : ')
    tosscall = tosscall.lower()

def toss():
    randomnumber = randint(1,2)
    move = int(input('Enter a number : '))
    print(f'Bot chose {randomnumber}\n')
    if (randomnumber+move)%2==0 and (tosscall=='e' or tosscall=='even'):
        return True
    return False

tossResult = toss()

if tossResult:
    print('You won the toss !! Choose to Bat or Bowl\n')

    while tosscall not in ['bat','ball']:
        tosscall = input('Enter Bat or Ball : ')
        tosscall = tosscall.lower()
    
    player = tosscall

    while tosscall not in ['simple','crazy','s','c']:
        tosscall = input('Enter Simple or Crazy : ')
        tosscall = tosscall.lower()

    simple = True if tosscall=='simple' or tosscall=='s' else False
else:
    print('You lost the toss !! \n')

    botchoice = ['Bat','Ball'][randint(0,1)]
    print(f'Bot chooses to {botchoice}')
    botchoice = botchoice.lower()
    player = 'bat' if botchoice=='ball' else 'ball'

    botchoice = [True,False][randint(0,1)]
    print(f'Bot chooses {'Simple' if botchoice else 'Crazy'} Mode')
    simple = botchoice

print('\n')

print(f'MODE : {'Simple' if simple else 'Crazy'}\n')

print('Start of innings 1, All the best!\n')

balls = 0

out = False
runs = 0
move = None
print('++++++++++++ INNINGS ++++++++++++')
print(f'Player will {player}\n')

while not out:
    balls+=1
    move = 11
    while move not in range(0,11):
        move = int(input('Player = '))
    botchoice = randint(0,10)
    print(f'Bot = {botchoice}\n')
    
    diff=abs(move-botchoice)

    if not simple:
        if (botchoice==10 and move==0) or (botchoice==0 and move==10):
            out = True
            continue
        elif botchoice==0 and move==0:
            print('Crazyy...!\n')
            runs += 200
            continue
    if diff==0:
        if simple:
            out = True
            continue
        else:
            print('Crazyy...!')
            runs += (move**2) if player=='bat' else (botchoice**2)
            continue
    elif diff==1:
        if not simple:
            out = True
            continue
        else:
            runs += move if player=='bat' else botchoice
            continue
    runs += move if player=='bat' else botchoice

print('++++++++++++   END   ++++++++++++\n')

target = runs+1
print(f'{target} Runs needed in {balls} Balls\n')
player = 'bat' if player=='ball' else 'ball'

print('Start of innings 2, All the best!')
print("To check match status, type 'c' in Player Move\n")

out = False
runs = 0

print('++++++++++++ INNINGS ++++++++++++')
print(f'Player will {player}\n')

while (not out) and balls>0 and runs<=target:
    
    balls-=1

    move = 11
    while move not in range(0,11):
        move = input('Player = ')
        if move=='c':
            print(f'{target-runs} runs needed in {balls+1}')
        else:
            move=int(move)
    
    botchoice = randint(0,10)
    print(f'Bot = {botchoice}\n')
    
    diff=abs(move-botchoice)

    if not simple:
        if (botchoice==10 and move==0) or (botchoice==0 and move==10):
            out = True
            continue
        elif botchoice==0 and move==0:
            print('Crazyy...!')
            runs += 200
            continue
    if diff==0:
        if simple:
            out = True
            continue
        else:
            print('Crazyy...!')
            runs += (move**2) if player=='bat' else (botchoice**2)
            continue
    elif diff==1:
        if not simple:
            out = True
            continue
        else:
            runs += move if player=='bat' else botchoice
            continue
    runs += move if player=='bat' else botchoice

print('++++++++++++   END   ++++++++++++\n')

if target-runs==1:
    print("It's a Draw")
elif player=='bat':
    if runs>=target:
        print('Congractulations! You Win...!')
    else:
        print('Unfortunately You lost...!')
elif player=='ball':
    if runs>=target:
        print('Unfortunately You lost...!')
    else:
        print('Congractulations! You Win...!')

print('\n\n')