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
        txt_clave.configure(show='*')
        btn_acceso=ttk.Button(self.lblframe_login, text='Log in', width=38, command=self.logueo)
        btn_acceso.pack(padx=10,pady=10)

    def ventana_menu(self):
        self.frame_left=Frame(self, width=200)
        self.frame_left.grid(row=0,column=0,sticky=NS)
        self.frame_center=Frame(self)
        self.frame_center.grid(row=0, column=1, sticky=NSEW)
        self.frame_rigth=Frame(self, width=400)
        self.frame_rigth.grid(row=0, column=2, sticky=NSEW)

        lbl1=Label(self.frame_left,text='Aqui pondremos los botones del menú')
        lbl1.grid(row=0,column=0,padx=10,pady=10)

        lbl2=Label(self.frame_center,text='Aqui pondremos las ventanas que creemos')
        lbl2.grid(row=0,column=0,padx=10,pady=10)

        lbl3=Label(self.frame_rigth,text='Aqui pondremos las busquedas para la venta')
        lbl3.grid(row=0,column=0,padx=10,pady=10)
    
    def logueo(self):
        self.frame_login.pack_forget()
        self.ventana_menu()

def main():
    app=Ventana()
    app.title("Sistema de ventas")
    app.state("zoomed")
    tb.Style("superhero")
    app.mainloop()

if __name__=="__main__":
    main()