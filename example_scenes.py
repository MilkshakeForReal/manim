#!/usr/bin/env python

from manimlib.imports import *

# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle -pl
#
# Use the flat -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.
# Use -r <number> to specify a resolution (for example, -r 1080
# for a 1920x1080 video)
class ConfigExmaple(Scene):
    CONFIG={
        "camera_config":{"background_color": RED}
    }
    def construct(self):
        text = TextMobject("text")
        self.play(Write(text))
        self.wait()

class OpeningManimExample(Scene):
    def construct(self):
        title = TextMobject("This is some \\LaTeX")
        basel = TexMobject(
            "\\sum_{n=1}^\\infty "
            "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
        )
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeInFrom(basel, UP),
        )
        self.wait()

        transform_title = TextMobject("That was a transform")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*map(FadeOutAndShiftDown, basel)),
        )
        self.wait()

        grid = NumberPlane()
        grid_title = TextMobject("This is a grid")
        grid_title.scale(1.5)
        grid_title.move_to(transform_title)

        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            FadeOut(title),
            FadeInFromDown(grid_title),
            ShowCreation(grid, run_time=3, lag_ratio=0.1),
        )
        self.wait()

        grid_transform_title = TextMobject(
            "That was a non-linear function \\\\"
            "applied to the grid"
        )
        grid_transform_title.move_to(grid_title, UL)
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.apply_function,
            lambda p: p + np.array([
                np.sin(p[1]),
                np.sin(p[0]),
                0,
            ]),
            run_time=3,
        )
        self.wait()
        self.play(
            Transform(grid_title, grid_transform_title)
        )
        self.wait()


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


class WarpSquare(Scene):
    def construct(self):
        square = Square()
        self.play(ApplyPointwiseFunction(
            lambda point: complex_to_R3(np.exp(R3_to_complex(point))),
            square
        ))
        self.wait()


class WriteStuff(Scene):
    def construct(self):
        example_text = TextMobject(
            "This is a some text",
            tex_to_color_map={"text": YELLOW}
        )
        example_tex = TexMobject(
            "\\sum_{k=1}^\\infty {1 \\over k^2} = {\\pi^2 \\over 6}",
        )
        group = VGroup(example_text, example_tex)
        group.arrange(DOWN)
        group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

        self.play(Write(example_text))
        self.play(Write(example_tex))
        self.wait()


class UpdatersExample(Scene):
    def construct(self):
        decimal = DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=True,
        )
        square = Square().to_edge(UP)

        decimal.add_updater(lambda d: d.next_to(square, RIGHT))
        decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))
        self.add(square, decimal)
        self.play(
            square.to_edge, DOWN,
            rate_func=there_and_back,
            run_time=5,
        )
        self.wait()

# See old_projects folder for many, many more
class RiemannRectangles(GraphScene):
    CONFIG = {
        "y_max": 8,
        "y_axis_height": 5,
    }
    def construct(self):
        self.setup_axes()
        def func(x):
            return 0.1 * (x + 3-5) * (x - 3-5) * (x-5) + 5

        graph=self.get_graph(func,x_min=0.3,x_max=9.2)
        riemann_rectangles=self.get_riemann_rectangles(
                                    graph,
                                    x_min=2,
                                    x_max=8,
                                    dx=0.5
                                    )
        self.add(graph,riemann_rectangles)

class Ball(SpecialThreeDScene):
    def construct(self):
        self.set_camera_to_default_position()
        axes = ThreeDAxes()
        self.add(axes)
        self.wait(0.2)
        sphere1 = Sphere(radius=2, checkerboard_colors=None, fill_opacity=0.3)
        self.play(*[FadeInFrom(sphere1[i],
                               sphere1[i].get_center()[0] * 2 * RIGHT + sphere1[i].get_center()[2] * 2 * OUT +
                               sphere1[i].get_center()[1] * 2 * UP, run_time=np.random.random() * 2)
                    for i in range(len(sphere1))])
        self.wait()

class RiemannRectanglesAnimation(GraphScene):
    CONFIG = {
        "y_max": 8,
        "y_axis_height": 5,
        "init_dx":0.5,
    }
    def construct(self):
        self.setup_axes()
        def func(x):
            return 0.1 * (x + 3-5) * (x - 3-5) * (x-5) + 5

        graph=self.get_graph(func,x_min=0.3,x_max=9.2)
        kwargs = {
            "x_min" : 2,
            "x_max" : 8,
            "fill_opacity" : 0.75,
            "stroke_width" : 0.25,
        }
        flat_rectangles = self.get_riemann_rectangles(
                                self.get_graph(lambda x : 0),
                                dx=self.init_dx,
                                start_color=invert_color(PURPLE),
                                end_color=invert_color(ORANGE),
                                **kwargs
        )
        riemann_rectangles_list = self.get_riemann_rectangles_list(
                                graph,
                                6,
                                max_dx=self.init_dx,
                                power_base=2,
                                start_color=PURPLE,
                                end_color=ORANGE,
                                 **kwargs
        )
        self.add(graph)
        # Show Riemann rectangles
        self.play(ReplacementTransform(flat_rectangles,riemann_rectangles_list[0]))
        self.wait()
        for r in range(1,len(riemann_rectangles_list)):
            self.transform_between_riemann_rects(
                    riemann_rectangles_list[r-1],
                    riemann_rectangles_list[r],
                    replace_mobject_with_target_in_scene = True,
                )
        self.wait()

