from manimlib.imports import *
import numpy as np
class Intd(Scene):
    def construct(self):
        title = TextMobject("Lebesgue Integration").scale(2)
        title_2 = TextMobject(
            "Lebesgue Integration",
            color = YELLOW
        ).to_edge(UP,buff=1).scale(1.4)
        title_line = Line(
            color='white',
            start =title_2.get_left()+LEFT,
            end = title_2.get_right()+RIGHT,
        ).next_to(title_2, DOWN)
        self.play(Write(title))
        self.wait()
        #self.play(title.to_edge(UP).scale(1))
        self.play(ReplacementTransform(title,title_2))
        self.play(ShowCreation(title_line))

        num_contents=2
        dots = [
            Dot(radius=0.1, color = BLUE).move_to([-3,-i+1,0]) for i in range(num_contents)
        ]
        content_text = [
            "Definition",
            "Properties"
        ]
        contents = [
            TextMobject(content_text[i]).next_to(dots[i],RIGHT, buff=0.3) for i in range(num_contents)
        ]
        for dot, con in zip(dots, contents):
            self.play(ShowCreation(dot))
            self.wait(0.1)
            self.play(Write(con))
            self.wait(0.5)
        self.wait()
        line_1 = VGroup(dots[0], contents[0])
        rec =  SurroundingRectangle(mobject= line_1,color = YELLOW_C)
        self.play(ShowCreation(rec))
        self.wait()
        self.play(FadeOut(VGroup(*self.mobjects)))
        self.wait()

class Definition(Scene):
    def construct(self):
        title = TexMobject(r"\mathbf{Definition}", color = BLUE).to_corner(UL)
        title_line = Line(
            color='white',
            start=title.get_left()+[-0.1,-.4,0],
            end= title.get_right()+[11,-.4,0]
        )
        self.play(Write(title))
        self.play(ShowCreation(title_line))
        self.wait()
        deft_1 = TextMobject(
            "A function ",
            "$f:X\\rightarrow R$",
            " is called \n",
            "countably simple\n",
            "if it has only ",
            "a countable ",
            " number of values.").scale(0.8).move_to([-0.2,2,0])
        deft_1[3].set_color(YELLOW)
        deft_1[-1].next_to(deft_1[0],DOWN, aligned_edge = LEFT)
        self.play(Write(deft_1))
        self.wait()

        deft_2 = TextMobject(
            "Given a measure space ",
            "$(X,\\mathcal{M},\\mu)$",
            " the ",
            " intergral ",
            " of a \\textit{nonnegative measurable} ",
            "\\textit{countably simple} function $f$ is defined by",
        ).scale(0.8).next_to(deft_1, DOWN).shift(RIGHT*0.2)
        deft_2[3].set_color(YELLOW)
        deft_2[-1].next_to(deft_2[0],DOWN, aligned_edge = LEFT)
        self.play(Write(deft_2))
        self.wait()

        eq_1 = TexMobject(
            "\\int_{X}{fdu}=\sum_{i=1}^{\infty}",
            "{a_i",
            "\mu(f^{-1}\{a_i\})}"
        ).shift(DOWN)
        self.play(Write(eq_1))
        self.wait()
        rec = SurroundingRectangle(mobject=eq_1[1], color=YELLOW_C)
        self.play(ShowCreation(rec))

        arrow = Arrow(UP, DOWN,color = BLUE).next_to(rec, DOWN)
        self.play(ShowCreation(arrow))


        note = TexMobject(r"\text{range}(f)=\{a_1,a_2,...\}").next_to(arrow, DOWN).scale(0.6)
        self.play(FadeInFromDown(note))
        self.wait()
        self.play(FadeOut(VGroup(*self.mobjects)))
        self.wait()

