import tkinter
import math
from tkinter import *
from tkinter import ttk
from PIL import ImageTk , Image
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import os
############# LIBRERIAS USADAS ############
windows = tkinter.Tk()
note=ttk.Notebook(windows)
note.pack(fill='both',expand='yes')
pes0= ttk.Frame(note)
pes1= ttk.Frame(note)
note.add(pes0 , text="Tax Help")
absolute_folder_path = os.path.dirname(os.path.realpath(__file__))
absolute_image_path = os.path.join(absolute_folder_path,'intru.png')
image = PhotoImage(file =absolute_image_path)
image = image.subsample(2,2)
label = Label(image=image)
label.place(x=450,y=70)

menu = Menu(windows)
windows.config(menu=menu)
Help = Menu(menu, tearoff=0)
Help.add_command(label = "Sobre Nosotros..." , command = lambda: about())
Help.add_command(label = "Contactanos..." , command = lambda: contac())
Help.add_command(label = "Donaciones", command = lambda: don())
menu.add_cascade(label= "Información" , menu= Help)
windows.geometry("900x900")  
windows.resizable(False,False)
windows.title("Tax Help Ultimate Edition")
windows.configure(background="cadet blue")
mensaje= tkinter.Label(windows,font=("Times New Roman",15,"bold"), text = "Gracias por usar Tax Help! ", bg="aquamarine",width=22)
mensaje.pack(fill= tkinter.X)

texto1 = tkinter.Entry(pes0,font=("Times New Roman",15,"bold"))
texto1.place(x=220,y=50)
texto1.insert(0,"0")
label = Label(pes0, text="ENERO : " , bg="aquamarine", width=22,borderwidth=5)
label.place(x=31,y=50)
################################
texto2 = tkinter.Entry(pes0,font=("Times New Roman",15,"bold") )
texto2.place(x=220,y=100)
texto2.insert(0,"0")
label = Label(pes0 , text="FEBRERO : " , bg="aquamarine", width=22,borderwidth=5)
label.place(x=31,y=100)
#################################
texto3 = tkinter.Entry(pes0,font=("Times New Roman",15,"bold") )
texto3.place(x=220,y=150)
texto3.insert(0,"0")
label = Label(pes0, text="MARZO : " , bg="aquamarine", width=22,borderwidth=5)
label.place(x=31,y=150)
#################################
texto4 = tkinter.Entry(pes0,font=("Times New Roman",15,"bold") )
texto4.place(x=220,y=200)
texto4.insert(0,"0")
label = Label(pes0, text="ABRIL : " , bg="aquamarine", width=22,borderwidth=5)
label.place(x=31,y=200)
################################
texto5 = tkinter.Entry(pes0,font=("Times New Roman",15,"bold") )
texto5.place(x=220,y=250)
texto5.insert(0,"0")
label = Label(pes0, text="MAYO : " , bg="aquamarine", width=22,borderwidth=5)
label.place(x=31,y=250)
##############################
texto6 = tkinter.Entry(pes0,font=("Times New Roman",15,"bold") )
texto6.place(x=220,y=300)
texto6.insert(0,"0")
label = Label(pes0 , text="JUNIO : " , bg="aquamarine", width=22,borderwidth=5)
label.place(x=31,y=300)
###############################
texto7 = tkinter.Entry(pes0,font=("Times New Roman",15,"bold") )
texto7.place(x=220,y=350)
texto7.insert(0,"0")
label = Label(pes0, text="JULIO : " , bg="aquamarine", width=22,borderwidth=5)
label.place(x=31,y=350)
##############################
texto8 = tkinter.Entry(pes0,font=("Times New Roman",15,"bold") )
texto8.place(x=220,y=400)
texto8.insert(0,"0")
label = Label(pes0, text="AGOSTO : " , bg="aquamarine", width=22,borderwidth=5)
label.place(x=31,y=400)
##################################
texto9 = tkinter.Entry(pes0,font=("Times New Roman",15,"bold") )
texto9.place(x=220,y=450)
texto9.insert(0,"0")
label = Label(pes0, text="SEPTIEMBRE : " , bg="aquamarine", width=22,borderwidth=5)
label.place(x=31,y=450)
##############################
texto10 = tkinter.Entry(pes0,font=("Times New Roman",15,"bold") )
texto10.place(x=220,y=500)
texto10.insert(0,"0")
label = Label(pes0 , text="OCTUBRE : " , bg="aquamarine", width=22,borderwidth=5)
label.place(x=31,y=500)
##################################
texto11 = tkinter.Entry(pes0,font=("Times New Roman",15,"bold") )
texto11.place(x=220,y=550)
texto11.insert(0,"0")
label = Label(pes0, text="NOVIEMBRE : " , bg="aquamarine", width=22,borderwidth=5)
label.place(x=31,y=550)
##############################
texto12 = tkinter.Entry(pes0,font=("Times New Roman",15,"bold") )
texto12.place(x=220,y=600)
texto12.insert(0,"0")
label = Label(pes0, text="DICIEMBRE : " , bg="aquamarine", width=22,borderwidth=5)
label.place(x=31,y=600)

