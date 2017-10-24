from App import db

class Usuario(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	nome = db.Column(db.String(200))
	user = db.Column(db.String(200), unique = True)
	senha = db.Column(db.String(50))
	#Tipo 1 define que o usuario é administrador. Tipo 2 define que é usuário cliente
	tipo = db.Column(db.Integer)

	def __init__(self, nome, user, senha, tipo):
		self.nome = nome
		self.user = user
		self.senha = senha
		self.tipo = tipo

class Autor(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	nome = db.Column(db.String(200))
	funcs = db.relationship('Livro', backref = 'Autor', lazy = 'dynamic')
	def __init__(self, nome):
		self.nome = nome

class Editora(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	nome = db.Column(db.String(200))
	funcs = db.relationship('Livro', backref = 'Editora', lazy = 'dynamic')
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
	#catalogo define se o livro está ou não no catálogo
	#0 não está, 1 está
	catalogo = db.Column(db.Integer)
	def __init__(self, isbn, titulo, categoria, edicao, ano, descricao, catalogo, id_editora, id_autor):
		self.isbn = isbn
		self.titulo = titulo
		self.categoria = categoria
		self.edicao = edicao
		self.ano = ano
		self.descricao = descricao
		self.catalogo = catalogo
		self.id_editora = id_editora
		self.id_autor = id_autor
		

class Local(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	bairro = db.Column(db.String(200))