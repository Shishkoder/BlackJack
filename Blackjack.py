from random import shuffle


class Card:
    """
    Описание типов карт с последующим их созданием.

    :values_tuple: Кортеж достоинства
    :suits_tuple: Кортеж мастей

    """
    __values_tuple = (
        2, 3, 4, 5, 6, 7, 8, 9, 10,
        'Валет', 'Дама', 'Король', 'Туз'
    )

    __suits_tuple = (
        'Черви', 'Пики', 'Крести', 'Буби'
    )

    @classmethod
    @property
    def values_tuple(cls):
        return cls.__values_tuple

    @classmethod
    @property
    def suits_tuple(cls):
        return cls.__suits_tuple

    def __init__(self, value, suit):
        """
        Создание карты в виде словаря {достоинство: масть}.

        : value : Достинство
        : suit : Масть
        : card_dict : Карта
        """
        self.__value = value
        self.__suit = suit
        self.__card_dict = {self.__value: self.__suit}

    @property
    def value(self):
        return self.__value

    @property
    def suit(self):
        return self.__suit

    def __str__(self):
        """ Вывод карты при обращении к экземпляру класса """
        return f"{self.__card_dict}"


class Deck:
    """
    Описание колоды карт из экземпляров Card.

    : deck_cards_list : Список с колодой карт
    : count_decks : Количество колод
    """
    __deck_cards_list = []
    __count_decks = int(input("Количество колод: "))

    # Добавление карты в колоду через циклы
    for value in Card.values_tuple:
        for suit in Card.suits_tuple:
            __deck_cards_list.append(Card(value, suit))

    __deck_cards_list *= __count_decks

    # Имитация перемешивания колоды
    shuffle(__deck_cards_list)
    # print(__deck_cards_list[-1]) # Проверка на смешивание колоды(верхняя карта)

    @classmethod
    @property
    def deck_cards_list(cls):
        return cls.__deck_cards_list


class Person:
    """
    Описание человека за столом.
    """
    def __init__(self, name='Крупье'):
        """
        Создание экземпляра человека.

        : name : Имя человека
        : score : Его счёт
        : cards_list : Список с картами на руках
        """
        self._name = name
        self._score = 0
        self._cards_list = []

    def add_point(self, n=1):
        """
        Подсчёт очков карт.

        : n : Количество новых карт
        """
        for i in range(n):
            # Перехватываем исключение, если значение нельзя типизировать.
            try:
                self._score += self._cards_list[i].value
            except TypeError:
                # Проверка на Туз, так как он может быть 1 и 11.
                """
                result = 0
        # Количество тузов на руке.
        aces = 0
        for card in self.cards:
        result += card.card_value()
        # Если на руке есть туз - увеличиваем количество тузов
        if card.get_rank() == "A":
                aces += 1
        # Решаем считать тузы за 1 очко или за 11
        if result + aces * 10 <= 21:
        result += aces * 10
        return result
        """
                if self._cards_list[i].value == 'Туз':
                    if self._score + 11 > 21:
                        self._score += 1
                    else:
                        self._score += 11
                else:
                    self._score += 10

    def giveCard(self, deck, count=1):
        """
        Выдать карту.

        : deck : Класс колоды, в которой хранится сама колода карт
        : count : Количество карт, которые нужно выдать
        """
        for i in range(count):
            self._cards_list.append(deck.deck_cards_list.pop())

    @property
    def name(self):
        return self._name

    @property
    def score(self):
        return self._score

    @property
    def cards_list(self):
        return self._cards_list


class Player(Person):

    def passCard(self):
        pass

    def doubleCard(self):
        pass

    def splitCard(self):
        pass


class Dealer(Person):
    pass


class Game:
    Deck()
    players_list = []
    count_players = int(input("Введите количество игроков: "))

    for i in range(count_players):
        name = input(f"Введите имя {i+1}-го игрока: ")
        players_list.append(Player(name))
        players_list[i].giveCard(Deck, 2)
        players_list[i].add_point(2)

        print(f"Карты игрока {players_list[i].name}")
        # Проверка карт на руках
        print(players_list[i].cards_list[0], players_list[i].cards_list[1])
        print(f"Очки: {players_list[i].score}")  # Проверка подсчёта очков

    dealer = Dealer()
    dealer.giveCard(Deck, 2)
    dealer.add_point(2)

    print(f"Карты {dealer.name.lower()}")
    print(dealer.cards_list[0], dealer.cards_list[1])  # Проверка карт на руках
    print(f"Очки: {dealer.score}")  # Проверка подсчёта очков
    # Проверка на уменьшении карт в колоде
    print(f"Осталось карт: {len(Deck.deck_cards_list)}")


Game()
