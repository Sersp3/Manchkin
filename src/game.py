import random
from src.datacards import card_database

def load_deck(deck_type):
    if deck_type == "doors":
        """Перебирает список дверей, создает объекты Monster (или Curse), возвращает список объектов"""
    if deck_type == "treasures":
        """Перебирает список сокровищ, создает объекты Gear, возвращает список"""

class Game:
    _instance = None # Реализуем синглетонннн

    def __init__(self, count_of_players : int) -> None:
        self.count_of_players 


    def __new__(cls):
        if (cls._instance == None):
            cls._instance = super().__new__(cls)
        return cls._instance 
    
    __doors_deck = []
    __treasure_deck = []

    def shuffle_decks(self) -> None:
        random.shuffle

    def start():
        print("Добро пожаловать в игру Манчкин v0.0.0...")
        print("Введите количество игроков:")