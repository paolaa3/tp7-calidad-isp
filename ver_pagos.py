import sqlite3

# Conectamos a la base de datos
conexion = sqlite3.connect('clientes_isp.db')
cursor = conexion.cursor()

# Pedimos a la base de datos todos los registros de la tabla clientes
cursor.execute("SELECT id, nombre, mes, pagado FROM clientes")
registros = cursor.fetchall()

print("\n" + "="*40)
print("   LISTADO DE PAGOS - ISP FAMILIAR")
print("="*40)
print(f"{'ID':<4} | {'Cliente':<20} | {'Mes':<10} | {'Estado'}")
print("-"*40)

# Recorremos cada fila que nos devolvió la base de datos
for r in registros:
    id_cli, nombre, mes, pagado = r
    # Convertimos el 1/0 binario en algo legible para humanos
    estado = "✅ PAGADO" if pagado == 1 else "❌ DEBE"
    
    # Imprimimos con formato de columnas
    print(f"{id_cli:<4} | {nombre:<20} | {mes:<10} | {estado}")

print("="*40)
print(f"Total de registros: {len(registros)}\n")

conexion.close()
