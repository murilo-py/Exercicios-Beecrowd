'''
Neste problema você é solicitado a escrever um simples programa de conversão de base. A entrada será um valor hexadecimal ou decimal. Você deverá converter cada valor da entrada. Se o valor for hexadecimal, você deve convertê-lo para decimal e vice-versa. O valor hexadecimal inicia sempre com “0x” ou também, é aquele valor cuja segunda casa contém a letra 'x'.

Entrada
A entrada contém vários casos de teste. Cada linha de entrada, com exceção da última, contém um número não-negativo, decimal ou hexa. O valor decimal será menor ou igual a 231. A última linha contém um número negativo que não deve ser processado, indicando o encerramento do programa.

Saída
Para cada linha de entrada (exceto a última) deve ser produzido uma linha de saída. Todo número hexadecimal deve ser precedido na saída por '0x' (zero xis).
'''
valores_hexa = "0123456789ABCDEF"

while True:

    linha = input().strip()
    
    if linha[0] == '-':
        break

    if len(linha) > 1 and (linha[1] == 'x' or linha[1] == 'X'):
        hexa = linha[2:].upper()
        
        decimal = 0
        
        hexa_invertido = hexa[::-1]
        
        
        for i in range(len(hexa_invertido)):
            digito = hexa_invertido[i]
            
            valor_digito = valores_hexa.index(digito)
            
            
            decimal += valor_digito * (16 ** i)
            
        print(decimal)


    else:
        numero = int(linha)
        
        
        if numero == 0:
            print("0x0")
            continue
            
        resultado_hexa = ""

        while numero > 0:
            resto = numero % 16
            resultado_hexa += valores_hexa[resto] 
            numero = numero // 16                 

        resultado_hexa = resultado_hexa[::-1]
        
        print("0x" + resultado_hexa)