class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self._ativo = ativo
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self._ativo}'
    
    def listar_restaurantes():
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(20)} | {"Ativo".ljust(6)}')
        print(f'{"-" * 57}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(20)} | {restaurante.ativo}')
    
    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_pizza = Restaurante('pizza Express','Italiana',True)

Restaurante.listar_restaurantes()

