import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# --- FUNCIONES DE LÓGICA ---
def cargar_datos_en_tabla():
    # Limpiar tabla antes de recargar
    for item in tabla.get_children():
        tabla.delete(item)
    
    conexion = sqlite3.connect('clientes_isp.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre, mes, pagado FROM clientes")
    for fila in cursor.fetchall():
        estado = "PAGADO" if fila[2] == 1 else "DEBE"
        tabla.insert("", "end", values=(fila[0], fila[1], estado))
    conexion.close()

def guardar_cliente():
    nombre = entry_nombre.get()
    mes = entry_mes.get()
    pagado = 1 if var_pago.get() else 0
    
    if nombre == "" or mes == "":
        messagebox.showwarning("Atención", "Por favor completa todos los campos")
        return

    conexion = sqlite3.connect('clientes_isp.db')
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO clientes (nombre, mes, pagado) VALUES (?, ?, ?)", (nombre, mes, pagado))
    conexion.commit()
    conexion.close()
    
    # Limpiar campos y refrescar tabla
    entry_nombre.delete(0, tk.END)
    cargar_datos_en_tabla()
    messagebox.showinfo("Éxito", f"Cliente {nombre} guardado")

# --- INTERFAZ GRÁFICA ---
root = tk.Tk()
root.title("Gestión ISP Familiar")
root.geometry("500x500")

# Entradas de texto
tk.Label(root, text="Nombre del Cliente:").pack(pady=5)
entry_nombre = tk.Entry(root)
entry_nombre.pack()

tk.Label(root, text="Mes de Pago:").pack(pady=5)
entry_mes = tk.Entry(root)
entry_mes.pack()

var_pago = tk.BooleanVar()
tk.Checkbutton(root, text="¿Pago realizado?", variable=var_pago).pack(pady=10)

tk.Button(root, text="Guardar Registro", command=guardar_cliente, bg="green", fg="white").pack(pady=10)

# Tabla visual
columnas = ("Nombre", "Mes", "Estado")
tabla = ttk.Treeview(root, columns=columnas, show="headings")
for col in columnas:
    tabla.heading(col, text=col)
    tabla.column(col, width=100)
tabla.pack(pady=20, fill="both", expand=True)

cargar_datos_en_tabla() # Cargar lo que ya existe al abrir

root.mainloop()
