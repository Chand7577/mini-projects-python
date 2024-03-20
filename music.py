from pygame import mixer
mixer.init()

mixer.music.load('dark.mp3')
mixer.music.play()

while True:
    inp=input("Enter your choice..l...")
    if inp=='p':
        mixer.music.pause()

    elif inp=='u':
        mixer.music.unpause()
    else:
        mixer.music.stop()
        break