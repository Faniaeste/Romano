from main import entero_a_romano

def test_entero_romano_1994():
    assert entero_a_romano(1994) == 'MCMXCI'

def test_entero_romano_3():
    assert entero_a_romano(3) == 'III'

def test_entero_romano_33():
    assert entero_a_romano(33) == 'XXXIII'

def test_entero_romano_333():
    assert entero_a_romano(333) == 'CCCXXXIII'
    


