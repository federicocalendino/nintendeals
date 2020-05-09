from nintendeals.classes.games import Game
from typing import Optional


class N3DSGame(Game):

    platform = "Nintendo 3DS"

    def __init__(
        self,
        title: str,
        region: str,
        nsuid: str = None,
        product_code: str = None,
    ):
        super().__init__(
            title=title,
            region=region,
            nsuid=nsuid,
            product_code=product_code
        )

        self.download_play: bool = None
        self.internet: bool = None
        self.motion_control: bool = None
        self.spot_pass: bool = None
        self.street_pass: bool = None
        self.virtual_console: bool = None

    @property
    def unique_id(self) -> Optional[str]:
        if not self.product_code:
            return None

        return self.product_code[-4:-1]