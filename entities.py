import random


class Entities:
    # Possibly could be moved to a better location
    choices = {
        "R": {"name": "Rock", "beats": "Scissors"},
        "S": {"name": "Scissors", "beats": "Paper"},
        "P": {"name": "Paper", "beats": "Rock"},
    }

    def __init__(
        self,
        name: str = "John",
        level: int = 1,
        attack: int = 5,
        defense: int = 5,
        health: int = 10,
        discovered: bool = False,
    ) -> None:
        self.name = name
        self.level = int(level)
        self.attack = int(attack)
        self.defense = int(defense)
        self.health = int(health)
        self.discovered = True if discovered == True else False

    def choice(self) -> dict:
        return random.choice(list(self.choices.values()))

    def return_move(self, move: str) -> str:
        return self.choices[move.upper()]["name"]

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "level": self.level,
            "attack": self.attack,
            "defense": self.defense,
            "health": self.health,
        }

    def display_stats(self):
        return f"{self.name} [Level {self.level}]\nAttack: {self.attack}, Defense: {self.defense}, Health: {self.health}"

    # def attack_with_opponent(self, opponent):
    #     player_choice = input(
    #         f"[ATTACK PHASE]\nWhat will you do {self.name}?\nChoose your move [R]ock [P]aper [S]cissors: "
    #     ).upper()

    #     print(f"You chose {self.return_move(player_choice[0])}!  ", end="")
    #     if player_choice[0] == opponent.choice["name"][0]:
    #         opponent_choice = print(f"{opponent.name} chose {opponent['name']}!\n")
    #         damage_dealt_msg = print("You hit but not for much. 1 Damage dealt\n")
    #         damage_dealt = opponent.health -= 1

    #     elif player_choice[0] == opponent.choice["beats"][0]:
    #         print(f"{opponent.name} chose {opponent.choice['name']}!\n")
    #         print("The enemy perfectly blocked the attack!\n")

    #     else:
    #         print(f"{opponent.name} chose {opponent.choice['name']}!\n")
    #         print("You critically hit! 2 Damage dealt!\n")
    #         opponent.health -= 2
    #         return

    def __str__(self):
        return self.name


if __name__ == "__main__":
    player = Entities
