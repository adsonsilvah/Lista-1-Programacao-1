import pyxel


class Quadrado:

    def __init__(self):
        pyxel.init(160, 160)
        pyxel.run(self.update, self.draw)

    def update(self):
       if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(25, 25,50,50,7)
        pyxel.rectb(25,25, 50, 50, 5)
        pyxel.rectb(50,25,25,50, 5)
        pyxel.rectb(25,50,50,25, 5)
        
Quadrado()