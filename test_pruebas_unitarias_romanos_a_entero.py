from main import romano_a_entero, RomanNumberError
import pytest

def test_romano_a_entero_I():
    assert romano_a_entero('I') == 1

def test_romano_a_entero_MDCCXIII():
    assert romano_a_entero('MDCCXIII') == 1713

def test_romano_a_entero_IV():
    assert romano_a_entero('IV') == 4

def test_romano_a_entero_no_repetir_3_veces():
    with pytest.raises( RomanNumberError ) as exeptionInfo:
        romano_a_entero("IIII")
        assert str(exeptionInfo.value) == "No se puede repetir el valor más de tres veces"
