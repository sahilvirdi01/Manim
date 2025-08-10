from manim import *

class Helloworld(Scene):
    def construct(self):
        text=Text("Hello World")
        self.play(Write(text))
