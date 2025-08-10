from manim import *

class rotations(Scene):
    def construct(self):
        l_square=Square(color="BLUE",fill_opacity=0.7).shift(2*LEFT)
        r_square=Square(color="Green",fill_opacity=0.7).shift(2*RIGHT)
        self.play(l_square.animate.rotate(PI),Rotate(r_square,angle=PI), run_time=2)
        self.wait()
