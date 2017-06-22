import player
import scene
from ui import progressbar
from ui import window

class PlayerWindow(window.Window):
    def __init__(self, x, y, width, height, title='Players'):
        super().__init__(x, y, width, height, title)

    def draw(self, console):
        super().draw(console)

        row = 1
        for entity in scene.Scene.current_scene.entities:
            if not isinstance(entity, player.Player):
                continue

            self.data.draw_str(1, row, entity.nickname, fg=entity.fg)
            row += 1

        console.blit(self.data, self.x, self.y)

    def handle_events(self, event):
        pass