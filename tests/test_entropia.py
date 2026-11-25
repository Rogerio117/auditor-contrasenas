import pytest
from app.core.entropia import (
    tamano_alfabeto, calcular_entropia, tiempo_crackeo_segundos,
    formatear_tiempo, clasificar,
)


def test_tamano_alfabeto():
    assert tamano_alfabeto("abc") == 26
    assert tamano_alfabeto("abc123") == 36
    assert tamano_alfabeto("Abc123!") == 94


def test_entropia_conocida():
    assert calcular_entropia("abc123") == pytest.approx(31.02, abs=0.1)
    assert calcular_entropia("Tr0ub4dor&3") == pytest.approx(72.1, abs=0.1)


def test_vacia():
    assert calcular_entropia("") == 0.0


def test_clasificacion():
    assert clasificar(20) == "muy débil"
    assert clasificar(72) == "fuerte"


def test_tiempo_debil_es_instantaneo():
    t = tiempo_crackeo_segundos(calcular_entropia("abc123"))
    assert formatear_tiempo(t) == "menos de 1 segundo"