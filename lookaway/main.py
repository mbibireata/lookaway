import os
from audio.sound_player import SoundPlayer

if __name__ == "__main__":
    player = SoundPlayer(sound=None, reminder_freq=5)
    player.run(never_stop=True)
