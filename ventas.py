from tkinter import Frame, LabelFrame, Label, NSEW, NS, messagebox, Toplevel, W, Entry
from tkinter import ttk
import ttkbootstrap as tb  # type: ignore
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
            if datos_logueo:
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

        btn_nuevo_usuario=tb.Button(self.lblframe_botones_listusu, text='Nuevo usuario', width=15, command=self.ventana_nuevo_usuario, style='success')
        btn_nuevo_usuario.grid(row=0,column=0,padx=5,pady=5)
        btn_modificar_usuario=tb.Button(self.lblframe_botones_listusu, text='Modificar usuario', width=15,style='warning', command=self.ventana_modificar_usuario)
        btn_modificar_usuario.grid(row=0,column=1,padx=5,pady=5)
        btn_eliminar_usuario=tb.Button(self.lblframe_botones_listusu, text='Eliminar usuario', width=15, style='danger')
        btn_eliminar_usuario.grid(row=0,column=2,padx=5,pady=5)

        self.lblframe_busqueda_listusu=LabelFrame(self.frame_lista_usuarios)
        self.lblframe_busqueda_listusu.grid(row=1,column=0, padx=10, pady=10,sticky=NSEW)

        self.txt_busqueda_usuario=ttk.Entry(self.lblframe_busqueda_listusu, width=96)
        self.txt_busqueda_usuario.grid(row=0,column=0,padx=5,pady=5)
        self.txt_busqueda_usuario.bind('<Key>', self.buscar_usuarios)


        self.lblframe_tree_listusu=LabelFrame(self.frame_lista_usuarios)
        self.lblframe_tree_listusu.grid(row=2,column=0, padx=10, pady=10,sticky=NSEW)
        
        columnas=("codigo","nombre", "clave", "rol")
        self.tree_lista_usuarios=tb.Treeview(self.lblframe_tree_listusu, columns=columnas, height=17, show='headings', style='dark')
        self.tree_lista_usuarios.grid(row=0,column=0)

        self.tree_lista_usuarios.heading("codigo", text="Codigo", anchor=W)
        self.tree_lista_usuarios.heading("nombre", text="Nombre", anchor=W)
        self.tree_lista_usuarios.heading("clave", text="Clave", anchor=W)
        self.tree_lista_usuarios.heading("rol", text="Rol", anchor=W)
        self.tree_lista_usuarios['displaycolumns']=("codigo","nombre", "rol")

        tree_scroll_listausu=tb.Scrollbar(self.frame_lista_usuarios, style='round-success')
        tree_scroll_listausu.grid(row=2,column=1)
        tree_scroll_listausu.config(command=self.tree_lista_usuarios.yview)

        # we call the function to show the users
        self.mostrar_usuarios()

    def mostrar_usuarios(self):
        
        try:
            # we establish the connection to the database
            mi_conexion=sqlite3.connect("ventas.db")
            # We create a cursor to perform operations on the database
            mi_cursor=mi_conexion.cursor()
            # We delete the records from the treeview
            registros=self.tree_lista_usuarios.get_children()

            #we iterate over the records and delete them
            for elementos in registros:
                self.tree_lista_usuarios.delete(elementos)
                
            # We perform the database query
            mi_cursor.execute("SELECT * FROM usuarios")
            # Save the data in a  variable
            datos=mi_cursor.fetchall()

            for row in datos:
                self.tree_lista_usuarios.insert("",0,text=row[0], values=(row[0],row[1],row[2],row[3]))

            # apply changes and close the connection
            mi_conexion.commit()
            mi_conexion.close()
        except:
            
            messagebox.showerror("User list", "error to show the user list")

    def ventana_nuevo_usuario(self):

        self.frame_nuevo_usuario=Toplevel(self) # window above the user list
        self.frame_nuevo_usuario.title("Nuevo usuario") #Title of the window
        self.centrar_ventana_nuevo_usuario(400,400) # size of the window
        self.frame_nuevo_usuario.resizable(0,0) # we do not want to resize the window
        self.frame_nuevo_usuario.grab_set() # so that it does not allow any other accion until the window is closed

        lblframe_nuevo_usuario=LabelFrame(self.frame_nuevo_usuario)
        lblframe_nuevo_usuario.grid(row=0,column=0,padx=10,pady=10,sticky=NSEW)

        lbl_codigo_nuevo_usuario=Label(lblframe_nuevo_usuario, text="Codigo")
        lbl_codigo_nuevo_usuario.grid(row=0,column=0,padx=10,pady=10)
        self.txt_codigo_nuevo_usuario=ttk.Entry(lblframe_nuevo_usuario, width=40)
        self.txt_codigo_nuevo_usuario.grid(row=0,column=1,padx=10,pady=10)
        
        lbl_nombre_nuevo_usuario=Label(lblframe_nuevo_usuario, text="Nombre")
        lbl_nombre_nuevo_usuario.grid(row=1,column=0,padx=10,pady=10)
        self.txt_nombre_nuevo_usuario=ttk.Entry(lblframe_nuevo_usuario, width=40)
        self.txt_nombre_nuevo_usuario.grid(row=1,column=1,padx=10,pady=10)

        lbl_clave_nuevo_usuario=Label(lblframe_nuevo_usuario, text="Clave")
        lbl_clave_nuevo_usuario.grid(row=2,column=0,padx=10,pady=10)
        self.txt_clave_nuevo_usuario=ttk.Entry(lblframe_nuevo_usuario, width=40)
        self.txt_clave_nuevo_usuario.grid(row=2,column=1,padx=10,pady=10)

        lbl_rol_nuevo_usuario=Label(lblframe_nuevo_usuario, text="Rol")
        lbl_rol_nuevo_usuario.grid(row=3,column=0,padx=10,pady=10)
        self.txt_rol_nuevo_usuario=ttk.Combobox(lblframe_nuevo_usuario, width=38, values=("Administrador", "Vendedor", "Bodega"), state="readonly")
        self.txt_rol_nuevo_usuario.grid(row=3,column=1,padx=10,pady=10)
        self.txt_rol_nuevo_usuario.current(0) # set the default value to "Administrador"

        btn_guardar_nuevo_usuario=ttk.Button(lblframe_nuevo_usuario, text="Guardar", width=38,style='success', command=self.guardar_usuario)
        btn_guardar_nuevo_usuario.grid(row=4,column=1,padx=10,pady=10)

        self.ultimo_usuario()

    def guardar_usuario(self):
        if self.txt_codigo_nuevo_usuario.get()=="" or self.txt_nombre_nuevo_usuario.get()=="" or self.txt_clave_nuevo_usuario.get()=="" or self.txt_rol_nuevo_usuario.get()=="":
            messagebox.showwarning("Guardando usuarios", "Rellene todos los campos")
            return
        try:
            mi_conexion=sqlite3.connect("ventas.db")
            mi_cursor=mi_conexion.cursor()

            datos_guardar_usuario=self.txt_codigo_nuevo_usuario.get(), self.txt_nombre_nuevo_usuario.get(), self.txt_clave_nuevo_usuario.get(), self.txt_rol_nuevo_usuario.get()
            mi_cursor.execute("INSERT INTO usuarios VALUES(?,?,?,?)", datos_guardar_usuario)
            messagebox.showinfo("Guardando usuarios", "Usuario guardado correctamente")

            mi_conexion.commit()
            self.frame_nuevo_usuario.destroy() # close the window
            self.mostrar_usuarios() # refresh the user list
            mi_conexion.close()
        except:
            messagebox.showerror("Guardando usuarios", "Error al guardar el usuario")

    def ultimo_usuario(self):
        try:
            mi_conexion=sqlite3.connect("ventas.db")
            mi_cursor=mi_conexion.cursor()

            mi_cursor.execute("SELECT MAX(codigo) FROM usuarios")
            datos=mi_cursor.fetchone()

            for codusu in datos:
                if codusu==None:
                    self.ultusu=(int(1))
                    self.txt_codigo_nuevo_usuario.config(state="normal")
                    self.txt_codigo_nuevo_usuario.insert(0,str(self.ultusu))
                    self.txt_codigo_nuevo_usuario.config(state="readonly")
                    break
                if codusu=="":
                    self.ultusu=(int(1))
                    self.txt_codigo_nuevo_usuario.config(state="normal")
                    self.txt_codigo_nuevo_usuario.insert(0,str(self.ultusu))
                    self.txt_codigo_nuevo_usuario.config(state="readonly")
                    break
                else:
                    self.ultusu=(int(codusu)+1)
                    self.txt_codigo_nuevo_usuario.config(state="normal")
                    self.txt_codigo_nuevo_usuario.insert(0,str(self.ultusu))
                    self.txt_codigo_nuevo_usuario.config(state="readonly")
                    break

            mi_conexion.commit()
            mi_conexion.close()       
        except:
            messagebox.showerror("Guardando usuarios", "Error al guardar el usuario")           

    def centrar_ventana_nuevo_usuario(self,ancho,alto):
        ventana_ancho=ancho
        ventana_alto=alto
        pantalla_ancho=self.winfo_screenwidth()
        pantalla_alto=self.winfo_screenheight()
        coordenadas_x=int((pantalla_ancho/2)-(ventana_ancho/2))
        coordenadas_y=int((pantalla_alto/2)-(ventana_alto/2))
        self.frame_nuevo_usuario.geometry("{}x{}+{}+{}".format(ventana_ancho, ventana_alto, coordenadas_x, coordenadas_y))
        
    def buscar_usuarios(self, event):
        try:
            mi_conexion=sqlite3.connect("ventas.db")
            mi_cursor=mi_conexion.cursor()

            registros=self.tree_lista_usuarios.get_children()
            for elementos in registros:
                self.tree_lista_usuarios.delete(elementos)
            
            mi_cursor.execute("SELECT * FROM usuarios WHERE nombre LIKE ?", (self.txt_busqueda_usuario.get()+'%',))

            datos=mi_cursor.fetchall()

            for row in datos:
                self.tree_lista_usuarios.insert("",0,text=row[0], values=(row[0],row[1],row[2],row[3]))

            mi_conexion.commit()
            mi_conexion.close()
        except:
            messagebox.showerror("Buscando usuarios", "Error al buscar el usuario")

    def ventana_modificar_usuario(self):

        self.usuario_seleccionado=self.tree_lista_usuarios.focus() # get the selected user

        self.val_mod_usu=self.tree_lista_usuarios.item(self.usuario_seleccionado, 'values') # get the selected user

        if self.val_mod_usu!="":

            self.frame_modificar_usuario=Toplevel(self) # window above the user list
            self.frame_modificar_usuario.title("modificar usuario") #Title of the window
            self.frame_modificar_usuario.geometry("400x400") # size of the window
            #self.centrar_ventana_modificar_usuario(400,400) # size of the window
            self.frame_modificar_usuario.resizable(0,0) # we do not want to resize the window
            self.frame_modificar_usuario.grab_set() # so that it does not allow any other accion until the window is closed

            lblframe_modificar_usuario=LabelFrame(self.frame_modificar_usuario)
            lblframe_modificar_usuario.grid(row=0,column=0,padx=10,pady=10,sticky=NSEW)

            lbl_codigo_modificar_usuario=Label(lblframe_modificar_usuario, text="Codigo")
            lbl_codigo_modificar_usuario.grid(row=0,column=0,padx=10,pady=10)
            self.txt_codigo_modificar_usuario=ttk.Entry(lblframe_modificar_usuario, width=40)
            self.txt_codigo_modificar_usuario.grid(row=0,column=1,padx=10,pady=10)
            
            lbl_nombre_modificar_usuario=Label(lblframe_modificar_usuario, text="Nombre")
            lbl_nombre_modificar_usuario.grid(row=1,column=0,padx=10,pady=10)
            self.txt_nombre_modificar_usuario=ttk.Entry(lblframe_modificar_usuario, width=40)
            self.txt_nombre_modificar_usuario.grid(row=1,column=1,padx=10,pady=10)

            lbl_clave_modificar_usuario=Label(lblframe_modificar_usuario, text="Clave")
            lbl_clave_modificar_usuario.grid(row=2,column=0,padx=10,pady=10)
            self.txt_clave_modificar_usuario=ttk.Entry(lblframe_modificar_usuario, width=40)
            self.txt_clave_modificar_usuario.grid(row=2,column=1,padx=10,pady=10)

            lbl_rol_modificar_usuario=Label(lblframe_modificar_usuario, text="Rol")
            lbl_rol_modificar_usuario.grid(row=3,column=0,padx=10,pady=10)
            self.txt_rol_modificar_usuario=ttk.Combobox(lblframe_modificar_usuario, width=38, values=("Administrador", "Vendedor", "Bodega"))
            self.txt_rol_modificar_usuario.grid(row=3,column=1,padx=10,pady=10)
            

            btn_modificar_usuario=ttk.Button(lblframe_modificar_usuario, text="Modificar", width=38,style='warning',command=self.modificar_usuario)
            btn_modificar_usuario.grid(row=4,column=1,padx=10,pady=10)
            self.llenar_entrys_modificar_usuario()

            self.txt_nombre_modificar_usuario.focus()

    def llenar_entrys_modificar_usuario(self):
        # clear the entrys
        self.txt_codigo_modificar_usuario.delete(0, 'end')
        self.txt_nombre_modificar_usuario.delete(0, 'end')  
        self.txt_clave_modificar_usuario.delete(0, 'end')
        self.txt_rol_modificar_usuario.delete(0, 'end')
        # fill the entrys with the selected user data
        self.txt_codigo_modificar_usuario.insert(0, self.val_mod_usu[0])
        self.txt_codigo_modificar_usuario.config(state="readonly")
        self.txt_nombre_modificar_usuario.insert(0, self.val_mod_usu[1])
        self.txt_clave_modificar_usuario.insert(0, self.val_mod_usu[2])
        self.txt_rol_modificar_usuario.insert(0, self.val_mod_usu[3])
        self.txt_rol_modificar_usuario.config(state="readonly")

    def modificar_usuario(self):
        if self.txt_codigo_modificar_usuario.get()=="" or self.txt_nombre_modificar_usuario.get()=="" or self.txt_clave_modificar_usuario.get()=="" or self.txt_rol_modificar_usuario.get()=="":
            messagebox.showwarning("Modificar usuario", "Rellene todos los campos")
            return
        try:
            mi_conexion=sqlite3.connect("ventas.db")
            mi_cursor=mi_conexion.cursor()
            print("hola")

            datos_modificar_usuario= self.txt_nombre_modificar_usuario.get(), self.txt_clave_modificar_usuario.get(), self.txt_rol_modificar_usuario.get()
            
            mi_cursor.execute("UPDATE usuarios SET nombre=?, clave=?, rol=? WHERE codigo="+self.txt_codigo_modificar_usuario.get(),(datos_modificar_usuario))
            messagebox.showinfo("Modificar usuarios", "Usuario modificado correctamente")

            mi_conexion.commit()
            self.val_mod_usu=self.tree_lista_usuarios.item(self.usuario_seleccionado,text='', values=(self.txt_codigo_modificar_usuario.get(), self.txt_nombre_modificar_usuario.get(), self.txt_clave_modificar_usuario.get(), self.txt_rol_modificar_usuario.get(),))
            self.frame_modificar_usuario.destroy() # close the window
            self.ventana_lista_usuarios() # refresh the user list
            mi_conexion.close()
        except Exception as e:
            messagebox.showerror("Modificar usuarios", f"Error al modificar el usuario: {e}")
            # messagebox.showerror("Guardando usuarios", "Error al actualizar el usuario")
        

def main():
    app=Ventana()
    app.title("Sistema de ventas")
    app.state("zoomed")
    tb.Style("superhero")
    app.mainloop()

if __name__=="__main__":
    main()