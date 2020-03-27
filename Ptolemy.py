from manimlib.imports import *
import numpy as np

class First(Scene):
    def construct(self):
        Dot_color = YELLOW
        r = 3.25

        center = np.array([0,0,0])
        theta_A = ValueTracker(PI * 0.75)
        theta_B = ValueTracker(PI * 0.4)
        theta_C = ValueTracker(PI * -0.1)
        theta_D = ValueTracker(PI * -0.87)

        #get position
        get_pos = lambda theta: r*np.cos(theta.get_value())*LEFT + r*np.sin(theta.get_value())*UP+center
        A = get_pos(theta_A)
        B = get_pos(theta_B)
        C = get_pos(theta_C)
        D = get_pos(theta_D)

        # dot, circle, line
        circle = Circle(radius=r, color=BLUE).move_to(center)
        dot_A = Dot(A, color= Dot_color)
        dot_B = Dot(B, color=Dot_color)
        dot_C = Dot(C, color=Dot_color)
        dot_D = Dot(D, color=Dot_color)

        dots = [dot_A, dot_B, dot_C, dot_D]

        AB = Line(A,B,color=PINK)
        BC = Line(B,C,color=ORANGE)
        CD = Line(C,D,color=TEAL)
        DA = Line(D,A,color=GREEN)
        AC = Line(A,C,color=MAROON)
        BD = Line(B,D,color=PURPLE)

        lines = [AB, BC, CD, DA, AC, BD]

        #text
        text_A = TexMobject('A').scale(0.8).next_to(dot_A, RIGHT * 0.2 + UP * 0.2)
        text_B = TexMobject('B').scale(0.8).next_to(dot_B, LEFT * 0.2 + UP * 0.2)
        text_C = TexMobject('C').scale(0.8).next_to(dot_C, LEFT * 0.2 + DOWN * 0.2)
        text_D = TexMobject('D').scale(0.8).next_to(dot_D, RIGHT* 0.2 + DOWN * 0.2)

        texts = [text_A, text_B, text_C, text_D]

        #all objects
        all = Group(*self.mobjects)

        #animations
        self.play(ShowCreation(circle))
        self.wait(0.4)
        self.play(
            *[ShowCreation(obj) for obj in dots],
            *[Write(text) for text in texts]
        )
        self.wait()
        self.play(
            *[ShowCreation(obj) for obj in lines]
        )
        self.wait()
        self.play(Group(*self.mobjects).scale, 0.5,{"about_point":UP*4}, run_time = 1.5)
        self.wait()


        ##########################Blow
        start_1 = DOWN+LEFT*4
        start_2 = DOWN*1+RIGHT * 1
        start_3 = DOWN*0.3+RIGHT*6.5
        BC_cp = Line(start_1, start_1 + DOWN * BC.get_length(), color=BC.color)
        DA_cp = Line(start_1, start_1 + LEFT * DA.get_length(), color=DA.color)
        AB_cp = Line(start_2, start_2 + DOWN * AB.get_length(), color=AB.color)
        CD_cp = Line(start_2, start_2 + LEFT * CD.get_length(), color=CD.color)
        BD_cp = Line(start_3, start_3 + DOWN * BD.get_length(), color=BD.color)
        AC_cp = Line(start_3, start_3 + LEFT * AC.get_length(), color=AC.color)

        BC_DA = Rectangle(
            height = BC.get_length(),
            width = DA.get_length(),
            stroke_width=1,
            fill_color= DARK_BLUE,
            fill_opacity = 0.3
        ).next_to(BC_cp,LEFT,buff = 0)

        AB_CD = Rectangle(
            height=AB.get_length(),
            width=CD.get_length(),
            stroke_width=1,
            fill_color=DARK_BLUE,
            fill_opacity=0.3
        ).next_to(AB_cp, LEFT, buff=0)

        BD_AC = Rectangle(
            height=BD.get_length(),
            width=AC.get_length(),
            stroke_width=1,
            fill_color=DARK_BLUE,
            fill_opacity=0.3
        ).next_to(BD_cp,LEFT, buff=0)

        BC_text = TexMobject('\\cdot BC',color = BC.color).scale(0.8).next_to(BC_cp,LEFT,buff = .2)
        DA_text = TexMobject('DA', color = DA.color).scale(0.8).next_to(BC_text, LEFT, buff = .05)
        AB_text = TexMobject('\\cdot AB',color = AB.color).scale(0.8).next_to(AB_cp, LEFT, buff=0.8)
        CD_text = TexMobject('CD',color=CD.color).scale(0.8).next_to(AB_text, LEFT, buff=.05)
        BD_text = TexMobject('\\cdot BD',color = BD.color).scale(0.8).next_to(BD_cp, LEFT, buff=1)
        AC_text = TexMobject('AC',color=AC.color).scale(0.8).next_to(BD_text, LEFT, buff=.05)

        plus = TexMobject('+').scale(0.8).next_to(BC_cp, buff =0.8)
        equals = TexMobject('=').scale(0.8).next_to(AB_cp, buff = 1)

        #updater
        r,center = circle.radius*0.5, circle.get_center()

        circle.add_updater(lambda c:c.move_to(center))
        AB.add_updater(lambda l: l.become(Line(get_pos(theta_A), get_pos(theta_B), color=l.color)))
        BC.add_updater(lambda l: l.become(Line(get_pos(theta_B), get_pos(theta_C), color=l.color)))
        CD.add_updater(lambda l: l.become(Line(get_pos(theta_C), get_pos(theta_D), color=l.color)))
        DA.add_updater(lambda l: l.become(Line(get_pos(theta_D), get_pos(theta_A), color=l.color)))
        AC.add_updater(lambda l: l.become(Line(get_pos(theta_A), get_pos(theta_C), color=l.color)))
        BD.add_updater(lambda l: l.become(Line(get_pos(theta_B), get_pos(theta_D), color=l.color)))

        BC_cp.add_updater(lambda l: l.become(Line(start_1, start_1 + DOWN * BC.get_length(), color=l.color)))
        DA_cp.add_updater(lambda l: l.become(Line(start_1, start_1 + LEFT * DA.get_length(), color=l.color)))
        AB_cp.add_updater(lambda l: l.become(Line(start_2, start_2 + DOWN * AB.get_length(), color=l.color)))
        CD_cp.add_updater(lambda l: l.become(Line(start_2, start_2 + LEFT * CD.get_length(), color=l.color)))
        BD_cp.add_updater(lambda l: l.become(Line(start_3, start_3 + DOWN * BD.get_length(), color=l.color)))
        AC_cp.add_updater(lambda l: l.become(Line(start_3, start_3 + LEFT * AC.get_length(), color=l.color)))

        dot_A.add_updater(lambda d: d.become(Dot(get_pos(theta_A), color= Dot_color)))
        dot_B.add_updater(lambda d: d.become(Dot(get_pos(theta_B), color= Dot_color)))
        dot_C.add_updater(lambda d: d.become(Dot(get_pos(theta_C), color= Dot_color)))
        dot_D.add_updater(lambda d: d.become(Dot(get_pos(theta_D), color= Dot_color)))

        text_A.add_updater(lambda d: d.next_to(dot_A, RIGHT * 0.2 + UP * 0.2))
        text_B.add_updater(lambda d: d.next_to(dot_B, LEFT * 0.2 + UP * 0.2))
        text_C.add_updater(lambda d: d.next_to(dot_C, LEFT * 0.2 + DOWN * 0.2))
        text_D.add_updater(lambda d: d.next_to(dot_D, RIGHT* 0.2 + DOWN * 0.2))


        BC_DA.add_updater(lambda r: r.become(Rectangle(
            height=BC.get_length(),
            width=DA.get_length(),
            stroke_width=1,
            fill_color=DARK_BLUE,
            fill_opacity=0.3
        ).next_to(BC_cp, LEFT, buff=0)))

        AB_CD.add_updater(lambda r: r.become(Rectangle(
            height=AB.get_length(),
            width=CD.get_length(),
            stroke_width=1,
            fill_color=DARK_BLUE,
            fill_opacity=0.3
        ).next_to(AB_cp, LEFT, buff=0)))

        BD_AC.add_updater(lambda r: r.become(Rectangle(
            height=BD.get_length(),
            width=AC.get_length(),
            stroke_width=1,
            fill_color=DARK_BLUE,
            fill_opacity=0.3
        ).next_to(BD_cp, LEFT, buff=0)))



        #anim
        self.play(ApplyWave(BC,color = BC.color, direction = LEFT,amplitude = 0.2),
                  ApplyWave(DA,color =DA.color, direction = LEFT,amplitude = 0.2))
        self.wait()
        self.play(
            TransformFromCopy(BC,BC_cp),
            TransformFromCopy(DA,DA_cp)
        )
        self.wait()
        self.play(
            TransformFromCopy(BC_cp,BC_text),
            TransformFromCopy(DA_cp,DA_text),
            ShowCreation(BC_DA)
        )
        self.wait()
        self.play(Write(plus))
