class Deck:
    def __init__(self, row: int, column: int, is_alive: bool = True) -> None:
        self.row = row
        self.column = column
        self.is_alive = is_alive

    def __repr__(self) -> str:
        return f"Deck({self.row}, {self.column}," \
               f" {'Alive' if self.is_alive else 'Dead'})"


class Ship:
    def __init__(self, start: tuple, end: tuple) -> None:
        self.start = start
        self.end = end
        self.decks = []

        if start[0] == end[0]:  # Горизонтальный корабль
            for col in range(start[1], end[1] + 1):
                self.decks.append(Deck(start[0], col))
        else:  # Вертикальный корабль
            for row in range(start[0], end[0] + 1):
                self.decks.append(Deck(row, start[1]))

    def get_deck(self, row: int, column: int) -> Deck:
        for deck in self.decks:
            if deck.row == row and deck.column == column:
                return deck
        return None

    def fire(self, row: int, column: int) -> str:
        deck = self.get_deck(row, column)
        if deck:
            deck.is_alive = False
            if all(not d.is_alive for d in self.decks):
                return "Sunk!"
            return "Hit!"
        return "Miss!"

    def __repr__(self) -> str:
        return f"Ship({self.decks})"


class Battleship:
    def __init__(self, ships: tuple[tuple]) -> None:
        self.ships = []
        self.field = {}

        for start, end in ships:
            ship = Ship(start, end)
            self.ships.append(ship)
            for deck in ship.decks:
                self.field[(deck.row, deck.column)] = ship

    def fire(self, location: tuple) -> str:
        if location in self.field:
            ship = self.field[location]
            return ship.fire(*location)
        return "Miss!"
