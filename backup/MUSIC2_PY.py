# Add your Python code here. E.g.
from microbit import *
import music
sing_song_id = 0
sing_bpm = 120

songs = [music.DADADADUM, music.ENTERTAINER, music.PRELUDE, music.ODE,
         music.NYAN, music.RINGTONE, music.FUNK, music.BLUES,
         music.BIRTHDAY, music.WEDDING, music.FUNERAL, music.PUNCHLINE,
         music.PYTHON, music.BADDY, music.CHASE, music.BA_DING,
         music.WAWAWAWAA, music.JUMP_UP, music.JUMP_DOWN, music.POWER_UP,
         music.POWER_DOWN]

while True:
    sleep(1000)
    press_a = button_a.get_presses()
    press_b = button_b.get_presses()
    if press_a:
        sing_song_id = press_a
    elif press_b == 0:
        sing_song_id = sing_song_id + 1

    sing_song_id = sing_song_id % len(songs)
    play_song = songs[sing_song_id]
    display.show(str(sing_song_id))
    sing_bpm = 120 + press_b * 10
#    music.pitch(freq, 6)
    music.set_tempo(bpm=sing_bpm)
    music.play(play_song)
