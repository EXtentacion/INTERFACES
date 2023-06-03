import tkinter as tk
from tkinter import messagebox

class Bebida:
    def __init__(self, id, nombre, clasificacion, marca, precio):
        self.id = id
        self.nombre = nombre
        self.clasificacion = clasificacion
        self.marca = marca
        self.precio = precio

class AlmacenApp:
    def __init__(self):
        self.bebidas = []

        bebida1 = Bebida("1", "Coca Cola", "Refresco", "Coca Cola", "2.5")
        bebida2 = Bebida("2", "Coca Cola", "Refresco", "Coca Cola", "2.0")
        bebida3 = Bebida("3", "Agua Mineral", "Agua", "San Pellegrino", "1.0")
        bebida4 = Bebida("4", "Agua Mineral", "Agua", "Topo chico", "1.0")
        bebida5 = Bebida("5", "Coca Cola", "Refresco", "Coca-Cola", "2.5")

        self.bebidas.append(bebida1)
        self.bebidas.append(bebida2)
        self.bebidas.append(bebida3)
        self.bebidas.append(bebida4)
        self.bebidas.append(bebida5)

        self.root = tk.Tk()
        self.root.title("Almacén de Bebidas")

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.id_label = tk.Label(self.frame, text="ID:")
        self.id_label.grid(row=0, column=0)
        self.id_entry = tk.Entry(self.frame)
        self.id_entry.grid(row=0, column=1)

        self.nombre_label = tk.Label(self.frame, text="Nombre:")
        self.nombre_label.grid(row=1, column=0)
        self.nombre_entry = tk.Entry(self.frame)
        self.nombre_entry.grid(row=1, column=1)

        self.clasificacion_label = tk.Label(self.frame, text="Clasificación:")
        self.clasificacion_label.grid(row=2, column=0)
        self.clasificacion_entry = tk.Entry(self.frame)
        self.clasificacion_entry.grid(row=2, column=1)

        self.marca_label = tk.Label(self.frame, text="Marca:")
        self.marca_label.grid(row=3, column=0)
        self.marca_entry = tk.Entry(self.frame)
        self.marca_entry.grid(row=3, column=1)

        self.precio_label = tk.Label(self.frame, text="Precio:")
        self.precio_label.grid(row=4, column=0)
        self.precio_entry = tk.Entry(self.frame)
        self.precio_entry.grid(row=4, column=1)

        self.agregar_button = tk.Button(self.frame, text="Agregar", command=self.agregar_bebida)
        self.agregar_button.grid(row=0, column=2)

        self.eliminar_button = tk.Button(self.frame, text="Eliminar", command=self.eliminar_bebida)
        self.eliminar_button.grid(row=1, column=2)

        self.actualizar_button = tk.Button(self.frame, text="Actualizar", command=self.actualizar_bebida)
        self.actualizar_button.grid(row=2, column=2)

        self.mostrar_button = tk.Button(self.frame, text="Mostrar Todas", command=self.mostrar_todas_bebidas)
        self.mostrar_button.grid(row=3, column=2)

        self.calcular_promedio_button = tk.Button(self.frame, text="Calcular Precio Promedio", command=self.calcular_precio_promedio)
        self.calcular_promedio_button.grid(row=4, column=2)

        self.calcular_total_button = tk.Button(self.frame, text="Calcular Precio Total", command=self.calcular_precio_total)
        self.calcular_total_button.grid(row=5, column=2)

        self.cantidad_marca_button = tk.Button(self.frame, text="Cantidad de bebidas de una marca", command=self.cantidad_de_vevidad_de_una_marca)
        self.cantidad_marca_button.grid(row=6, column=0)

        self.cantidad_clasificacion_button = tk.Button(self.frame, text="Cantidad de bebidas de una clasificación", command=self.cantidad_de_vevidad_de_una_clasificacion)
        self.cantidad_clasificacion_button.grid(row=7, column=0)

        self.root.mainloop()

    def agregar_bebida(self):
        id = self.id_entry.get()
        nombre = self.nombre_entry.get()
        clasificacion = self.clasificacion_entry.get()
        marca = self.marca_entry.get()
        precio = self.precio_entry.get()

        # Verificar si el ID ya existe
        for bebida in self.bebidas:
            if bebida.id == id:
                messagebox.showerror("Error", "Ya existe una bebida con ese ID")
                return

        bebida = Bebida(id, nombre, clasificacion, marca, precio)
        self.bebidas.append(bebida)

        messagebox.showinfo("Bebida Agregada", "Bebida agregada exitosamente")

        self.id_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.clasificacion_entry.delete(0, tk.END)
        self.marca_entry.delete(0, tk.END)
        self.precio_entry.delete(0, tk.END)


    def eliminar_bebida(self):
        id = self.id_entry.get()

        for bebida in self.bebidas:
            if bebida.id == id:
                self.bebidas.remove(bebida)
                messagebox.showinfo("Bebida Eliminada", "Bebida eliminada exitosamente")
                return

        messagebox.showerror("Error", "No existe una bebida con ese ID")

    def actualizar_bebida(self):
        id = self.id_entry.get()
        nombre = self.nombre_entry.get()
        clasificacion = self.clasificacion_entry.get()
        marca = self.marca_entry.get()
        precio = self.precio_entry.get()

        for bebida in self.bebidas:
            if bebida.id == id:
                bebida.nombre = nombre
                bebida.clasificacion = clasificacion
                bebida.marca = marca
                bebida.precio = precio
                messagebox.showinfo("Bebida Actualizada", "Bebida actualizada exitosamente")
                return

        messagebox.showerror("Error", "No existe una bebida con ese ID")

    def mostrar_todas_bebidas(self):
        bebidas = ""

        for bebida in self.bebidas:
            bebidas += "ID: " + bebida.id + "\n"
            bebidas += "Nombre: " + bebida.nombre + "\n"
            bebidas += "Clasificación: " + bebida.clasificacion + "\n"
            bebidas += "Marca: " + bebida.marca + "\n"
            bebidas += "Precio: " + bebida.precio + "\n\n"

        messagebox.showinfo("Bebidas", bebidas)

    def calcular_precio_promedio(self):
        total = 0

        for bebida in self.bebidas:
            total += float(bebida.precio)

        promedio = total / len(self.bebidas)

        messagebox.showinfo("Precio Promedio", "El precio promedio de las bebidas es: " + str(promedio))

    def calcular_precio_total(self):
        total = 0

        for bebida in self.bebidas:
            total += float(bebida.precio)

        messagebox.showinfo("Precio Total", "El precio total de las bebidas es: " + str(total))
        
    def cantidad_de_vevidad_de_una_marca(self):
        marca = self.marca_entry.get()
        cantidad = 0
        
        for bebida in self.bebidas:
            if bebida.marca == marca:
                cantidad += 1
        
        messagebox.showinfo("Cantidad de bebidas", "La cantidad de bebidas de la marca " + marca + " son: " + str(cantidad))



    def cantidad_de_vevidad_de_una_clasificacion(self):
        clasificacion = self.clasificacion_entry.get()
        cantidad = 0
        for bebida in self.bebidas:
            if bebida.clasificacion == clasificacion:
                cantidad += 1
        messagebox.showinfo("Cantidad de bebidas", "La cantidad de bebidas de la clasificación " + clasificacion + " son: " + str(cantidad))


def main():
    app = AlmacenApp()

if __name__ == "__main__":
    main()
