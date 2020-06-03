from pynput.keyboard import Controller, Key
import math, time, os

def main():

    mode = input("Adventure mode (1 - 30): ")
    if 1 <= int(mode) <= 30:
        booster(int(mode))

    else:
        os.system('cls')
        print("Invalid input.\n")
        main()

def booster(mode):
    boost = input("Do you have a time booster enabled (y/n)? ")

    if boost == "y":
        totaltime = float(mode/2)
        body(totaltime, mode)

    elif boost == "n":
        totaltime = float(mode)
        body(totaltime, mode)

    else:
        print("Invalid input.\n")
        booster()

def body(fulltime, mode):
    keyboard = Controller()

    period = fulltime * 3600
    halftime = fulltime * 3600 / 2

    print('\nPeriod (T) of adventure: ', period, ' second(s)')
    print('T/2 of adventure: ', halftime, 'second(s)\n')

    adventure_mode = '$adventure ' + str(mode)
    halftime_message = '[BOT] '+ str(halftime / 3600) + ' hours have passed since @wins started their adventure.'

    try:
        print('5')
        time.sleep(1)
        print('4')
        time.sleep(1)
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)

        print('The adventure has begun')

        while True:		
            keyboard.type('[BOT] This is an automatic IdleRPG message bot made by @wins.')
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)

            keyboard.type(adventure_mode)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)

            time.sleep(4)
            keyboard.type('$status')
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)

            time.sleep(4)
            keyboard.type('$xp')
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)

            time.sleep(halftime - 8)
            print(halftime_message)
            keyboard.type(halftime_message)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)

            time.sleep(halftime + 3)
            print('The adventure ended.')
            keyboard.type('$status')
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)

            time.sleep(5)

    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()

