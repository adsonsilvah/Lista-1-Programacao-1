import pyxel

class Linha:

    def __init__(self):
        pyxel.init(100, 100)
        pyxel.run(self.update, self.draw)

    def update(self):
       if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.line(0,0, pyxel.mouse_x, pyxel.mouse_y, 7)
        pyxel.line(99,0, pyxel.mouse_x, pyxel.mouse_y, 7)
        pyxel.line(0,99, pyxel.mouse_x, pyxel.mouse_y, 7)
        pyxel.line(99,99, pyxel.mouse_x, pyxel.mouse_y, 7)
Linha()