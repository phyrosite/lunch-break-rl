import random

import palette

from ai import action
from entities import creature
from entities import item

class Kobold(creature.Creature):
    def __init__(self, char='K', position=(0, 0), fg=palette.BRIGHT_GREEN, bg=(0, 0, 0)):
        super().__init__(char, position, fg, bg=(0, 0, 0))
        self.name = 'kobold'
        self.brain.add_action(action.IdleAction())
        self.max_health = 4
        self.current_health = self.max_health

        if random.randint(0, 3) == 0:
            self.held_item = item.Sword()