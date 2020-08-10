#!/usr/bin/env python

from pynput.keyboard import Controller, Key
import math, time, os

class IdleBot:
    
    def __init__(self):
        
        print('Initialising script...')

    def booster(self, mode):
        
        boost = input("Do you have a time booster enabled (y/n)? ")

        if boost == "y":
            totaltime = float(mode/2)
            self.body(totaltime, mode)

        elif boost == "n":
            totaltime = float(mode)
            self.body(totaltime, mode)

        else:
            print("Invalid input.\n")
            self.booster()

    def body(self, fulltime, mode):
        
        keyboard = Controller()

        period = fulltime * 3600
        halftime = fulltime * 3600 / 2

        print('\nPeriod (T) of adventure: ', period, ' second(s)')
        print('T/2 of adventure: ', halftime, 'second(s)\n')

        adventure_mode = '$adventure ' + str(mode)
        halftime_message = '[BOT] '+ str(halftime / 3600) + ' hours have passed since @wins started their adventure.'

        try:
            print('Please click on your Discord chat within the next 5 seconds.')
            time.sleep(1)
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
    
def main():

    bot = IdleBot()
    
    mode = input("Adventure mode (1 - 30): ")
    if 1 <= int(mode) <= 30:
        bot.booster(int(mode))

    else:
        os.system('cls')
        print("Invalid input.\n")
        main()

if __name__ == '__main__':
    main()

