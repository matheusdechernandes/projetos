#Entrada de dados
nomeAparelho = input("Digite o nome do aparelho: ")
potencia = float(
    input("Digite a potência do aparelho em Watts: ") 
)
horasDia = float(
    input("Digite o tempo médio de consumo diário: ")
)

#Parametros para calculo
diasMes = 30
tarifaKwh = 0.75


#Calculo de consumo
if potencia>0 and horasDia>0:
    consumoMensal = (potencia*horasDia*diasMes)/1000
    custoEstimado = (consumoMensal*tarifaKwh)

#Saida de dados
print (f"Aparelho: {nomeAparelho}")
print (f"Consumo estimado: {consumoMensal:.2f} kWh/mês")
print (f"Valor estimado em R$: {custoEstimado:.2f} mês")