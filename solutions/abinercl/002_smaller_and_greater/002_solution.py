def encontra_min_max(numeros):

  menor = min(numeros)
  maior = max(numeros)
  return menor, maior


meu_array = [1, 2, 3, 4, 5, 6, -7, -8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, -20]
menor_valor, maior_valor = encontra_min_max(meu_array)
print(meu_array)
print(f"O menor valor é: {menor_valor}")
print(f"O maior valor é: {maior_valor}")