#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 11:59:37 2020

@author: lino
"""




###############################################################################
#000000000000000000000000000000000000000000000000000000000000000000000000000000
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
###############################################################################

#                            PyZHAireS 3_20w22a

###############################################################################
#000000000000000000000000000000000000000000000000000000000000000000000000000000
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
###############################################################################



import os

# Por si acaso el usuario no tiene instalado alguno de los siguientes módulos, checkeamos si los tiene y en caso contrario los instalamos:


try:
    import tkinter
except ImportError:
    instruccion = "echo {} | iconv -f utf8 -t eucjp | pip install tkinter" # Meto el comando como cuando lo hago en la consola
    os.system(instruccion)

try:
    import time
except ImportError:
    instruccion = "echo {} | iconv -f utf8 -t eucjp | pip install time" # Meto el comando como cuando lo hago en la consola
    os.system(instruccion)

try:
    import getpass
except ImportError:
    instruccion = "echo {} | iconv -f utf8 -t eucjp | pip install getpass" # Meto el comando como cuando lo hago en la consola
    os.system(instruccion)


try:
    import shutil
except ImportError:
    instruccion = "echo {} | iconv -f utf8 -t eucjp | pip install shutil" # Meto el comando como cuando lo hago en la consola
    os.system(instruccion)

try:
    import numpy
except ImportError:
    instruccion = "echo {} | iconv -f utf8 -t eucjp | pip install numpy" # Meto el comando como cuando lo hago en la consola
    os.system(instruccion)

try:
    import matplotlib
except ImportError:
    instruccion = "echo {} | iconv -f utf8 -t eucjp | pip install matplotlib" # Meto el comando como cuando lo hago en la consola
    os.system(instruccion)

try:
    import PIL
except ImportError:
    instruccion = "echo {} | iconv -f utf8 -t eucjp | pip install PIL" # Meto el comando como cuando lo hago en la consola
    os.system(instruccion)


# Ahora que deberían estar todos listos, los importo "a mi manera"

from tkinter import *
from tkinter import ttk
from tkinter import font
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image
from tkinter.filedialog import askopenfilename # Para abrir interfaz de búsqueda de archivos ("examinar")
from tkinter.filedialog import *
from tkinter import messagebox # Para abrir cuadros de diálogo al cerrar una ventana
import sys



from matplotlib.patches import Ellipse
from array import array
import ROOT



# Directorio donde tenemos alojada la app
directorio_de_PyZHAireS = os.path.dirname(__file__)

# Directorio donde tenemos alojadas las imágenes que muestra la app
ruta_de_imagenes = os.path.join(directorio_de_PyZHAireS,'Imagenes_de_PyZHAireS')



# Creo una lista con todos los colores de la librería matplotlib

Lista_de_colores=['black','red','navy','darkgreen','gray','saddlebrown','turquoise','olive','fuchsia','dodgerblue','lime','orange','indigo','gold']
Lista_de_Rutas=[]
Lista_de_leyendas=[]

DEBUG=0 # Un debug que creo para testear



def restart_program():
    print()
    #python = sys.executable
    #os.execl(python, python, * sys.argv)




class Aplicacion():  # Creamos la aplicación
    
    
    print()
    print('%%%%%%%%%%%%%%%%%%%%%%%%%')
    print('  Abriendo aplicación')
    print('%%%%%%%%%%%%%%%%%%%%%%%%%')
    print()
    
    global DEBUG

    DEBUG+=1
    print('DEBUG: ',DEBUG)
    
    def __init__(self): # Definimos todas las vainas con las que opera la app
        
        
        self.primera_ventana = Tk() # Creamos la ventana de bienvenida
        
        
        if ( sys.platform.startswith('win')): # Defino el icono de la ventana por si es windows o linux el S.O.
            try:
                Ruta_logo=os.path.join(ruta_de_imagenes,'PRUEBA_ICONOS.ICO')
                logo = PhotoImage(file=Ruta_logo)
                self.primera_ventana.call('wm', 'iconphoto', self.primera_ventana._w, logo)        
            except:
                pass
        else:
            try:
                Ruta_logo=os.path.join(ruta_de_imagenes,'PRUEBA_ICONOS.xbm')
                logo = PhotoImage(file=Ruta_logo)
                self.primera_ventana.call('wm', 'iconphoto', self.primera_ventana._w, logo)        
            except:
                pass
        
        
        
        
        def on_closing(): # Defino el mensaje para cerrar la aplicación
            if messagebox.askokcancel("Quit", "Seguro que desexas pechar a aplicación?"):
                self.primera_ventana.destroy()

        self.primera_ventana.protocol("WM_DELETE_WINDOW", on_closing)

        
        
        
        self.primera_ventana.geometry("600x540") # Tamaño de la ventana
        
        self.primera_ventana.resizable(0,0) # Esta instrucción es para impedir que la ventana se pueda modificar de tamaño (rollo maximizar y así), '0' es equivalente a poner False. A su vez, poner un '1' equivale a un True.
        
        self.primera_ventana.title('PyZHAireS v.2.3')
        
        self.fuente_del_titulo = font.Font(family="Times New Roman",size=36,weight='bold') # Defino un tipo de fuente que empleo después para escribir el título
   
        self.Titulo=ttk.Label(self.primera_ventana,text='PyZHAireS v.2.3',font=self.fuente_del_titulo)                                        
        self.Titulo.place(x=50,y=372)     
        
        

                
        Imagen_portada = PhotoImage(file=os.path.join(ruta_de_imagenes,'portadeixon_root_boceto_2.png'),width = 650, height = 350) # Invoco la imagen de la portada
        self.Imagen_portada = ttk.Label(self.primera_ventana, image=Imagen_portada, anchor='center')  # Creo el widget de la imagen com una etiqueta simple pero con imagen
        self.Imagen_portada.pack(side=TOP, fill=BOTH, expand=True, padx=600, pady=100)          
        self.Imagen_portada.place(x=95,y=10) # Dónde la pongo dentro de la ventana
        
    
        Help = PhotoImage(file=os.path.join(ruta_de_imagenes,'help.png'),width = 65, height = 80)           
        self.Ayuda = ttk.Button(self.primera_ventana , image = Help, compound="top", padding=(-10,-20),command=self.ayuda)        
        self.Ayuda.pack(side=TOP, fill=BOTH, expand=True, padx=1000, pady=5000)          
        self.Ayuda.place(x=400,y=420)
        # Definimos hacia el final lo que hace



    
        # Defino el resto de widgets que pondré en la ventana
        
        self.raya1 = ttk.Separator(self.primera_ventana, orient=HORIZONTAL)
        self.raya1.place(x=5, y=490, bordermode=OUTSIDE,height=10, width=590)
            
        self.pie1 = ttk.Label(self.primera_ventana,text='Facultade de Física de Santiago de Compostela')
        self.pie1.place(x=5,y=495)
            
        self.pie2 = ttk.Label(self.primera_ventana,text='Técnicas de análise e simulación en física nuclear e de partículas')
        self.pie2.place(x=5,y=515)
            
        self.pie3 = ttk.Label(self.primera_ventana,text='PyZHAireS v.2.3')
        self.pie3.place(x=470,y=495)


        self.acceso = ttk.Button(self.primera_ventana, text="Acceso", padding=(100,22),command=self.aceptar) # El evento asociado al comando 'self.acceder' lo defino después del bucle de esta ventana y con una tabulación hacia la izquierda


        self.acceso.place(x=120,y=420)
        
        self.primera_ventana.mainloop() # Fin del bucle de la ventana de bienvenida
        
        
    
    
    #------------------------------------------------------------------------------
    
            
    
    def aceptar(self): 
        '''
        try:
            self.primera_ventana.destroy()
        except:
            pass
        '''
        
        global DEBUG
        
        
        if DEBUG>=3:
            
            
            try:
                self.segunda_ventana.destroy()
                self.lectura_o_escritura.deiconify() # Para cuando le damos a la opción de cambiar módulo, que vuelva a aparecer la ventana
            except:
                self.lectura_o_escritura= Tk() # Creo la ventana principal
                
                # Define la dimensión de la ventana
                    
                self.lectura_o_escritura.geometry("610x500")
        
        
                def on_closing(): # Defino el mensaje para cerrar la aplicación
                    if messagebox.askokcancel("Quit", "Seguro que desexas pechar a aplicación?"):
                        self.lectura_o_escritura.destroy()

                self.lectura_o_escritura.protocol("WM_DELETE_WINDOW", on_closing)
        
        
                DEBUG+=1
                print('DEBUG: ',DEBUG)
        
        
                if ( sys.platform.startswith('win')): # Defino el icono de la ventana por si es windows o linux el S.O.
                    try:
                        Ruta_logo=os.path.join(ruta_de_imagenes,'PRUEBA_ICONOS.ICO')
                        logo = PhotoImage(file=Ruta_logo)
                        self.lectura_o_escritura.call('wm', 'iconphoto', self.lectura_o_escritura._w, logo)        
                    except:
                        pass
                else:
                    try:
                        Ruta_logo=os.path.join(ruta_de_imagenes,'PRUEBA_ICONOS.xbm')
                        logo = PhotoImage(file=Ruta_logo)
                        self.lectura_o_escritura.call('wm', 'iconphoto', self.lectura_o_escritura._w, logo)        
                    except:
                        pass
        
        
        
        
                # Establece que no se pueda cambiar el tamaño de la
                # ventana
        
                self.lectura_o_escritura.resizable(0,0) # Me gusta más que quede sin poder maximizar
                self.lectura_o_escritura.title("PyZHAireS v.2.3")
                self.fuente_en_negrita = font.Font(weight='bold')   
            
                self.barrita = ttk.Separator(self.lectura_o_escritura, orient=HORIZONTAL)
                self.barrita.place(x=5,y=60,bordermode=OUTSIDE,height=10, width=590)
            
            
            
            
            
                self.fuente_de_bienvenida = font.Font(family="Arial",size=22,weight='bold')
                #self.fuente_de_bienvenida.config(size=30)
            
                self.Benvido = ttk.Label(self.lectura_o_escritura, text="Escolle o modo a empregar: ", font=self.fuente_de_bienvenida)
                self.Benvido.place(x=30, y=80)
                self.Benvido.config(foreground='blue')

            
                self.fuente_de_modulos= font.Font(family="Arial",size=12,weight='bold')
                
                Escritura = PhotoImage(file=os.path.join(ruta_de_imagenes,'Escritura.png'),width = 400, height = 300)           
                self.Escritura = ttk.Button(self.lectura_o_escritura, image=Escritura,compound="top", padding=(-70,-60),command=self.SIMULAR)        
                self.Escritura.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)          
                self.Escritura.place(x=30,y=120)
            
                Lectura = PhotoImage(file=os.path.join(ruta_de_imagenes,'Lectura.png'),width = 400, height = 300)           
                self.Lectura = ttk.Button(self.lectura_o_escritura, image=Lectura,compound="top", padding=(-80,-60),command=self.LECTURAS)        
                self.Lectura.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)          
                self.Lectura.place(x=345,y=120)
            
            
                self.sim = ttk.Label(self.lectura_o_escritura,text='Módulo de simulación',font=self.fuente_de_modulos)
                self.sim.place(x=62,y=330)
                self.sim.config(foreground='navy')
                
                self.lec = ttk.Label(self.lectura_o_escritura,text='Módulo de lectura',font=self.fuente_de_modulos)
                self.lec.place(x=370,y=330)
                self.lec.config(foreground='navy')

            
                self.etiqueta_explicativa3 = ttk.Label(self.lectura_o_escritura,text='Nota: En caso de dúbida de emprego consúltese o manual')
                self.etiqueta_explicativa3.place(x=30,y=390)
            
            
                self.barrita_vertical = ttk.Separator(self.lectura_o_escritura, orient=VERTICAL)
                self.barrita_vertical.place(x=317,y=120,bordermode=INSIDE,height=230, width=10)
         
                        
                self.fecha = ttk.Label(self.lectura_o_escritura,text='Inicio de sesión: '+ str(time.localtime()[2]) + '/' + str(time.localtime()[1]) + '/' + str(time.localtime()[0]) +'  ' + str(time.localtime()[3]) + ':' + str(time.localtime()[4]) + ':' + str(time.localtime()[5]))
                self.fecha.place(x=345,y=20)
            
                self.raya1 = ttk.Separator(self.lectura_o_escritura, orient=HORIZONTAL)
                self.raya1.place(x=5, y=435, bordermode=OUTSIDE,height=10, width=590)
            
                self.pie1 = ttk.Label(self.lectura_o_escritura,text='Facultade de Física de Santiago de Compostela')
                self.pie1.place(x=5,y=440)
            
                self.pie2 = ttk.Label(self.lectura_o_escritura,text='Técnicas de análise e simulación en física nuclear e de partículas')
                self.pie2.place(x=5,y=460)
            
                self.pie3 = ttk.Label(self.lectura_o_escritura,text='PyZHAireS v.2.3')
                self.pie3.place(x=470,y=440)
            
            
            
                self.lectura_o_escritura.mainloop() # Fin del bucle de la ventana principal de menú
        
        

        
        try: # Si es la primera vez que accedemos a la ventana:
            
            self.primera_ventana.destroy()
            self.lectura_o_escritura= Tk() # Creo la ventana principal
                
            # Define la dimensión de la ventana
                
            self.lectura_o_escritura.geometry("610x500")
    
            def on_closing(): # Defino el mensaje para cerrar la aplicación
                if messagebox.askokcancel("Quit", "Seguro que desexas pechar a aplicación?"):
                    self.lectura_o_escritura.destroy()

            self.lectura_o_escritura.protocol("WM_DELETE_WINDOW", on_closing)
    
    
    
            DEBUG+=1
            print('DEBUG: ',DEBUG)
    
    
    
    
            if ( sys.platform.startswith('win')): # Defino el icono de la ventana por si es windows o linux el S.O.
                try:
                    Ruta_logo=os.path.join(ruta_de_imagenes,'PRUEBA_ICONOS.ICO')
                    logo = PhotoImage(file=Ruta_logo)
                    self.lectura_o_escritura.call('wm', 'iconphoto', self.lectura_o_escritura._w, logo)        
                except:
                    pass
            else:
                try:
                    Ruta_logo=os.path.join(ruta_de_imagenes,'PRUEBA_ICONOS.xbm')
                    logo = PhotoImage(file=Ruta_logo)
                    self.lectura_o_escritura.call('wm', 'iconphoto', self.lectura_o_escritura._w, logo)        
                except:
                    pass
    

    
            # Establece que sí se pueda cambiar el tamaño de la
            # ventana
    
            self.lectura_o_escritura.resizable(0,0) # Me gusta más que quede sin poder maximizar
            self.lectura_o_escritura.title("PyZHAireS v.2.3")
            self.fuente_en_negrita = font.Font(weight='bold')   
        
            self.barrita = ttk.Separator(self.lectura_o_escritura, orient=HORIZONTAL)
            self.barrita.place(x=5,y=60,bordermode=OUTSIDE,height=10, width=590)
        
        
        
            self.boton_restart = ttk.Button(self.lectura_o_escritura,text='RESTART',padding=(5,5),command=restart_program)
            self.boton_restart.place(x=30,y=10)
            
        
            self.fuente_de_bienvenida = font.Font(family="Arial",size=22,weight='bold')
            #self.fuente_de_bienvenida.config(size=30)
        
            self.Benvido = ttk.Label(self.lectura_o_escritura, text="Escolle o modo a empregar: ", font=self.fuente_de_bienvenida)
            self.Benvido.place(x=30, y=80)
            self.Benvido.config(foreground='blue')

        
            self.fuente_de_modulos= font.Font(family="Arial",size=12,weight='bold')
        
            Escritura = PhotoImage(file=os.path.join(ruta_de_imagenes,'Escritura.png'),width = 400, height = 300)           
            self.Escritura = ttk.Button(self.lectura_o_escritura, image=Escritura,compound="top", padding=(-70,-60),command=self.SIMULAR)        
            self.Escritura.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)          
            self.Escritura.place(x=30,y=120)
        
            Lectura = PhotoImage(file=os.path.join(ruta_de_imagenes,'Lectura.png'),width = 400, height = 300)           
            self.Lectura = ttk.Button(self.lectura_o_escritura, image=Lectura,compound="top", padding=(-80,-60),command=self.LECTURAS)        
            self.Lectura.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)          
            self.Lectura.place(x=345,y=120)
        
        
            self.sim = ttk.Label(self.lectura_o_escritura,text='Módulo de simulación',font=self.fuente_de_modulos)
            self.sim.place(x=62,y=330)
            self.sim.config(foreground='navy')
            
            
            
            
            
        
            self.lec = ttk.Label(self.lectura_o_escritura,text='Módulo de lectura',font=self.fuente_de_modulos)
            self.lec.place(x=370,y=330)
            self.lec.config(foreground='navy')

        
            self.etiqueta_explicativa3 = ttk.Label(self.lectura_o_escritura,text='Nota: En caso de dúbida de emprego consúltese o manual')
            self.etiqueta_explicativa3.place(x=30,y=390)
        
        
            self.barrita_vertical = ttk.Separator(self.lectura_o_escritura, orient=VERTICAL)
            self.barrita_vertical.place(x=317,y=120,bordermode=INSIDE,height=230, width=10)
     
        
            self.fecha = ttk.Label(self.lectura_o_escritura,text='Inicio de sesión: '+ str(time.localtime()[2]) + '/' + str(time.localtime()[1]) + '/' + str(time.localtime()[0]) +'  ' + str(time.localtime()[3]) + ':' + str(time.localtime()[4]) + ':' + str(time.localtime()[5]))
            self.fecha.place(x=325,y=20)
        
            self.raya1 = ttk.Separator(self.lectura_o_escritura, orient=HORIZONTAL)
            self.raya1.place(x=5, y=435, bordermode=OUTSIDE,height=10, width=590)
        
            self.pie1 = ttk.Label(self.lectura_o_escritura,text='Facultade de Física de Santiago de Compostela')
            self.pie1.place(x=5,y=440)
        
            self.pie2 = ttk.Label(self.lectura_o_escritura,text='Técnicas de análise e simulación en física nuclear e de partículas')
            self.pie2.place(x=5,y=460)
        
            self.pie3 = ttk.Label(self.lectura_o_escritura,text='PyZHAireS v.2.3')
            self.pie3.place(x=470,y=440)
        
        
        
            self.lectura_o_escritura.mainloop() # Fin del bucle de la ventana principal de menú
            
            
            
        except:
            pass
            
    # Vamos a poner la ventana donde vamos a construir y ejecutar la simulación en fortran desde python        
            
    def SIMULAR(self):
        
        self.sim = ttk.Label(self.lectura_o_escritura,text='Non dispoñible nesta versión',font=self.fuente_de_modulos)
        self.sim.place(x=30,y=350)
        self.sim.config(foreground='red')




        
    def LECTURAS(self):
            
        ###################################################################
        #                        VENTANA PRINCIPAL DE LECTURA:
        ###################################################################
        #??????????????????????????????????????????????????????????????????    
        
        try:
            self.lectura_o_escritura.withdraw() # Cerramos temporalmente la ventana de opciones de módulos
        except:
            pass
            
        self.segunda_ventana= Toplevel() # Creo la ventana principal
                
        # Define la dimensión de la ventana
        # Define la dimensión de la ventana
        
        self.segunda_ventana.geometry("920x560")

        def on_closing(): # Defino el mensaje para cerrar la aplicación
            if messagebox.askokcancel("Quit", "Seguro que desexas pechar a aplicación?"):
                self.lectura_o_escritura.destroy()

        self.segunda_ventana.protocol("WM_DELETE_WINDOW", on_closing)

        self.boton_restart = ttk.Button(self.segunda_ventana,text='RESTART',padding=(5,5),command=restart_program)
        self.boton_restart.place(x=30,y=10)
        
        global DEBUG
        DEBUG+=1
        print('DEBUG: ',DEBUG)
        
        
        if ( sys.platform.startswith('win')): # Defino el icono de la ventana por si es windows o linux el S.O.
            try:
                Ruta_logo=os.path.join(ruta_de_imagenes,'PRUEBA_ICONOS.ICO')
                logo = PhotoImage(file=Ruta_logo)
                self.segunda_ventana.tk.call('wm', 'iconphoto', self.segunda_ventana._w, logo)        
            except:
                pass
        else:
            try:
                Ruta_logo=os.path.join(ruta_de_imagenes,'PRUEBA_ICONOS.xbm')
                logo = PhotoImage(file=Ruta_logo)
                self.segunda_ventana.tk.call('wm', 'iconphoto', self.segunda_ventana._w, logo)        
            except:
                pass
        
        
        
        # Establece que sí se pueda cambiar el tamaño de la
        # ventana
        
        #self.segunda_ventana.resizable(0,0) # Me gusta más que quede sin poder maximizar
        self.segunda_ventana.title("PyZHAireS: MÓDULO DE LECTURAS")
        self.fuente_en_negrita = font.Font(weight='bold')   
        
        self.barrita = ttk.Separator(self.segunda_ventana, orient=HORIZONTAL)
        self.barrita.place(x=5,y=50,bordermode=OUTSIDE,height=10, width=890)
        
        self.fuente_de_bienvenida = font.Font(family="Arial",size=20,weight='bold')
        #self.fuente_de_bienvenida.config(size=30)
        

        self.etiqueta1 = ttk.Label(self.segunda_ventana,text='Introduce a ruta ao directorio /anillos que contén as simulacións (ou, no seu defecto, ao arquivo Simulacions_TTree.root,')
        self.etiqueta1.place(x=20,y=70)
        self.etiqueta2 = ttk.Label(self.segunda_ventana,text='de telo xa creado no equipo): ')
        self.etiqueta2.place(x=20,y=92)





        self.ruta_simulacions = StringVar()
        self.Entrada_usuario_1= ttk.Entry(self.segunda_ventana,textvariable=self.ruta_simulacions, width=80)
        self.Entrada_usuario_1.place(x=230,y=92)

        self.boton_examinar = ttk.Button(self.segunda_ventana,text='Examinar',padding=(3,3),command=self.buscar)
        self.boton_examinar.place(x=800,y=89)


        self.etiqueta3 = ttk.Label(self.segunda_ventana,text='Introduce o nome da carpeta a crear: ')
        self.etiqueta3.place(x=20,y=130)

        self.etiquetai = ttk.Label(self.segunda_ventana,text='(Só se non tes xerado o arquivo Simulacions_TTree.root)')
        self.etiquetai.place(x=500,y=130)

        self.nome_carpeta = StringVar()
        self.Entrada_usuario_2= ttk.Entry(self.segunda_ventana,textvariable=self.nome_carpeta, width=30)
        self.Entrada_usuario_2.place(x=280,y=129)


        self.ray = ttk.Separator(self.segunda_ventana, orient=HORIZONTAL)
        self.ray.place(x=30, y=170, bordermode=OUTSIDE,height=10, width=370)

        self.etiqueta4 = ttk.Label(self.segunda_ventana,text='Opcións gráficas (opcionais):')
        self.etiqueta4.place(x=110,y=180)

        self.ray2 = ttk.Separator(self.segunda_ventana, orient=HORIZONTAL)
        self.ray2.place(x=30, y=200, bordermode=OUTSIDE,height=10, width=370)


        self.etiqueta5 = ttk.Label(self.segunda_ventana,text='Etiqueta do eixo horizontal: ')
        self.etiqueta5.place(x=20,y=230)

        self.eixox = StringVar()
        self.Entrada_usuario_3= ttk.Entry(self.segunda_ventana,textvariable=self.eixox, width=45)
        self.Entrada_usuario_3.place(x=220,y=230)


        self.etiqueta6 = ttk.Label(self.segunda_ventana,text='Etiqueta do eixo vertical: ')
        self.etiqueta6.place(x=20,y=260)

        self.eixoy = StringVar()
        self.Entrada_usuario_4= ttk.Entry(self.segunda_ventana,textvariable=self.eixoy, width=45)
        self.Entrada_usuario_4.place(x=220,y=260)


        self.etiqueta7 = ttk.Label(self.segunda_ventana,text='Etiqueta da lenda (barra de cores): ')
        self.etiqueta7.place(x=20,y=290)

        self.lenda = StringVar()
        self.Entrada_usuario_5= ttk.Entry(self.segunda_ventana,textvariable=self.lenda, width=38)
        self.Entrada_usuario_5.place(x=270,y=290)


        self.etiqueta8 = ttk.Label(self.segunda_ventana,text='Imaxe de referencia:')
        self.etiqueta8.place(x=20,y=320)

        Imagen = PhotoImage(file=os.path.join(ruta_de_imagenes,'Lectura_matplotlib.png'),width = 650, height = 350) # Invoco la imagen de la portada
        self.Imagen = ttk.Label(self.segunda_ventana, image=Imagen, anchor='center')  # Creo el widget de la imagen com una etiqueta simple pero con imagen
        self.Imagen.pack(side=TOP, fill=BOTH, expand=True, padx=600, pady=100)          
        self.Imagen.place(x=20,y=340) # Dónde la pongo dentro de la ventana


        self.barrita_vertical2 = ttk.Separator(self.segunda_ventana, orient=VERTICAL)
        self.barrita_vertical2.place(x=570,y=170,bordermode=INSIDE,height=300, width=10)


        self.boton_leer = ttk.Button(self.segunda_ventana,text='LECTURA',padding=(50,30),command=self.traballo_root)
        self.boton_leer.place(x=650,y=170)














        '''
        self.fuente_WAIT = font.Font(family="Times New Roman",size=15,weight='bold') # Defino un tipo de fuente que empleo después para escribir el título
        self.WAIT = ttk.Label(self.segunda_ventana,text='                                                               ',font=self.fuente_WAIT)
        self.WAIT.place(x=30,y=450)
        

        # Para quitar la imagen le meto una letra muy gruesa:

        self.fuentetocha = font.Font(family="Times New Roman",size=90,weight='bold')
        self.fuentetocha.config(size=90)
        self.letra_tapar = ttk.Label(self.segunda_ventana,text=' ')           
        self.letra_tapar.place(x=400,y=355)
        '''




            
        self.fecha = ttk.Label(self.segunda_ventana,text='Inicio de sesión: '+ str(time.localtime()[2]) + '/' + str(time.localtime()[1]) + '/' + str(time.localtime()[0]) +'  ' + str(time.localtime()[3]) + ':' + str(time.localtime()[4]) + ':' + str(time.localtime()[5]))
        self.fecha.place(x=645,y=20)
            
        self.raya1 = ttk.Separator(self.segunda_ventana, orient=HORIZONTAL)
        self.raya1.place(x=5, y=495, bordermode=OUTSIDE,height=10, width=890)
            
        self.pie1 = ttk.Label(self.segunda_ventana,text='Facultade de Física de Santiago de Compostela')
        self.pie1.place(x=5,y=500)
            
        self.pie2 = ttk.Label(self.segunda_ventana,text='Técnicas de análise e simulación en física nuclear e de partículas')
        self.pie2.place(x=5,y=520)
            
        self.pie3 = ttk.Label(self.segunda_ventana,text='PyZHAireS v.2.3')
        self.pie3.place(x=770,y=500)
            
        self.Boton_cerrar_sesion = ttk.Button(self.segunda_ventana,text='Cambiar de módulo',padding=(5,5),command=self.aceptar)
        self.Boton_cerrar_sesion.place(x=760,y=520)
            
            
        
            
        self.segunda_ventana.mainloop() # Fin del bucle de la ventana principal de menú
            
            
            
        #------------------------------------------------------------------------------
            
            
    def traballo_root(self):
        
                
        
        relojito = PhotoImage(file=os.path.join(ruta_de_imagenes,'relojarena2.png'),width = 400, height = 200)           
        self.reloj_arenaa = ttk.Label(self.segunda_ventana, image = relojito ,anchor="e")        
        self.reloj_arenaa.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)          
        self.reloj_arenaa.place(x=640,y=262)


        time.sleep(2)
        
        
            
        #??????????????????????????????????????????????????????????????????????????????
        #????????????????????   LECTURA_SIMULACIONS_ROOT.py   ?????????????????????????
        #??????????????????????????????????????????????????????????????????????????????
        
        
        
        
        
        
        
        
        #!/usr/bin/env python3
        # -*- coding: utf-8 -*-
        """
        Created on Sun May  3 00:45:09 2020
        
        @author: lino
        """
        
        
        
        
        # Imos diferenciar dúas situacións: que o usuario xa teña as simulacións feitas
        # e gardadas nun directorio pero sen ler con ROOT (~22 GB) e outra situación na
        # cal o usuario non teña as simulacións pero si teña o arquivo Simulacions_TTree.root
        # na cal están todas as simulacións xa lidas.
        
        # Para o primeiro caso, o usuario deberá dar o path ao directorio onde están to-
        # das as carpetas con formato "anillo_i" e python efectuará a lectura e creará
        # unha carpeta (cuxo nome debe dalo tamén o usuario) onde se gardará un TTree e
        # os plots da simulación.
        
        # Para o segundo caso, o usuario deberá dar o path ao directorio onde se atopa 
        # o arquivo Simulacions_TTree.root e python lerá dese TTree toda a información
        # e xerará unha carpeta con todos os plots.
        
        os.chdir(self.ruta_simulacions.get())
        
        Ruta_arquivo_root = self.ruta_simulacions.get() 

        
        Pregunta_inicial = 'n'
        
        for archivo in os.listdir(os.getcwd()):
            if archivo.startswith('Simulacions_TTree.root'):
                Pregunta_inicial = 's'
        
        
        
        if Pregunta_inicial != 's':
        
            # Insertamos a ruta ao directorio onde temos as simulacións (carpeta cos 49 aneis)
            Ruta_simulacions = self.ruta_simulacions.get() 
        
        
            Nome_carpeta = self.nome_carpeta.get()
        
        
            os.chdir(Ruta_simulacions)
        
            Lista_de_rutas = []
        
        
            for archivo in os.listdir():
                if archivo.startswith('anillo'):
                    os.chdir(archivo)
                    Lista_de_rutas.append(os.getcwd())
                    os.chdir(Ruta_simulacions)
        
        
            instante_inicial = time.time()
    
    
    
            # Defino as miñas variables de almacén
            primera_columna = [] # A primeira columna é o tempo
            segunda_columna = [] # A segunda columna é a envolvente de Hilbert
            segunda_columna_auxiliar = []
            maximos = []
        
            columna_x = []
            columna_y = []
            columna_z = []
        
        
        
            # Abrimos coa opción de 'lectura' o arquivo 'field_envelope_antenna_i.dat'
        
            for simulacion in range(len(Lista_de_rutas)):    
            
                Lista_de_Arquivos_aqui = []
            
                Ruta = Lista_de_rutas[simulacion]
        
                os.chdir(Ruta) # Cambio o directorio no que estaba polo que ingreso manualmente
        
                Lista_de_arquivos_aqui_auxiliar = os.listdir() # Lista con todos os arquivos de este directorio
            
                for i in range(len(Lista_de_arquivos_aqui_auxiliar)):
                
                    Arquivito = Lista_de_arquivos_aqui_auxiliar[i]
           
                    if Arquivito.startswith('field_envelope_antenna_') == True: # Contamos os arquivos cuxos nomes empezan así
                        Lista_de_Arquivos_aqui.append(Arquivito)
                    else:
                        continue
                
                Numero_de_arquivos = len(Lista_de_Arquivos_aqui)
                
            
            
        
                for antena in range(Numero_de_arquivos):
        
                    Arquivo_1 = 'field_envelope_antenna_' # Nome do arquivo que imos abrir
                    Arquivo_2 = str(antena+1)
                    Arquivo_3 = '.dat'
                    Arquivo_completo = Arquivo_1 + Arquivo_2 + Arquivo_3
        
                    file = open(Arquivo_completo,'r') # Abrimos o arquivo en 'modo lectura'
                    contenido = file.readlines() # Contenido == Todo o noso arquivo leído en Python
        
                    # Si escribimos en la linea de comandos "contenido" nos sale toooodo el documento de texto y, si
                    # escribimos "contenido[0]" nos sale la primerísima línea del documento, entonces ya me hago una
                    # idea de que el documento en sí es una matriz donde cada línea es un vector. Así pues, recorrere-
                    # mos la matriz "contenido" por vectores y en cada línea almacenaremos cada elemento en unas listas
                    # que definimos ahora como variables de almacén.
        
        
                    for i in range(len(contenido)): # Recorremos todo el fichero. Si hubieran unos párrafos al principio informativos que no quisiera almacenar (rollo el mítiko que nos dice que tal columna es tal cosa) entonces haríamos "for i in range(principio,len(contenido)):", donde "principio" es igual al número de línea donde comienzan las columnas ya 
                        a = contenido[i].split(' ')   # Separamos cada línea en vectores (eso hace el split) cuyos elementos son los caracteres que salen en cada línea separados por lo que pongo entre paréntesis (un espacio)
                        edito = a[-1].replace('\n','') # Al final de cada línea me sale un \n,o lo que es lo mismo, en el último elemento de cada vector me sale eso, por lo que lo elimino
                        a[-1] = edito # Para evitar errores
        
                        if a[0] == '#':   # Con esta instrucción señalo que la primera línea de cada antena posee la información de la distancia al core de la cascada
                            print('Leyendo antena %i ...'%(int(a[2])+1)) # Decimos el número de antena
        
                        else:   # En el caso de que no estemos en la primera línea (descriptiva) de la antena...:
                            if a[0] != '':    # Si no estamos en el final de la antena...:
                                try:    # Almacenamos los valores de cada columna
                                    primera_columna.append(a[0]) # Por ahora no me sirve para nada este valor, luego lo elimino
                                    segunda_columna_auxiliar.append(a[1])
                                
                                except IndexError: # Daría error en el final de la antena
                                    continue       # por eso le damos la instrucción de seguir
                        
                            else:   # En el caso de que llegásemos al final de la antena...:
                           
                                for j in range(len(segunda_columna_auxiliar)): # Nos detenemos y almacenamos el valor máximo de la quinta columna (que es la que me interesa)
                                    elemento = float(segunda_columna_auxiliar[j])
                                    segunda_columna.append(elemento)
                            
                                maximos.append(np.max(segunda_columna)*1e6) # Lo dicho (el 1e6 es para ponerlo en microvoltios · m⁻¹!!!)
                                print(np.max(segunda_columna)*1e6)
                                # Reseteamos las variables de almacén
                                primera_columna=[]
                                segunda_columna=[]
                                segunda_columna_auxiliar=[]
                                print('Fin de antena %i'%int(antena+1)) 
        
        
                print()
        
        
                # Hasta aquí todo perfecto, ya tenemos la lista con los valores máximos de cada envolvente de Hilbert.
                # Ahora tenemos que abrir otro archivo para leer la posición de cada antena.
        
                Archivo_con_extension_sry = str()
        
                for file in os.listdir(Ruta):
                    if file.endswith(".sry"):
                        Archivo_con_extension_sry = file
                        print(Archivo_con_extension_sry)
        
                file = open(Archivo_con_extension_sry,'r') # Abrimos el archivo en 'modo lectura'
                contenido = file.readlines() # Contenido == Todo nuestro archivo leído en Python
        
        
        
                linea_descripcion_antenas = 0
        
                for i in range(len(contenido)): # Recorremos todo el fichero. Si hubieran unos párrafos al principio informativos que no quisiera almacenar (rollo el mítiko que nos dice que tal columna es tal cosa) entonces haríamos "for i in range(principio,len(contenido)):", donde "principio" es igual al número de línea donde comienzan las columnas ya 
                    if 'Antenna|' in contenido[i]: # Detectamos dónde está la zona de las antenas
                        linea_descripcion_antenas = i
        
                linea_descripcion_antenas = linea_descripcion_antenas + 1 # Nos movemos a la línea de abajo
                
                # Volvemos ahora a leer el archivo .sry pero empezando por la línea que hemos encontrado y hasta que acabemos el número de antenas:
        
                for j in range(linea_descripcion_antenas,int(linea_descripcion_antenas)+Numero_de_arquivos):
            
                
                    linea = contenido[j].split(' ') # Convierto cada linea en un vector
            
                    linea = ' '.join(linea).split() # Le quito esos espacios en blanco
            
                    columna_x.append(float(linea[1]))
                    columna_y.append(float(linea[2]))
                    columna_z.append(float(linea[3]))
            
            
            # OLLOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!!!!!!!!!!!!!!!!!
            elemento_maximo = np.max(maximos)
            indice_elemento_maximo = maximos.index(elemento_maximo)
            maximos.pop(indice_elemento_maximo)    
            columna_x.pop(indice_elemento_maximo)    
            columna_y.pop(indice_elemento_maximo)    
            columna_z.pop(indice_elemento_maximo)    
        
            plt.rcParams['figure.figsize'] = 15, 6
            plt.rcParams['axes.facecolor'] = 'black' # Para que tengamos un background de la imagen final negro (es por estética)
            plt.scatter(columna_x,columna_y,c=maximos,s=30,cmap='inferno')
        
            plt.title('Neutrino de 10 EeV de enerxía interaccionando a unha profundidade de 700 g·cm⁻² na atmósfera e cun ángulo cenital de 75⁰')
            plt.xlabel('Posición das antenas con respecto ao eixo da fervenza (m)')
            plt.ylabel('Posición das antenas con respecto ao eixo da fervenza (m)')
            cbar = plt.colorbar()    # Creo la barra de leyenda de colores
            cbar.set_label('Envolvente de Hilbert do campo eléctrico (μV·m⁻¹)')
            
            plt.rcParams['axes.facecolor'] = 'white' # Regresamos el fondo blanco por si nos movemos a otros programas
        
        
        
            instante_final = time.time()
        
            duracion = (instante_final-instante_inicial)/60
        
            print('Tempo de lectura: ',duracion,' min')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            os.chdir(Ruta_simulacions) # Movémonos de volta á carpeta orixinal
        
        
            os.mkdir(Nome_carpeta) # Creamos a carpeta co nome especificado polo usuario...
        
            os.chdir(Nome_carpeta) # e movémonos a ela
            Nome_carpeta = os.getcwd() # Almaceno a ruta da carpeta
        
            # Asegurarnos de que las listas de columnas_xymaximos no están vacías antes!
        
        
            #??????????????????????????????????????????????????????????????????????????????
            
            # PARTE CREACIÓN DO TTREE
            # Aquí imos almacenar toodos os datos nun TTree para poder telos a nosa dispo-
            # sición sen ter que ler de novo toooodas as simulacións (e perder un tempo va-
            # lioso).    
        
            # Defino primeiro as miñas variables auxiliares de almacén:
            a = array('d',[0.])
            b = array('d',[0.])
            c = array('d',[0.])
            d = array('d',[0.])
        
            # Creamos o arquivo.root
            ARQUIVO = ROOT.TFile("Simulacions_TTree.root","recreate")
            # Creamos o TTree:
            ARBORE_1 = ROOT.TTree("Almacen_parametros_simulacion","Un Tree simplon")
        
            # Definimos cada rama do noso Tree:
            ARBORE_1.Branch("columna_x",a,"a/D")
            ARBORE_1.Branch("columna_y",b,"b/D")
            ARBORE_1.Branch("columna_z",c,"c/D")
            ARBORE_1.Branch("maximos",d,"d/D")
        
            # Agora enchemos todas as ramas coas listas completas que queremos:
            for i in range(len(maximos)):
                a[0] = columna_x[i]
                b[0] = columna_y[i]
                c[0] = columna_z[i]
                d[0] = maximos[i]
                ARBORE_1.Fill()
        
            # Aplicamos os cambios e gardamos:
            ARBORE_1.Write()
            ARQUIVO.Close()
        
        
        
        
        
            # Para volver acceder a este Tree faríamos o seguinte:
        
            # Primeiro defino as listas onde almacenarei os valores que obteño do TTree
            # (Chamándoas co mesmo nome que a lectura con Python podo checkear se vai ben)
            maximos = []
            columna_x = []
            columna_y = []
            columna_z = []
            instante_inicial = time.time()
        
            # Abrimos o arquivo.root onde temos o TTree:
            ARQUIVO = ROOT.TFile("Simulacions_TTree.root","update")
        
            # Xeramos un punteiro ao TTree que buscamos:
            tree_que_busco = ARQUIVO.Get("Almacen_parametros_simulacion")
        
            # Almacenamos o número total de entradas que ten o TTree, é dicir,o número de
            # filas que conteñe se fixésemos a instrucción: tree_que_busco.Scan()
            Numero_de_entradas = tree_que_busco.GetEntries()
        
            # Agora iteramos en cada TBranch do Tree:
            for i in range(Numero_de_entradas):
                entry = tree_que_busco.GetEntry(i) # Metémonos na fila i-ésima
                maximos.append(tree_que_busco.maximos)
                columna_x.append(tree_que_busco.columna_x)
                columna_y.append(tree_que_busco.columna_y)
        
            # Xa teríamos de volta todos os parámetros e nun instante!!
            instante_final = time.time()
        
            duracion = instante_final-instante_inicial
            
            print()
            print('Duración da lectura directa do TTree: ',duracion,' s.')
            print()
        
        
            # Vou crear a maiores uns histogramas co cales farei algunhas cousas:
            histmax = ROOT.TH1F("campos electricos (factor rebinning 28)", "Test data", 350, np.min(maximos), np.max(maximos))    
            histx = ROOT.TH1F("posicions eixo x (factor rebinning 28)", "Test data", 350, np.min(columna_x), np.max(columna_x))    
            histy = ROOT.TH1F("posicions eixo y (factor rebinning 28)", "Test data", 350, np.min(columna_y), np.max(columna_y))    
        
            for i in range(Numero_de_entradas):
                entry = tree_que_busco.GetEntry(i) # Metémonos na fila i-ésima
                histmax.Fill(tree_que_busco.maximos)
                histx.Fill(tree_que_busco.columna_x)
                histy.Fill(tree_que_busco.columna_y)
        
            # Customización do histograma maximos
            histmax.GetXaxis().SetTitle("Campos electricos")
            histmax.Draw()
            histmax.Write()
        
            #-----
        
            # Customización do histograma Y
            c = ROOT.TCanvas("Canvas", "Canvas", 1000, 800)
            histy.GetXaxis().SetTitle("Posicion das antenas no eixo y")
            histy.Draw()
            axuste_y = histy.Fit("gaus","","",np.min(columna_y),np.max(columna_y))
            
            # Engadimos a lenda ao histograma
            legend = ROOT.TLegend(0.1,0.7,0.43,0.9)
            legend.AddEntry(histy, "Datos", "l")
            legend.Draw()
            
            histy.Write()
            
            # Actualizamos o canvas:
            c.Draw()
            c.Update()
        
            #-----
            
            # Customización do histograma X
            c = ROOT.TCanvas("Canvas", "Canvas", 1000, 800)
            histx.GetXaxis().SetTitle("Posicions das antenas no eixo x")
            histx.Draw()
            # Facemos primeiro o axuste do primeiro pico
            
            g1    =  ROOT.TF1("g1","gaus",np.min(columna_x),0)
            axuste_1x = histx.Fit(g1,"R+")
        
            # Engadimos a lenda ao histograma
            legend = ROOT.TLegend(0.1,0.7,0.43,0.9)
            legend.AddEntry(histx, "Datos", "l")
            legend.Draw()
            
            histx.Write()
            
            # Actualizamos o canvas:
            c.Draw()
            c.Update()
        
            # Rescatamos de novo o histograma e facemos o fit do segundo pico:
            histx = ARQUIVO.Get('posicions eixo x (factor rebinning 28)')
        
            # Customización do histograma X
            c = ROOT.TCanvas("Canvas", "Canvas", 1000, 800)
            histx.GetXaxis().SetTitle("Posicions das antenas no eixo x")
            histx.Draw()
            # Facemos primeiro o axuste do primeiro pico
            g2    =  ROOT.TF1("g2","gaus",0,np.max(columna_x))
            axuste_2x = histx.Fit(g2,"R+")    
        
            # Engadimos a lenda ao histograma
            legend = ROOT.TLegend(0.1,0.7,0.43,0.9)
            legend.AddEntry(histx, "Datos", "l")
            legend.Draw()
            
            histx.Write()
            
            # Actualizamos o canvas:
            c.Draw()
            c.Update()
        
            ARQUIVO.Close()
        
        
        
        
            if os.getcwd() != Nome_carpeta:
                os.chdir(Nome_carpeta) # Movémonos á carpeta creada polo usuario
        
            os.mkdir('plots')
            os.chdir('plots')
            Ruta_plots = os.getcwd()
        
        
            plt.savefig('Sinal_matplotlib') # Gardamos a imaxe que xa tiña aberta de antes
            plt.close('all')
        
        
            os.chdir(Nome_carpeta) # Movémonos á carpeta creada polo usuario
        
            # Imos escribir os resultados do axuste nun arquivo de texto externo:
        
            ARQUIVO = ROOT.TFile("Simulacions_TTree.root","update")
            histx = ARQUIVO.Get('posicions eixo x (factor rebinning 28);2')    
            histy = ARQUIVO.Get('posicions eixo y (factor rebinning 28)')    
        
        
            g1x =histx.GetFunction('g1')
            g2x =histx.GetFunction('g2')
            gy =histy.GetFunction('gaus')
            
            resultados = open("resultados_dos_fits.txt","w+")
        
            resultados.write("###########################\n")                    
            resultados.write("    RESULTADOS DOS FITS    \n")
            resultados.write("###########################\n")
            resultados.write("\n")                     
            resultados.write("\n")                     
            resultados.write("\n")                     
            resultados.write("Parámetros do axuste á gaussiana da columna y:\n")                     
            resultados.write("\n")                     
            resultados.write("%f    %f    %f\n"%(gy.GetParameter(0),gy.GetParameter(1),2*gy.GetParameter(2)))                     
            resultados.write("\n")                     
            resultados.write("Parámetros dos axustes ás gaussianas da columna x:\n")                     
            resultados.write("\n")                     
            resultados.write("%f    %f    %f\n"%(g1x.GetParameter(0),g1x.GetParameter(1),2*g1x.GetParameter(2)))                     
            resultados.write("%f    %f    %f\n"%(g2x.GetParameter(0),g2x.GetParameter(1),2*g2x.GetParameter(2)))                     
            resultados.close()
            
            Anchura_elipse = (2*g1x.GetParameter(2) + np.abs(g1x.GetParameter(1))/2.) + (2*g2x.GetParameter(2) + np.abs(g1x.GetParameter(1))/2.)
            Altura_elipse = 2*gy.GetParameter(2)
            
            
            ARQUIVO.Close()
            
            
            os.chdir('plots')
            
            # A partires dos valores dos fits imos recrear a elipse da sinal en terra:
            
            plt.rcParams['axes.facecolor'] = 'black' # Para que tengamos un background de la imagen final negro (es por estética)
            
            NUM = 1
            
            ells = [Ellipse(xy=array('f',[0,0]), width=Anchura_elipse, height=Altura_elipse, angle=0.)
                    for i in range(NUM)]
            
            fig = plt.figure(0)
            ax = fig.add_subplot(111, aspect='equal')
            for e in ells:
                ax.add_artist(e)
                e.set_clip_box(ax.bbox)
                e.set_alpha(0.5)
            
            plt.rcParams['figure.figsize'] = 15, 6
        
            plt.scatter(columna_x,columna_y,c=maximos,cmap='inferno')
            ax.set_xlim(np.min(columna_x), np.max(columna_x))
            ax.set_ylim(np.min(columna_y), np.max(columna_y))
            
            plt.xlabel('Pocición das antenas respecto ao core da fervenza - Este (m)')
            plt.ylabel('Pocición das antenas respecto ao core da fervenza - Norte (m)')
            cbar = plt.colorbar()    # Creo la barra de leyenda de colores
            cbar.set_label('Envolvente de Hilbert do campo eléctrico (μV·m⁻¹)')
            plt.title('Neutrino de 10 EeV de enerxía interaccionando a unha profundidade de 700 g·cm⁻² na atmósfera e cun ángulo cenital de 75⁰')
        
            
            plt.show()
            plt.savefig('Elipticidade_da_sinal.png')
            plt.close('all')
            
            plt.rcParams['axes.facecolor'] = 'white' # Para que tengamos un background de la imagen final negro (es por estética)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            #??????????????????????????????????????????????????????????????????????????????
            
            
            
            
            # Imos crear a modo exemplo uns plots con distintas paletas de cores (para facer
            # máis ilustrativos os plots. Para iso gardaremos as figuras en diferentes car-
            # petas en función da paleta que empreguemos.
            # No final deste script atópase un exemplo e os códigos de paletas para ROOT.
                    
            
            os.mkdir('paleta_por_defecto')
            os.chdir('paleta_por_defecto')
            
            
            # Creación de scatter color plots en ROOT
            
            ROOT.gStyle.SetPalette(57) # Por se acaso non tiñamos xa de antes posta a paleta.
            
            # Defino as dimensións dos canvas que vou crear
            altura = 600
            anchura = 1500
            
            
            # Recuperamos los valores que sacamos de las simulaciones
            x = columna_x
            y = columna_y
            z = maximos
            Number_of_points = len(z)
            graph = ROOT.TGraph2D(Number_of_points)
            for i in range(Number_of_points): graph.SetPoint(i, y[i], x[i], z[i])
            c1 = ROOT.TCanvas("c")
            graph.SetMarkerStyle(20); graph.Draw("PCOL Z") # A opción "PCOL" fai un scatter
                                                           # plot dos puntos que definimos
                                                           # antes. Ademáis, a opción "Z" ao
                                                           # seu carón indica que queremos
                                                           # mostrar tamén una barra de co-
                                                           # res a modo "lenda"
            
            # Poño eses ángulos para verse guai
            c1.SetTheta(270)
            c1.SetPhi(270)
            c1.SetWindowSize(anchura + (anchura - c1.GetWw()), altura + (altura - c1.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            c1.SaveAs("figura_1.png")
            c1.SaveAs("figura_1.root")
            
            
            
            # Imos facer outros plots alternativos interesantes:
            
            
            # Histograma bidimensional
            c2 = ROOT.TCanvas("c")
            graph.Draw("COL Z") # A opción "COL" debuxa unha un histograma bidimensional a 
                                # partires dos puntos que ten o plot.
            
            c2.SetTheta(270)
            c2.SetPhi(270)
            c2.SetWindowSize(anchura + (anchura - c2.GetWw()), altura + (altura - c2.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c2.SaveAs("figura_2.png")
            c2.SaveAs("figura_2.root")
            
            
            
            
            # Plot de superficie
            c3 = ROOT.TCanvas("c")
            graph.Draw("CONT Z") # A opción "CONT" fai un plot empregando un mapa de cores
                                 # para distinguir contornos/superficies.
                               
            c3.SetTheta(270)
            c3.SetPhi(270)
            c3.SetWindowSize(anchura + (anchura - c3.GetWw()), altura + (altura - c3.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c3.SaveAs("figura_3.png")
            c3.SaveAs("figura_3.root")
            
            
            
            # Plot de relieve
            c11 = ROOT.TCanvas("c")
            graph.Draw("SURF3") # A opción "SURF3" fai un plot de superficie igual que fa-
                                # ría a opción "SURF" pero engadindo un relieve sobre a fi-
                                # gura.
            w = 2000
            h = 2000
            
            c11.SetTheta(-30)
            c11.SetPhi(300)
            c11.SetWindowSize(anchura + (anchura - c11.GetWw()), altura + (altura - c11.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            c11.SaveAs("figura_4.png")
            c11.SaveAs("figura_4.root")
            
            
            
            # Triangulación de Delaunay
            c12 = ROOT.TCanvas("c")
            graph.Draw("TRI2 Z") # A opción "TRI2" fai unha reconstrucción por triangulación
                                 # de Delaunay. Moi útil para casos nos que temos imaxes "par-
                                 # cialmente" incompletas ou nos que o scatter plot ofrece unha
                                 # resolución mellorable (vese ambas situacións no noso caso).
            
            c12.SetTheta(270)
            c12.SetPhi(270)
            c12.SetWindowSize(anchura + (anchura - c12.GetWw()), altura + (altura - c12.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c12.SaveAs("figura_5.png")
            c12.SaveAs("figura_5.root")
            
            
            #------------------------------------------------------------------------------
            
            # Rematados os plots que queríamos facer, movémonos á seguinte paleta de cores.
            os.chdir(Ruta_plots)
            os.mkdir('paleta_kDarkBodyRadiator')
            os.chdir('paleta_kDarkBodyRadiator')
            ROOT.gStyle.SetPalette(53)
            
            # Defino as dimensións dos canvas que vou crear
            altura = 600
            anchura = 1500
            
            
            # Scatter plot normal e corrente
            
            graph = ROOT.TGraph2D(Number_of_points)
            for i in range(Number_of_points): graph.SetPoint(i, y[i], x[i], z[i])
            c1 = ROOT.TCanvas("c")
            graph.SetMarkerStyle(20); graph.Draw("PCOL Z")
            
            # Poño eses ángulos para verse guai
            c1.SetTheta(270)
            c1.SetPhi(270)
            c1.SetWindowSize(anchura + (anchura - c1.GetWw()), altura + (altura - c1.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            c1.SaveAs("figura_1.png")
            c1.SaveAs("figura_1.root")
            
            # Histograma bidimensional
            c2 = ROOT.TCanvas("c")
            graph.Draw("COL Z") # A opción "COL" debuxa unha un histograma bidimensional a 
                                # partires dos puntos que ten o plot.
            
            c2.SetTheta(270)
            c2.SetPhi(270)
            c2.SetWindowSize(anchura + (anchura - c2.GetWw()), altura + (altura - c2.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c2.SaveAs("figura_2.png")
            c2.SaveAs("figura_2.root")
            
            
            
            
            # Plot de superficie
            c3 = ROOT.TCanvas("c")
            graph.Draw("CONT Z") # A opción "CONT" fai un plot empregando un mapa de cores
                                 # para distinguir contornos/superficies.
                               
            c3.SetTheta(270)
            c3.SetPhi(270)
            c3.SetWindowSize(anchura + (anchura - c3.GetWw()), altura + (altura - c3.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c3.SaveAs("figura_3.png")
            c3.SaveAs("figura_3.root")
            
            
            
            # Plot de relieve
            c11 = ROOT.TCanvas("c")
            graph.Draw("SURF3") # A opción "SURF3" fai un plot de superficie igual que fa-
                                # ría a opción "SURF" pero engadindo un relieve sobre a fi-
                                # gura.
            w = 2000
            h = 2000
            
            c11.SetTheta(-30)
            c11.SetPhi(300)
            c11.SetWindowSize(anchura + (anchura - c11.GetWw()), altura + (altura - c11.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            c11.SaveAs("figura_4.png")
            c11.SaveAs("figura_4.root")
            
            
            
            # Triangulación de Delaunay
            c12 = ROOT.TCanvas("c")
            graph.Draw("TRI2 Z") # A opción "TRI2" fai unha reconstrucción por triangulación
                                 # de Delaunay. Moi útil para casos nos que temos imaxes "par-
                                 # cialmente" incompletas ou nos que o scatter plot ofrece unha
                                 # resolución mellorable (vese ambas situacións no noso caso).
            
            c12.SetTheta(270)
            c12.SetPhi(270)
            c12.SetWindowSize(anchura + (anchura - c12.GetWw()), altura + (altura - c12.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c12.SaveAs("figura_5.png")
            c12.SaveAs("figura_5.root")
            
            
            
            
            
            #------------------------------------------------------------------------------
            
            # Rematados os plots que queríamos facer, movémonos á seguinte paleta de cores.
            os.chdir(Ruta_plots)
            os.mkdir('paleta_kRainBow')
            os.chdir('paleta_kRainBow')
            ROOT.gStyle.SetPalette(55)
            
            # Defino as dimensións dos canvas que vou crear
            altura = 600
            anchura = 1500
            
            
            # Scatter plot normal e corrente
            
            graph = ROOT.TGraph2D(Number_of_points)
            for i in range(Number_of_points): graph.SetPoint(i, y[i], x[i], z[i])
            c1 = ROOT.TCanvas("c")
            graph.SetMarkerStyle(20); graph.Draw("PCOL Z")
            
            # Poño eses ángulos para verse guai
            c1.SetTheta(270)
            c1.SetPhi(270)
            c1.SetWindowSize(anchura + (anchura - c1.GetWw()), altura + (altura - c1.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            c1.SaveAs("figura_1.png")
            c1.SaveAs("figura_1.root")
            
            # Histograma bidimensional
            c2 = ROOT.TCanvas("c")
            graph.Draw("COL Z") # A opción "COL" debuxa unha un histograma bidimensional a 
                                # partires dos puntos que ten o plot.
            
            c2.SetTheta(270)
            c2.SetPhi(270)
            c2.SetWindowSize(anchura + (anchura - c2.GetWw()), altura + (altura - c2.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c2.SaveAs("figura_2.png")
            c2.SaveAs("figura_2.root")
            
            
            
            
            # Plot de superficie
            c3 = ROOT.TCanvas("c")
            graph.Draw("CONT Z") # A opción "CONT" fai un plot empregando un mapa de cores
                                 # para distinguir contornos/superficies.
                               
            c3.SetTheta(270)
            c3.SetPhi(270)
            c3.SetWindowSize(anchura + (anchura - c3.GetWw()), altura + (altura - c3.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c3.SaveAs("figura_3.png")
            c3.SaveAs("figura_3.root")
            
            
            
            # Plot de relieve
            c11 = ROOT.TCanvas("c")
            graph.Draw("SURF3") # A opción "SURF3" fai un plot de superficie igual que fa-
                                # ría a opción "SURF" pero engadindo un relieve sobre a fi-
                                # gura.
            w = 2000
            h = 2000
            
            c11.SetTheta(-30)
            c11.SetPhi(300)
            c11.SetWindowSize(anchura + (anchura - c11.GetWw()), altura + (altura - c11.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            c11.SaveAs("figura_4.png")
            c11.SaveAs("figura_4.root")
            
            
            
            # Triangulación de Delaunay
            c12 = ROOT.TCanvas("c")
            graph.Draw("TRI2 Z") # A opción "TRI2" fai unha reconstrucción por triangulación
                                 # de Delaunay. Moi útil para casos nos que temos imaxes "par-
                                 # cialmente" incompletas ou nos que o scatter plot ofrece unha
                                 # resolución mellorable (vese ambas situacións no noso caso).
            
            c12.SetTheta(270)
            c12.SetPhi(270)
            c12.SetWindowSize(anchura + (anchura - c12.GetWw()), altura + (altura - c12.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c12.SaveAs("figura_5.png")
            c12.SaveAs("figura_5.root")
            
            
            
            
            #------------------------------------------------------------------------------
            
            # Rematados os plots que queríamos facer, movémonos á seguinte paleta de cores.
            os.chdir(Ruta_plots)
            os.mkdir('paleta_kSunset')
            os.chdir('paleta_kSunset')
            ROOT.gStyle.SetPalette(103)
            
            # Defino as dimensións dos canvas que vou crear
            altura = 600
            anchura = 1500
            
            
            # Scatter plot normal e corrente
            
            graph = ROOT.TGraph2D(Number_of_points)
            for i in range(Number_of_points): graph.SetPoint(i, y[i], x[i], z[i])
            c1 = ROOT.TCanvas("c")
            graph.SetMarkerStyle(20); graph.Draw("PCOL Z")
            
            # Poño eses ángulos para verse guai
            c1.SetTheta(270)
            c1.SetPhi(270)
            c1.SetWindowSize(anchura + (anchura - c1.GetWw()), altura + (altura - c1.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            c1.SaveAs("figura_1.png")
            c1.SaveAs("figura_1.root")
            
            # Histograma bidimensional
            c2 = ROOT.TCanvas("c")
            graph.Draw("COL Z") # A opción "COL" debuxa unha un histograma bidimensional a 
                                # partires dos puntos que ten o plot.
            
            c2.SetTheta(270)
            c2.SetPhi(270)
            c2.SetWindowSize(anchura + (anchura - c2.GetWw()), altura + (altura - c2.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c2.SaveAs("figura_2.png")
            c2.SaveAs("figura_2.root")
            
            
            
            
            # Plot de superficie
            c3 = ROOT.TCanvas("c")
            graph.Draw("CONT Z") # A opción "CONT" fai un plot empregando un mapa de cores
                                 # para distinguir contornos/superficies.
                               
            c3.SetTheta(270)
            c3.SetPhi(270)
            c3.SetWindowSize(anchura + (anchura - c3.GetWw()), altura + (altura - c3.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c3.SaveAs("figura_3.png")
            c3.SaveAs("figura_3.root")
            
            
            
            # Plot de relieve
            c11 = ROOT.TCanvas("c")
            graph.Draw("SURF3") # A opción "SURF3" fai un plot de superficie igual que fa-
                                # ría a opción "SURF" pero engadindo un relieve sobre a fi-
                                # gura.
            w = 2000
            h = 2000
            
            c11.SetTheta(-30)
            c11.SetPhi(300)
            c11.SetWindowSize(anchura + (anchura - c11.GetWw()), altura + (altura - c11.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            c11.SaveAs("figura_4.png")
            c11.SaveAs("figura_4.root")
            
            
            
            # Triangulación de Delaunay
            c12 = ROOT.TCanvas("c")
            graph.Draw("TRI2 Z") # A opción "TRI2" fai unha reconstrucción por triangulación
                                 # de Delaunay. Moi útil para casos nos que temos imaxes "par-
                                 # cialmente" incompletas ou nos que o scatter plot ofrece unha
                                 # resolución mellorable (vese ambas situacións no noso caso).
            
            c12.SetTheta(270)
            c12.SetPhi(270)
            c12.SetWindowSize(anchura + (anchura - c12.GetWw()), altura + (altura - c12.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c12.SaveAs("figura_5.png")
            c12.SaveAs("figura_5.root")
            
            
            
            
            
            
            #------------------------------------------------------------------------------
            
            # Rematados os plots que queríamos facer, movémonos á seguinte paleta de cores.
            os.chdir(Ruta_plots)
            os.mkdir('paleta_kSolar')
            os.chdir('paleta_kSolar')
            ROOT.gStyle.SetPalette(100)
            
            # Defino as dimensións dos canvas que vou crear
            altura = 600
            anchura = 1500
            
            
            # Scatter plot normal e corrente
            
            graph = ROOT.TGraph2D(Number_of_points)
            for i in range(Number_of_points): graph.SetPoint(i, y[i], x[i], z[i])
            c1 = ROOT.TCanvas("c")
            graph.SetMarkerStyle(20); graph.Draw("PCOL Z")
            
            # Poño eses ángulos para verse guai
            c1.SetTheta(270)
            c1.SetPhi(270)
            c1.SetWindowSize(anchura + (anchura - c1.GetWw()), altura + (altura - c1.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            c1.SaveAs("figura_1.png")
            c1.SaveAs("figura_1.root")
            
            # Histograma bidimensional
            c2 = ROOT.TCanvas("c")
            graph.Draw("COL Z") # A opción "COL" debuxa unha un histograma bidimensional a 
                                # partires dos puntos que ten o plot.
            
            c2.SetTheta(270)
            c2.SetPhi(270)
            c2.SetWindowSize(anchura + (anchura - c2.GetWw()), altura + (altura - c2.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c2.SaveAs("figura_2.png")
            c2.SaveAs("figura_2.root")
            
            
            
            
            # Plot de superficie
            c3 = ROOT.TCanvas("c")
            graph.Draw("CONT Z") # A opción "CONT" fai un plot empregando un mapa de cores
                                 # para distinguir contornos/superficies.
                               
            c3.SetTheta(270)
            c3.SetPhi(270)
            c3.SetWindowSize(anchura + (anchura - c3.GetWw()), altura + (altura - c3.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c3.SaveAs("figura_3.png")
            c3.SaveAs("figura_3.root")
            
            
            
            # Plot de relieve
            c11 = ROOT.TCanvas("c")
            graph.Draw("SURF3") # A opción "SURF3" fai un plot de superficie igual que fa-
                                # ría a opción "SURF" pero engadindo un relieve sobre a fi-
                                # gura.
            w = 2000
            h = 2000
            
            c11.SetTheta(-30)
            c11.SetPhi(300)
            c11.SetWindowSize(anchura + (anchura - c11.GetWw()), altura + (altura - c11.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            c11.SaveAs("figura_4.png")
            c11.SaveAs("figura_4.root")
            
            
            
            # Triangulación de Delaunay
            c12 = ROOT.TCanvas("c")
            graph.Draw("TRI2 Z") # A opción "TRI2" fai unha reconstrucción por triangulación
                                 # de Delaunay. Moi útil para casos nos que temos imaxes "par-
                                 # cialmente" incompletas ou nos que o scatter plot ofrece unha
                                 # resolución mellorable (vese ambas situacións no noso caso).
            
            c12.SetTheta(270)
            c12.SetPhi(270)
            c12.SetWindowSize(anchura + (anchura - c12.GetWw()), altura + (altura - c12.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c12.SaveAs("figura_5.png")
            c12.SaveAs("figura_5.root")
            
            
            #------------------------------------------------------------------------------
            
            # Rematados os plots que queríamos facer, movémonos á seguinte paleta de cores.
            os.chdir(Ruta_plots)
            os.mkdir('paleta_kBlueRedYellow')
            os.chdir('paleta_kBlueRedYellow')
            ROOT.gStyle.SetPalette(60)
            
            # Defino as dimensións dos canvas que vou crear
            altura = 600
            anchura = 1500
            
            
            # Scatter plot normal e corrente
            
            graph = ROOT.TGraph2D(Number_of_points)
            for i in range(Number_of_points): graph.SetPoint(i, y[i], x[i], z[i])
            c1 = ROOT.TCanvas("c")
            graph.SetMarkerStyle(20); graph.Draw("PCOL Z")
            
            # Poño eses ángulos para verse guai
            c1.SetTheta(270)
            c1.SetPhi(270)
            c1.SetWindowSize(anchura + (anchura - c1.GetWw()), altura + (altura - c1.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            c1.SaveAs("figura_1.png")
            c1.SaveAs("figura_1.root")
            
            # Histograma bidimensional
            c2 = ROOT.TCanvas("c")
            graph.Draw("COL Z") # A opción "COL" debuxa unha un histograma bidimensional a 
                                # partires dos puntos que ten o plot.
            
            c2.SetTheta(270)
            c2.SetPhi(270)
            c2.SetWindowSize(anchura + (anchura - c2.GetWw()), altura + (altura - c2.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c2.SaveAs("figura_2.png")
            c2.SaveAs("figura_2.root")
            
            
            
            
            # Plot de superficie
            c3 = ROOT.TCanvas("c")
            graph.Draw("CONT Z") # A opción "CONT" fai un plot empregando un mapa de cores
                                 # para distinguir contornos/superficies.
                               
            c3.SetTheta(270)
            c3.SetPhi(270)
            c3.SetWindowSize(anchura + (anchura - c3.GetWw()), altura + (altura - c3.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c3.SaveAs("figura_3.png")
            c3.SaveAs("figura_3.root")
            
            
            
            # Plot de relieve
            c11 = ROOT.TCanvas("c")
            graph.Draw("SURF3") # A opción "SURF3" fai un plot de superficie igual que fa-
                                # ría a opción "SURF" pero engadindo un relieve sobre a fi-
                                # gura.
            w = 2000
            h = 2000
            
            c11.SetTheta(-30)
            c11.SetPhi(300)
            c11.SetWindowSize(anchura + (anchura - c11.GetWw()), altura + (altura - c11.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            c11.SaveAs("figura_4.png")
            c11.SaveAs("figura_4.root")
            
            
            
            # Triangulación de Delaunay
            c12 = ROOT.TCanvas("c")
            graph.Draw("TRI2 Z") # A opción "TRI2" fai unha reconstrucción por triangulación
                                 # de Delaunay. Moi útil para casos nos que temos imaxes "par-
                                 # cialmente" incompletas ou nos que o scatter plot ofrece unha
                                 # resolución mellorable (vese ambas situacións no noso caso).
            
            c12.SetTheta(270)
            c12.SetPhi(270)
            c12.SetWindowSize(anchura + (anchura - c12.GetWw()), altura + (altura - c12.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c12.SaveAs("figura_5.png")
            c12.SaveAs("figura_5.root")
            
            
            
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            
            #??????????????????????????????????????????????????????????????????????????????
            
            # Atendendo ao TTree que fixen, vemos que o histograma "columna_x" ofrécenos unha
            # relación de recurrencias nas que temos distribuidas as nosas antenas ao longo
            # do eixo x (e o mesmo para o y e para o z, sendo este último un único valor por
            # estar todas as antenas á mesma altura sobre o nivel do mar). Pero o que me
            # chama a atención é o histograma "maximos", pois permítenos ver "cantas antenas
            # rexistran TAL valor máximo de sinal", e isto ofrece bastantes posibilidades.
            
            # O primeiro que se me ocorre é empregalo como FILTRO de sinal.
            # Imos acceder ao TTree e coller un valor mínimo do campo eléctrico e logo crear
            # uns plots alternativos na cal vexamos só a sinal verdadeiramente forte.
            
            os.chdir(Nome_carpeta)
            
            # Primeiro defino as listas onde almacenarei os valores que obteño do TTree
            maximos_filtro = []
            columna_x_filtro = []
            columna_y_filtro = []
            columna_z_filtro = []
            instante_inicial = time.time()
            
            # Abrimos o arquivo.root onde tenemos o TTree:
            ARQUIVO = ROOT.TFile("Simulacions_TTree.root","old")
            
            # Xeramos un punteiro ao TTree que buscamos:
            tree_que_busco = ARQUIVO.Get("Almacen_parametros_simulacion")
            
            # Almacenamos o número total de entradas que ten o TTree, é dicir,o número de
            # filas que conteñe se fixésemos a instrucción: tree_que_busco.Scan()
            Numero_de_entradas = tree_que_busco.GetEntries()
            
            SINAL_FILTRADA = 12000
            
            # Agora iteramos en cada TBranch do Tree:
            for i in range(Numero_de_entradas):
                entry = tree_que_busco.GetEntry(i) # Metémonos na fila i-ésima
                if tree_que_busco.maximos >= SINAL_FILTRADA: # Aplicamos o filtro
                    maximos_filtro.append(tree_que_busco.maximos)
                    columna_x_filtro.append(tree_que_busco.columna_x)
                    columna_y_filtro.append(tree_que_busco.columna_y)
                    columna_z_filtro.append(tree_que_busco.columna_z)
                else:
                    continue # Se a sinal non pasa o filtro seguimos
            
            # Xa teríamos a sinal filtrada
            instante_final = time.time()
            
            duracion = instante_final-instante_inicial
            
            print()
            print('Duración da lectura directa do TTree: ',duracion,' s.')
            print()
            
            ARQUIVO.Close()
            
            
            # Imos crear outro TTree con estes valores
            
            
            # Defino primeiro as miñas variables auxiliares de almacén:
            a = array('d',[0.])
            b = array('d',[0.])
            c = array('d',[0.])
            d = array('d',[0.])
            
            # Abrimos o arquivo.root onde tenemos o TTree:
            ARQUIVO = ROOT.TFile("Simulacions_TTree.root","UPDATE") # Poño a opción UPDATE
                                                                    # porque vou modificar
                                                                    # o arquivo orixinal.
            # Creamos o TTree:
            ARBORE_2 = ROOT.TTree("Sinal_filtrada","Outro Tree simplon")
            
            # Definimos cada rama do noso Tree:
            ARBORE_2.Branch("columna_x",a,"a/D")
            ARBORE_2.Branch("columna_y",b,"b/D")
            ARBORE_2.Branch("columna_z",c,"c/D")
            ARBORE_2.Branch("maximos",d,"d/D")
            
            # Agora enchemos todas as ramas coas listas completas que queremos:
            for i in range(len(maximos_filtro)):
                a[0] = columna_x_filtro[i]
                b[0] = columna_y_filtro[i]
                c[0] = columna_z_filtro[i]
                d[0] = maximos_filtro[i]
                ARBORE_2.Fill()
            
            # Aplicamos os cambios e gardamos:
            ARBORE_2.Write()
            ARQUIVO.Close()
            
            
            
            # Agora imos facer uns cantos plots a ver que tal:
            
            os.chdir(Ruta_plots)
            
            
            
            # Vou mover todo primeiro a unha carpeta chamada "Sinal"
            
            os.mkdir('Filtro')
            os.chdir('Filtro')
            Ruta_filtro = os.getcwd()
            
            
            os.chdir(Ruta_filtro) # Movémonos á carpeta onde poremos a sinal filtrada
            
            # Gardamos primeiro a imaxe xerada con matplotlib:
            
            plt.close('all')
            plt.rcParams['figure.figsize'] = 15, 6
            plt.rcParams['axes.facecolor'] = 'black' # Para que tengamos un background de la imagen final negro (es por estética)
            plt.scatter(columna_x_filtro,columna_y_filtro,c=maximos_filtro,s=30,cmap='inferno')
            
            plt.title('Neutrino de 10 EeV de enerxía interaccionando a unha profundidade de 700 g·cm⁻² na atmósfera e cun ángulo cenital de 75⁰')
            plt.xlabel('Posición das antenas con respecto ao eixo da fervenza (m)')
            plt.ylabel('Posición das antenas con respecto ao eixo da fervenza (m)')
            cbar = plt.colorbar()    # Creo la barra de leyenda de colores
            cbar.set_label('Envolvente de Hilbert do campo eléctrico (μV·m⁻¹)')
            plt.savefig('Sinal_filtrada')   
             
            plt.rcParams['axes.facecolor'] = 'white' # Regresamos el fondo blanco por si nos movemos a otros programas
            plt.close('all')
            
            # E agora gardamos a imaxe xerada con ROOT
            
            ROOT.gStyle.SetPalette(55)
            
            # Defino as dimensións dos canvas que vou crear
            altura = 600
            anchura = 1500
            
            
            
            
            # Recuperamos los valores que sacamos de las simulaciones
            x = columna_x_filtro
            y = columna_y_filtro
            z = maximos_filtro
            Number_of_points = len(z)
            graph = ROOT.TGraph2D(Number_of_points)
            for i in range(Number_of_points): graph.SetPoint(i, y[i], x[i], z[i])
            c1 = ROOT.TCanvas("c")
            
            
            # Scatter plot normal e corrente
            
            graph = ROOT.TGraph2D(Number_of_points)
            for i in range(Number_of_points): graph.SetPoint(i, y[i], x[i], z[i])
            c1 = ROOT.TCanvas("c")
            graph.SetMarkerStyle(20); graph.Draw("PCOL Z")
            
            # Poño eses ángulos para verse guai
            c1.SetTheta(270)
            c1.SetPhi(270)
            c1.SetWindowSize(anchura + (anchura - c1.GetWw()), altura + (altura - c1.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            c1.SaveAs("figura_1.png")
            c1.SaveAs("figura_1.root")
            
            # Histograma bidimensional
            c2 = ROOT.TCanvas("c")
            graph.Draw("COL Z") # A opción "COL" debuxa unha un histograma bidimensional a 
                                # partires dos puntos que ten o plot.
            
            c2.SetTheta(270)
            c2.SetPhi(270)
            c2.SetWindowSize(anchura + (anchura - c2.GetWw()), altura + (altura - c2.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c2.SaveAs("figura_2.png")
            c2.SaveAs("figura_2.root")
            
            
            
            
            # Plot de superficie
            c3 = ROOT.TCanvas("c")
            graph.Draw("CONT Z") # A opción "CONT" fai un plot empregando un mapa de cores
                                 # para distinguir contornos/superficies.
                               
            c3.SetTheta(270)
            c3.SetPhi(270)
            c3.SetWindowSize(anchura + (anchura - c3.GetWw()), altura + (altura - c3.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c3.SaveAs("figura_3.png")
            c3.SaveAs("figura_3.root")
            
            
            
            # Plot de relieve
            c11 = ROOT.TCanvas("c")
            graph.Draw("SURF3") # A opción "SURF3" fai un plot de superficie igual que fa-
                                # ría a opción "SURF" pero engadindo un relieve sobre a fi-
                                # gura.
            w = 2000
            h = 2000
            
            c11.SetTheta(-30)
            c11.SetPhi(300)
            c11.SetWindowSize(anchura + (anchura - c11.GetWw()), altura + (altura - c11.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            c11.SaveAs("figura_4.png")
            c11.SaveAs("figura_4.root")
            
            
            
            # Triangulación de Delaunay
            c12 = ROOT.TCanvas("c")
            graph.Draw("TRI2 Z") # A opción "TRI2" fai unha reconstrucción por triangulación
                                 # de Delaunay. Moi útil para casos nos que temos imaxes "par-
                                 # cialmente" incompletas ou nos que o scatter plot ofrece unha
                                 # resolución mellorable (vese ambas situacións no noso caso).
            
            c12.SetTheta(270)
            c12.SetPhi(270)
            c12.SetWindowSize(anchura + (anchura - c12.GetWw()), altura + (altura - c12.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c12.SaveAs("figura_5.png")
            c12.SaveAs("figura_5.root")
            
        
        
            #??????????????????????????????????????????????????????????????????????????
        
    
        else: # Se xa temos o arquivo Simulacions_TTree.root imos lelo directamente
        
            Ruta_arquivo_root = self.ruta_simulacions.get() 
            print()
            os.chdir(Ruta_arquivo_root)
            Ruta_arquivo_root = os.getcwd()

            
            # Primeiro defino as listas onde almacenarei os valores que obteño do TTree
            # (Chamándoas co mesmo nome que a lectura con Python podo checkear se vai ben)
            maximos = []
            columna_x = []
            columna_y = []
            columna_z = []
            instante_inicial = time.time()
        
            # Abrimos o arquivo.root onde tenemos o TTree:
            ARQUIVO = ROOT.TFile("Simulacions_TTree.root","update")
        
            # Xeramos un punteiro ao TTree que buscamos:
            tree_que_busco = ARQUIVO.Get("Almacen_parametros_simulacion")
        
            # Almacenamos o número total de entradas que ten o TTree, é dicir,o número de
            # filas que conteñe se fixésemos a instrucción: tree_que_busco.Scan()
            Numero_de_entradas = tree_que_busco.GetEntries()
            
            
            # Agora iteramos en cada TBranch do Tree:
            for i in range(Numero_de_entradas):
                entry = tree_que_busco.GetEntry(i) # Metémonos na fila i-ésima
                maximos.append(tree_que_busco.maximos)
                columna_x.append(tree_que_busco.columna_x)
                columna_y.append(tree_que_busco.columna_y)
                columna_z.append(tree_que_busco.columna_z)
                
            # Xa teríamos de volta todos os parámetros e nun instante!!
            instante_final = time.time()
        
            duracion = instante_final-instante_inicial
            
            print()
            print('Duración da lectura directa do TTree: ',duracion,' s.')
            print()
        
            # Vou crear a maiores uns histogramas co cales farei algunhas cousas:
            histmax = ROOT.TH1F("campos electricos (factor rebinning 28)", "Test data", 350, np.min(maximos), np.max(maximos))    
            histx = ROOT.TH1F("posicions eixo x (factor rebinning 28)", "Test data", 350, np.min(columna_x), np.max(columna_x))    
            histy = ROOT.TH1F("posicions eixo y (factor rebinning 28)", "Test data", 350, np.min(columna_y), np.max(columna_y))    
        
            for i in range(Numero_de_entradas):
                entry = tree_que_busco.GetEntry(i) # Metémonos na fila i-ésima
                histmax.Fill(tree_que_busco.maximos)
                histx.Fill(tree_que_busco.columna_x)
                histy.Fill(tree_que_busco.columna_y)
        
            # Customización do histograma maximos
            histmax.GetXaxis().SetTitle("Campos electricos")
            histmax.Draw()
            histmax.Write()
        
            #-----
        
            # Customización do histograma Y
            c = ROOT.TCanvas("Canvas", "Canvas", 1000, 800)
            histy.GetXaxis().SetTitle("Posicion das antenas no eixo y")
            histy.Draw()
            axuste_y = histy.Fit("gaus","","",np.min(columna_y),np.max(columna_y))
            
            # Engadimos a lenda ao histograma
            legend = ROOT.TLegend(0.1,0.7,0.43,0.9)
            legend.AddEntry(histy, "Datos", "l")
            legend.Draw()
            
            histy.Write()
            
            # Actualizamos o canvas:
            c.Draw()
            c.Update()
        
            #-----
            
            # Customización do histograma X
            c = ROOT.TCanvas("Canvas", "Canvas", 1000, 800)
            histx.GetXaxis().SetTitle("Posicions das antenas no eixo x")
            histx.Draw()
            # Facemos primeiro o axuste do primeiro pico
            
            g1    =  ROOT.TF1("g1","gaus",np.min(columna_x),0)
            axuste_1x = histx.Fit(g1,"R+")
        
            # Engadimos a lenda ao histograma
            legend = ROOT.TLegend(0.1,0.7,0.43,0.9)
            legend.AddEntry(histx, "Datos", "l")
            legend.Draw()
            
            histx.Write()
            
            # Actualizamos o canvas:
            c.Draw()
            c.Update()
        
            # Rescatamos de novo o histograma e facemos o fit do segundo pico:
            histx = ARQUIVO.Get('posicions eixo x (factor rebinning 28)')
        
            # Customización do histograma X
            c = ROOT.TCanvas("Canvas", "Canvas", 1000, 800)
            histx.GetXaxis().SetTitle("Posicions das antenas no eixo x")
            histx.Draw()
            # Facemos primeiro o axuste do primeiro pico
            g2    =  ROOT.TF1("g2","gaus",0,np.max(columna_x))
            axuste_2x = histx.Fit(g2,"R+")    
        
            # Engadimos a lenda ao histograma
            legend = ROOT.TLegend(0.1,0.7,0.43,0.9)
            legend.AddEntry(histx, "Datos", "l")
            legend.Draw()
            
            histx.Write()
            
            # Actualizamos o canvas:
            c.Draw()
            c.Update()
        
            ARQUIVO.Close()
        
        
            # Imos escribir os resultados do axuste nun arquivo de texto externo:
        
            ARQUIVO = ROOT.TFile("Simulacions_TTree.root","update")
            histx = ARQUIVO.Get('posicions eixo x (factor rebinning 28);2')    
            histy = ARQUIVO.Get('posicions eixo y (factor rebinning 28)')    
        
            g1x =histx.GetFunction('g1')
            g2x =histx.GetFunction('g2')
            gy =histy.GetFunction('gaus')
            
            resultados = open("resultados_dos_fits.txt","w+")
        
            resultados.write("###########################\n")                    
            resultados.write("    RESULTADOS DOS FITS    \n")
            resultados.write("###########################\n")
            resultados.write("\n")                     
            resultados.write("\n")                     
            resultados.write("\n")                     
            resultados.write("Parámetros do axuste á gaussiana da columna y:\n")                     
            resultados.write("\n")                     
            resultados.write("%f    %f    %f\n"%(gy.GetParameter(0),gy.GetParameter(1),2*gy.GetParameter(2)))                     
            resultados.write("\n")                     
            resultados.write("Parámetros dos axustes ás gaussianas da columna x:\n")                     
            resultados.write("\n")                     
            resultados.write("%f    %f    %f\n"%(g1x.GetParameter(0),g1x.GetParameter(1),2*g1x.GetParameter(2)))                     
            resultados.write("%f    %f    %f\n"%(g2x.GetParameter(0),g2x.GetParameter(1),2*g2x.GetParameter(2)))                     
            resultados.close()
            
            Anchura_elipse = (2*g1x.GetParameter(2) + np.abs(g1x.GetParameter(1))/2.) + (2*g2x.GetParameter(2) + np.abs(g1x.GetParameter(1))/2.)
            Altura_elipse = 2*gy.GetParameter(2)
            
            ARQUIVO.Close()
        
        
        
        
        
        
            #??????????????????????????????????????????????????????????????????????????
            
            # Plots da lectura directa do TTree:
            
            # Imos crear a modo exemplo uns plots con distintas paletas de cores (para facer
            # máis ilustrativos os plots. Para iso gardaremos as figuras en diferentes car-
            # petas en función da paleta que empreguemos.
            # No final deste script atópase un exemplo e os códigos de paletas para ROOT.
                    
            
            os.mkdir('plots')
            os.chdir('plots')
            Ruta_plots = os.getcwd()
            
            
            # Primeiro ploteo con matplotlib a imaxe e logo creamos uns cantos directo-
            # rios con distintas paletas e plots con ROOT:
            plt.rcParams['figure.figsize'] = 15, 6
            plt.rcParams['axes.facecolor'] = 'black' # Para que tengamos un background de la imagen final negro (es por estética)
            plt.scatter(columna_x,columna_y,c=maximos,s=30,cmap='inferno')
        
            plt.title('Neutrino de 10 EeV de enerxía interaccionando a unha profundidade de 700 g·cm⁻² na atmósfera e cun ángulo cenital de 75⁰')
            plt.xlabel('Posición das antenas con respecto ao eixo da fervenza (m)')
            plt.ylabel('Posición das antenas con respecto ao eixo da fervenza (m)')
            cbar = plt.colorbar()    # Creo la barra de leyenda de colores
            cbar.set_label('Envolvente de Hilbert do campo eléctrico (μV·m⁻¹)')
            
            plt.rcParams['axes.facecolor'] = 'white' # Regresamos el fondo blanco por si nos movemos a otros programas
            
            plt.savefig('Sinal_matplotlib')
            plt.close('all')
            
        
            # A partires dos valores dos fits imos recrear a elipse da sinal en terra:
            
            plt.rcParams['axes.facecolor'] = 'black' # Para que tengamos un background de la imagen final negro (es por estética)
            
            NUM = 1
            
            ells = [Ellipse(xy=array('f',[0,0]), width=Anchura_elipse, height=Altura_elipse, angle=0.)
                    for i in range(NUM)]
            
            fig = plt.figure(0)
            ax = fig.add_subplot(111, aspect='equal')
            for e in ells:
                ax.add_artist(e)
                e.set_clip_box(ax.bbox)
                e.set_alpha(0.5)
            
            plt.rcParams['figure.figsize'] = 15, 6
        
            plt.scatter(columna_x,columna_y,c=maximos,cmap='inferno')
            ax.set_xlim(np.min(columna_x), np.max(columna_x))
            ax.set_ylim(np.min(columna_y), np.max(columna_y))
            
            plt.xlabel('Pocición das antenas respecto ao core da fervenza - Este (m)')
            plt.ylabel('Pocición das antenas respecto ao core da fervenza - Norte (m)')
            cbar = plt.colorbar()    # Creo la barra de leyenda de colores
            cbar.set_label('Envolvente de Hilbert do campo eléctrico (μV·m⁻¹)')
            plt.title('Neutrino de 10 EeV de enerxía interaccionando a unha profundidade de 700 g·cm⁻² na atmósfera e cun ángulo cenital de 75⁰')
            
        
            
            plt.show()
            plt.savefig('Elipticidade_da_sinal.png')
            plt.close('all')
            
            plt.rcParams['axes.facecolor'] = 'white' # Para que tengamos un background de la imagen final negro (es por estética)
            
            
            
            
            
            
            
            os.mkdir('paleta_por_defecto')
            os.chdir('paleta_por_defecto')
            
            
            # Creación de scatter color plots en ROOT
            
            ROOT.gStyle.SetPalette(57) # Por se acaso non tiñamos xa de antes posta a paleta.
            
            # Defino as dimensións dos canvas que vou crear
            altura = 600
            anchura = 1500
            
            
            # Recuperamos los valores que sacamos de las simulaciones
            x = columna_x
            y = columna_y
            z = maximos
            Number_of_points = len(z)
            graph = ROOT.TGraph2D(Number_of_points)
            for i in range(Number_of_points): graph.SetPoint(i, y[i], x[i], z[i])
            c1 = ROOT.TCanvas("c")
            graph.SetMarkerStyle(20); graph.Draw("PCOL Z") # A opción "PCOL" fai un scatter
                                                           # plot dos puntos que definimos
                                                           # antes. Ademáis, a opción "Z" ao
                                                           # seu carón indica que queremos
                                                           # mostrar tamén una barra de co-
                                                           # res a modo "lenda"
            
            # Poño eses ángulos para verse guai
            c1.SetTheta(270)
            c1.SetPhi(270)
            c1.SetWindowSize(anchura + (anchura - c1.GetWw()), altura + (altura - c1.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            c1.SaveAs("figura_1.png")
            c1.SaveAs("figura_1.root")
            
            
            
            # Imos facer outros plots alternativos interesantes:
            
            
            # Histograma bidimensional
            c2 = ROOT.TCanvas("c")
            graph.Draw("COL Z") # A opción "COL" debuxa unha un histograma bidimensional a 
                                # partires dos puntos que ten o plot.
            
            c2.SetTheta(270)
            c2.SetPhi(270)
            c2.SetWindowSize(anchura + (anchura - c2.GetWw()), altura + (altura - c2.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c2.SaveAs("figura_2.png")
            c2.SaveAs("figura_2.root")
            
            
            
            
            # Plot de superficie
            c3 = ROOT.TCanvas("c")
            graph.Draw("CONT Z") # A opción "CONT" fai un plot empregando un mapa de cores
                                 # para distinguir contornos/superficies.
                               
            c3.SetTheta(270)
            c3.SetPhi(270)
            c3.SetWindowSize(anchura + (anchura - c3.GetWw()), altura + (altura - c3.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c3.SaveAs("figura_3.png")
            c3.SaveAs("figura_3.root")
            
            
            
            # Plot de relieve
            c11 = ROOT.TCanvas("c")
            graph.Draw("SURF3") # A opción "SURF3" fai un plot de superficie igual que fa-
                                # ría a opción "SURF" pero engadindo un relieve sobre a fi-
                                # gura.
            w = 2000
            h = 2000
            
            c11.SetTheta(-30)
            c11.SetPhi(300)
            c11.SetWindowSize(anchura + (anchura - c11.GetWw()), altura + (altura - c11.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            c11.SaveAs("figura_4.png")
            c11.SaveAs("figura_4.root")
            
            
            
            # Triangulación de Delaunay
            c12 = ROOT.TCanvas("c")
            graph.Draw("TRI2 Z") # A opción "TRI2" fai unha reconstrucción por triangulación
                                 # de Delaunay. Moi útil para casos nos que temos imaxes "par-
                                 # cialmente" incompletas ou nos que o scatter plot ofrece unha
                                 # resolución mellorable (vese ambas situacións no noso caso).
            
            c12.SetTheta(270)
            c12.SetPhi(270)
            c12.SetWindowSize(anchura + (anchura - c12.GetWw()), altura + (altura - c12.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c12.SaveAs("figura_5.png")
            c12.SaveAs("figura_5.root")
            
            
            #------------------------------------------------------------------------------
            
            # Rematados os plots que queríamos facer, movémonos á seguinte paleta de cores.
            os.chdir(Ruta_plots)
            os.mkdir('paleta_kDarkBodyRadiator')
            os.chdir('paleta_kDarkBodyRadiator')
            ROOT.gStyle.SetPalette(53)
            
            # Defino as dimensións dos canvas que vou crear
            altura = 600
            anchura = 1500
            
            
            # Scatter plot normal e corrente
            
            graph = ROOT.TGraph2D(Number_of_points)
            for i in range(Number_of_points): graph.SetPoint(i, y[i], x[i], z[i])
            c1 = ROOT.TCanvas("c")
            graph.SetMarkerStyle(20); graph.Draw("PCOL Z")
            
            # Poño eses ángulos para verse guai
            c1.SetTheta(270)
            c1.SetPhi(270)
            c1.SetWindowSize(anchura + (anchura - c1.GetWw()), altura + (altura - c1.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            c1.SaveAs("figura_1.png")
            c1.SaveAs("figura_1.root")
            
            # Histograma bidimensional
            c2 = ROOT.TCanvas("c")
            graph.Draw("COL Z") # A opción "COL" debuxa unha un histograma bidimensional a 
                                # partires dos puntos que ten o plot.
            
            c2.SetTheta(270)
            c2.SetPhi(270)
            c2.SetWindowSize(anchura + (anchura - c2.GetWw()), altura + (altura - c2.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c2.SaveAs("figura_2.png")
            c2.SaveAs("figura_2.root")
            
            
            
            
            # Plot de superficie
            c3 = ROOT.TCanvas("c")
            graph.Draw("CONT Z") # A opción "CONT" fai un plot empregando un mapa de cores
                                 # para distinguir contornos/superficies.
                               
            c3.SetTheta(270)
            c3.SetPhi(270)
            c3.SetWindowSize(anchura + (anchura - c3.GetWw()), altura + (altura - c3.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c3.SaveAs("figura_3.png")
            c3.SaveAs("figura_3.root")
            
            
            
            # Plot de relieve
            c11 = ROOT.TCanvas("c")
            graph.Draw("SURF3") # A opción "SURF3" fai un plot de superficie igual que fa-
                                # ría a opción "SURF" pero engadindo un relieve sobre a fi-
                                # gura.
            w = 2000
            h = 2000
            
            c11.SetTheta(-30)
            c11.SetPhi(300)
            c11.SetWindowSize(anchura + (anchura - c11.GetWw()), altura + (altura - c11.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            c11.SaveAs("figura_4.png")
            c11.SaveAs("figura_4.root")
            
            
            
            # Triangulación de Delaunay
            c12 = ROOT.TCanvas("c")
            graph.Draw("TRI2 Z") # A opción "TRI2" fai unha reconstrucción por triangulación
                                 # de Delaunay. Moi útil para casos nos que temos imaxes "par-
                                 # cialmente" incompletas ou nos que o scatter plot ofrece unha
                                 # resolución mellorable (vese ambas situacións no noso caso).
            
            c12.SetTheta(270)
            c12.SetPhi(270)
            c12.SetWindowSize(anchura + (anchura - c12.GetWw()), altura + (altura - c12.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c12.SaveAs("figura_5.png")
            c12.SaveAs("figura_5.root")
            
            
            
            
            
            #------------------------------------------------------------------------------
            
            # Rematados os plots que queríamos facer, movémonos á seguinte paleta de cores.
            os.chdir(Ruta_plots)
            os.mkdir('paleta_kRainBow')
            os.chdir('paleta_kRainBow')
            ROOT.gStyle.SetPalette(55)
            
            # Defino as dimensións dos canvas que vou crear
            altura = 600
            anchura = 1500
            
            
            # Scatter plot normal e corrente
            
            graph = ROOT.TGraph2D(Number_of_points)
            for i in range(Number_of_points): graph.SetPoint(i, y[i], x[i], z[i])
            c1 = ROOT.TCanvas("c")
            graph.SetMarkerStyle(20); graph.Draw("PCOL Z")
            
            # Poño eses ángulos para verse guai
            c1.SetTheta(270)
            c1.SetPhi(270)
            c1.SetWindowSize(anchura + (anchura - c1.GetWw()), altura + (altura - c1.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            c1.SaveAs("figura_1.png")
            c1.SaveAs("figura_1.root")
            
            # Histograma bidimensional
            c2 = ROOT.TCanvas("c")
            graph.Draw("COL Z") # A opción "COL" debuxa unha un histograma bidimensional a 
                                # partires dos puntos que ten o plot.
            
            c2.SetTheta(270)
            c2.SetPhi(270)
            c2.SetWindowSize(anchura + (anchura - c2.GetWw()), altura + (altura - c2.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c2.SaveAs("figura_2.png")
            c2.SaveAs("figura_2.root")
            
            
            
            
            # Plot de superficie
            c3 = ROOT.TCanvas("c")
            graph.Draw("CONT Z") # A opción "CONT" fai un plot empregando un mapa de cores
                                 # para distinguir contornos/superficies.
                               
            c3.SetTheta(270)
            c3.SetPhi(270)
            c3.SetWindowSize(anchura + (anchura - c3.GetWw()), altura + (altura - c3.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c3.SaveAs("figura_3.png")
            c3.SaveAs("figura_3.root")
            
            
            
            # Plot de relieve
            c11 = ROOT.TCanvas("c")
            graph.Draw("SURF3") # A opción "SURF3" fai un plot de superficie igual que fa-
                                # ría a opción "SURF" pero engadindo un relieve sobre a fi-
                                # gura.
            w = 2000
            h = 2000
            
            c11.SetTheta(-30)
            c11.SetPhi(300)
            c11.SetWindowSize(anchura + (anchura - c11.GetWw()), altura + (altura - c11.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            c11.SaveAs("figura_4.png")
            c11.SaveAs("figura_4.root")
            
            
            
            # Triangulación de Delaunay
            c12 = ROOT.TCanvas("c")
            graph.Draw("TRI2 Z") # A opción "TRI2" fai unha reconstrucción por triangulación
                                 # de Delaunay. Moi útil para casos nos que temos imaxes "par-
                                 # cialmente" incompletas ou nos que o scatter plot ofrece unha
                                 # resolución mellorable (vese ambas situacións no noso caso).
            
            c12.SetTheta(270)
            c12.SetPhi(270)
            c12.SetWindowSize(anchura + (anchura - c12.GetWw()), altura + (altura - c12.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c12.SaveAs("figura_5.png")
            c12.SaveAs("figura_5.root")
            
            
            
            
            #------------------------------------------------------------------------------
            
            # Rematados os plots que queríamos facer, movémonos á seguinte paleta de cores.
            os.chdir(Ruta_plots)
            os.mkdir('paleta_kSunset')
            os.chdir('paleta_kSunset')
            ROOT.gStyle.SetPalette(103)
            
            # Defino as dimensións dos canvas que vou crear
            altura = 600
            anchura = 1500
            
            
            # Scatter plot normal e corrente
            
            graph = ROOT.TGraph2D(Number_of_points)
            for i in range(Number_of_points): graph.SetPoint(i, y[i], x[i], z[i])
            c1 = ROOT.TCanvas("c")
            graph.SetMarkerStyle(20); graph.Draw("PCOL Z")
            
            # Poño eses ángulos para verse guai
            c1.SetTheta(270)
            c1.SetPhi(270)
            c1.SetWindowSize(anchura + (anchura - c1.GetWw()), altura + (altura - c1.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            c1.SaveAs("figura_1.png")
            c1.SaveAs("figura_1.root")
            
            # Histograma bidimensional
            c2 = ROOT.TCanvas("c")
            graph.Draw("COL Z") # A opción "COL" debuxa unha un histograma bidimensional a 
                                # partires dos puntos que ten o plot.
            
            c2.SetTheta(270)
            c2.SetPhi(270)
            c2.SetWindowSize(anchura + (anchura - c2.GetWw()), altura + (altura - c2.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c2.SaveAs("figura_2.png")
            c2.SaveAs("figura_2.root")
            
            
            
            
            # Plot de superficie
            c3 = ROOT.TCanvas("c")
            graph.Draw("CONT Z") # A opción "CONT" fai un plot empregando un mapa de cores
                                 # para distinguir contornos/superficies.
                               
            c3.SetTheta(270)
            c3.SetPhi(270)
            c3.SetWindowSize(anchura + (anchura - c3.GetWw()), altura + (altura - c3.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c3.SaveAs("figura_3.png")
            c3.SaveAs("figura_3.root")
            
            
            
            # Plot de relieve
            c11 = ROOT.TCanvas("c")
            graph.Draw("SURF3") # A opción "SURF3" fai un plot de superficie igual que fa-
                                # ría a opción "SURF" pero engadindo un relieve sobre a fi-
                                # gura.
            w = 2000
            h = 2000
            
            c11.SetTheta(-30)
            c11.SetPhi(300)
            c11.SetWindowSize(anchura + (anchura - c11.GetWw()), altura + (altura - c11.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            c11.SaveAs("figura_4.png")
            c11.SaveAs("figura_4.root")
            
            
            
            # Triangulación de Delaunay
            c12 = ROOT.TCanvas("c")
            graph.Draw("TRI2 Z") # A opción "TRI2" fai unha reconstrucción por triangulación
                                 # de Delaunay. Moi útil para casos nos que temos imaxes "par-
                                 # cialmente" incompletas ou nos que o scatter plot ofrece unha
                                 # resolución mellorable (vese ambas situacións no noso caso).
            
            c12.SetTheta(270)
            c12.SetPhi(270)
            c12.SetWindowSize(anchura + (anchura - c12.GetWw()), altura + (altura - c12.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c12.SaveAs("figura_5.png")
            c12.SaveAs("figura_5.root")
            
            
            
            
            
            
            #------------------------------------------------------------------------------
            
            # Rematados os plots que queríamos facer, movémonos á seguinte paleta de cores.
            os.chdir(Ruta_plots)
            os.mkdir('paleta_kSolar')
            os.chdir('paleta_kSolar')
            ROOT.gStyle.SetPalette(100)
            
            # Defino as dimensións dos canvas que vou crear
            altura = 600
            anchura = 1500
            
            
            # Scatter plot normal e corrente
            
            graph = ROOT.TGraph2D(Number_of_points)
            for i in range(Number_of_points): graph.SetPoint(i, y[i], x[i], z[i])
            c1 = ROOT.TCanvas("c")
            graph.SetMarkerStyle(20); graph.Draw("PCOL Z")
            
            # Poño eses ángulos para verse guai
            c1.SetTheta(270)
            c1.SetPhi(270)
            c1.SetWindowSize(anchura + (anchura - c1.GetWw()), altura + (altura - c1.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            c1.SaveAs("figura_1.png")
            c1.SaveAs("figura_1.root")
            
            # Histograma bidimensional
            c2 = ROOT.TCanvas("c")
            graph.Draw("COL Z") # A opción "COL" debuxa unha un histograma bidimensional a 
                                # partires dos puntos que ten o plot.
            
            c2.SetTheta(270)
            c2.SetPhi(270)
            c2.SetWindowSize(anchura + (anchura - c2.GetWw()), altura + (altura - c2.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c2.SaveAs("figura_2.png")
            c2.SaveAs("figura_2.root")
            
            
            
            
            # Plot de superficie
            c3 = ROOT.TCanvas("c")
            graph.Draw("CONT Z") # A opción "CONT" fai un plot empregando un mapa de cores
                                 # para distinguir contornos/superficies.
                               
            c3.SetTheta(270)
            c3.SetPhi(270)
            c3.SetWindowSize(anchura + (anchura - c3.GetWw()), altura + (altura - c3.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c3.SaveAs("figura_3.png")
            c3.SaveAs("figura_3.root")
            
            
            
            # Plot de relieve
            c11 = ROOT.TCanvas("c")
            graph.Draw("SURF3") # A opción "SURF3" fai un plot de superficie igual que fa-
                                # ría a opción "SURF" pero engadindo un relieve sobre a fi-
                                # gura.
            w = 2000
            h = 2000
            
            c11.SetTheta(-30)
            c11.SetPhi(300)
            c11.SetWindowSize(anchura + (anchura - c11.GetWw()), altura + (altura - c11.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            c11.SaveAs("figura_4.png")
            c11.SaveAs("figura_4.root")
            
            
            
            # Triangulación de Delaunay
            c12 = ROOT.TCanvas("c")
            graph.Draw("TRI2 Z") # A opción "TRI2" fai unha reconstrucción por triangulación
                                 # de Delaunay. Moi útil para casos nos que temos imaxes "par-
                                 # cialmente" incompletas ou nos que o scatter plot ofrece unha
                                 # resolución mellorable (vese ambas situacións no noso caso).
            
            c12.SetTheta(270)
            c12.SetPhi(270)
            c12.SetWindowSize(anchura + (anchura - c12.GetWw()), altura + (altura - c12.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c12.SaveAs("figura_5.png")
            c12.SaveAs("figura_5.root")
            
            
            #------------------------------------------------------------------------------
            
            # Rematados os plots que queríamos facer, movémonos á seguinte paleta de cores.
            os.chdir(Ruta_plots)
            os.mkdir('paleta_kBlueRedYellow')
            os.chdir('paleta_kBlueRedYellow')
            ROOT.gStyle.SetPalette(60)
            
            # Defino as dimensións dos canvas que vou crear
            altura = 600
            anchura = 1500
            
            
            # Scatter plot normal e corrente
            
            graph = ROOT.TGraph2D(Number_of_points)
            for i in range(Number_of_points): graph.SetPoint(i, y[i], x[i], z[i])
            c1 = ROOT.TCanvas("c")
            graph.SetMarkerStyle(20); graph.Draw("PCOL Z")
            
            # Poño eses ángulos para verse guai
            c1.SetTheta(270)
            c1.SetPhi(270)
            c1.SetWindowSize(anchura + (anchura - c1.GetWw()), altura + (altura - c1.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            c1.SaveAs("figura_1.png")
            c1.SaveAs("figura_1.root")
            
            # Histograma bidimensional
            c2 = ROOT.TCanvas("c")
            graph.Draw("COL Z") # A opción "COL" debuxa unha un histograma bidimensional a 
                                # partires dos puntos que ten o plot.
            
            c2.SetTheta(270)
            c2.SetPhi(270)
            c2.SetWindowSize(anchura + (anchura - c2.GetWw()), altura + (altura - c2.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c2.SaveAs("figura_2.png")
            c2.SaveAs("figura_2.root")
            
            
            
            
            # Plot de superficie
            c3 = ROOT.TCanvas("c")
            graph.Draw("CONT Z") # A opción "CONT" fai un plot empregando un mapa de cores
                                 # para distinguir contornos/superficies.
                               
            c3.SetTheta(270)
            c3.SetPhi(270)
            c3.SetWindowSize(anchura + (anchura - c3.GetWw()), altura + (altura - c3.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c3.SaveAs("figura_3.png")
            c3.SaveAs("figura_3.root")
            
            
            
            # Plot de relieve
            c11 = ROOT.TCanvas("c")
            graph.Draw("SURF3") # A opción "SURF3" fai un plot de superficie igual que fa-
                                # ría a opción "SURF" pero engadindo un relieve sobre a fi-
                                # gura.
            w = 2000
            h = 2000
            
            c11.SetTheta(-30)
            c11.SetPhi(300)
            c11.SetWindowSize(anchura + (anchura - c11.GetWw()), altura + (altura - c11.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            c11.SaveAs("figura_4.png")
            c11.SaveAs("figura_4.root")
            
            
            
            # Triangulación de Delaunay
            c12 = ROOT.TCanvas("c")
            graph.Draw("TRI2 Z") # A opción "TRI2" fai unha reconstrucción por triangulación
                                 # de Delaunay. Moi útil para casos nos que temos imaxes "par-
                                 # cialmente" incompletas ou nos que o scatter plot ofrece unha
                                 # resolución mellorable (vese ambas situacións no noso caso).
            
            c12.SetTheta(270)
            c12.SetPhi(270)
            c12.SetWindowSize(anchura + (anchura - c12.GetWw()), altura + (altura - c12.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c12.SaveAs("figura_5.png")
            c12.SaveAs("figura_5.root")
        
        
            #??????????????????????????????????????????????????????????????????????????
        
            # Imos crear agora a carpeta co filtro:
            
            os.chdir(Ruta_plots)
            os.mkdir('Filtro')
        
            os.chdir(Ruta_arquivo_root)
        
            # Primeiro defino as listas onde almacenarei os valores que obteño do TTree
            maximos_filtro = []
            columna_x_filtro = []
            columna_y_filtro = []
            columna_z_filtro = []
            instante_inicial = time.time()
        
            # Antes de movernos á carpeta creada, lemos do TTree a Branch co filtro:
            # Abrimos o arquivo.root onde tenemos o TTree:
            ARQUIVO = ROOT.TFile("Simulacions_TTree.root","old")
        
            # Xeramos un punteiro ao TTree que buscamos:
            tree_que_busco = ARQUIVO.Get("Sinal_filtrada")
        
            # Almacenamos o número total de entradas que ten o TTree, é dicir,o número de
            # filas que conteñe se fixésemos a instrucción: tree_que_busco.Scan()
            Numero_de_entradas = tree_que_busco.GetEntries()
        
            # Agora iteramos en cada TBranch do Tree:
            for i in range(Numero_de_entradas):
                entry = tree_que_busco.GetEntry(i) # Metémonos na fila i-ésima
                maximos_filtro.append(tree_que_busco.maximos)
                columna_x_filtro.append(tree_que_busco.columna_x)
                columna_y_filtro.append(tree_que_busco.columna_y)
                columna_z_filtro.append(tree_que_busco.columna_z)
        
            # Xa teríamos de volta todos os parámetros e nun instante!!
            instante_final = time.time()
        
            duracion = instante_final-instante_inicial
            
            print()
            print('Duración da lectura directa do TTree: ',duracion,' s.')
            print()
        
            ARQUIVO.Close()
        
        
            os.chdir(Ruta_plots)
            os.chdir('Filtro')
            Ruta_filtro = os.getcwd()
        
        
        
            # Gardamos primeiro a imaxe xerada con matplotlib:
            
            plt.close('all')
            plt.rcParams['figure.figsize'] = 15, 6
            plt.rcParams['axes.facecolor'] = 'black' # Para que tengamos un background de la imagen final negro (es por estética)
            plt.scatter(columna_x_filtro,columna_y_filtro,c=maximos_filtro,s=30,cmap='inferno')
            
            plt.title('Neutrino de 10 EeV de enerxía interaccionando a unha profundidade de 700 g·cm⁻² na atmósfera e cun ángulo cenital de 75⁰')
            plt.xlabel('Posición das antenas con respecto ao eixo da fervenza (m)')
            plt.ylabel('Posición das antenas con respecto ao eixo da fervenza (m)')
            cbar = plt.colorbar()    # Creo la barra de leyenda de colores
            cbar.set_label('Envolvente de Hilbert do campo eléctrico (μV·m⁻¹)')
            plt.savefig('Sinal_filtrada')   
             
            plt.rcParams['axes.facecolor'] = 'white' # Regresamos el fondo blanco por si nos movemos a otros programas
            plt.close('all')
            
            # E agora gardamos a imaxe xerada con ROOT
            
            ROOT.gStyle.SetPalette(55)
            
            # Defino as dimensións dos canvas que vou crear
            altura = 600
            anchura = 1500
            
            
            
            
            # Recuperamos los valores que sacamos de las simulaciones
            x = columna_x_filtro
            y = columna_y_filtro
            z = maximos_filtro
            Number_of_points = len(z)
            graph = ROOT.TGraph2D(Number_of_points)
            for i in range(Number_of_points): graph.SetPoint(i, y[i], x[i], z[i])
            c1 = ROOT.TCanvas("c")
            
            
            # Scatter plot normal e corrente
            
            graph = ROOT.TGraph2D(Number_of_points)
            for i in range(Number_of_points): graph.SetPoint(i, y[i], x[i], z[i])
            c1 = ROOT.TCanvas("c")
            graph.SetMarkerStyle(20); graph.Draw("PCOL Z")
            
            # Poño eses ángulos para verse guai
            c1.SetTheta(270)
            c1.SetPhi(270)
            c1.SetWindowSize(anchura + (anchura - c1.GetWw()), altura + (altura - c1.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            c1.SaveAs("figura_1.png")
            c1.SaveAs("figura_1.root")
            
            # Histograma bidimensional
            c2 = ROOT.TCanvas("c")
            graph.Draw("COL Z") # A opción "COL" debuxa unha un histograma bidimensional a 
                                # partires dos puntos que ten o plot.
            
            c2.SetTheta(270)
            c2.SetPhi(270)
            c2.SetWindowSize(anchura + (anchura - c2.GetWw()), altura + (altura - c2.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c2.SaveAs("figura_2.png")
            c2.SaveAs("figura_2.root")
            
            
            
            
            # Plot de superficie
            c3 = ROOT.TCanvas("c")
            graph.Draw("CONT Z") # A opción "CONT" fai un plot empregando un mapa de cores
                                 # para distinguir contornos/superficies.
                               
            c3.SetTheta(270)
            c3.SetPhi(270)
            c3.SetWindowSize(anchura + (anchura - c3.GetWw()), altura + (altura - c3.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c3.SaveAs("figura_3.png")
            c3.SaveAs("figura_3.root")
            
            
            
            # Plot de relieve
            c11 = ROOT.TCanvas("c")
            graph.Draw("SURF3") # A opción "SURF3" fai un plot de superficie igual que fa-
                                # ría a opción "SURF" pero engadindo un relieve sobre a fi-
                                # gura.
            w = 2000
            h = 2000
            
            c11.SetTheta(-30)
            c11.SetPhi(300)
            c11.SetWindowSize(anchura + (anchura - c11.GetWw()), altura + (altura - c11.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            c11.SaveAs("figura_4.png")
            c11.SaveAs("figura_4.root")
            
            
            
            # Triangulación de Delaunay
            c12 = ROOT.TCanvas("c")
            graph.Draw("TRI2 Z") # A opción "TRI2" fai unha reconstrucción por triangulación
                                 # de Delaunay. Moi útil para casos nos que temos imaxes "par-
                                 # cialmente" incompletas ou nos que o scatter plot ofrece unha
                                 # resolución mellorable (vese ambas situacións no noso caso).
            
            c12.SetTheta(270)
            c12.SetPhi(270)
            c12.SetWindowSize(anchura + (anchura - c12.GetWw()), altura + (altura - c12.GetWh()))
            graph.GetZaxis().SetTitle("Envolvente de Hilbert do campo eléctrico (#muV )")
            graph.GetYaxis().SetTitle("Posicion das antenas (m) - Este")
            graph.GetXaxis().SetTitle("Posicion das antenas (m) - Norte")
            
            c12.SaveAs("figura_5.png")
            c12.SaveAs("figura_5.root")
        
        
        
        
        
        
        #------------------------------------------------------------------------------
        
        
        '''
        
        
        c4 = ROOT.TCanvas("c")
        
        graph.Draw("CONT1")
        # Le pongo esos ángulos porque así se ve guay
        c4.SetTheta(270)
        c4.SetPhi(270)
        
        c4.SaveAs("example4.png")
        c4.SaveAs("example4.root")
        
        
        c5 = ROOT.TCanvas("c")
        
        graph.Draw("CONT2")
        # Le pongo esos ángulos porque así se ve guay
        c5.SetTheta(270)
        c5.SetPhi(270)
        
        c5.SaveAs("example5.png")
        c5.SaveAs("example5.root")
        
        
        
        
        c6 = ROOT.TCanvas("c")
        
        graph.Draw("CONT3")
        # Le pongo esos ángulos porque así se ve guay
        c6.SetTheta(270)
        c6.SetPhi(270)
        
        c6.SaveAs("example6.png")
        c6.SaveAs("example6.root")
        
        
        
        c7 = ROOT.TCanvas("c")
        
        graph.Draw("CONT4")
        # Le pongo esos ángulos porque así se ve guay
        c7.SetTheta(270)
        c7.SetPhi(270)
        
        c7.SaveAs("example7.png")
        c7.SaveAs("example7.root")
        
        
        c8 = ROOT.TCanvas("c")
        
        graph.Draw("CONT5")
        # Le pongo esos ángulos porque así se ve guay
        c8.SetTheta(270)
        c8.SetPhi(270)
        
        c8.SaveAs("example8.png")
        c8.SaveAs("example8.root")
        
        
        
        
        c9 = ROOT.TCanvas("c")
        
        graph.Draw("ARR")
        # Le pongo esos ángulos porque así se ve guay
        c9.SetTheta(270)
        c9.SetPhi(270)
        
        c9.SaveAs("example9.png")
        c9.SaveAs("example9.root")
        
        
        
        
        c10 = ROOT.TCanvas("c")
        
        graph.Draw("BOX")
        # Le pongo esos ángulos porque así se ve guay
        c10.SetTheta(270)
        c10.SetPhi(270)
        
        c10.SaveAs("example10.png")
        c10.SaveAs("example10.root")
        
        
        
        
        
        
        c11 = ROOT.TCanvas("c")
        
        graph.Draw("SURF3")
        # Le pongo esos ángulos porque así se ve guay
        c11.SetTheta(270)
        c11.SetPhi(270)
        
        c11.SaveAs("example11.png")
        c11.SaveAs("example11.root")
        
        
        
        
        
        c12 = ROOT.TCanvas("c")
        
        graph.Draw("SURF5")
        # Le pongo esos ángulos porque así se ve guay
        c12.SetTheta(270)
        c12.SetPhi(270)
        
        c12.SaveAs("example12.png")
        c12.SaveAs("example12.root")
        
        
        
        
        
        
        c12 = ROOT.TCanvas("c")
        graph.Draw("TRI2")
        # Le pongo esos ángulos porque así se ve guay
        c12.SetTheta(270)
        c12.SetPhi(270)
        c12.SaveAs("example12.png")
        c12.SaveAs("example12.root")
        
        
        
        
        
        c13 = ROOT.TCanvas("c")
        ROOT.gStyle.SetPalette(55)
        graph.Draw("TRI2Z")
        # Le pongo esos ángulos porque así se ve guay
        c13.SetTheta(270)
        c13.SetPhi(270)
        
        c13.SaveAs("example13.png")
        c13.SaveAs("example13.root")
        
        
        
        #------------------------------------------------------------------------------
        # Paletas de cores en HD de ROOT:
        
        # exemplo:
        # ROOT.gStyle.SetPalette(55) --> Pon o estilo kRainBow
        
        # Máis info en: https://root.cern.ch/doc/master/classTColor.html
        
        kDeepSea=51,          kGreyScale=52,    kDarkBodyRadiator=53,
        kBlueYellow= 54,      kRainBow=55,      kInvertedDarkBodyRadiator=56,
        kBird=57,             kCubehelix=58,    kGreenRedViolet=59,
        kBlueRedYellow=60,    kOcean=61,        kColorPrintableOnGrey=62,
        kAlpine=63,           kAquamarine=64,   kArmy=65,
        kAtlantic=66,         kAurora=67,       kAvocado=68,
        kBeach=69,            kBlackBody=70,    kBlueGreenYellow=71,
        kBrownCyan=72,        kCMYK=73,         kCandy=74,
        kCherry=75,           kCoffee=76,       kDarkRainBow=77,
        kDarkTerrain=78,      kFall=79,         kFruitPunch=80,
        kFuchsia=81,          kGreyYellow=82,   kGreenBrownTerrain=83,
        kGreenPink=84,        kIsland=85,       kLake=86,
        kLightTemperature=87, kLightTerrain=88, kMint=89,
        kNeon=90,             kPastel=91,       kPearl=92,
        kPigeon=93,           kPlum=94,         kRedBlue=95,
        kRose=96,             kRust=97,         kSandyTerrain=98,
        kSienna=99,           kSolar=100,       kSouthWest=101,
        kStarryNight=102,     kSunset=103,      kTemperatureMap=104,
        kThermometer=105,     kValentine=106,   kVisibleSpectrum=107,
        kWaterMelon=108,      kCool=109,        kCopper=110,
        kGistEarth=111,       kViridis=112,     kCividis=113
        
        """
        
        #------------------------------------------------------------------------------
        
        
        
        '''
        
        
        
        
        
        
        
        
        
        
        
        #??????????????????????????????????????????????????????????????????????????????
        #??????????????????????????????????????????????????????????????????????????????
        #??????????????????????????????????????????????????????????????????????????????
    
    
    
    
    
    









        
        
        
        
        
        
        print()
        print('Aplicación preparada. Esperando instrucciones')
        print()
        
        
        self.boton_scatterplot = ttk.Button(self.segunda_ventana,text='Scatter plot',padding=(36,10),command=self.abrir_imagen_scatter)
        self.boton_scatterplot.place(x=380,y=345)

        self.boton_sinal_reconstruida = ttk.Button(self.segunda_ventana,text='Sinal reconstruida',padding=(15,10),command=self.abrir_imagen_normal)
        self.boton_sinal_reconstruida.place(x=380,y=385)

        self.boton_sinal_filtrada = ttk.Button(self.segunda_ventana,text='Sinal filtrada',padding=(29,10),command=self.abrir_imagen_filtro)
        self.boton_sinal_filtrada.place(x=380,y=425)
        
        
        
        
        
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    
    
    
    
    
    
    def buscar(self): # Función para examinar directorio donde está el archivo a abrir y leer
        
        
        global DEBUG # No llega aquí la señal!!!!!!!
        DEBUG+=1
        print('DEBUG: ',DEBUG)
        
        self.busqueda_ventana=self.segunda_ventana.withdraw() # Ocultamos la ventana y creamos una temporal en la que examinar el archivo a buscar

        Ruta_archivo = askdirectory(parent=self.segunda_ventana) # Abrimos un diálogo donde almacenar la ruta
 
        try:  
            self.Entrada_usuario_1.insert(0,Ruta_archivo) # Hacemos que aparezca la ruta en la entrada de usuario
        
        except:
            pass

        self.segunda_ventana.deiconify() # Volvemos a dibujar la ventana



    def abrir_imagen_scatter(self):
        
        if self.nome_carpeta.get() != '': # Se non temos o arquivo .root creado no equipo:
            nombre_de_la_foto = 'Sinal_matplotlib.png'
            Ruta = self.ruta_simulacions.get() +'/'+self.nome_carpeta.get() +'/plots'
            os.chdir(Ruta) # Nos trasladamos al directorio donde se guardó la imagen
            self.imagen = PIL.Image.open(nombre_de_la_foto)
            self.imagen.show()
        else:
            nombre_de_la_foto = 'Sinal_matplotlib.png'
            Ruta = self.ruta_simulacions.get() +'/plots'
            os.chdir(Ruta) # Nos trasladamos al directorio donde se guardó la imagen
            self.imagen = PIL.Image.open(nombre_de_la_foto)
            self.imagen.show()


    def abrir_imagen_normal(self):
        
        if self.nome_carpeta.get() != '': # Se non temos o arquivo .root creado no equipo:
            nombre_de_la_foto = 'figura_5.png'
            Ruta = self.ruta_simulacions.get() +'/'+self.nome_carpeta.get() +'/plots/paleta_kRainBow'
            os.chdir(Ruta) # Nos trasladamos al directorio donde se guardó la imagen
            self.imagen = PIL.Image.open(nombre_de_la_foto)
            self.imagen.show()
        else:
            nombre_de_la_foto = 'figura_5.png'
            Ruta = self.ruta_simulacions.get() +'/plots/paleta_kRainBow'
            os.chdir(Ruta) # Nos trasladamos al directorio donde se guardó la imagen
            self.imagen = PIL.Image.open(nombre_de_la_foto)
            self.imagen.show()
            
            
    def abrir_imagen_filtro(self):
        
        if self.nome_carpeta.get() != '': # Se non temos o arquivo .root creado no equipo:
            nombre_de_la_foto = 'figura_5.png'
            Ruta = self.ruta_simulacions.get() +'/'+self.nome_carpeta.get() +'/plots/Filtro'
            os.chdir(Ruta) # Nos trasladamos al directorio donde se guardó la imagen
            self.imagen = PIL.Image.open(nombre_de_la_foto)
            self.imagen.show()
        else:
            nombre_de_la_foto = 'figura_5.png'
            Ruta = self.ruta_simulacions.get() +'/plots/Filtro'
            os.chdir(Ruta) # Nos trasladamos al directorio donde se guardó la imagen
            self.imagen = PIL.Image.open(nombre_de_la_foto)
            self.imagen.show()
       
        
#?????????????????????????????????????????????????????????????????????????????        
        
        
        
       
        
    def ayuda(self):

        self.Ventana_ayuda = Toplevel() # Creamos la ventana de ayuda
                
        self.Ventana_ayuda.geometry("400x400") # Tamaño de la ventana
        
        self.Ventana_ayuda.resizable(0,0) # Esta instrucción es para impedir que la ventana se pueda modificar de tamaño (rollo maximizar y así), '0' es equivalente a poner False. A su vez, poner un '1' equivale a un True.
        
        self.Ventana_ayuda.title('Axuda')


        self.fuente_de_bienvenidaaa = font.Font(family="Times New Roman",size=13,weight='bold') 
        self.Bienvenida = ttk.Label(self.Ventana_ayuda,text='Benvido a PyZHAireS v.2.3',font=self.fuente_de_bienvenidaaa)
        self.Bienvenida.place(x=30,y=30)
        
        #self.Bienvenida.config(foreground='blue')
        
        #self.e1 = ttk.Label(self.Ventana_ayuda,text='heeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeo') # Límite de letras para que quede bien
        #self.e1.place(x=30,y=30)
        
        self.e2 =ttk.Label(self.Ventana_ayuda,text='Nesta aplicación están incluídas todas as fun-')
        self.e3 =ttk.Label(self.Ventana_ayuda,text='cións do código LECTURA_SIMULACIONS_ROOT.py do')
        self.e4 =ttk.Label(self.Ventana_ayuda,text='traballo de Técnicas de Análise e Simulación en')
        self.e5 =ttk.Label(self.Ventana_ayuda,text='Física Nuclear e de Partículas co motivo de fa-')
        self.e6 =ttk.Label(self.Ventana_ayuda,text='cer máis sinxelo e visual o seu emprego.')
        self.e7 =ttk.Label(self.Ventana_ayuda,text='')
        self.e8 =ttk.Label(self.Ventana_ayuda,text='ROOZHAireS.py inclúe un módulo de lectura inte-')
        self.e9 =ttk.Label(self.Ventana_ayuda,text='ractivo co cal pódense ler todos os ficheiros ')
        self.e10 =ttk.Label(self.Ventana_ayuda,text='das simulacións e almacenar toda a información')
        self.e11 =ttk.Label(self.Ventana_ayuda,text='nun arquivo .root, a partires do cal xerará unha')
        self.e12 =ttk.Label(self.Ventana_ayuda,text='serie de histogramas, plots, etc.')
        self.e13 =ttk.Label(self.Ventana_ayuda,text='No caso de non ter os arquivos das simulacións')
        self.e14 =ttk.Label(self.Ventana_ayuda,text='pero si o arquivo .root pode facerse unha lectu-')
        self.e15 =ttk.Label(self.Ventana_ayuda,text='ra directa indicando o directorio dese arquivo.')

        self.e2.place(x=30,y=70)
        self.e3.place(x=30,y=90)
        self.e4.place(x=30,y=110)
        self.e5.place(x=30,y=130)
        self.e6.place(x=30,y=150)
        self.e7.place(x=30,y=170)
        self.e8.place(x=30,y=190)
        self.e9.place(x=30,y=210)
        self.e10.place(x=30,y=230)
        self.e11.place(x=30,y=250)
        self.e12.place(x=30,y=270)
        self.e13.place(x=30,y=310)
        self.e14.place(x=30,y=330)
        self.e15.place(x=30,y=350)




        if ( sys.platform.startswith('win')): # Defino el icono de la ventana por si es windows o linux el S.O.
            try:
                Ruta_logo=os.path.join(ruta_de_imagenes,'PRUEBA_ICONOS.ICO')
                logo = PhotoImage(file=Ruta_logo)
                self.Ventana_ayuda.tk.call('wm', 'iconphoto', self.Ventana_ayuda._w, logo)        
            except:
                pass
        else:
            try:
                Ruta_logo=os.path.join(ruta_de_imagenes,'PRUEBA_ICONOS.xbm')
                logo = PhotoImage(file=Ruta_logo)
                self.Ventana_ayuda.tk.call('wm', 'iconphoto', self.Ventana_ayuda._w, logo)        
            except:
                pass

        
        
        
        self.Ventana_ayuda.mainloop() # Fin del bucle de la ventana de ayuda
        
        
        
        
            

    # Declara un método para borrar el mensaje anterior y
    # la caja de entrada de la contraseña

    def borrar_mensa(self, evento):
        self.clave.set("")
        self.mensa.set("")

def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()

print()
print('%%%%%%%%%%%%%%%%%%%%%%%%%')
print('  Cerrando aplicación')
print('%%%%%%%%%%%%%%%%%%%%%%%%%')
print()







