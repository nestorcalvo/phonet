# -*- coding: utf-8 -*-
"""
Created on Feb 28 2019
@author: J. C. Vasquez-Correa
        Pattern recognition Lab, University of Erlangen-Nuremberg
        Faculty of Engineering, University of Antioquia,
        juan.vasquez@fau.de
"""
import sys
# sys.path
# sys.path.append('.')
# print(sys.path)
from phonet import Phonet
import os

class Graph:
        
	def __init__(self, path_audio_file, path_store_features, path_store_plots):
		self.path_audio_file = path_audio_file
		self.path_store_features = path_store_features
		self.path_store_plots = path_store_plots
	def plot_store_graph(self):
		#PATH=os.path.dirname(os.path.abspath(__file__))
		phon=Phonet(["vowel", "voiceless", "fricative", "plosive"])
		phon.get_phon_wav(self.path_audio_file, 
                    self.path_store_features, 
                    self.path_store_plots, 
                    True)
		return True




