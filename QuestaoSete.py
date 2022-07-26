import pyxel

class Quadrado:

    def __init__(self):
        pyxel.init(100, 100)
        pyxel.run(self.update, self.draw)

    def update(self):
       if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

    def draw(self):
        while True:
            pyxel.cls(0)
            pyxel.rect(pyxel.frame_count % 140 - 40, 20, 40, 40, 7)
            pyxel.flip()
Quadrado()