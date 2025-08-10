from manim import *

class square(Scene):
    def construct(self):
        square=Square()
        square.set_fill("RED",opacity=0.6)
        self.play(Create(square))
