from tkinter import *

class Janela:
    def __init__(self, toplevel):
        self.quantas_vezes_calculou = 0

        self.frame_Titulo = Frame(toplevel)
        self.frame_a = Frame(toplevel)
        self.frame_b = Frame(toplevel)
        self.frame_funcoes = Frame(toplevel)
        self.frame_xy = Frame(toplevel)
        self.frame_x = Frame(self.frame_xy)
        self.frame_y = Frame(self.frame_xy)

        self.frame_Titulo.pack(side=TOP)
        self.frame_xy.pack(side=TOP)
        self.frame_x.pack(side=LEFT)
        self.frame_y.pack(side=RIGHT)
        self.frame_a.pack(side=TOP)
        self.frame_b.pack(side=TOP)
        self.frame_funcoes.pack(side=TOP)

        self.titulo = Label(self.frame_Titulo, text="Calcular Equação geral da reta", font=('Consolas', 12))

        self.x = Label(self.frame_x, text='  X', font=('Consolas', 12))
        self.y = Label(self.frame_y, text='   Y', font=('Consolas', 12))

        self.lblA = Label(self.frame_a, text="A (", font=('Consolas', 12))
        self.txtXA = Entry(self.frame_a, width=3, justify=CENTER, font=('Consolas', 12))
        self.lblPVA = Label(self.frame_a, text=";", font=('Consolas', 12))
        self.txtYA = Entry(self.frame_a, width=3, justify=CENTER, font=('Consolas', 12))
        self.lblParantesesA = Label(self.frame_a, text=")", font=('Consolas', 12))

        self.lblB = Label(self.frame_b, text="B (", font=('Consolas', 12))
        self.txtXB = Entry(self.frame_b, width=3, justify=CENTER, font=('Consolas', 12))
        self.lblPVB = Label(self.frame_b, text=";", font=('Consolas', 12))
        self.txtYB = Entry(self.frame_b, width=3, justify=CENTER, font=('Consolas', 12))
        self.lblParantesesB = Label(self.frame_b, text=")", font=('Consolas', 12))

        self.btnCalc = Button(self.frame_funcoes, text="Calcular", font=('Consolas', 12))

        self.Resultado = Entry(self.frame_funcoes, font=('Consolas', 12), width=20, justify=CENTER)
        self.Resultado2 = Entry(self.frame_funcoes, font=('Consolas', 12), width=20, justify=CENTER)


        self.titulo.pack()

        self.lblA.pack(side=LEFT)
        self.txtXA.pack(side=LEFT)
        self.txtXA.focus()
        self.txtXA.select_range(0, 'end')
        #self.txtXA.icursor('end')
        self.txtXA.select_adjust(0)
        self.lblPVA.pack(side=LEFT)
        self.txtYA.pack(side=LEFT)
        self.lblParantesesA.pack(side=LEFT)

        self.lblB.pack(side=LEFT)
        self.txtXB.pack(side=LEFT)
        self.lblPVB.pack(side=LEFT)
        self.txtYB.pack(side=LEFT)
        self.lblParantesesB.pack(side=LEFT)

        self.btnCalc.pack(side=TOP)

        self.x.pack(side=RIGHT)
        self.y.pack(side=LEFT)


        self.btnCalc["command"] = lambda: self.mostrar_resultado(int(self.txtXA.get()), int(self.txtYA.get()), int(self.txtXB.get()), int(self.txtYB.get()))

    def calcular_Equacao_Geral(self, xa, ya, xb, yb):
        """
        Y-Yo = m(X-Xo)
        Yb - Ya = m(Xb - Xa)

        Y = mX - mXo + Yo
        Y = m*X - mXa + Ya

        X = (Y/m)-(Yo/m) - Xo
        X = (Y/m)-(Ya/m) - Xa

        ax + by + c = 0
        """
        m = float((yb - ya) / (xb - xa))
        b = (-(m * xa) - (ya * -1))
        return (m, b)

    def mostrar_resultado(self, xa, ya, xb, yb):
        m ,b = self.calcular_Equacao_Geral(xa, ya, xb, yb)
        a = m
        equacaoY = ''
        equacaoX = ''
        if self.quantas_vezes_calculou > 0:
            self.Resultado.delete(0, 'end')
        if (a > 1):
            if (b < 0):
                equacaoY = f'Y = {a}X - {b * -1}'
            elif (b == 0):
                equacaoY = f'Y = {a}X'
            else:
                equacaoY = f'Y = {a}X + {b}'
        elif (a == 1):
            if (b < 0):
                equacaoY = f'Y =X - {b * -1}'
            elif (b == 0):
                equacaoY = 'Y = X'
            else:
                equacaoY = f'Y = X + {b}'
        self.Resultado.insert(0, equacaoY)
        #self.Resultado2.insert(0, equacaoX)
        self.Resultado.pack()
        #self.Resultado2.pack()
        self.quantas_vezes_calculou += 1

raiz = Tk()
Janela(raiz)
raiz.mainloop()