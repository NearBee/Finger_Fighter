import random
from unittest.mock import patch

import pytest

from entities import Entities
from project import (
    create_enemy,
    display_grimoire,
    display_player_stats,
    player_creation,
)


def test_player_creation(capsys, monkeypatch):
    # monkeypatch.setattr("project.player_creation", lambda: "John")
    # player_creation()
    pass


def test_display_player_stats(capfd):
    test_player = Entities("John", 1, 5, 5, 10, False)
    expected_output = (
        "=====  PLAYER STATS  =======================================\n"
        "\n"
        "John [Level 1]\n"
        "Attack: 5, Defense: 5, Health: 10\n"
        "\n"
        "============================================================\n"
        "\n"
        "\n"
    )

    # with patch("from_file.function", returns=None) as whatever:
    # could use returns or sideeffects for mocking inputs
    with patch("project.clear_screen") as patch_mock:
        display_player_stats(test_player)
        out, err = capfd.readouterr()

        assert expected_output == out


def test_load_monsters():
    pass


def test_create_enemy():
    test_dict = [
        {
            "name": "John",
            "level": 1,
            "attack": 5,
            "defense": 5,
            "health": 10,
            "discovered": False,
        }
    ]

    enemy = create_enemy(test_dict)

    assert enemy.name == test_dict[0]["name"]


def test_town_loop():
    pass


def test_display_grimoire(capfd):
    test_dict = [
        {
            "name": "forest diety",
            "level": 1,
            "attack": 1,
            "defense": 1,
            "health": 1,
            "discovered": True,
        }
    ]
    test_dict2 = [
        {
            "name": "forest diety",
            "level": 1,
            "attack": 1,
            "defense": 1,
            "health": 1,
            "discovered": False,
        }
    ]
    expected_output = (
        "=====  GRIMOIRE  ===========================================\n"
        "\n"
        "1.  forest diety - Level: 1, Attack: 1, Defense: 1, Health: 1\n"
        "\n"
        "============================================================\n"
        "\n"
        "\n"
    )
    expected_output2 = (
        "=====  GRIMOIRE  ===========================================\n"
        "\n"
        "1.  Undiscovered Monster\n"
        "\n"
        "============================================================\n"
        "\n"
        "\n"
    )

    with patch("project.clear_screen") as mocked_out:
        display_grimoire(test_dict)
        out, err = capfd.readouterr()

        assert expected_output == out

    with patch("project.clear_screen") as mocked_out:
        display_grimoire(test_dict2)
        out, err = capfd.readouterr()

        assert expected_output2 == out


def test_combat_loop():
    pass
