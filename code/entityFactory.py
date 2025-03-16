#!/usr/bin/python
# -*- coding: utf-8 -*-

from Player import Player
from Enemy import Enemy
from Backgroud import Backgroud


class EntityFactory(Player, Enemy, Backgroud):
    def __init__(self):
        self.get_entity(entity_type:str): Entity = None
