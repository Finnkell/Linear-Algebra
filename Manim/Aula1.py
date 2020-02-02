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

        \\end{flushleft}
        """)
        Tex2.set_width(2*(FRAME_X_RADIUS-1))
        Tex2.next_to(Tex1, BOTTOM, aligned_edge=LEFT)

        self.play(Write(Tex2))