###
        self.play(ApplyWave(AB, color=AB.color,amplitude = 0.2),
                  ApplyWave(CD, color=CD.color,amplitude = 0.2))
        self.wait()
        self.play(
            TransformFromCopy(AB, AB_cp),
            TransformFromCopy(CD, CD_cp)
        )
        self.wait()
        self.play(
            TransformFromCopy(AB_cp, AB_text),
            TransformFromCopy(CD_cp, CD_text),
            ShowCreation(AB_CD)
        )
        self.wait()
        self.play(Write(equals))
    #######
        self.play(ApplyWave(BD, color=BD.color,direction = UP+RIGHT, amplitude = 0.2),
                  ApplyWave(AC, color=AC.color,direction = DOWN+RIGHT, amplitude = 0.2))
        self.wait()
        self.play(
            TransformFromCopy(BD, BD_cp),
            TransformFromCopy(AC, AC_cp)
        )
        self.wait()
        self.play(
            TransformFromCopy(BD_cp, BD_text),
            TransformFromCopy(AC_cp, AC_text),
            ShowCreation(BD_AC)
        )
        self.wait()

        #update theta
        delta = 1/9*PI
        self.play(
            ApplyMethod(theta_A.increment_value, delta*-1.5,
                run_time = 4, rate_func = there_and_back),

            ApplyMethod(theta_B.increment_value, delta*-0.3,
                run_time=4, rate_func=there_and_back),

            ApplyMethod(theta_C.increment_value, delta*0.7,
                run_time=4, rate_func=there_and_back),
            ApplyMethod(theta_D.increment_value, delta*-0.9,
                  run_time=4, rate_func=there_and_back))
        self.wait()

        self.play(
            *[FadeOut(obj) for obj in
              [DA_cp, BC_cp, AB_cp, CD_cp, AC_cp,BD_cp,plus,equals,BC_DA,AB_CD,BD_AC,
               BC_text,DA_text,AB_text,CD_text,BD_text,AC_text]
        ],run_time = 1.5)
        self.wait()
        self.remove(*[DA_cp, BC_cp, AB_cp, CD_cp, AC_cp,BD_cp,plus,equals,BC_DA,AB_CD,BD_AC,
               BC_text,DA_text,AB_text,CD_text,BD_text,AC_text])
        ######

        delta_length = (0.8-center[1])/60
        delta_t = 1/60
        run_time = 2
        steps = int(run_time/delta_t)
        for i in range(steps):
            center += np.array([0,delta_length,0])
            self.add(Group(*self.mobjects))
            self.wait(delta_t)
        self.wait()

        A = get_pos(theta_A)
        B = get_pos(theta_B)
        C = get_pos(theta_C)
        D = get_pos(theta_D)

        ABD = Polygon(
            A,B,D,
            fill_color=DARK_BLUE,
            fill_opacity=0.5
        )
        CBD = Polygon(
            C, B, D,
            fill_color=YELLOW,
            fill_opacity=0.5
        )
        ABC = Polygon(
            A,B, C,
            fill_color=PINK,
            fill_opacity=0.5
        )

        def get_angle(a,b,c):
            ba = a - b
            bc = c - b
            cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
            return np.abs(np.arccos(cosine_angle))

        self.play(
            ShowCreation(ABD),
            ShowCreation(CBD),
            run_time = 2
        )
        self.wait()
        self.play(
            Rotating(
                ABD,
                radians = -get_angle(D,B,C),
                run_time = 2,
                about_point = B
            ),
            Rotating(
                CBD,
                radians=get_angle(A, B, D),
                run_time=2,
                about_point=B
            )
        )
        self.wait()

        self.play(
            Rotating(
                ABD,
                radians = PI,
                run_time=2,
                axis = C-B,
                about_point = B
            ),
            Rotating(
                CBD,
                radians=PI,
                run_time=2,
                axis= B - A,
                about_point = B
            )
        )
        self.wait()

        def perpendicular(a):
            b = np.empty_like(a)
            b[0] = -a[1]
            b[1] = a[0]
            return b

        ABD_v = ABD.get_vertices()
        CBD_v = CBD.get_vertices()
        self.play(
            Rotating(ABD, axis = perpendicular(B - C),radians = PI,
                          about_point = (ABD_v[1] + ABD_v[2])/2),
            Rotating(CBD, axis=perpendicular(A - B),radians = PI,
                        about_point=(CBD_v[1] + CBD_v[2]) / 2),
            run_time = 2
        )
        self.wait()

        self.play(
            ApplyMethod(ABD.scale, BC.get_length()*0.8,{"about_point":B}),
            ApplyMethod(CBD.scale, AB.get_length()*0.8,{"about_point":B}),
            run_time = 2
        )
        self.wait()

        ABD_v = ABD.get_vertices()
        CBD_v = CBD.get_vertices()

        final = BraceLabel(
            Line(ABD_v[1], CBD_v[1]),
            ['AC', '\\cdot', ' BD'],
            perpendicular(C - A)
        )
        final.label[0].set_color(AC.color)
        final.label[2].set_color(BD.color)

        BC_brace = BraceLabel(
            Line(ABD_v[1], ABD_v[2]),
            ['BD','\\cdot',' BC'],
            perpendicular(ABD_v[2] - ABD_v[1])
        )
        BC_brace.label[0].set_color(BD.color)
        BC_brace.label[2].set_color(BC.color)

        AB_brace = BraceLabel(
            Line(CBD_v[1], CBD_v[2]),
            ['BD', '\\cdot',' AB'],
            perpendicular(CBD_v[1] - CBD_v[2])
        )
        AB_brace.label[0].set_color(BD.color)
        AB_brace.label[2].set_color(AB.color)

        up_l_brace = BraceLabel(
            Line(ABD_v[0], ABD_v[2]),
            text = ['AD','\\cdot',' BC'],
            brace_direction = perpendicular(ABD_v[2] - ABD_v[0])
        )
        up_l_brace.label[0].set_color(DA.color)
        up_l_brace.label[2].set_color(BC.color)

        up_r_brace = BraceLabel(
            Line(CBD_v[0], CBD_v[2]),
            text=['CD','\\cdot',' AB'],
            brace_direction=perpendicular(CBD_v[0] - CBD_v[2])
        )
        up_r_brace.label[0].set_color(CD.color)
        up_r_brace.label[2].set_color(AB.color)


        #BD_text = TexMobject('BD').scale(0.4).next_to()
        #AB_text = TexMobject('\\dot AB').scale(0.4).next_to()

        self.play(
            ShowCreation(BC_brace),
            ShowCreation(up_l_brace),
            ShowCreation(AB_brace),
            ShowCreation(up_r_brace),
            run_time = 2
        )
        self.wait()
        self.play(ShowCreation(ABC),run_time=2)
        self.wait()
        self.play(ABC.scale, BD.get_length() *0.8, {"about_point": B},run_time=2)
        self.wait()

        self.play(ShowCreation(final))
        self.wait()


        equation = TexMobject(
            "AD",
            "\\cdot",
            " BC",
            "+",
            "CD",
            "\\cdot",
            " AB",
            "=",
            "AC",
            "\\cdot",
            "BD"
        ).scale(0.8).to_corner(UL)
        equation[0].set_color(DA.color)
        equation[2].set_color(BC.color)
        equation[4].set_color(CD.color)
        equation[6].set_color(AB.color)
        equation[8].set_color(DA.color)
        equation[10].set_color(BD.color)

        self.play(
            *[TransformFromCopy(up_l_brace.label[i],equation[i]) for i in range(3)]
        )
        self.wait()
        self.play(Write(equation[3]))
        self.play(
            *[TransformFromCopy(up_r_brace.label[i], equation[i+4]) for i in range(3)]
        )
        self.wait()
        self.play(Write(equation[7]))
        self.play(
            *[TransformFromCopy(final.label[i], equation[i + 8]) for i in range(3)]
        )
        self.wait()
        rec = SurroundingRectangle(mobject=equation, color=YELLOW_C)
        self.play(ShowCreation(rec))
        self.wait(3)









