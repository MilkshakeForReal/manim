from manimlib.imports import *
import numpy as np

class First(SpecialThreeDScene):

    def construct(self):
        self.set_camera_orientation(distance = 6)

        l = 1
        square = VGroup(
            ParametricSurface(lambda u, v:  u * RIGHT + v * UP,
                                 u_min=0, u_max=l, v_min=0, v_max=l, resolution=(10, 10),
                                 checkerboard_colors=[BLUE_D]),
            Arrow(start=[0, 0, 0], end=[l, 0, 0], color=RED),
            Arrow(start=[0, l, 0], end=[l, l, 0], color=RED)
        )

        twisted_square = VGroup(
            ParametricSurface(lambda u, v: np.array([u,l/PI*np.cos(v), l/PI*np.sin(v)+l/PI]),
                                         u_min=0, u_max=l, v_min=-PI/2, v_max=PI/2, resolution=(10, 10),
                                         checkerboard_colors=[BLUE_D]),

            Arrow(start=[0, 0, 0], end=[l, 0, 0], color=RED),
            Arrow(start=[0, 0, 2*l/PI], end=[10, 0, 2*l/PI], color=RED)
        )
        cylinder = ParametricSurface(lambda u, v: np.array([u,l/2/PI*np.cos(v), l/2/PI*np.sin(v)+l/TAU]),
                                         u_min=0, u_max=l, v_min=-PI, v_max=PI, resolution=(10, 10),
                                        checkerboard_colors=[BLUE_D])

        self.play(ShowCreation(square[0]), run_time=1.2)
        self.wait()
        self.move_camera(phi = 75*DEGREES, theta = -45*DEGREES, run_time= 3)
        self.play(
            *[FadeInFrom(square[i],LEFT) for i in [1,2]]
        )
        self.wait()
        self.play(ReplacementTransform(square, twisted_square), run_time=2)
        self.wait()
        self.play(ReplacementTransform(twisted_square, cylinder), run_time=2)


class twod(GraphScene):
    def construct(self):
        l = 5
        text1 = TextMobject("Consider $R$ equipped with the Euclidean topology,",
                            " and a subset $A=[0,1]$ ",
                            " with the topology $\\mathcal{T}_A$  induced on $A$."
                ).scale(0.8)
        text1[2].next_to(text1[0],DOWN, aligned_edge = LEFT)
        text2 = TextMobject("Now we \"paste\" the end points of $A$",
                            " together."
                        ).scale(0.8)
        text3 = TextMobject("More precisely, the map is $f(x)=(\\cos{2\\pi x},\\sin{2\\pi x}), x\\in A.$").scale(0.8)

        line = Line(start = [1,0.8,0], end = [1+l,0.8,0],color = BLUE)
        circle = Circle(radius=l / TAU, color=BLUE).next_to(line, DOWN, buff=2)

        line_dots = VGroup(
            line,
            Dot(color=YELLOW).next_to(line, RIGHT, buff=-0.08),
            Dot(color = YELLOW).next_to(line, LEFT, buff = -0.08)
        )

        circle_dots = VGroup(
            circle,
            Dot(color=YELLOW).next_to(circle, RIGHT, buff=-0.1)
        )
        extra_dot = Dot(color=YELLOW).next_to(circle, RIGHT, buff=-0.08)

        #Properties
        num_contents = 3
        dots = VGroup(*[
            Dot(radius=0.1, color=BLUE).move_to([-5.5, -i + 1, 0]) for i in range(num_contents)
        ])
        content_text =  [
            "$f$ is onto",
            "$f$ is continuous",
            "If $f^{-1}(U)$ is open, $U$ is open",
        ]
        contents = VGroup(*[
            TextMobject(content_text[i]).scale(0.8).next_to(dots[i], RIGHT, buff=0.3) for i in range(num_contents)
        ])


        self.play(Write(text1))
        self.wait()
        self.play(text1.to_edge, UP)
        text2[0].next_to(text1[-1], RIGHT)
        text2[1].next_to(text1[-1], DOWN, aligned_edge = LEFT)
        text3.next_to(text2[-1], RIGHT)

        self.play(ShowCreation(line))
        self.wait()
        self.play(Write(text2))
        self.wait()
        self.play(ShowCreation(line_dots[1:3]))
        self.play(TransformFromCopy(line_dots[:2], circle_dots),
                  TransformFromCopy(line_dots[2], extra_dot),
                  run_time = 2)
        self.wait(2)
        self.play(Write(text3))
        self.wait()


        rotate_dot = extra_dot.copy().set_color(RED)
        shift_dot = line_dots[-1].copy().set_color(RED)
        dash_line = DashedLine(rotate_dot,shift_dot)
        def updater(object):
            object.put_start_and_end_on(rotate_dot.get_center(),
                                        shift_dot.get_center())
        dash_line.add_updater(updater)

        self.play(ShowCreation(dots[0]))
        self.wait(0.1)
        self.play(Write(contents[0]))
        self.wait()
        self.play(
            FadeIn(rotate_dot),
            FadeIn(shift_dot),
            FadeIn(dash_line)
        )
        self.wait()
        self.play(MoveAlongPath(rotate_dot,circle),
                  MoveAlongPath(shift_dot, line),
                  run_time = 2)
        dash_line.remove_updater(updater)

        self.wait()

        self.play(
            FadeOut(rotate_dot),
            FadeOut(shift_dot),
            FadeOut(dash_line)
        )
        self.play(ShowCreation(dots[1]))
        self.wait(0.1)
        self.play(Write(contents[1]))

        self.wait()

        self.play(ShowCreation(dots[2]))
        self.wait(0.1)
        self.play(Write(contents[2]))
        self.wait()

        self.play(VGroup(dots,contents).shift, RIGHT*1.5)

        brace = Brace(VGroup(*dots), LEFT)
        label = TextMobject("Quotient",
                           " Mapping", color=YELLOW).scale(0.8)
        label[0].next_to(brace, LEFT).shift(UP*0.4)
        label[1].next_to(label[0], DOWN)
        self.play(FadeInFrom(brace, LEFT))
        self.wait()

        self.play(ShowCreation(label))
        self.wait()

        warning = TextMobject("But $f$ is",
                              " not homeomorphic",
                              "!").next_to(
                                            text1,
                                            DOWN,
                                            aligned_edge = LEFT,
                                            buff = 5
                                        )
        warning[1].set_color(YELLOW)
        self.play(FadeInFromDown(warning))
        self.wait()
