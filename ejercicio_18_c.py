# Importar librerías necesarias
import numpy as np

# Parámetros del problema
tasa_mensual = 0.01        # Tasa efectiva mensual del 1%
inversion_mensual = 1000   # Inversión mensual
flujos_futuros = 18000     # Valor presente de los flujos futuros en el mes 12
meses = 12                 # Duración inicial del proyecto en meses
meses_extendido = 15       # Duración extendida del proyecto en meses (12 + 3)

# Función para calcular el VPN
def calcular_vpn(meses, inversion_mensual, flujos_futuros, tasa_mensual):
    # Calcular el valor presente de las inversiones mensuales
    valor_presente_inversion = sum([inversion_mensual / (1 + tasa_mensual)**t for t in range(1, meses+1)])
    
    # Calcular el valor presente de los flujos futuros en el mes "meses"
    valor_presente_flujos_futuros = flujos_futuros / (1 + tasa_mensual)**meses
    
    # VPN = Valor presente de los flujos futuros - Valor presente de las inversiones
    vpn = valor_presente_flujos_futuros - valor_presente_inversion
    return vpn

# Función para calcular la rentabilidad
def calcular_rentabilidad(meses, inversion_mensual, flujos_futuros, tasa_mensual):
    # Calcular el valor presente de las inversiones
    valor_presente_inversion = sum([inversion_mensual / (1 + tasa_mensual)**t for t in range(1, meses+1)])
    
    # Calcular el VPN
    vpn = calcular_vpn(meses, inversion_mensual, flujos_futuros, tasa_mensual)
    
    # Calcular la rentabilidad
    rentabilidad = vpn / valor_presente_inversion
    return rentabilidad

# Rentabilidad para 12 meses
rentabilidad_12_meses = calcular_rentabilidad(meses, inversion_mensual, flujos_futuros, tasa_mensual)

# Rentabilidad para 15 meses
rentabilidad_15_meses = calcular_rentabilidad(meses_extendido, inversion_mensual, flujos_futuros, tasa_mensual)

# Mostrar resultados
print(f"Rentabilidad para la duración original de 12 meses: {rentabilidad_12_meses:.4f}")
print(f"Rentabilidad para la duración extendida de 15 meses: {rentabilidad_15_meses:.4f}")
