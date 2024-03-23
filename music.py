from pygame import mixer
mixer.init()

mixer.music.load('dark.mp3')
mixer.music.play()

while True:
    print('Enter p to pause or u to unpause music')
    inp=input("Enter your choice.....")
    if inp=='p':
        mixer.music.pause()

    elif inp=='u':
        mixer.music.unpause()
    else:
        mixer.music.stop()
        break
