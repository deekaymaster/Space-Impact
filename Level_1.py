from Level import Level
from OpponentSpaceShip import OpponentSpaceShip
import random
import game_module as gm


class Level_1(Level):
    def __init__(self, player, number_of_opponents, image):
        super().__init__(player, image)
        self.number_of_opponents = number_of_opponents
        self.create_level()

    def create_level(self):
        self._create_opponents_spaceships()

    def _create_opponents_spaceships(self):

        for i in range(self.number_of_opponents):
            opponent = OpponentSpaceShip(random.randrange(gm.WIDTH + 100 + i * 20, gm.WIDTH + 1500),
                                         random.randrange(85, gm.HEIGHT - 50), gm.OPPONENT_BLACK_SPACE_SHIP, 1, 3, 1,
                                         self.player)
            self.opponents_spaceships.append(opponent)

        opponent_boss = OpponentSpaceShip((gm.WIDTH + 1500 + gm.WIDTH), random.randrange(85, gm.HEIGHT - gm.OPPONENT_BOSS.get_height()), gm.OPPONENT_BOSS, 1, 4, 20, self.player)
        self.opponents_spaceships.append(opponent_boss)
