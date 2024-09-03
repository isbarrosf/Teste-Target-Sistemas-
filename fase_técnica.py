# -*- coding: utf-8 -*-
"""Fase Técnica

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HsbwNWy8pDPLB85YsVHFXI5BT1Rsv6Lk

Questão 1)
"""

INDICE = 13
SOMA = 0
K = 0
while K < INDICE:
    K = K + 1
    SOMA = SOMA + K;

print('o resultado é ', (SOMA));

"""Questão 2"""

def is_fibonacci(n):
    a, b = 0, 1
    while b <= n:
        if b == n:
            return f"{n} pertence à sequência de Fibonacci."
        a, b = b, a + b
    return f"{n} não pertence à sequência de Fibonacci."

# Exemplo de uso
numero = 21
resultado = is_fibonacci(numero)
print(resultado)

"""Questão 3"""

import json

# Carregar dados do JSON
with open('/content/dados.json') as file:
    data = json.load(file)

# Filtrar os dias com faturamento
faturamento = [item['valor'] for item in data if item['valor'] > 0]

# Calcular menor, maior e média
menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)
media_faturamento = sum(faturamento) / len(faturamento)

# Dias com faturamento acima da média
dias_acima_da_media = sum(1 for valor in faturamento if valor > media_faturamento)

print(f"Menor faturamento: R${menor_faturamento:.2f}")
print(f"Maior faturamento: R${maior_faturamento:.2f}")
print(f"Dias acima da média: {dias_acima_da_media}")

"""Questão 4"""

# Valores fornecidos
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Total
total_faturamento = sum(faturamento_estados.values())

# Percentual de cada estado
percentuais = {estado: (valor / total_faturamento) * 100 for estado, valor in faturamento_estados.items()}

for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")

"""Questão 5

"""

def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

# Exemplo de uso
string = "Cachorro"
resultado = inverter_string(string)
print(f"String invertida: {resultado}")