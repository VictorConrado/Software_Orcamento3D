

from tkinter import *
from tkinter import ttk

#cores

co0 = "#ffffff" #White
co1 = "#252422" #Black
co2 = "#eb5e28" #Orange

janela = Tk()
janela.title("Orçamento Impressão 3D")
janela.geometry("337x292")
janela.configure(bg=co0)

# divisão de janelas 

frame_cima= Frame(janela,width=330, height=50, bg=co0, pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo= Frame(janela,width=330, height=180, bg=co0, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)

#Frame cima

app_nome = Label(frame_cima, text='Impressão 3D', width=23, height=1, padx=0, relief='flat', anchor='center', font=('Montserrat 16 bold'), bg=co0, fg=co1)
app_nome.place(x=0,y=0)

app_linha = Label(frame_cima, text='', width=400, height=1, padx=0, relief='flat', anchor='center', font=('Montserrat 1'), bg=co1, fg=co1)
app_linha.place(x=0,y=35)

def calcular():
 MinutosdoProjeto = float(e_minutos.get())
 GramasdoProjeto = float(e_gramas.get())
 ConstanteLuz = float(0.21)
 ConstanteLucro = float(4.32)
 MaterialGramas = int(1000)
 MaterialReais = float(150.00)


#Variaveis

 Valor1 = MinutosdoProjeto * ConstanteLuz
 Valor2 = MinutosdoProjeto * ConstanteLucro
 Valor3 = GramasdoProjeto * MaterialReais / MaterialGramas +0.013
 Valor4 = Valor1+Valor2+Valor3

 l_resultado['text'] = "{:.{}f}".format(Valor4, 2)
 
 l_luz['text'] = "O valor de sua Luz é: {:.{}f}".format(Valor1, 2)
 l_lucro['text'] = "O valor de seu lucro é: {:.{}f}".format(Valor2, 2)
 l_material['text'] = "O valor de seu Material é: {:.{}f}".format(Valor3, 2)
 l_reais['text'] = "O valor em Reais é R$: {:.{}f}".format(Valor4, 2)

#Frame baixo
l_minutos = Label(frame_baixo, text='Insira os Minutos', height=1, padx=0, relief='flat', anchor='center', font=('Montserrat 10 bold'), bg=co0, fg=co1)
l_minutos.grid(row=0, column=0, sticky=NSEW, pady=10, padx=3)

e_minutos = Entry(frame_baixo, width= 5, relief='solid', font=('Montserrat 10 bold'), justify='center')
e_minutos.grid(row=0, column=1, sticky=NSEW, pady=10, padx=3)


l_gramas = Label(frame_baixo, text='Insira as Gramas', height=1, padx=0, relief='flat', anchor='center', font=('Montserrat 10 bold'), bg=co0, fg=co1)
l_gramas.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3)

e_gramas = Entry(frame_baixo, width= 5, relief='solid', font=('Montserrat 10 bold'), justify='center')
e_gramas.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3)

#bloco laranja

l_resultado = Label(frame_baixo, text='---',width=5, height=1, padx=6,pady=12, relief='flat', anchor='center', font=('Montserrat 20 bold'), bg=co2, fg=co1)
l_resultado.place(x=200,y=10)

#abaixo dos entrys e blocos

#Valor1
l_luz = Label(frame_baixo, text='O valor de sua Luz é:',width=37, height=1, padx=0,pady=0, relief='flat', anchor='center', font=('Montserrat 10 bold'), bg=co0, fg=co1)
l_luz.place(x=0,y=120)

#Valor2
l_lucro = Label(frame_baixo, text='O valor de seu Lucro é:',width=37, height=1, padx=0,pady=0, relief='flat', anchor='center', font=('Montserrat 10 bold'), bg=co0, fg=co1)
l_lucro.place(x=0,y=140)

#Valor3
l_material = Label(frame_baixo, text='O valor de seu Material é:',width=37, height=1, padx=0,pady=0, relief='flat', anchor='center', font=('Montserrat 10 bold'), bg=co0, fg=co1)
l_material.place(x=0,y=160)

#Valor4
l_reais = Label(frame_baixo, text='O valor total em R$ é:',width=37, height=1, padx=0,pady=0, relief='flat', anchor='center', font=('Montserrat 10 bold'), bg=co0, fg=co1)
l_reais.place(x=0,y=180)


b_calcular= Button(frame_baixo,command=calcular, text='Calcular',width=36, height=1,overrelief=SOLID,  relief='raised', anchor='center', font=('Montserrat 10 bold'), bg=co2, fg=co1)
b_calcular.grid(row=4, column=0, sticky=NSEW, pady=110, padx=1, columnspan=30)



janela.mainloop()