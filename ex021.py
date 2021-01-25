from pygame import mixer

print('BEM VINDO AO MANTRA MAHAMRITYUNJAYA!')
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
while mixer.music.get_busy(): pass
