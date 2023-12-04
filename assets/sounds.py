import pygame


def play_music(volume=1):
    pygame.mixer.init()
    pygame.mixer.music.load('assets/sounds/song.mid')
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(loops=1.0, start=0.0)


def stop_music():
    pygame.mixer.music.stop()
