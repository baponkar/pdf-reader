import keyboard
IsPressed = False

# once you press the button('f') the function happens once
# when you release the button('f') the loop resets

def here():
    print('a')

while True:
    if not keyboard.is_pressed('f'):
        IsPressed = False
    while not IsPressed:
        if keyboard.is_pressed('f'):
            here()
            IsPressed = True

# or if you want to detect every frame it loops then:

def here():
    print('a')

while True:
    if keyboard.is_pressed('f'):
        here()