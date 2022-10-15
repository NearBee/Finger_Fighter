import csv
import os
import random
import sys
from time import sleep
import textwrap

from entities import Entities


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def display_header():
    print("=" * 60)
    print()
    print(" " * 23 + "Finger Fighter" + " " * 23)
    print()
    print("=" * 60)
    print()

    instructions = "You'll be playing a 2 phase rock-paper-scissors combat simulator, You and your opponent will both choose a move for both attack and defense phase to determine the outcome of said phase."
    for line in textwrap.wrap(instructions, width=50):
        print(line.center(60))

    print()


def main():
    display_header()  # TODO: Add FIGLET Ascii art to Title as well as change title
    player = player_creation()
    monster = load_monsters()
    clear_screen()
    print("== !!! READY PLAYER !!! ==")
    game_loop(player, monster)


def player_creation() -> Entities:
    """Function for instantiating a new Entities class"""

    while True:
        try:
            player_name = input("What is your name traveler? ").strip().capitalize()
            if player_name.isalpha() == False:
                raise ValueError
        except ValueError:
            clear_screen()
            print("Enter a valid name (only letters)")
            sleep(1)
            print()
            continue
        stat_allocation = input(
            "\nAre you more [D]efensive, [A]ggressive, or [B]alanced? "
        ).lower()
        if stat_allocation == "d":
            player_attack = 3
            player_defense = 7
            return Entities(player_name, 1, player_attack, player_defense, 10)
        elif stat_allocation == "a":
            player_attack = 7
            player_defense = 3
            return Entities(player_name, 1, player_attack, player_defense, 10)
        elif stat_allocation == "b":
            player_attack = 5
            player_defense = 5
            return Entities(player_name, 1, player_attack, player_defense, 10)
        else:
            print("Please choose [a]/[b]/[d]")


# POSSIBLY could remove this since it's only a confirmation between moving from creation to game
def game_loop(player: Entities, monster: list[dict]) -> None:
    while True:
        confirmation = input("Enter [c] to continue! ").lower()
        if confirmation == "c":
            clear_screen()
            break

    town_loop(player, monster)


# Test DONE
def display_player_stats(player: Entities):
    clear_screen()
    print("=" * 5 + "  PLAYER STATS  " + "=" * 39)
    print("\n" + player.display_stats() + "\n")
    print("=" * 60 + "\n" * 2)


# Test DONE
def display_grimoire(monster: list[dict]):
    clear_screen()
    print("=" * 5 + "  GRIMOIRE  " + "=" * 43)
    print()

    for index, current_monster in enumerate(monster, start=1):
        if not current_monster["discovered"]:
            print(f"{index}.  Undiscovered Monster")
        else:
            print(
                f"{index}.  {current_monster['name']:<9} - Level: {current_monster['level']}, Attack: {current_monster['attack']}, Defense: {current_monster['defense']}, Health: {current_monster['health']}"
            )

    print()
    print("=" * 60 + "\n" * 2)


def town_loop(player: Entities, monster: list[dict]) -> None:
    while True:
        print(f"What would you like to do {player.name}?\n")
        town_menu = input(
            "[P]layer stats, [C]heck grimoire, [H]unt monsters\n\nOr would you like to [Q]uit? "
        ).lower()
        if town_menu == "p":
            display_player_stats(player)
        elif town_menu == "c":
            display_grimoire(monster)
        elif town_menu == "h":
            combat_loop(player, monster)
        elif town_menu == "q":
            clear_screen()
            sys.exit(f"\nGoodbye, thank you for playing {player.name}!\n")


def load_monsters() -> list[dict]:
    monsters = []
    print("\nLoading monsters", end="", flush=True)
    with open("monster_entities.csv") as csv_file:
        for line in csv.DictReader(csv_file):
            line["discovered"] = False
            monsters.append(line)

            print(".", end="", flush=True)
            sleep(0.5)

    return monsters


def create_enemy(monsters: list[dict]) -> Entities:
    """Creates an enemy based on Entities guidelines"""
    enemy = random.choice(monsters)
    new_enemy = Entities(**enemy)
    enemy["discovered"] = True

    return new_enemy


def combat_loop(player: Entities, monster: list[dict]) -> None:
    enemy = create_enemy(monster)

    clear_screen()
    print("Hunting", end="", flush=True)
    for _ in range(5):
        print(".", end="", flush=True)
        sleep(0.1)

    print(f"   It's a {enemy.name}!\n")
    sleep(1)

    while enemy.health > 0 and player.health > 0:
        # This would be the attack portion of combat, your first RPS choice
        print(
            f"{player.name:<9} [Level: {player.level}] - Current health: {player.health}"
        )
        print(
            f"{enemy.name:<9} [Level: {enemy.level}] - Current health: {enemy.health}"
        )
        print()

        player_attack = input(
            f"[ATTACK PHASE]\nWhat will you do {player.name}?\nChoose your move [R]ock [P]aper [S]cissors: "
        ).upper()
        clear_screen()

        enemy_choice_attack = enemy.choice()

        print(f"You chose {player.return_move(player_attack[0])}!  ", end="")
        if player_attack[0] == enemy_choice_attack["name"][0]:
            print(f"{enemy.name} chose {enemy_choice_attack['name']}!\n")
            print("You hit but not for much. 1 Damage dealt\n")
            enemy.health -= 1

        elif player_attack[0] == enemy_choice_attack["beats"][0]:
            print(f"{enemy.name} chose {enemy_choice_attack['name']}!\n")
            print("The enemy perfectly blocked the attack!\n")

        else:
            print(f"{enemy.name} chose {enemy_choice_attack['name']}!\n")
            print("You critically hit! 2 Damage dealt!\n")
            enemy.health -= 2

        if enemy.health <= 0:
            print(f"{enemy.name} killed! Hunt complete!")
            sleep(2)
            clear_screen()
            player.health = 10
            break

        # This will be the defense section of combat, basically another round of RPS
        print(
            f"{player.name:<9} [Level: {player.level}] - Current health: {player.health}"
        )
        print(
            f"{enemy.name:<9} [Level: {enemy.level}] - Current health: {enemy.health}"
        )
        print()

        enemy_choice_defense = enemy.choice()

        player_defense = input(
            f"[DEFENSE PHASE]\nWhat will you do {player.name}?\nChoose your move [R]ock [P]aper [S]cissors: "
        ).upper()
        clear_screen()

        print(f"You chose {player.return_move(player_defense[0])}!  ", end="")
        if player_defense[0] == enemy_choice_defense["name"][0]:
            player.health -= 1
            print(f"{enemy.name} chose {enemy_choice_defense['name']}!\n")
            print("You took damage but not much. 1 Damage taken!\n")

        elif player_defense[0] == enemy_choice_defense["beats"][0]:
            player.health -= 2
            print(
                f"The {enemy.name} chose {enemy_choice_defense['name']} bypassing your defenses! 2 Damage taken!\n"
            )

        else:
            print(f"{enemy.name} chose {enemy_choice_defense['name']}!")
            print("\nYou perfectly blocked the attack!\n")

        if player.health <= 0:
            clear_screen()
            sys.exit("You have died. GAME OVER")


if __name__ == "__main__":
    main()
