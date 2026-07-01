Característica: Registro de pagos en el ISP Familiar

  Escenario: Cargar exitosamente un cliente que ya pagó el mes
    Dado que el sistema de base de datos está activo
    Cuando el usuario ingresa el nombre "Ana Gomez"
    Y el usuario ingresa el mes "Junio"
    Y confirma que el pago fue realizado con "s"
    Entonces el registro de "Ana Gomez" debe guardarse con el estado "PAGADO"
