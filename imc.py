def calcular_imc(peso, altura):
    if peso <= 0 or altura <= 0:
        raise ValueError("Peso e altura devem ser maiores que zero")

    return peso / (altura ** 2)


def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"