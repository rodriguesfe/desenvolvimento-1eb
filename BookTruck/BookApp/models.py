
# -*- coding: utf-8 -*-
from BookApp import db
from sqlalchemy.types import DECIMAL
#from flask_login import LoginManager, UserMixin

class Usuario(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	nome = db.Column(db.String(200))
	user = db.Column(db.String(200), unique = True)
	senha = db.Column(db.String(50))
	'''Tipo 1 define que o usuario é administrador. Tipo 2 define que é usuário cliente'''
	tipo = db.Column(db.Integer)
	carrinho = db.relationship('Carrinho', backref='usuario', uselist = False)
	#compra = db.relationship('Compra', backref='usuario', uselist=False)

	def __init__(self, nome, user, senha, tipo):
		self.nome = nome
		self.user = user
		self.senha = senha
		self.tipo = tipo

class Autor(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	nome = db.Column(db.String(200))
	livros = db.relationship('Livro', backref = 'autor', lazy = 'dynamic')
	def __init__(self, nome):
		self.nome = nome

class Editora(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	nome = db.Column(db.String(200))
	livros = db.relationship('Livro', backref = 'editora', lazy = 'dynamic')
	def __init__(self, nome):
		self.nome = nome

class Livro(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	isbn = db.Column(db.Integer, unique = True)
	titulo = db.Column(db.String(200))
	categoria = db.Column(db.String(100))
	edicao = db.Column(db.Integer)
	ano = db.Column(db.Integer)
	descricao = db.Column(db.Text)
	id_autor = db.Column(db.Integer, db.ForeignKey(Autor.id))
	id_editora = db.Column(db.Integer, db.ForeignKey(Editora.id))
	preco = db.Column(DECIMAL(10,2))
	#item = db.relationship('Item', uselist = False, back_populates = 'livro')
	#catalogo define se o livro está ou não no catálogo
	#0 não está, 1 está
	catalogo = db.Column(db.Integer)
	def __init__(self, isbn, titulo, categoria, edicao, ano, descricao, id_autor, id_editora, preco, catalogo):
		self.isbn = isbn
		self.titulo = titulo
		self.categoria = categoria
		self.edicao = edicao
		self.ano = ano
		self.descricao = descricao
		self.id_autor = id_autor
		self.id_editora = id_editora
		self.preco = preco
		self.catalogo = catalogo

class Carrinho(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	id_usuario = db.Column(db.Integer, db.ForeignKey(Usuario.id))
	id_livro = db.Column(db.Integer, db.ForeignKey(Livro.id))
	#usuario = db.relationship('Usuario', backref='carrinho', uselist=False)
	#item = db.relationship('Item', uselist = False, back_populates = 'carrinho')
	def __init__(self, id_usuario):
		self.id_usuario = id_usuario
		

class Local(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	bairro = db.Column(db.String(200))

'''
class Compra(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    #id_usuario = db.Column(db.Integer, db.ForeiginKey(Usuario.id))
    nome = db.Column(db.String(200))
    itens = db.relationship('Item', backref='compra', lazy = 'dynamic')
    def __init__(self, nome):
    	self.nome = nome
    def get_itens(self):
    	return list(db.session.execute(self.itens))


class Item(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	id_compra = db.Column(db.Integer, db.ForeignKey('compra.id'), nullable=False)
	def __init__(self, id_compra):
		self.id_compra = id_compra
'''

'''class Compra(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
	total = db.Column(DECIMAL(10,2))
	def __init__(self, id_usuario):
		self.id_usuario = id_usuario'''

'''
class Carrinho(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	id_usuario = db.Column(db.Integer, db.ForeignKey(Usuario.id))
	id_livro = db.Column(db.Integer, db.ForeignKey(Livro.id))
	#usuario = db.relationship('Usuario', backref='carrinho', uselist=False)
	#item = db.relationship('Item', uselist = False, back_populates = 'carrinho')
	def __init__(self, id_usuario, id_livro):
		self.id_usuario = id_usuario
		self.id_livro = id_livro'''
    	


'''class Item(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	id_carrinho = db.Column(db.Integer, db.ForeignKey('carrinho.id'), nullable=True)
	id_compra = db.Column(db.Integer, db.ForeignKey('compra.id'), nullable=True)
	id_livro = db.Column(db.Integer, db.ForeignKey('livro.id'))
	carrinho = db.relationship('Carrinho', back_populates='item')
	compra = db.relationship('Compra', backref='itens', uselist=False)
	livro = db.relationship('Livro', back_populates='item')

	def __init__(self, id_compra):
		self.id_compra = id_compra'''
