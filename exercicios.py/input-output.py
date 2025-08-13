#Soma dois números, multiplica o resultado por um terceiro e exibe o valor final.

num1 = int(input("Escreva um número:")) 
num2 = int(input("Escreva outro número:")) 
num3 = int(input("Escreva mais um número:")) 

soma = (num1 + num2) 
valorfinal = (soma * num3) 

print (valorfinal) 

#Calcula a média ponderada de notas e informa se o aluno foi aprovado ou reprovado.

notaTrabalho = float(input("Digite sua nota do trabalho:"))  
notaAtividade = float(input("Digite sua nota da atividade:"))  
notaParticipacao = float(input("Digite sua nora de participação nas provas:")) 
media = (notaTrabalho * 0.3) + (notaAtividade * 0.2) + (notaParticipacao * 0.5) 

if media >=6.0: print("Aprovado!") 
  else: print("Reprovado!") 

#Calcula aumento salarial baseado no código do cargo e exibe salário antigo, novo e a diferença.

salario = float(input("Digite o salário atual: ")) 
codigo = int(input("Digite o código do cargo: ")) 
if codigo == 101: 
    percentual = 0.10 
else: 
    if codigo == 102: 
        percentual = 0.20 
    else: 
        if codigo == 103: 
            percentual = 0.30 
        else: 
            percentual = 0.40 

novo_salario = salario * (1 + percentual) 
diferenca = novo_salario - salario 

print(f"Salário antigo: R$ {salario:.2f}") 
print(f"Novo salário: R$ {novo_salario:.2f}") 
print(f"Diferença: R$ {diferenca:.2f}") 