####################### Creación de variables de Set() ####################
tramo1 = StringVar()
retenido1 = StringVar()
impuestos1 = StringVar()

etiqueta = Label(pes0,textvariable=tramo1 , bg= "gray90" ,width=52,borderwidth=15)
etiqueta.place(x=450,y=450)

etiqueta1 = Label(pes0,textvariable=impuestos1 , bg= "gray90" ,width=52,borderwidth=15)
etiqueta1.place(x=450,y=550)

etiqueta2 = Label(pes0,textvariable=retenido1 , bg= "gray90" ,width=52,borderwidth=15)
etiqueta2.place(x=450,y=650)


################### Funciones donde obtenemos resultados ################

def about():
    messagebox.showinfo("Sobre Nosotros", " Esta aplicación contiene fines academicos, no obstante es funcional y comprable.")
    
def contac():
    messagebox.showinfo("Contactenos", "Para mayor información visitenos en www.Proyectotaxhelp.cl")
   
def don():
    messagebox.showinfo("donaciones", "Cuenta de ahorro Banco udp : 0012312891237")
    
def  text1():
    
    ########## creacion de variables para obtener texto
    a = int(texto1.get())
    b = int(texto2.get()) 
    c = int(texto3.get())
    d = int(texto4.get())
    e = int(texto5.get())
    f = int(texto6.get())
    g = int(texto7.get())
    h = int(texto8.get())
    i = int(texto9.get())
    j = int(texto10.get())
    k = int(texto11.get())
    l = int(texto12.get())
    
    arr_boletas = [a,b,c,d,e,f,g,h,i,j,k,l] 
    tramo =(round((sum(arr_boletas))*0.7))

    impuesto = 0
    float(impuesto)
    for j in range(12):
           
           impuesto = int(impuesto + float( (arr_boletas[j] * 0.1225)))
           
    
    ############ if´s que determinarán el tramo en el que este el usuario ##############
    if(tramo >= 0 and tramo <= 8266698.00):
        
        retenido = (impuesto)
        tramo1.set("Usted esta en el primer Tramo : "+"$" + (str) (tramo))  
        retenido1.set("Su devolucion de impuestos es :  " +"$" + (str)("{0:.2f}".format (retenido)))
        
    else:
        if(tramo >=8266698.01 and tramo <= 18370440.00):
            retenido = (impuesto - ((tramo * 0.04) - 330667.92))        
            tramo1.set("Usted esta en el segundo Tramo : "+"$" + (str) (tramo))
            if(retenido < 0):
                retenido = retenido * (-1)
                retenido1.set("Usted debe : " +"$" +(str) (str)("{0:.2f}".format (retenido)))
            else:
                retenido1.set("Su devolucion de impuestos es : " +"$" + (str)("{0:.2f}".format (retenido)))
            
        else:
            if(tramo >=18370440.01 and tramo <= 30617400.00):
                retenido = (impuesto - ( (tramo * 0.08) - 1065485.52))
                tramo1.set("Usted esta en el tercer Tramo : "+"$" + (str) (tramo))
                if(retenido < 0):
                    retenido = retenido * (-1)
                    retenido1.set("Usted debe : " +"$" +(str) (str)("{0:.2f}".format (retenido)))
                else:
                    retenido1.set("Su devolucion de impuestos es : " + "$" +(str) (str)("{0:.2f}".format (retenido)))
            else:
                if(tramo >=30617400.01 and tramo <= 42864360.00):
                    retenido = (impuesto - ( (tramo * 0.135) - 2749442.52 ))        
                    tramo1.set("Usted esta en el cuarto Tramo : "+"$" + (str) (tramo))
                    if(retenido < 0):
                        retenido = retenido * (-1)
                        retenido1.set("Usted debe : " +"$" +(str)("{0:.2f}".format (retenido)))
                    else:
                        retenido1.set("Su devolucion de impuestos es : " +"$" + (str)("{0:.2f}".format (retenido)))
                else:
                    if(tramo >= 42864360.01 and tramo <= 55111320.00):
                        retenido = impuesto - ((tramo * 0.23) - 6821556.72)
                        tramo1.set("Usted esta en el quinto Tramo :  "+"$" + (str) (tramo))
                        if(retenido < 0):
                            retenido = retenido * (-1)
                            retenido1.set("Usted debe : " +"$" +(str)("{0:.2f}".format (retenido)))
                        else:
                            retenido1.set("Su devolucion de impuestos es : " +"$" + (str)("{0:.2f}".format (retenido)))
                    else:
                        if(tramo >= 55111320.01 and tramo <= 73481760.00):
                            retenido = impuesto - ((tramo * 0.304) - 10899794.40 )      
                            tramo1.set("Usted esta en el sexto Tramo :  "  +"$" + (str) (tramo))
                            if(retenido < 0):
                                retenido = retenido *(-1)
                                retenido.set("Usted debe : " +"$" +(str)("{0:.2f}".format (retenido)))
                            else:
                                retenido1.set("Su devolucion de impuestos es : " +"$" +(str)("{0:.2f}".format (retenido)))
                        else:
                            if(tramo >= 73481760.01 and tramo <= 189827880.00):
                                retenido = (impuesto - ((tramo * 0.35) - 14279955.36 ))         
                                tramo1.set("Usted esta en el septimo Tramo : "+"$" + (str) (tramo))
                                if(retenido < 0):
                                    retenido = retenido * (-1)
                                    retenido1.set("Usted debe : " + "$" +(str)("{0:.2f}".format (retenido)))
                                else:
                                    retenido1.set("Su devolucion de impuestos es :  " + "$" + (str)("{0:.2f}".format (retenido)))
                            else:
                                if(tramo >=189827880.01):
                                    retenido = (impuesto - ((tramo * 0.4) - 23771349.36)) 
                                    tramo1.set("Usted esta en el octavo Tramo : "+ "$" + (str) (tramo))
                                    if(retenido < 0):
                                        retenido = colocolo * (-1)
                                        retenido1.set("Usted debe : "+ "$" + (str)("{0:.2f}".format (retenido)))
                                    else:
                                        retenido1.set("Su devolucion de impuestos es : " + "$" + (str)("{0:.2f}".format (retenido)))
                                        
    impuestos1.set("Sus impuestos retenidos son : " + "$" +(str) (impuesto))
    
################## boton para correr la función y obtener todo #########################

btn_prueba = tkinter.Button(pes0, text = "clickea" , command = lambda: text1())
btn_prueba.pack(side=tkinter.BOTTOM)

windows.mainloop()