#Entrada de dados
valorCompra = float(input("Digite o valor total da comprar: R$ "))

#Condições para desconto

if valorCompra <200:
    taxaDesconto = 0.05 #5% de desconto.

elif valorCompra <300:
    taxaDesconto = 0.10 #10% de desconto.

else: 
    taxaDesconto = 0.15 #15% de desconto.

#Calculo de desconto e valor final da compra
valorDesconto =  valorCompra * taxaDesconto
valorFinal = valorCompra - valorDesconto

#Saída exibição das informações
print ("\n --- Resumo da compra ---")
print (f"Valor da Compra: R$ {valorCompra:.2f}")
print (f"Taxa de desconto aplicada: {taxaDesconto * 100:.0f}%")
print (f"Valor de desconto: R$ {valorDesconto:.2f}")
print (f"Valor a ser pago: R$ {valorFinal:.2f}")