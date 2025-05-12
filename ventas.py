from tkinter import Frame, LabelFrame, Label, NSEW, NS, Scrollbar, W
from tkinter import messagebox
from tkinter import ttk
import ttkbootstrap as tb
import sqlite3

class Ventana(tb.Window):
    def __init__(self):
        super().__init__() # type: ignore
        self.ventana_login()

       
        
    
    def ventana_login(self):
        self.frame_login=Frame(self)
        self.frame_login.pack()

        self.lblframe_login=LabelFrame(self.frame_login, text='Acceso')
        self.lblframe_login.pack(padx=10, pady=10)

        lbltitulo=ttk.Label(self.lblframe_login, text='Inicio de sesión', font=('Arial',22))
        lbltitulo.pack(padx=10, pady=35)

        self.txt_usuario=ttk.Entry(self.lblframe_login, width=40,justify='center')
        self.txt_usuario.pack(padx=10,pady=10)
        self.txt_clave=ttk.Entry(self.lblframe_login, width=40, justify='center')
        self.txt_clave.pack(padx=10,pady=10)
        self.txt_clave.configure(show='*')
        btn_acceso=ttk.Button(self.lblframe_login, text='Log in', width=38, command=self.logueo)
        btn_acceso.pack(padx=10,pady=10)

    def ventana_menu(self):
        self.frame_left=Frame(self, width=200)
        self.frame_left.grid(row=0,column=0,sticky=NS)
        self.frame_center=Frame(self)
        self.frame_center.grid(row=0, column=1, sticky=NSEW)
        self.frame_rigth=Frame(self, width=400)
        self.frame_rigth.grid(row=0, column=2, sticky=NSEW)

        btn_productos=ttk.Button(self.frame_left, text='Productos', width=15)
        btn_productos.grid(row=0,column=0,padx=10,pady=10)
        btn_ventas=ttk.Button(self.frame_left, text='Ventas', width=15)
        btn_ventas.grid(row=1,column=0,padx=10,pady=10)
        btn_clientes=ttk.Button(self.frame_left, text='Clientes', width=15)
        btn_clientes.grid(row=2,column=0,padx=10,pady=10)
        btn_compras=ttk.Button(self.frame_left, text='Compras', width=15)
        btn_compras.grid(row=3,column=0,padx=10,pady=10)
        btn_usuarios=ttk.Button(self.frame_left, text='Usuarios', width=15, command=self.ventana_lista_usuarios)
        btn_usuarios.grid(row=4,column=0,padx=10,pady=10)
        btn_reportes=ttk.Button(self.frame_left, text='Reportes', width=15)
        btn_reportes.grid(row=5,column=0,padx=10,pady=10)
        btn_backup=ttk.Button(self.frame_left, text='Backup', width=15)
        btn_backup.grid(row=6,column=0,padx=10,pady=10)
        btn_restauradb=ttk.Button(self.frame_left, text='Restaurar DB', width=15)
        btn_restauradb.grid(row=7,column=0,padx=10,pady=10)

        

        lbl2=Label(self.frame_center,text='Aqui pondremos las ventanas que creemos')
        lbl2.grid(row=0,column=0,padx=10,pady=10)

        lbl3=Label(self.frame_rigth,text='Aqui pondremos las busquedas para la venta')
        lbl3.grid(row=0,column=0,padx=10,pady=10)
    
    def logueo(self):

        try:
            #Establecemos la conexion a la base de datos
            mi_conexion=sqlite3.connect("ventas.db")
            #Creamos un cursor para realizar operaciones en la base de datos
            mi_cursor=mi_conexion.cursor()
            
            nombre_usuario=self.txt_usuario.get()
            clave_usuario=self.txt_clave.get()

            mi_cursor.execute("SELECT * FROM usuarios WHERE nombre=? AND clave=?", (nombre_usuario, clave_usuario))
           
            datos_logueo=mi_cursor.fetchall()
            if datos_logueo != "":
                for row in datos_logueo:
                    cod_usu=row[0]
                    nom_usu=row[1]
                    cla_usu=row[2]
                    rol_usu=row[3]
                
                if nom_usu.strip() == self.txt_usuario.get().strip() and str(cla_usu) ==self.txt_clave.get():
                    self.frame_login.pack_forget()
                    self.ventana_menu()
                else:
                    messagebox.showerror("Acceso", "El usuario o la clave son incorrectos")
            # Aplicamos cambios y cerramos la conexion
            mi_conexion.commit()
            mi_conexion.close()
        except Exception as e:
            print("Error:", e)  # Muestra el error en consola
            messagebox.showerror("Acceso", f"Error en el login: {e}")


        

    def  ventana_lista_usuarios(self):
        self.frame_lista_usuarios=Frame(self.frame_center)
        self.frame_lista_usuarios.grid(row=0,column=0, columnspan=2,sticky=NSEW)

        self.lblframe_botones_listusu=LabelFrame(self.frame_lista_usuarios)
        self.lblframe_botones_listusu.grid(row=0,column=0, padx=10, pady=10,sticky=NSEW)

        btn_nuevo_usuario=tb.Button(self.lblframe_botones_listusu, text='Nuevo usuario', width=15, bootstyle='success')
        btn_nuevo_usuario.grid(row=0,column=0,padx=5,pady=5)
        btn_modificar_usuario=tb.Button(self.lblframe_botones_listusu, text='Modificar usuario', width=15,bootstyle='warning')
        btn_modificar_usuario.grid(row=0,column=1,padx=5,pady=5)
        btn_eliminar_usuario=tb.Button(self.lblframe_botones_listusu, text='Eliminar usuario', width=15, bootstyle='danger')
        btn_eliminar_usuario.grid(row=0,column=2,padx=5,pady=5)

        self.lblframe_busqueda_listusu=LabelFrame(self.frame_lista_usuarios)
        self.lblframe_busqueda_listusu.grid(row=1,column=0, padx=10, pady=10,sticky=NSEW)

        txt_busqueda_usuario=ttk.Entry(self.lblframe_busqueda_listusu, width=96)
        txt_busqueda_usuario.grid(row=0,column=0,padx=5,pady=5)


        self.lblframe_tree_listusu=LabelFrame(self.frame_lista_usuarios)
        self.lblframe_tree_listusu.grid(row=2,column=0, padx=10, pady=10,sticky=NSEW)
        
        columnas=("codigo","nombre", "clave", "rol")
        self.tree_lista_usuarios=tb.Treeview(self.lblframe_tree_listusu, columns=columnas, height=17, show='headings', bootstyle='dark')
        self.tree_lista_usuarios.grid(row=0,column=0)

        self.tree_lista_usuarios.heading("codigo", text="Codigo", anchor=W)
        self.tree_lista_usuarios.heading("nombre", text="Nombre", anchor=W)
        self.tree_lista_usuarios.heading("clave", text="Clave", anchor=W)
        self.tree_lista_usuarios.heading("rol", text="Rol", anchor=W)
        self.tree_lista_usuarios['displaycolumns']=("codigo","nombre", "rol")

        tree_scroll_listausu=tb.Scrollbar(self.frame_lista_usuarios, bootstyle='round-success')
        tree_scroll_listausu.grid(row=2,column=1)
        tree_scroll_listausu.config(command=self.tree_lista_usuarios.yview)

        #llamamos a la funcion que muestra los usuarios
        self.mostrar_usuarios()

    def mostrar_usuarios(self):
        
        try:
            #Establecemos la conexion a la base de datos
            mi_conexion=sqlite3.connect("ventas.db")
            #Creamos un cursor para realizar operaciones en la base de datos
            mi_cursor=mi_conexion.cursor()
            #Eliminamos los registros que ya existen en el treeview
            registros=self.tree_lista_usuarios.get_children()

            #Recorremos los registros y los eliminamos
            for elementos in registros:
                self.tree_lista_usuarios.delete(elementos)
                
            #Realizamos la consulta a la base de datos
            mi_cursor.execute("SELECT * FROM usuarios")
            #Guardamos los resultados en una variable
            datos=mi_cursor.fetchall()

            for row in datos:
                self.tree_lista_usuarios.insert("",0,text=row[0], values=(row[0],row[1],row[2],row[3]))

            # Aplicamos cambios y cerramos la conexion
            mi_conexion.commit()
            mi_conexion.close()
        except:
            
            messagebox.showerror("Lista de usuario", "No se pudo conectar a la base de datos")


def main():
    app=Ventana()
    app.title("Sistema de ventas")
    app.state("zoomed")
    tb.Style("superhero")
    app.mainloop()

if __name__=="__main__":
    main()