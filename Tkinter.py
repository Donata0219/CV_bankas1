from tkinter import *
# import Naujas1
def mygtuko_veiksmas():
    # Į konsolę išvedam žmogaus įvestą reikšmę
    print( field.get() )
    # Pavyzdys, kaip dinamiškai pakeisti laukelio tekstą
    lbl.config( text = "Miestas" + field.get() )

def antro_mygtuko_veiksmas():
    lbl = Label( window, text="Naujas tekstas " )
    lbl.pack()

# Sukuriam norimo dydžio langą
window = Tk()
window.geometry( "300x400" )

# Sukuriame naudojamus grafinius komponentus
lbl = Label( window, text="Miestas: " )
field = Entry( window )

# Kuriant mygtuką, galim nurodyti kuri funkcija turi būti paleista paspaudimo metu
# command vietoje taip pat galim naudoti lambda
btn = Button(window, text="Pridėti miestą", command=mygtuko_veiksmas )
btn2 = Button( window, text="Pridėti dar vieną miestą", command=antro_mygtuko_veiksmas)

# Komponentus sudėliojame į langą
lbl.pack()
field.pack()
btn.pack()
btn2.pack()

# Paleidžiame programą
window.mainloop()