from .sound import Sound
import os
import time

class SoundPlayer:
    def __init__(self, sound=None, reminder_freq=20):
        self.reminder_freq = reminder_freq
        if sound is None:
            self.sound = Sound()
        else:
            self.sound = sound

    def run(self, run_time=20, num_repeats=3, never_stop=False):
        if never_stop:
            while True:
                self.sound.play()
                time.sleep(self.reminder_freq)
