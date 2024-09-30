# Importar librerías necesarias
import numpy as np
from scipy.optimize import fsolve

# Parámetros del problema
tasa_mensual = 0.01        # Tasa efectiva mensual del 1%
flujos_futuros = 18000     # Valor presente de los flujos futuros en el mes 12
meses = 12                 # Duración inicial del proyecto
meses_extendido = 15       # Duración extendida del proyecto (12 + 3)
inversion_mensual = 1000   # Inversión mensual original

# Función para calcular el VPN
def calcular_vpn(meses, inversion_mensual, flujos_futuros, tasa_mensual):
    # Calcular el valor presente de las inversiones mensuales
    valor_presente_inversion = sum([inversion_mensual / (1 + tasa_mensual)**t for t in range(1, meses+1)])
    
    # Calcular el valor presente de los flujos futuros en el mes "meses"
    valor_presente_flujos_futuros = flujos_futuros / (1 + tasa_mensual)**meses
    
    # VPN = Valor presente de los flujos futuros - Valor presente de las inversiones
    vpn = valor_presente_flujos_futuros - valor_presente_inversion
    return vpn

# VPN para 12 meses con el costo original
vpn_12_meses = calcular_vpn(meses, inversion_mensual, flujos_futuros, tasa_mensual)

# Función objetivo para encontrar C_max que iguale el VPN de 15 meses al VPN de 12 meses
def funcion_objetivo(costo_mensual):
    # Calcular el VPN para 15 meses con el costo mensual que buscamos (C_max)
    vpn_15_meses = calcular_vpn(meses_extendido, costo_mensual, flujos_futuros, tasa_mensual)
    # Queremos que el VPN de 15 meses sea igual al VPN de 12 meses
    return vpn_15_meses - vpn_12_meses

# Usamos fsolve para encontrar el costo mensual que hace VPN_15 = VPN_12
costo_maximo_aceptable = fsolve(funcion_objetivo, inversion_mensual)[0]

# Mostrar el resultado
print(f"El costo mensual máximo aceptable para que el VPN de 15 meses sea igual al de 12 meses es: ${costo_maximo_aceptable:.2f}")
