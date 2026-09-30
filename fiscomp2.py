print("Números impares del 1 al 30")
for numero in range(1, 31, 2):
    print(numero)
print("\n" + "=" * 40 + "\n")
dicc = {
    "entero": 15,
    "flotante": 5.3,
    "lista": ["Bleach", "One Piece", "Naruto"],
    "tupla": (3, 10, 2),
}
print("ELEMENTOS DEL DICCIONARIO")
print("Elemento int:", dicc["entero"])
print("Elemento float:", dicc["flotante"])
print("Elemento list:", dicc["lista"])
print("Elemento tupla:", dicc["tupla"])
print("\n" + "=" * 40 + "\n")
def calcular_e_k(m_kg, v_kmh):
    v_ms = v_kmh / 3.6
    ek = 0.5 * m_kg * (v_ms**2)
    return ek, v_ms
masa = 4
velocidad_kmh = 2 
energia_j, velocidad_ms = calcular_e_k(masa, velocidad_kmh)
print("CÁLCULO ENERGIA CINETICA")
print(f"Masa: {masa} kg")
print(f"Velocidad: {velocidad_kmh} km/h ({velocidad_ms:.2f} m/s)")
print(f"Energía cinética (Ek): {energia_j:.2f} Joules")