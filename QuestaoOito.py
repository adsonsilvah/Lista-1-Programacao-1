import pyxel

class Quadrado:
    def __init__(self):
        pyxel.init(100, 100)
        self.y = 40
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        self.y = (self.y + 1) % pyxel.width

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(40, self.y, 20, 20, 7)

Quadrado()