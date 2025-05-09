from tkinter import *
from tkinter import ttk
import ttkbootstrap as tb

class Ventana(tb.Window):
    def __init__(self):
        super().__init__()
        self.ventana_login()
    
    def ventana_login(self):
        self.frame_login=Frame(self)
        self.frame_login.pack()

        self.lblframe_login=LabelFrame(self.frame_login, text='Acceso')
        self.lblframe_login.pack(padx=10, pady=10)

        lbltitulo=ttk.Label(self.lblframe_login, text='Inicio de sesión', font=('Arial',22))
        lbltitulo.pack(padx=10, pady=35)

        txt_usuario=ttk.Entry(self.lblframe_login, width='40',justify='center')
        txt_usuario.pack(padx=10,pady=10)
        txt_clave=ttk.Entry(self.lblframe_login, width='40', justify='center')
        txt_clave.pack(padx=10,pady=10)
        btn_acceso=ttk.Button(self.lblframe_login, text='Log in', width='38')
        btn_acceso.pack(padx=10,pady=10)


def main():
    app=Ventana()
    app.title("Sistema de ventas")
    app.state("zoomed")
    tb.Style("superhero")
    app.mainloop()

if __name__=="__main__":
    main()