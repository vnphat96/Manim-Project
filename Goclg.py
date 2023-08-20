from manim import *

class PlotParametricFunction(Scene):
    def construct(self):
        ax = Axes(x_range=[-4, 4, 4], y_range=[-4, 4, 4], x_length=8, y_length=8)
        pcircle = Circle(3, stroke_color=WHITE)
        self.add(ax, pcircle)
        
        a = ValueTracker(0.1)
        oa = Line([0,0,0], [3,0,0], stroke_color=GOLD)
        m = always_redraw(lambda: Dot(np.array([3*np.cos(a.get_value()*PI), 3*np.sin(a.get_value()*PI),0]),color=BLUE))
        h = always_redraw(lambda: Dot(np.array([0, 3*np.sin(a.get_value()*PI),0]),color=GOLD))
        k = always_redraw(lambda: Dot(np.array([3*np.cos(a.get_value()*PI), 0,0]),color=GOLD))        
        om = always_redraw(lambda : Line([0,0,0], m, stroke_color=BLUE))
        mh = always_redraw(lambda : DashedLine(m,h,stroke_color=GOLD))
        mk = always_redraw(lambda : DashedLine(m,k,stroke_color=GOLD))
        self.add(oa,m,h,k,om,mh,mk)
        a_number = DecimalNumber(
            a.get_value(),
            color=RED,
            num_decimal_places=1,
            show_ellipsis=False
        )
        a_number.add_updater(
            lambda mob: mob.set_value(a.get_value())
        )
        textA=always_redraw(lambda: MathTex("\\alpha =",color=RED).next_to(a_number,LEFT))
        textB=always_redraw(lambda: MathTex("\\pi",color=RED).next_to(a_number,RIGHT))
        text = VGroup(textA,a_number,textB).to_edge(UL)
        vegoc = lambda x,t: np.array([t,t,0]) if x==0 else (
             np.array([abs(0.7 + 0.1*t)* np.cos(t*PI), abs(0.7 + 0.1*t) * np.sin(t*PI), 0])
             if x>0 else np.array([abs(0.7 + 0.1*t)* np.cos(t*PI), -abs(0.7 + 0.1*t) * np.sin(t*PI), 0])
        )
        dot = Dot(color=RED)
        goclg = always_redraw(lambda: ParametricFunction(lambda t: vegoc(a.get_value(),t), t_range=[0,abs(a.get_value())],stroke_color=RED))
        # arrow = always_redraw(lambda: Line(goclg.get_end())
        # arrow.add_tip(tip_shape=StealthTip, tip_length=1, tip_width=1)
              
        self.add(goclg, text)
        self.play(a.animate(rate_func=linear).set_value(4),run_time=4)
        self.wait(1)
        self.play(a.animate.set_value(-3),run_time=7)

