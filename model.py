from conf import *

class Livros(db.Entity):
    nome = Required(str)
    autor = Required(str)
    ano = Optional(str)
    genero = Optional(str)
    classificacao = Optional(str)
    avaliacao = Optional(str)
    def __str__(self):
        return f'{self.nome}, {self.autor}, {self.ano}, {self.genero}, {self.classificacao}, {self.avaliacao}'

db.bind(provider='sqlite', filename='person.db', create_db=True)
db.generate_mapping(create_tables=True)
