def evaluar_estado_pago(valor_binario):
    return "PAGADO" if valor_binario == 1 else "DEBE"

def test_evaluar_estado_pago():
    assert evaluar_estado_pago(1) == "PAGADO"
    assert evaluar_estado_pago(0) == "DEBE"
