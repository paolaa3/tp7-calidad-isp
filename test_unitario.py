from app_isp import validar_registro_v1, validar_registro_v2, validar_registro_v3

def test_validar_registro_v1():
 
    assert validar_registro_v1("Carlos", "Julio") == True
    # Falla si mandamos vacíos
    assert validar_registro_v1("", "") == False

def test_validar_registro_v2():
  
    assert validar_registro_v2("   ", "Julio") == False

def test_validar_registro_v3():
    # La v2 aceptaba nombres de una sola letra ("A"). 
    # La v3 evoluciona exigiendo un mínimo seguro de 3 caracteres
    assert validar_registro_v3("Al", "Julio") == False
    assert validar_registro_v3("Ana", "Julio") == True
