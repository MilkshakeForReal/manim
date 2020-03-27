from manimlib.imports import *

class Formula(Scene):
    def construct(self):
        formula_tex_1 = TexMobject(r"\frac{df}{dx}")
        formula_tex_2 = TexMobject("\\frac{df}{dx}")
        formula_tex_1.scale(1.5)
        self.add(formula_tex_1)

class TextFormula(Scene):
    def construct(self):
        formula = TextMobject("Fraction: $\\frac{df}{dx}$")
        self.add(formula)
