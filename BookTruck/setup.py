from BookApp import db, models
from copy import copy

db.drop_all()
db.create_all()


'''Cria usuários administradores'''
nome = 'admin'
user = 'admin'
senha = 1234

admin = models.Usuario(user=user, nome=nome, senha=senha, tipo=1)
db.session.add(admin)
db.session.commit()

nome = 'adm'
user = 'adm'
senha = 5678

admin = models.Usuario(user=user, nome=nome, senha=senha, tipo=1)
db.session.add(admin)
db.session.commit()

print('done')
