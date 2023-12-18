
"""
Created on Feb 28 2019
@author: J. C. Vasquez-Correa
        Pattern recognition Lab, University of Erlangen-Nuremberg
        Faculty of Engineering, University of Antioquia,
        juan.vasquez@fau.de
"""

import numpy as np
import pandas as pd

class Phonological:

    def __init__(self):

        self.list_phonological={"silence" : ["<p:>"],
                                "diphthong" : ["eI", "@U", "I@", "OI", "aI", "aU"],
                                "back" : ["u", "u:", "O:", "Q", "U", "V"],
                                "closed" : ["i:", "u", "u:", "I", "U"],
                                "rounded" : ["u", "u:", "O:", "Q", "U"],
                                "vowel" : ["3`", "i:", "6",  "@", "u", "u:",  "E", "I", "{", "O:", "Q", "U", "V"],
                                "voiceless" : ["f", "h", "k", "p", "s", "t", "tS", "S", "T"],
                                "postalveolar" : ["dZ", "tS", "S", "Z"],
                                "open" : ["3`", "E", "{", "O:", "Q", "V"],
                                "velar" : ["g", "k", "p", "t", "N", "N="],
                                "nasal" : ["m", "m=", "n", "n=", "N", "N="],
                                "alveolar" : ["4", "l", "n", "n=", "r", "s", "t", "z", "d"],
                                "bilabial" : ["m", "m=", "p", "b"],
                                "front" : ["3`", "i:",  "E", "I", "{"],
                                "glottal" : ["h", "h\\", "?"],
                                "voiced" : ["dZ", "g", "h\\", "D", "v", "z", "Z",  "b", "d"],
                                "fricative" : ["f", "h", "h\\", "s", "D", "v", "z", "S", "T", "Z"],
                                "approximant" : ["j", "l", "w"],
                                "labiodental" : ["f", "v"],
                                "dental" : ["D", "T"],
                                "plosive" : ["g", "k", "p", "t",  "b", "d"],
                                "trill" : ["r", "R"],
                                "lateral" : ["l", "l="]}

    def get_list_phonological(self):
        return self.list_phonological

    def get_list_phonological_keys(self):
        keys=self.list_phonological.keys()
        return list(keys)


    def get_d1(self):
        keys=self.get_list_phonological_keys()
        dict_1={"xmin":[],"xmax":[],"phoneme":[],"phoneme_code":[]}
        for k in keys:
            dict_1[k]=[]
        return dict_1

    def get_d2(self):
        keys=self.get_list_phonological_keys()
        dict_2={"n_frame":[],"phoneme":[],"phoneme_code":[]}
        for k in keys:
            dict_2[k]=[]
        return dict_2

    def get_list_phonemes(self):
        keys=self.get_list_phonological_keys()
        phon=[]
        for k in keys:
            phon.append(self.list_phonological[k])
        phon=np.hstack(phon)

        return np.unique(phon)


def main():
    phon=Phonological()
    keys=phon.get_list_phonological_keys()

    d1=phon.get_d1()
    d2=phon.get_d2()
    ph=phon.get_list_phonemes()

if __name__=="__main__":
    main()


