from tkinter import *
import time as time

pantalla= Tk()
pantalla.geometry("10000x800")
pantalla.title("PAVL MARKET S.L")
#pantalla.config(bg="brown")

tema=Label(pantalla,text="PAVL MARKET",font=16).pack(pady=1)

doble1=PanedWindow(pantalla,orient="horizontal",width=700,height=700)
doble1.place(x=160,y=50)

izquierda=Listbox(doble1,relief="raised")
doble1.add(izquierda)

texto= " "
var_texto = StringVar()
entrada= StringVar()

def Guardar():
    global texto
    with open("Ventas.txt","a") as Archivo:
        Entrada=entrada.get()
        total=str(eval(texto))
        cadena=str(list(time.localtime()))
        fecha=cadena[1:11].replace(",","-")
        hora=cadena[14:19].replace(",",":")
        escribir=Archivo.write(f"{Entrada}                            {total}FCFA                                {fecha}         {hora}\n")
    with open("Ventas.txt","r") as abrrir:
        lineas=abrrir.readlines()
        for i in lineas:
            if i[0:len(Entrada)]==Entrada:
                izquierda.insert(1,i)
    
                
def botones(num_o_sig):
    global texto
    texto= texto + str(num_o_sig)
    var_texto.set(texto)

def igual():
    global texto
    try:
        total=str(eval(texto))
        var_texto.set(total)
    except SyntaxError:
        var_texto.set("Error de calculo")

def borrar_total():
    global texto
    texto= " "
    var_texto.set(texto)

def limpiar():
    global izquierda
    with open("Ventas.txt","w") as abrrir:
       izquierda=Listbox(doble1,relief="raised")
       doble1.add(izquierda)
       
        
            

prodtag=Label(pantalla,text="Producto: ",font=12).place(x=1020,y=30)
entprod=Entry(pantalla,textvar=entrada,width=60,borderwidth=5).place(x=1120,y=30)

peqpan=Label(pantalla,width=70,borderwidth=5,height=19,relief="sunken",bg="grey",textvar=var_texto).place(x=1020,y=100)
derecho=Frame(pantalla,width=500,borderwidth=5,height=450,relief="sunken",bg="grey").place(x=1020,y=300)
prectag=Label(derecho,text="Precios ",font=12,fg="black").place(x=1240,y=720)


boton7=Button(pantalla,text=7,bg="black",fg="white",command= lambda: botones(7)).place(x=1025,y=305,width=100,height=100)
boton8=Button(pantalla,text=8,bg="black",fg="white",command=lambda: botones(8)).place(x=1130,y=305,width=100,height=100)
boton9=Button(pantalla,text=9,bg="black",fg="white",command=lambda: botones(9)).place(x=1235,y=305,width=100,height=100)
boton4=Button(pantalla,text=4,bg="black",fg="white",command=lambda: botones(4)).place(x=1025,y=410,width=100,height=100)
boton5=Button(pantalla,text=5,bg="black",fg="white",command=lambda: botones(5)).place(x=1130,y=410,width=100,height=100)
boton6=Button(pantalla,text=6,bg="black",fg="white",command=lambda: botones(6)).place(x=1235,y=410,width=100,height=100)
boton1=Button(pantalla,text=1,bg="black",fg="white",command=lambda: botones(1)).place(x=1025,y=515,width=100,height=100)
boton2=Button(pantalla,text=2,bg="black",fg="white",command=lambda: botones(2)).place(x=1130,y=515,width=100,height=100)
boton3=Button(pantalla,text=3,bg="black",fg="white",command=lambda: botones(3)).place(x=1235,y=515,width=100,height=100)
boton0=Button(pantalla,text=0,bg="black",fg="white",command=lambda: botones(0)).place(x=1025,y=620,width=208,height=100)
borrador=Button(pantalla,text="CE",bg="red",fg="white",command=lambda: borrar_total()).place(x=1445,y=305,width=70,height=100)
suma=Button(pantalla,text="+",bg="black",fg="white",command= lambda: botones("+")).place(x=1340,y=305,width=100,height=100)
resta=Button(pantalla,text="-",bg="black",fg="white",command= lambda: botones("-")).place(x=1340,y=410,width=100,height=100)
multy=Button(pantalla,text="*",bg="black",fg="white",command= lambda: botones("*")).place(x=1340,y=515,width=100,height=100)
divi=Button(pantalla,text="/",bg="black",fg="white",command= lambda: botones("/")).place(x=1340,y=620,width=100,height=100)
decimal=Button(pantalla,text=".",bg="black",fg="white",command= lambda: botones(".")).place(x=1235,y=620,width=100,height=100)
igual_a=Button(pantalla,text="=",bg="orange",fg="white",command=lambda: igual()).place(x=1445,y=410,width=70,height=310)

guardar=Button(pantalla,text="Guardar",bg="orange",fg="white",command=Guardar).place(x=885,y=300,width=100,height=100)
salir=Button(pantalla,text="Salir",bg="red",fg="white",command=exit).place(x=1410,y=750,width=100,height=40)
limpia=Button(pantalla,text="Limpiar",bg="brown",fg="white",command=limpiar).place(x=500,y=750,width=100,height=40)
pantalla.mainloop()