class QT1(Scene):

    CONFIG = {
        "low_simple_color": RED,
        "up_simple_color": "#DC28E2"
    }

    def construct(self):
        qt = TextMobject("But what about arbitrary functions?")
        self.play(FadeInFromDown(qt))
        self.wait()
        self.play(FadeOut(qt))
        self.wait()
        text1 = TextMobject("Let's assume that $f$ is a",
                            " nonnegative ",
                            "measurable function.")
        text1[1].set_color(YELLOW)
        self.play(FadeInFromDown(text1))
        self.wait()
        self.play(FadeOut(text1))
        self.wait()
        title = TexMobject(r"\mathbf{Definition}", color=BLUE).to_corner(UL)
        title_line = Line(
            color='white',
            start=title.get_left() + [-0.1, -.4, 0],
            end=title.get_right() + [11, -.4, 0]
        )
        self.play(FadeIn(VGroup(title, title_line)))

        def1 = TextMobject(
            "Let ",
            "$g$",
            ",",
            " $h$",
            " be nonnegative mesurable coutably simple functions ",
            " such",
            " that "
        ).scale(0.8).next_to(title_line,DOWN, aligned_edge = LEFT)

        lower = TexMobject("f\\geq ",'g'
                           ).scale(0.8).next_to(def1,DOWN, buff = 0.6)

        upper = TexMobject("f\\leq ",'h'
                           ).scale(0.8).next_to(lower,DOWN, buff = 1.4)

        upper_int = TexMobject(
            "\\overset{-}{\\int_X{}}fd\\mu",
            "=",
            "\\text{inf}",
            "\\int^{}_X",
            "h",
            "d",
            "\\mu"
            ).move_to(upper)

        lower_int = TexMobject(
            "\\underset{- \\quad}{\\int_X{}}fd\\mu",
            "=",
            "\\text{sup}\\int_X",
            "g",
            "d",
            "\\mu"
            ).move_to(lower)

        brace = Brace(VGroup(upper_int, lower_int), RIGHT)
        eq = TexMobject("=", color = YELLOW).next_to(brace, RIGHT)

        def2 = TextMobject(
            "Define the",
            " integral ",
            "of $f$ by"
        ).scale(0.8).next_to(def1, DOWN, aligned_edge = LEFT,  buff = 3.8)

        integral = TexMobject("\\int_X{fd\\mu}",
                               "=\\overset{-}{\\int_X{}}fd\\mu",
                               "=\\underset{- \\quad}{\\int_X{}}fd\\mu"
                            ).scale(0.8).shift(DOWN*2.8)

        #color
        def1[1].set_color(self.low_simple_color)
        def1[3].set_color(self.up_simple_color)
        lower[1].set_color(self.low_simple_color)
        upper[1].set_color(self.up_simple_color)
        lower_int[-3].set_color(self.low_simple_color)
        upper_int[-3].set_color(self.up_simple_color)
        def2[1].set_color(YELLOW)
        integral[0].set_color(YELLOW)

        #animation
        self.play(Write(def1))
        self.wait()
        self.play(
            Write(lower),
            Write(upper)
        )
        self.wait()

        self.play(ReplacementTransform(lower, lower_int),
                  ReplacementTransform(upper, upper_int))
        self.wait()
        self.play(FadeInFrom(brace, LEFT))
        self.play(Write(eq))
        self.wait()
        self.play(Write(def2))
        self.wait()
        self.play(Write(integral))
        self.wait()
        self.play(FadeOut(VGroup(*self.mobjects)))
        self.wait()

