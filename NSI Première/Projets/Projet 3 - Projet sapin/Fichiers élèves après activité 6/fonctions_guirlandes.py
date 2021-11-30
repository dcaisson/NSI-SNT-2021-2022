#!/usr/bin/python
# -*- coding: UTF-8

from gpiozero import OutputDevice
from time import sleep
from random import randint

guirlande_1 = OutputDevice(26, active_high=False, initial_value=True)
guirlande_2 = OutputDevice(19, active_high=False, initial_value=True)
guirlande_3 = OutputDevice(13, active_high=False, initial_value=True)
guirlande_4 = OutputDevice(6, active_high=False, initial_value=True)
guirlande_5 = OutputDevice(5, active_high=False, initial_value=True)

liste = [guirlande_1, guirlande_2, guirlande_3, guirlande_4, guirlande_5]

def allume_ascendant():
    """Allume les guirlandes une par une, du bas vers le haut, 4 fois"""
    for guirlande in liste:
        guirlande.off()
    for i in range(4):
        for i in range(5):
            liste[i].on()
            sleep(0.2)
            liste[i].off()


def allume_descendant():
    """Allume les guirlandes une par une, du haut vers le bas, 4 fois"""
    for guirlande in liste:
        guirlande.off()
    for i in range(4):
        for i in range(4,-1,-1):
            liste[i].on()
            sleep(0.2)
            liste[i].off()


def allume_alterne():
    """Allume alternativement les guirlandes de numéro impair et les
    guirlandes de numéro pair, 4 fois
    """
    for guirlande in liste:
        guirlande.off()
    for i in range(4):
        guirlande_1.on()
        guirlande_3.on()
        guirlande_5.on()
        guirlande_2.off()
        guirlande_4.off()
        sleep(0.2)
        guirlande_1.off()
        guirlande_3.off()
        guirlande_5.off()
        guirlande_2.on()
        guirlande_4.on()
        sleep(0.2)
    guirlande_2.off()
    guirlande_4.off()


def allume_aleatoirement():
    """Allume 2 guirlandes au hasard, les éteint, puis recommence 19 fois,
    avec des guirlandes différentes à chaque fois
    """
    for guirlande in liste:
        guirlande.off()
    for i in range(19):
        indice_1 = randint(0,4)
        j = randint(0,4)
        while j == indice_1:
            j = randint(0,4)
        indice_2 = j
        liste[indice_1].on()
        liste[indice_2].on()
        sleep(0.2)
        liste[indice_1].off()
        liste[indice_2].off()
