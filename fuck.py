from manimlib.imports import  *

class Fuck_World(Scene):

    def construct(self):
        ##Making object
        fuckworld = TextMobject("Fuck World", color = RED)

        ##Position
        
        self.play(Write(fuckworld))
        self.wait(1)