class Restaurante:
    nome = ''
    categoria =''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza'
restaurante_pizza.categoria = 'Italiana'
restaurante_pizza.ativo = True

restaurantes = [restaurante_praca, restaurante_pizza]

for restaurante in restaurantes:
    if restaurante.ativo:
        print(vars(restaurante))
