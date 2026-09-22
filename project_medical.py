import arcade

class GameView(arcade.View):
    def __init__(self):
        super().__init__()

        self.background_color = arcade.color.RED

    def reset(self):
        pass

    def on_draw(self):
        self.clear()
    
    def on_update(self, delta_time):
        pass

    def on_key_press(self, key, key_modifiers):
        pass

    def on_key_release(self, key, key_modifiers):
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        pass


def main():
    window = arcade.Window(1080,720,"skibidiskibidi")
    gameView = GameView()

    window.show_view(gameView)

    arcade.run()


if __name__ == "__main__":
    main()