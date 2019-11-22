from Resource import *
from time import *


def start():
    print('--ODD OR EVE--')
    for i in 'Select difficulty:\n1)Easy\n2)Medium\n3)Hard':
        print(i, end='')
        sleep(0.05)
    while True:
        st = input('\n')
        if st == '1' or {i for i in st}.issubset({i for i in 'easyEASY'}):
            a = Cpu(1)
            print('-' * 100)
            print('-' * 100)
            return a

        elif st == '2' or {i for i in st}.issubset({i for i in 'mediumMEDIUM'}):
            a = Cpu(2)
            print('-' * 100)
            print('-' * 100)
            return a
        elif st == '3' or {i for i in st.lower()}.issubset({i for i in 'hardHARD'}):
            a = Cpu(3)
            print('-' * 100)
            print('-' * 100)
            return a
        print('I did\'nt get that.\nType again:')



def toss():
    print('Lets begin')
    print('How many tosses do you want the best out of?:\n')
    t = input()
    while (not t.isdigit()) or (not t > '0') or (int(t) % 2 == 0):
        print('I didn\'t get that(..BTW, number of tosses should be odd).\nType again:')
        t = input()
    t = int(t)
    user_win = []
    cpu_win = []
    for i in range(t):
        print('Choose Odd or eve:')
        inp = input()

        while True:
            if inp == '1' or {i for i in inp}.issubset({i for i in 'oddODD'}):
                user_choice = 'odd'
                break
            elif inp == '2' or {i for i in inp}.issubset({i for i in 'evenEVEN'}):
                user_choice = 'even'
                break
            else:
                print('I did\'nt get that.\nType again:')
                inp = input()
        user = input(f'Enter your Number(You want an {user_choice} number):')
        while not (('0' <= user <= '9') or user == '10'):
            print('You can\'t use that.\nType again')
            user = input()
        user_num = int(user)
        cpu = randint(0, 10)
        print(f'{f"Computer used {cpu}!!":>75}')
        if (((cpu + user_num) % 2 == 0) and (user_choice == 'even')) or (
                ((cpu + user_num) % 2 != 0) and (user_choice == 'odd')):
            print(f'It\'s {user_choice}!!')
            user_win.append('Win')
        else:
            print(f'It\'s not {user_choice}.')
            cpu_win.append('Win')
        print('-' * 100)
    if len(user_win) > len(cpu_win):
        print('You Win! UWU')
        playing = input('Batting or Bowling')
        while True:
            if playing == '1' or {i for i in playing}.issubset({i for i in 'battingBATTING'}):
                playing = 'bat'
                print('-' * 100)
                print('-' * 100)
                return playing
            elif playing == '2' or {i for i in playing}.issubset({i for i in 'bowlingBOWLING'}):
                playing = 'bowl'
                print('-' * 100)
                print('-' * 100)
                return playing
            else:
                print('I didn\'t get that.\nType again:')
                playing = input()
    else:
        print('You Lose =^=')
        cpu_choice = choice([True, False])
        if cpu_choice:
            print(f'{f"Computer chooses to Bat!!":>75}')
            print('You are Bowling')
            print('-' * 100)
            print('-' * 100)
            return 'bowl'
        else:
            print(f'{f"Computer chooses to Bowl!!":>75}')
            print('You are Batting')
            print('-' * 100)
            print('-' * 100)
            return 'bat'


def batting_first(cpu):
    print('You are Batting')
    target = 0
    while True:
        user = input('Enter your number:')
        while not (('0' <= user <= '9') or (user == '10')):
            print('You can\'t use that.\nType again')
            user = input()
        user = int(user)
        comp = cpu.bowling(user)
        print(f'{f"Computer used {comp}!!":>75}')
        if user == comp:
            print('...And it\'s a Wicket')
            print(f"Computer's Target is {target}")
            if target == 0:
                print('BOO! Duck out!')
            print('-' * 100)
            print('-' * 100)
            return target
        if user == 0:
            user = comp
        target += user
        print(f'Your score is {target}\n' + '-' * 100)


def bowling_first(cpu):
    print('You are Bowling')
    target = 0
    while True:
        user = input('Enter your number:')
        while not (('0' <= user <= '9') or (user == '10')):
            print('You can\'t use that.\nType again')
            user = input()
        user = int(user)
        comp = cpu.batting(user)
        print(f'{f"Computer used {comp}!!":>75}')
        if user == comp:
            print('...And it\'s a Wicket')
            print(f"Your Target is {target}")
            if target == 0:
                print('Yaay! Duck out!')
            print('-' * 100)
            print('-' * 100)
            return target
        if comp == 0:
            comp = user
        target += comp
        print(f'Computer\'s score is {target}\n' + '-' * 100)


def batting_second(cpu, target):
    print('You are Batting now')
    score = 0
    win_state = ''
    while True:
        user = input('Enter your number:')
        while not (('0' <= user <= '9') or (user == '10')):
            print('You can\'t use that.\nType again')
            user = input()
        user = int(user)
        comp = cpu.bowling(user)
        print(f'{f"Computer used {comp}!!":>75}')
        if user == comp:
            print('...And it\'s a Wicket')
            if score == 0:
                print('BOO! Duck out!')
            if score == target:
                print('It\'s a TIE!')
                win_state = 'TIE'
            else:
                print('You LOSE!')
                win_state = 'LOSE'
            print('-' * 100)
            print('-' * 100)
            return win_state
        if user == 0:
            user = comp
        score += user
        if score > target:
            print('You WIN!')
            print('-' * 100)
            print('-' * 100)
            win_state = 'WIN'
            return win_state
        print(f'Your score is {score}\n' + '-' * 100)


def bowling_second(cpu, target):
    print('You are Bowling now')
    score = 0
    win_state = ''
    while True:
        user = input('Enter your number:')
        while not (('0' <= user <= '9') or (user == '10')):
            print('You can\'t use that.\nType again')
            user = input()
        user = int(user)
        comp = cpu.batting(user)
        print(f'{f"Computer used {comp}!!":>75}')
        if user == comp:
            print('...And it\'s a Wicket')
            if score == 0:
                print('Yaay! Duck out!')
            if score == target:
                print('It\'s a TIE!')
                win_state = 'TIE'
            else:
                print('You WIN!')
                win_state = 'LOSE'
            print('-' * 100)
            print('-' * 100)
            return win_state
        if comp == 0:
            comp = user
        score += comp
        if score > target:
            print('You LOSE!')
            print('-' * 100)
            print('-' * 100)
            win_state = 'LOSE'
            return win_state
        print(f'Computer\'s score is {score}\n' + '-' * 100)


x = start()
bowling_second(x, 50)
