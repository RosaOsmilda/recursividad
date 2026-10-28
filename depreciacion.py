# Depreciación por saldo decreciente con recursividad
# V(0) = V0  |  V(t) = V(t-1) * (1 - d/100)

def valor_contable(v, d, t):
    if t == 0:                       # caso base
        return v
    return valor_contable(v, d, t - 1) * (1 - d / 100)   # caso recursivo


def pedir_anios():
    t = int(input("Años transcurridos (t): "))
    if t < 0:                        # validar años negativos
        print("  Error: no se permiten años negativos.")
        return pedir_anios()
    return t


print("=== Depreciación por saldo decreciente ===")
v = float(input("Valor de compra (V): "))
d = float(input("Tasa de depreciación anual % (d): "))
t = pedir_anios()

print(f"\nValor contable al final del año {t}: ${valor_contable(v, d, t):,.2f}")



