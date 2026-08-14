from app.gear.armour import Armour
from app.gear.potion import Potion
from app.gear.weapon import Weapon


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list | None = None,
                 weapon: dict | None = None,
                 potion: dict | None = None) -> None:
        self.name = name
        self.hp = hp
        self.base_power = power
        self.protection = 0
        self.power = power

        self.armour_pieces = [Armour(**a) for a in armour] if armour else []
        self.weapon = Weapon(**weapon) if weapon is not None else None
        self.potion = Potion(**potion) if potion is not None else None

    def wear_armour(self) -> None:
        self.protection = sum(piece.protection for piece in self.armour_pieces)

    def draw_weapon(self) -> None:
        self.power += self.weapon.power

    def use_potion(self) -> None:
        for stat, value in self.potion.effect.items():
            current = getattr(self, stat)
            setattr(self, stat, current + value)

    def hit_exchange(self, opponent: Knight) -> None:
        self.hp -= opponent.power - self.protection
        opponent.hp -= self.power - opponent.protection

        self.exceed_threshold()
        opponent.exceed_threshold()

    def exceed_threshold(self) -> None:
        if self.hp < 0:
            self.hp = 0
