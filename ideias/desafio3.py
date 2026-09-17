produto = input('Produto:=>')
preco_produto = float(input('Preço R$:=>'))
quantidade = int(input('Quantidade:=>'))

subtotal = preco_produto * quantidade

if subtotal >= 100:
    desconto = subtotal * 0.10
else:
    desconto = 0

total = subtotal - desconto
print(f'Produto {produto}')
print(f'Subtotal {subtotal:.2f}')
print(f'Desconto R$: {desconto:.2f}')
print(f'Total: R$ {total:.2f}')