class Graph1(GraphScene):
    CONFIG = {
        "y_max" : 10,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : -1,
        "axes_color" : BLUE,
        "low_simple_color": RED,
        "up_simple_color": "#DC28E2"
    }
    def construct(self):
        self.setup_axes(animate=True)
        def func(x):
            return 0.15*(x-0.5)*(x-2)*(x-5.5)+5

        pl = 0.15 * np.poly1d([0.5, 2, 5.5],True) + 5

        def get_roots(pl,ys):
            roots = np.array([])
            for y in ys:
                root = (pl-y).roots
                root = root[np.isreal(root)].real
                roots = np.append(roots,root)
            return np.sort(roots)


        graph = self.get_graph(
            func,
            x_min=self.x_min,
            x_max=self.x_max,
            color = GREEN
        )
        self.play(
            ShowCreation(graph),
            run_time=1
        )
        fx = TexMobject("f(x)",color = GREEN).move_to([4.6,3.,0.])
        self.play(FadeInFrom(fx,LEFT))
        self.wait()

        t = 1.2
        low_k, high_k = -26,28
        ys = np.array([t**k for k in range(low_k, high_k)])
        ys = ys[ys>func(self.x_min)]
        roots = get_roots(pl, ys)
        lower_sp, upper_sp = self.plot_simple(roots, func)

        t = 1.09
        low_k, high_k = -26, 30
        ys = np.array([t ** k for k in range(low_k, high_k)])
        ys = ys[ys > func(self.x_min)]
        roots = get_roots(pl, ys)
        lower_sp2, upper_sp2 = self.plot_simple(roots, func, False)

        self.play(ReplacementTransform(
            VGroup(lower_sp, upper_sp),
            VGroup(lower_sp2, upper_sp2)
        ))
        self.wait()

        t = 1.04
        low_k, high_k = -26, 120
        ys = np.array([t ** k for k in range(low_k, high_k)])
        ys = ys[ys > func(self.x_min)]
        roots = get_roots(pl, ys)
        lower_sp3, upper_sp3 = self.plot_simple(roots, func, False)

        self.play(ReplacementTransform(
            VGroup(lower_sp2, upper_sp2),
            VGroup(lower_sp3, upper_sp3)
        ))
        self.wait()

        t = 1.02
        low_k, high_k = -26, 120
        ys = np.array([t ** k for k in range(low_k, high_k)])
        ys = ys[ys > func(self.x_min)]
        roots = get_roots(pl, ys)
        lower_sp4, upper_sp4 = self.plot_simple(roots, func, False)

        self.play(ReplacementTransform(
            VGroup(lower_sp3, upper_sp3),
            VGroup(lower_sp4, upper_sp4)
        ))
        self.wait()




    def plot_simple(self, roots, fc,plot = True):
        upper_sp = []
        lower_sp = []
        for i in range(len(roots) - 1):
            left, mid, right = fc(roots[i]), fc((roots[i]+roots[i + 1])/2),fc(roots[i+1])
            graph_point_l = self.coords_to_point(roots[i], left)
            graph_point_r = self.coords_to_point(roots[i + 1], right)

            lower_line = Line(
                start=[graph_point_l[0],
                       min(graph_point_l[1],graph_point_r[1]),
                       0.],
                end=[graph_point_r[0],
                     min(graph_point_l[1],graph_point_r[1]),
                     0.],
                color=self.low_simple_color
            )

            upper_line = Line(
                start=[graph_point_l[0],
                       max(graph_point_l[1],graph_point_r[1]),
                       0.],
                end=[graph_point_r[0],
                     max(graph_point_l[1],graph_point_r[1]),
                     0.],
                color=self.up_simple_color
            )

            if mid > max(left, right):
                graph_point_m = self.coords_to_point((roots[i]+roots[i+1])/2, mid)
                upper_line = Line(
                    start=[graph_point_l[0],
                        graph_point_m[1]+3e-2,
                        0.],
                    end=[graph_point_r[0],
                        graph_point_m[1]+3e-2,
                        0.],
                    color=self.up_simple_color
                )
                print()

            elif mid < min(left, right):
                graph_point_m = self.coords_to_point((roots[i] + roots[i + 1]) / 2, mid)
                lower_line = Line(
                    start=[graph_point_l[0],
                           graph_point_m[1]-3e-2,
                           0.],
                    end=[graph_point_r[0],
                         graph_point_m[1]-3e-2,
                         0.],
                    color=self.low_simple_color
                )

            lower_sp.append(lower_line)
            upper_sp.append(upper_line)

        lower_sp = VGroup(*lower_sp)
        upper_sp = VGroup(*upper_sp)

        if plot == True:
            self.play(FadeInFrom(lower_sp, LEFT))

            gx = TexMobject("g(x)", color=self.low_simple_color).move_to([2., -0.8, 0.])
            hx = TexMobject("h(x)", color=self.up_simple_color).move_to([0.5, 1.6, 0.])
            self.play(FadeInFrom(gx, UP))
            self.wait()
            self.play(FadeInFrom(upper_sp,RIGHT))
            self.play(FadeInFrom(hx, DOWN))
            self.wait()
        return lower_sp,upper_sp

