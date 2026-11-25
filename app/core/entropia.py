import math
import string

# Conjuntos de caracteres y cuántos caracteres aporta cada uno
MINUSCULAS = string.ascii_lowercase   # 26
MAYUSCULAS = string.ascii_uppercase   # 26
DIGITOS = string.digits               # 10
SIMBOLOS = string.punctuation         # 32


def tamano_alfabeto(password: str) -> int:
    """Devuelve R: cuántos caracteres distintos podría haber usado el atacante."""
    tamano = 0
    if any(c in MINUSCULAS for c in password):
        tamano += 26
    if any(c in MAYUSCULAS for c in password):
        tamano += 26
    if any(c in DIGITOS for c in password):
        tamano += 10
    if any(c in SIMBOLOS for c in password):
        tamano += 32
    # Espacios, acentos, ñ, emojis, etc.
    conocidos = MINUSCULAS + MAYUSCULAS + DIGITOS + SIMBOLOS
    if any(c not in conocidos for c in password):
        tamano += 32
    return tamano


def calcular_entropia(password: str) -> float:
    """Entropía en bits: L * log2(R)."""
    if not password:
        return 0.0
    return len(password) * math.log2(tamano_alfabeto(password))

INTENTOS_POR_SEGUNDO = 10_000_000_000  # 10 mil millones (GPU potente)


def tiempo_crackeo_segundos(entropia: float) -> float:
    """En promedio el atacante acierta a la mitad de las combinaciones."""
    combinaciones = 2.0 ** min(entropia, 1000)   # el min evita desbordar el float
    return combinaciones / 2 / INTENTOS_POR_SEGUNDO


def formatear_tiempo(segundos: float) -> str:
    if segundos < 1:
        return "menos de 1 segundo"
    unidades = [
        ("años", 31_536_000),
        ("días", 86_400),
        ("horas", 3_600),
        ("minutos", 60),
        ("segundos", 1),
    ]
    for nombre, valor in unidades:
        if segundos >= valor:
            cantidad = segundos / valor
            if cantidad >= 1e12:
                return f"{cantidad:.2e} {nombre}"
            return f"{cantidad:,.0f} {nombre}"


def clasificar(entropia: float) -> str:
    if entropia < 28:
        return "muy débil"
    if entropia < 36:
        return "débil"
    if entropia < 60:
        return "media"
    if entropia < 128:
        return "fuerte"
    return "muy fuerte"