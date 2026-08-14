from app.battlefield.battle import Battle


def battle(knights_config: dict) -> dict:
    battle_instance = Battle(knights_config)
    return battle_instance.fight()
