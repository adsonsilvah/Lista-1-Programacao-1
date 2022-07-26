import pyxel

class Quadrado:

    def __init__(self):
        pyxel.init(100, 100)
        pyxel.run(self.update, self.draw)

    def update(self):
       if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

    def draw(self):
        pyxel.rect(pyxel.mouse_x, pyxel.mouse_y,20,20,7)
        
Quadrado()