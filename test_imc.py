import pytest
from imc import calcular_imc, classificar_imc


def test_calcular_imc_valido():
    imc = calcular_imc(70, 1.75)
    assert round(imc, 2) == 22.86


def test_calcular_imc_valor_invalido():
    with pytest.raises(ValueError):
        calcular_imc(0, 1.75)


def test_classificacao_abaixo_peso():
    assert classificar_imc(17) == "Abaixo do peso"


def test_classificacao_normal():
    assert classificar_imc(22) == "Peso normal"


def test_classificacao_sobrepeso():
    assert classificar_imc(27) == "Sobrepeso"


def test_classificacao_obesidade():
    assert classificar_imc(32) == "Obesidade"