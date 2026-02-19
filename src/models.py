class Card:
    """Логика карт"""

    def __init__(self, name : str, price : int) -> None:
        self._name = name
        self._price = price

    def __str__(self):
        return (f"Название карты: {self._name}" '\n'
                f"Цена карты: {self._price}"    '\n')

class Monster(Card):
    """Логика монстра"""

    def __init__(self, name: str, price: int, level : int, treasures : int, undead : bool) -> None:
        super().__init__(name, 0) #У монстров нет цены в манчкине
        self._level = level
        self._treasures = treasures
        self._undead = undead

    def __str__(self) -> str:
        return (f"Имя монстра: {self._name}"              '\n'
                f"Уровень монстра: {self._level}"         '\n'
                f"Количество сокровищ: {self._treasures}" '\n'
                f"Состояние жизни: {self._undead}"        '\n') 

class Gear(Card):
    """Логика гиров"""

    def __init__(self, name: str, price: int, bonus: int, slot : str, is_big : bool) -> None: 
        super().__init__(name, price)
        self._bonus = bonus
        self._slot = slot # Слот куда надевать шмотку
        self._is_big = is_big

    def __str__(self) -> str:
        return (f"{super().__str__()}"     '\n'
                f"Бонус: {self._bonus}"    '\n'
                f"Слот: {self._slot}"      '\n'
                f"Большой: {self._is_big}" '\n') 

class Player:
    """Логика игрока"""

    def __init__(self, name : str) -> None:
        self._name = name
        self._level = 1
        self._hand = []
        self._gear = []

    def __str__(self) -> str:
        return (f"Игрок: {self._name} (Уровень: {self._level}, Сила: {self.combat_power})\n"
                f"Шмотки: {[str(g) for g in self._gear]}")
    @property
    def gear_power(self) -> int:
        """Подсчет силы всех гиров"""
        return sum(item._bonus for item in self._gear)

    @property 
    def combat_power(self) -> int:
        """Подсчет общей мощности"""
        return self._level + self.gear_power
    
    def equip(self, card_index : int) -> None:
        """Переместить карту из hand в gear"""
        if 0 <= card_index < len(self._hand):
            card = self._hand(card_index)
            if isinstance(card, Gear):
                card = self._hand.pop(card_index)
                self._gear.append(card)
            else:
                print("Эта карта не является Gear")    

    def unequip(self, card_index : int) -> None:
        """Переместить карту из gear в hand"""
        if 0 <= card_index < len(self._gear):
            card = self._gear.pop(card_index)    
            self._hand.append(card)