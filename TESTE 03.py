"""3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa,
 na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
"""


import json

# Carregar os dados do faturamento mensal a partir de um arquivo JSON
with open('faturamento_indev.json', 'r') as f:
    faturamento_mensal = json.load(f)

# Inicializar as variáveis para o menor e o maior valor de faturamento
menor_faturamento = float('inf')
maior_faturamento = float('-inf')

# Calcular o menor e o maior valor de faturamento no mês
for faturamento_diario in faturamento_mensal:
    if faturamento_diario > maior_faturamento:
        maior_faturamento = faturamento_diario
    if faturamento_diario < menor_faturamento:
        menor_faturamento = faturamento_diario

# Calcular a média mensal, excluindo os dias sem faturamento
faturamento_total = sum(faturamento_mensal)
dias_com_faturamento = len([f for f in faturamento_mensal if f > 0])
media_mensal = faturamento_total / dias_com_faturamento

# Contar o número de dias em que o faturamento diário foi superior à média mensal
dias_acima_da_media = len([f for f in faturamento_mensal if f > media_mensal])

# Imprimir os resultados
print("Menor valor de faturamento: R$ {:.2f}".format(menor_faturamento))
print("Maior valor de faturamento: R$ {:.2f}".format(maior_faturamento))
print("Número de dias com faturamento acima da média mensal: {}".format(dias_acima_da_media))
