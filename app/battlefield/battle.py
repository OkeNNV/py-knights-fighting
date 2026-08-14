from app.fighter.knight import Knight


class Battle:
    """Manages a combat simulation between multiple knights,
    handling setup and fight execution.

        Attributes:
            knights (dict[str, Knight]):
            A dictionary mapping identifiers to initialized Knight objects.
    """
    def __init__(self, knights: dict) -> None:
        """INIT"""
        self.knights = {}
        for key, config in knights.items():
            knight = Knight(**config)

            knight.wear_armour()
            if knight.potion:
                knight.use_potion()
            if knight.weapon:
                knight.draw_weapon()
            self.knights[key] = knight

    def fight(self) -> dict:
        """Executes the pre-defined combat sequence between
        specific knights and returns their remaining hit points.

            Returns:
                dict: A dictionary mapping each
                knight's name to their final hit point value.
        """
        lancelot: Knight = self.knights["lancelot"]
        red_knight: Knight = self.knights["red_knight"]
        bastard: Knight = self.knights["mordred"]
        king: Knight = self.knights["arthur"]

        king.hit_exchange(red_knight)
        lancelot.hit_exchange(bastard)

        return {
            lancelot.name: lancelot.hp,
            king.name: king.hp,
            bastard.name: bastard.hp,
            red_knight.name: red_knight.hp
        }
