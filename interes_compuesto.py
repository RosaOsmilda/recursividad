# Interés compuesto con recursividad
# C(0) = m  |  C(n) = C(n-1) * (1 + i)

def monto(m, i, n):
    if n == 0:                       # caso base
        return m
    return monto(m, i, n - 1) * (1 + i)   # caso recursivo


print("=== Capitalización recursiva (interés compuesto) ===")
m = float(input("Capital inicial (m): "))
x = float(input("Tasa de interés anual en % (X): "))
n = int(input("Tiempo en años (n): "))

i = x / 100                          # convertir porcentaje a decimal
print(f"\nMonto acumulado después de {n} años: ${monto(m, i, n):,.2f}")

