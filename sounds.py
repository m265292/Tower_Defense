import pygame


def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load('assets/sounds/song.mid')
    pygame.mixer.music.set_volume(.5)
    pygame.mixer.music.play(loops=1, start=0)
def arrow_sound():
    pygame.mixer.init()
    pygame.mixer.music.load('assets/sounds/arrow_impact.wav')
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(loops=1, start=0)

def stop_music():
    pygame.mixer.music.stop()