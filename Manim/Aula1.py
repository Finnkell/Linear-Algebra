from manimlib.imports import *

class Animation(Scene):
    def construct(self):
        Tex1 = TextMobject("$\\Large{\\text{Capítulo 6: Decomposição em somas diretas invariantes}}$")
        Tex1.to_edge(UP)
        Tex1.set_color(GREEN)
        Tex1.set_width(2*(FRAME_X_RADIUS-1))
        self.play(Write(Tex1))

        Tex2 = TextMobject("""
        \\begin{flushleft}
        Se $W_1$, $W_2 \\subseteq{V}$ subespaços, já discutimos a soma $W = W_1 + W_2$, i.é, o subespaço de todos os $\\alpha = \\alpha_1 + \\alpha_2$ com $\\alpha_i \\in W_i$. Uma situação particularmente agradável ocorre quando $W_1$ e $W_2$ são disjuntos. De fato, neste caso, um dado vetor $\\alpha \\in W$ pode ser escrito sob a forma $\\alpha = \\alpha_1 + \\alpha_2$, $\\alpha_i \\in W_i$, de uma única maneira. Isto resulta do fato de que se também temos $\\alpha = \\beta_1 + \\beta_2$ com $\\beta_i \\in W_i$, então:

        $$\\alpha_1 + \\alpha_2 = \\beta_1 + \\beta_2$$

        de modo que

        $$\\alpha_1 - \\beta_1 = \\beta_2 - \\alpha_2$$

        \\end{flushleft}
        """)

        Tex3 = TextMobject("""
        \\begin{flushleft}
        Como $\\alpha_1 - \\beta_1 \\in W_1$ e $\\beta_2 - \\alpha_2 \\in W_2$, devemos ter $\\alpha_1 - \\beta_1 = \\beta_2 - \\alpha_2 = 0$, i.é, $\\alpha_1 = \\beta_1$ e $\\alpha_2 = \\beta_2$. Quando $W_1$ e $W_2$ forem disjuntos diremos que a soma $W = W_1 + W_2$ é direta, ou que $W$ é \\textbf{soma direta} de $W_1$ e $W_2$.

        \\end{flushleft}
        """)

        Tex2.set_width(2*(FRAME_X_RADIUS-1))
        Tex2.next_to(Tex1, BOTTOM, aligned_edge=LEFT)
        self.play(Write(Tex2))
        self.clear()
        Tex3.set_width(2*(FRAME_X_RADIUS-1))
        Tex3.to_edge(UP)
        self.play(Transform(Tex2, Tex3))

