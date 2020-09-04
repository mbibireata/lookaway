from .tone import *
import os 

class Sound:
    """ Actual sound is going to be comprised from a series of tones.
        This is what gets played by the alarm"""
    def __init__(self, identifier="", tone_list=[], spacings=[]):
        self.identifier = identifier
        self.tone_list = tone_list
        self.spacings = spacings

    def play(self):
        """ This function should be overloaded by inheritors? """
        # For now just play 3 beeps to keep it simple... figure out design 
        # details later
        monotone = Tone(440, 1)
        os.system('play -n synth %s sin %s' % (monotone.duration, monotone.freq))
        os.system('play -n synth %s sin %s' % (monotone.duration, monotone.freq))
        os.system('play -n synth %s sin %s' % (monotone.duration, monotone.freq))
