from loguru import logger

hero = {
    "name": "ckp",
    "health": 1000,
    "gold": 100,
    "defense": 10,
    "attack": 90,
    "level": 1,
    "weapon_list": [],
    "type" : "hero"
}

enemy = {
    "name": "zj",
    "health": 500,
    "defense": 5,
    "attack": 50,
    "gold": 100,
    "level": 1,
    "weapon_list": [],
    "type" : "enemy"
}


def attack(attacker, defenser):
    damage = attacker["attack"] - defenser["defense"]
    if damage > 0:
        defenser["health"] -= damage
        logger.info(f"{attacker['name']}攻击了{defenser['name']}，造成了{damage}点伤害。")
    else:
        logger.info(f"{attacker['name']}的攻击被{defenser['name']}防御了")


def buy_weapon(player, weapon):
    player["weapon_list"].append(weapon)
    logger.info(f"{player['name']}购买装备{weapon}")


def level_up(player):
    player["level"] += 1
    player["gold"] += 100
    logger.info(f"{player['name']}升级了，奖励金币100")


# buy_weapon(hero, "屠龙刀")
# attack(hero, enemy)
# attack(hero, enemy)
# attack(enemy, hero)
# level_up(hero)
