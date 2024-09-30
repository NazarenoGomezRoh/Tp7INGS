# Importar librerías necesarias
import numpy as np

# Parámetros del problema
tasa_mensual = 0.01        # Tasa efectiva mensual del 1%
inversion_mensual = 1000   # Inversión mensual
flujos_futuros = 18000     # Valor presente de los flujos futuros en el mes 12
meses = 12                 # Duración inicial del proyecto en meses
meses_extendido = 15       # Duración extendida del proyecto en meses (12 + 3)

# a) Cálculo del VPN cuando el proyecto dura 12 meses
def calcular_vpn(meses, inversion_mensual, flujos_futuros, tasa_mensual):
    # Calcular el valor presente de las inversiones mensuales
    valor_presente_inversion = sum([inversion_mensual / (1 + tasa_mensual)**t for t in range(1, meses+1)])
    
    # Calcular el valor presente de los flujos futuros en el mes "meses"
    valor_presente_flujos_futuros = flujos_futuros / (1 + tasa_mensual)**meses
    
    # VPN = Valor presente de los flujos futuros - Valor presente de las inversiones
    vpn = valor_presente_flujos_futuros - valor_presente_inversion
    return vpn

# Cálculo para 12 meses
vpn_12_meses = calcular_vpn(meses, inversion_mensual, flujos_futuros, tasa_mensual)

# b) Cálculo del VPN cuando el proyecto dura 15 meses (se extiende 3 meses más)
vpn_15_meses = calcular_vpn(meses_extendido, inversion_mensual, flujos_futuros, tasa_mensual)

# Mostrar resultados
print(f"VPN para la duración original de 12 meses: ${vpn_12_meses:.2f}")
print(f"VPN para la duración extendida de 15 meses: ${vpn_15_meses:.2f}")
