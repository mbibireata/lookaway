"""Interface for tone class"""

class Tone:
    def __init__(self, freq=440, duration=1):
        self.freq = freq
        self.duration = duration

    def set_freq(self, freq):
        self.freq = freq

    def set_duration(self, duration):
        self.duration = duration

    def get_freq(self):
        return self.freq

    def get_duration(self):
        return self.duration
