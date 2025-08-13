#Exibição de frase com as populações de duas cidades e o total somado.

populacaoNA = 45000 
fraseNA = f"Nova Andradina tem a população de {populacaoNA}" 
populacaoIV = 40000 
popTotal = populacaoNA + populacaoIV 

fraseTotal = f"Nova Andradina tem a população de {populacaoNA}, Ivinhema a população de {populacaoIV} e o total de {popTotal}" 

print(fraseNA) 

print(fraseTotal) 

#Calcule a quantidade de latas de tinta e o custo total para pintar uma área.

tamanho_area = float(input("Digite o tamanho da área a ser pintada (em m²): ")) 
cobertura_por_m2 = float(input("Digite a cobertura da tinta (litros por m²): ")) 
tamanho_lata = float(input("Digite o tamanho da lata de tinta (em litros): "))  
preco_lata = float(input("Digite o preço da lata de tinta (em R$): ")) 

litros_necessarios = tamanho_area / cobertura_por_m2 
qtd_latas = (litros_necessarios + tamanho_lata - 1) // tamanho_lata 
qtd_latas = int(qtd_latas) 

valor_total = qtd_latas * preco_lata 

print(f"\nQuantidade de latas a serem compradas: {qtd_latas}") print(f"Valor total: R$ {valor_total:.2f}") 


#Calcula quantas caixas de medicamentos devem ser compradas para cobrir o consumo de 30 dias, considerando o estoque atual.

from math import ceil 
def calcular_caixas(uso_diario, unidades_por_caixa, estoque_atual):  

total_mensal = uso_diario * 30  
falta = total_mensal - estoque_atual  
if falta <= 0:  
return 0  
return ceil(falta / unidades_por_caixa) 

caixas_prixicliato = calcular_caixas(3, 30, 44) 
caixas_zitaropan = calcular_caixas(4, 60, 52) 
caixas_madozol = calcular_caixas(1, 15, 36) 
caixas_tilazinan = calcular_caixas(1, 30, 14) 

print("Caixas a comprar para o próximo mês:")  
print(f"Prixicliato de Citamina: {caixas_prixicliato} caixa(s)")  
print(f"Zitaropan: {caixas_zitaropan} caixa(s)")  
print(f"Madozol: {caixas_madozol} caixa(s)")  