class Last(Scene):
    def construct(self):
        qt = TextMobject("What if $f$ is ",
                         " not ",
                         "nonnegative?")
        qt[1].set_color(YELLOW)
        self.play(FadeInFromDown(qt))
        self.wait()
        self.play(FadeOut(qt))
        self.wait()
        title = TexMobject(r"\mathbf{Definition}", color=BLUE).to_corner(UL)
        title_line = Line(
            color='white',
            start=title.get_left() + [-0.1, -.4, 0],
            end=title.get_right() + [11, -.4, 0]
        )
        self.play(FadeIn(VGroup(title, title_line)))
        self.wait()

        def1 = TextMobject(
            "If $f$ is a measurable function, define "
        ).scale(0.8).next_to(title_line, DOWN, aligned_edge=LEFT)

        plus = TexMobject("f^{",
                           "+} ",
                          ":=",
                           "\\max",
                           "(f,0)",
                          "\\geq 0"
                    ).scale(0.8).next_to(title_line, DOWN, buff = 0.8)

        mins = TexMobject("f^{",
                          "-}",
                          ":=",
                          "-\\min",
                          "(f,0)",
                          "\\geq 0"
                    ).scale(0.8).next_to(plus, DOWN, buff=0.4)

        plus[1].set_color(BLUE)
        mins[1].set_color(BLUE)

        self.play(Write(def1))
        self.play(
            Write(plus),
            Write(mins)
        )
        self.wait()
        def2 = TextMobject(
            "Thus, ",
            "$f=f^{+}-f^{-}$",
            ". Define"
        ).scale(0.8).next_to(title, DOWN, aligned_edge = LEFT, buff = 2.8)
        self.play(Write(def2))
        self.wait()

        integral = TexMobject(
            "\\int_X{fd\\mu}=",
            "\\int_X{f^+d\\mu}",
            "-",
            "\\int_X{f^-d\\mu}"
        ).scale(0.8).shift(DOWN * 0.8)

        integral[0].set_color(YELLOW)
        self.play(Transform(def2[1].copy(), integral))
        self.wait()

        inf = TexMobject(
            "\\infty",
            "-",
            "\\infty",
            "=",
            "?"
        )

        inf[0].next_to(integral[1], DOWN)
        inf[1].next_to(integral[2], DOWN, buff = 0.8)
        inf[2].next_to(integral[-1], DOWN)
        inf[3].next_to(inf[2], RIGHT)
        inf[4].next_to(inf[3], RIGHT)

        self.play(
            ShowCreationThenFadeAround(integral[1]),
            Write(inf[0])
        )

        self.play(Write(inf[1]))

        self.play(
            ShowCreationThenFadeAround(integral[3]),
            Write(inf[2])
        )
        self.wait()
        self.play(Write(inf[3:5]))
        self.wait()
        self.play(Indicate(inf[-1],color = RED))
        self.wait()

        cross = Cross(inf)
        self.play(GrowFromCenter(cross))
        self.wait()

        note = TextMobject("At least one term is finite, so that the integral",
                    " exits").scale(0.8).move_to(cross).shift(DOWN*0.8)
        note2 = TextMobject("If both are finite, we say $f$ is",
                    " integrable").scale(0.8).move_to(note)
        note[1].set_color(YELLOW)
        note2[1].set_color(YELLOW)

        self.play(
            *[FadeOut(mod) for mod in [cross,inf]]
        )
        self.wait()
        self.play(Write(note))
        self.wait()
        self.play(FadeOut(note))
        self.wait()
        self.play(Write(note2))
        self.wait()



