# _**Finger Fighter**_
#### Video Demo:  <URL HERE>
#### Description: 
Finger Fighter is a simple 2-phase Rock-Paper-Scissors game that has RPG elements to it using a basic RPS ruleset to allow for easier understandability of the combat mechanics to the game.

I went through many iterations of the combat system and ultimately came to the conclusion that I didn't want to simply add, "Rock is beaten by Paper, whereas Paper is beaten by Scissors" but rather go a step further to implementing "health" in my Entities Class to add an idea that it's more of a combat situation with moves being [Rock] [Paper] [Scissors] wherein there is an ATTACK phase and a DEFENSE phase and you as the player would choose Rock Paper or Scissors in each phase to be played against the enemies choice to determine how much damage has been done (During the ATTACK phase) or how much damage was taken (During the DEFENSE phase).

I created an Entities class in entities.py to be able to better implement and attach stats to both the Player and the monsters that would be chosen from the monster_entities.csv. The idea was originally to use Level, Attack, Defense and Health but to keep the combat pure without too much math to create potential issues currently the Name and Health are currently the only used stats whereas Attack, Defense and potentially Experience (for Level) could be used later to further upgrade this game in later iterations.


```
Class Entities:

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

    # Example of Entities: 
    Entities("Phillip", level = 5, attack = 7, defense = 3, health = 10)

# 'discovered' wouldn't be used for a Player but for a monster it would be hidden and used in the 'grimoire'
```

## *Damage Matrix*

![ATTACK/DEFENSE MATRIX](/images/attack_defense_matrix.png)