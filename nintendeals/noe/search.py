from typing import Iterator

from nintendeals.commons.classes.games import Game
from nintendeals.commons.enumerates import Platforms
from nintendeals.noe.api import nintendo
from nintendeals.noe.util import build_game


def search_games(query: str, platform: Platforms) -> Iterator[Game]:
    for data in nintendo.search_by_query(query, platform):
        yield build_game(data)


def search_3ds_games(query: str) -> Iterator[Game]:
    """
    Search for Nintendo 3DS games in the EU region.

    Available Features
    ------------------
        * AMIIBO

    Parameters
    ----------
    query: str
        Text to search.

    Yields
    -------
    nintendeals.classes.common.Game:
        Information of a game.
    """
    yield from search_games(query, Platforms.NINTENDO_3DS)


def search_switch_games(query: str) -> Iterator[Game]:
    """
    Search for Nintendo Switch games in the EU region.

    Available Features
    ------------------
        * AMIIBO
        * DEMO
        * DLC
        * NSO_REQUIRED
        * SAVE_DATA_CLOUD
        * VOICE_CHAT

    Parameters
    ----------
    query: str
        Text to search.

    Yields
    -------
    nintendeals.classes.common.Game:
        Information of a game.
    """
    yield from search_games(query, Platforms.NINTENDO_SWITCH)


def search_wiiu_games(query: str) -> Iterator[Game]:
    """
    Search for Nintendo WiiU games in the EU region.

    Available Features
    ------------------
        * AMIIBO
        * DEMO
        * DLC

    Parameters
    ----------
    query: str
        Text to search.

    Yields
    -------
    nintendeals.classes.common.Game:
        Information of a game.
    """
    yield from search_games(query, Platforms.NINTENDO_WIIU)
