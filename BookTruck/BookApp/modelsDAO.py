# -*- coding: utf-8 -*-
from BookApp import models, db

#teste ok
def obter_usuarios():
	return models.Usuario.query.all()

#testar
def obter_usuario_por_user(username):
	return models.Usuario.query.filter_by(user =  username).first()

#teste ok
def inserir_usuario(nome, user, senha, tipo):
	usuario = models.Usuario(nome, user, senha, tipo)
	db.session.add(usuario)
	db.session.commit()

#teste ok
def atualizar_usuario(id, nome, senha):
	usuario = models.Usuario.query.get(id)
	if(usuario is not None):
		usuario.nome = nome
		usuario.senha = senha
		db.session.commit()
	else:
		raise Exception('Usuario não existe')

#test ok
def remover_usuario(id):
	usuario = models.Usuario.query.get(id)
	if(usuario is not None):
		db.session.delete(usuario)
		db.session.commit()
	else:
		raise Exception('Usuario não existe')

#test ok
def obter_autores():
	return models.Autor.query.all()

#test ok
def inserir_autor(nome):
	autor = models.Autor(nome)
	db.session.add(autor)
	db.session.commit()

#test ok
def obter_autor_por_nome(nomeautor):
	return models.Autor.query.filter_by(nome = nomeautor).first()

#test ok
def atualizar_autor(id, nome):
	autor = models.Autor.query.get(id)
	if (autor is not None):
		autor.nome = nome
		db.session.commit()
	else:
		raise Exception('Autor não existe')

#test ok
def remover_autor(id):
	autor = models.Autor.query.get(id)
	if (autor is not None):
		db.session.delete(autor)
		db.session.commit()
	else:
		raise Exception('Usuário não existe')

#test ok
def obter_editoras():
	return models.Editora.query.all()

#test ok
def inserir_editora(nome):
	editora = models.Editora(nome)
	db.session.add(editora)
	db.session.commit()

#test ok
def obter_editora_por_nome(nomeeditora):
	return models.Editora.query.filter_by(nome = nomeeditora).first()

#test ok
def atualizar_editora(id, nome):
	editora = models.Editora.query.get(id)
	if (editora is not None):
		editora.nome = nome
		db.session.commit()
	else:
		raise Exception('Editora não existe')

#test ok
def remover_editora(id):
	editora = models.Editora.query.get(id)
	if (editora is not None):
		db.session.delete(editora)
		db.session.commit()
	else:
		raise Exception('Editora não existe')

#test ok
def obter_livros():
	return models.Livro.query.all()

#test ok
def inserir_livro(isbn, titulo, categoria, edicao, ano, descricao, catalogo, id_editora, id_autor):
	livro = models.Livro(isbn, titulo, categoria, edicao, ano, descricao, catalogo, id_editora, id_autor)
	db.session.add(livro)
	db.session.commit()


#test ok
def obter_livro_por_titulo(titulo):
	return models.Livro.query.filter_by(titulo =  titulo).first()

#test ok
def atualizar_livro(id, titulo):
	livro = models.Livro.query.get(id)
	if (livro is not None):
		db.session.titulo = titulo
		db.session.commit()
	else:
		raise Exception('Livro não existe')


#test ok
def remover_livro(id):
	livro = models.Livro.query.get(id)
	if (livro is not None):
		db.session.delete(livro)
		db.session.commit()
	else:
		raise Exception('Livro não existe')

