from pynput.keyboard import Controller, Key
import time, math

keyboard = Controller()

mode = input("Adventure mode (1 - 30): ")
t = input("Period of adventure (in hours): ")

fulltime = float(t) * 3600
halftime = float(t) * 3600 / 2

print('\nPeriod (T) of adventure: ', fulltime, ' second(s)')
print('T/2 of adventure: ', halftime, 'second(s)\n')

adventure_mode = '$adventure ' + mode
halftime_message = '[BOT] '+ str(float(t)/2) + ' hours have passed since @wins started their adventure.'

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
        keyboard.type(halftime_message)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(halftime + 3)
        keyboard.type('$status')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(5)

except KeyboardInterrupt:
    pass