class Pessoa:
    def __init__(self, *filhos, nome=None, idade=45):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    daniel = Pessoa(nome='Daniel')
    antunes = Pessoa(daniel, nome='Antunes')
    print(Pessoa.cumprimentar(antunes))
    print(id(antunes))
    print(antunes.cumprimentar())
    print(antunes.nome)
    print(antunes.idade)
    for filho in antunes.filhos:
        print(filho.nome)