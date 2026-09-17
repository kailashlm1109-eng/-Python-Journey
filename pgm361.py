# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 10:49:37 2026
states and cities by getting input
@author: KAILASH L M
"""
tn=[input("Enter cities in Tamil Nadu:") for i in range(3)]
kl=[input("Enter cities in Kerala:") for j in range(3)]
ap=[input("Enter cities in Andhra:") for k in range(3)]
d={'Tamilnadu':tn,'Kerala':kl,'AndhraPradesh':ap}
print(d)