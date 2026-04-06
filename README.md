# 📊 Calculadora de IMC

## 📌 Descrição

Este projeto consiste em uma aplicação simples para cálculo do Índice de Massa Corporal (IMC), com base no peso e altura do usuário.

O objetivo do projeto é demonstrar a aplicação de testes unitários automatizados para validação das regras de negócio, garantindo qualidade e confiabilidade do código.

---

## 🧠 Regras de Negócio Testadas

* O IMC é calculado pela fórmula:

  IMC = peso / (altura²)

* O peso deve ser maior que zero

* A altura deve ser maior que zero

* Caso contrário, o sistema deve lançar uma exceção (`ValueError`)

### Classificação do IMC:

| IMC             | Classificação  |
| --------------- | -------------- |
| IMC < 18.5      | Abaixo do peso |
| 18.5 ≤ IMC < 25 | Peso normal    |
| 25 ≤ IMC < 30   | Sobrepeso      |
| IMC ≥ 30        | Obesidade      |

---

## 🧪 Testes Unitários

Os testes foram implementados utilizando a biblioteca **Pytest**.

Os seguintes cenários são testados:

* Cálculo correto do IMC
* Validação de valores inválidos (peso e altura ≤ 0)
* Classificação correta para todas as faixas de IMC:

  * Abaixo do peso
  * Peso normal
  * Sobrepeso
  * Obesidade

---

## ⚙️ Tecnologias Utilizadas

* Python
* Pytest
* pytest-cov (para cobertura de testes)

---

## ▶️ Como Executar o Projeto

### 1. Instalar dependências

pip install pytest pytest-cov

---

### 2. Executar os testes

pytest --cov=imc

---

## 📊 Cobertura de Testes

Adicione aqui o print da cobertura gerada após rodar o comando acima.

---

## 📁 Estrutura do Projeto

imc-calculadora/
│
├── imc.py
├── test_imc.py
├── README.md

---

## 📊 Cobertura de Testes
<img width="1920" height="1080" alt="TESTE" src="https://github.com/user-attachments/assets/fcc13510-89eb-45e4-9646-dfbd03b7ae16" />
<img width="1920" height="1080" alt="TESTE" src="https://github.com/user-attachments/assets/fcc13510-89eb-45e4-9646-dfbd03b7ae16" />




## 👨‍💻 Autor


Dyego Kelven
