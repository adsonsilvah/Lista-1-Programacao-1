import pyxel

class Quadrado:

    def __init__(self):
        pyxel.init(100, 100)
        pyxel.run(self.update, self.draw)

    def update(self):
       if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(pyxel.mouse_x, pyxel.mouse_y,20,20,7)
        pyxel.circb(pyxel.mouse_x + 10,pyxel.mouse_y + 10,5,0)
        
Quadrado()