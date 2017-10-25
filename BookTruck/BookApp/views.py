from BookApp import app
from flask import render_template, redirect, url_for, request, flash, session
from BookApp import models, db, modelsDAO
from flask_sqlalchemy import SQLAlchemy
import os

@app.route('/')    
@app.route('/home')
def homepage():
	return render_template('index.html')

#--------------------------------LOGIN-------------------------------------#

@app.route('/login', methods = ['GET', 'POST'])  
def login():
	'''Se 'usuario estiver em sessão ele retorna pra pagina principal'''
	if 'usuario' in session:
		return render_template('index.html')
	'''Se não, ele pega atraves do 'POST' os dados que o usuário forneceu lá no formulário:'''
	if request.method == 'POST':
		nome = request.form['nome']
		senha = request.form['senha']
		'''Pesquisa o usuario no banco de acordo como a informação que o usuario forneceu'''
		usuario = models.Usuario.query.filter_by(nome=nome).first()

		'''Verifica se o usuario é válido e se a senha que o usuario forneceu é igual a que ele cadastrou'''
		if (usuario is not None and usuario.senha == senha):
			'''Pega o tipo do usuário, esse tipo é usado pra definir niveis de acesso'''
			session['usuario'] = usuario.tipo
			'''Retorna a página principal'''
			return render_template('index.html')
		else:
			'''Se algo der errado, ele retorna pra pagina de login novamente'''
			return render_template('login.html')
	return render_template('login.html')

#------------------------------------LOGOUT----------------------------------#

@app.route('/logout')
def logout():
	'''Verifica se o usúario está em sessão'''
	if 'usuario' in session:
		'''Se seim, ele dá um session.pop e encerra essa sessão'''
		session.pop('usuario', None)
		'''E retorn para a págia inicial'''
	return render_template('index.html')


#-----------------------------------CADASTRO---------------------------------#

@app.route('/registrar', methods = ['GET', 'POST'])
def registro():
	'''Verifica o metodo usado ('POST')'''
	if request.method == 'POST':
		'''Verifica se todos os campos do formulário foram preenchidos'''
		if not request.form['nome'] or not request.form['user'] or not request.form['senha']:
			flash('Por favor, preencha todos os campos!')
		else:
			'''Se sim, 'usuario' recebe as informações digitadas nos campos do formulário.
			Esse "2" é o tipo do usuario. Todo usuario inserido no banco atraves do formulário
			de cadastro vai ser do tipo "2", ou seja, tipo cliente'''
			usuario = models.Usuario(request.form['nome'], request.form['user'], request.form['senha'], 2)
			'''Adiciona no banco'''
			db.session.add(usuario)
			db.session.commit()
			flash('Registrado com sucesso!')
			'''Retorna pra página de login, para que o usuário possa logar'''
			return redirect(url_for('login'))
	return render_template('registrar.html')

#---------------------------------ADD LIVRO--------------------------------#

@app.route('/addLivro', methods = ['GET', 'POST'])
def addLivro():
	'''Verifica o metodo usado ('POST')'''
	if request.method == 'POST':
		'''Verifica se todos os campos do formulário foram preenchidos'''
		if not request.form['isbn'] or not request.form['titulo'] or not request.form['categoria'] or not request.form['edicao'] or not request.form['ano'] or not request.form['descricao'] or not request.form['preco'] or not request.form['catalogo'] or not request.form['id_autor'] or not request.form['id_editora']:
			flash('Por favor, preencha todos os campos!')
		else:
			'''Se sim, os dados fonecidos através do formulário são guardados em variaveis'''
			isbn = request.form['isbn']
			titulo = request.form['titulo']
			categoria = request.form['categoria']
			edicao = request.form['edicao']
			ano = request.form['ano']
			descricao = request.form['descricao']
			preco = request.form['preco']
			catalogo = request.form['catalogo']
			''' A variavel autor um pesquisa feita no banco de acordo com o nome fornecido pelo usuário'''
			autor = models.Autor.query.filter_by(nome = request.form['id_autor']).first()
			''' A variavel editora um pesquisa feita no banco de acordo com o nome fornecido pelo usuário'''
			editora = models.Editora.query.filter_by(nome = request.form['id_editora']).first()
			''' "livro" recebe as informações guardada nas variaveis
				editora.id e autor.id são os id de editora e autor'''
			livro = models.Livro(isbn, titulo, categoria, edicao, ano, descricao, preco, catalogo, editora.id, autor.id)
			'''Adiciona no banco'''
			db.session.add(livro)
			db.session.commit()
			flash('Livro adicionado com sucesso!')
			'''Retorna a página de add livro
			livros = livros = models.Livro.query.all() é a lista de todos os livros cadatrados no banco
			autores = models.Autor.query.all() é a lista de todos os autores cadatrados no banco
			editoras = models.Editora.query.all() é a lista de todos os editores cadatrados no banco '''
	return render_template('addLivro.html', livros = models.Livro.query.all(), autores = models.Autor.query.all(), editoras = models.Editora.query.all())


#----------------------------------REMOVER LIVRO--------------------------------------#

'''Esse metodo é similar ao metodo usado em modelsDAO na parte de testes'''
def remover_Livro(id):
	'''"livro" guarda o id do livro a ser excluído'''
	livro = models.Livro.query.get(id)
	'''verifica se o livro é válido'''
	if livro is not None:
		'''se sim, exclui o livro do banco'''
		db.session.delete(livro)
		db.session.commit()
	else:
		raise Exception('Livro não existe!')

'''o "<int:index>" na rota é o id do livro'''
@app.route('/addLivro/remover/<int:index>')
def removerlivro(index):
	'''chama o "metodo remover_livro"'''
	remover_Livro(index)
	'''Retorna a página de add livro'''
	return redirect(url_for('addLivro'))

#-------------------------------ATUALIZAR LIVRO---------------------------------------#

''' Pra atualizar um livro ele busca pelo id o livro que o usuario quer atualizar:
																	livro = models.Livro.query.get(id)
depois ele verifica qual é o metodo usado, se for 'GET', ele redireciona pra pagina de livros e a lista 
de livros já cadastrados. Se o metodo usado for 'POST' ele vai pegar as informações fornecidas pelo
usuario vai adicionar ao id do livro e vai dar um commit() pra atualizar.'''

@app.route('/addLivro/atualizar/<id>', methods = ['GET', 'POST'])
def atualizarLivro(id):
	'''"livro" guarda o id do livro a ser atualizado'''
	livro = models.Livro.query.get(id)
	'''Verifica o metodo usado ('GET')'''
	if request.method == 'GET':
		'''retorna pra página principal e a lista de livros do banco'''
		return render_template('addLivro.html', livro = models.Livro.query.all()) 
	else:
		'''se não, ele guarda as informações fornecidas pelo usuário no formulário e guarda em variaveis'''
		isbn = request.form['isbn']
		titulo = request.form['titulo']
		categoria = request.form['categoria']
		edicao = request.form['edicao']
		ano = request.form['ano']
		descricao = request.form['descricao']
		preco = request.form['preco']
		catalogo = request.form['catalogo']
		'''Mesma lógica usada pra adicionar'''
		autor = models.Autor.query.filter_by(nome = request.form['id_autor']).first()
		editora = models.Editora.query.filter_by(nome = request.form['id_editora']).first()

		'''recebe as variaveis com as novas informações'''
		livro.isbn = isbn
		livro.titulo = titulo
		livro.categoria = categoria
		livro.edicao = edicao
		livro.ano = ano
		livro.descricao = descricao
		livro.preco = preco
		livro.catalogo = catalogo
		livro.id_autor = autor.id
		livro.id_editora = editora.id
		'''faz commit das atualizãções'''
		db.session.commit()
		'''retorna pra página de add livro'''
	return redirect(url_for('addLivro'))


#-------------------------------------ADD AUTOR--------------------------------#
'''Funciona do mesmo jeito de addLivro'''

@app.route('/addAutor', methods = ['GET', 'POST'])
def addAutor():
	if request.method == 'POST':
		if not request.form['nome']:
			flash('Por favor, insira o nome do Autor!')
		else:
			autor = models.Autor(request.form['nome'])
			db.session.add(autor)
			db.session.commit()
			flash('Autor adicionado com sucesso!')
	return render_template('addAutor.html', autores = models.Autor.query.all())


#--------------------------------REMOVER AUTOR---------------------------------#	
'''Funciona do mesmo jeito de removerlivro'''
def remover_autor(id):
	autor = models.Autor.query.get(id)
	if (autor is not None):
		db.session.delete(autor)
		db.session.commit()
	else:
		raise Exception('Autor não existe')


@app.route('/addAutor/remover/<int:index>')
def removerAutor(index):
	remover_autor(index)
	flash('Autor removido!')
	return redirect(url_for('addAutor'))

#--------------------------------ATUALIZAR AUTOR---------------------------------#
'''Funciona do mesmo jeito de atualizarLIvro'''

@app.route('/addAutor/atualizar/<id>', methods = ['GET', 'POST'])
def atualizarAutor(id):
	autor = models.Autor.query.get(id)
	if request.method == 'GET':
		return render_template('addAutor.html', autor = models.Autor.query.all()) 
	else:
		nome = request.form['nome']
		
		autor.nome = nome

		db.session.commit()
		flash('autor atualizado!')
	return redirect(url_for('addAutor'))

#--------------------------------ADD EDITORA-------------------------------------#
'''Funciona do mesmo jeito de addLivro'''

@app.route('/addEditora', methods = ['GET', 'POST'])
def addEditora():
	if request.method == 'POST':
		if not request.form['nome']:
			flash('Por favor, adicione o nome da editora')
		else:
			editora = models.Editora(request.form['nome'])
			db.session.add(editora)
			db.session.commit()
			flash('Editora cadastrada com sucesso!')

	return render_template('addEditora.html', editoras = models.Editora.query.all())

#-------------------------------REMOVER EDITORA----------------------------------#	
'''Funciona do mesmo jeito de removerLIvro'''


def remover_editora(id):
	editora = models.Editora.query.get(id)
	if (editora is not None):
		db.session.delete(editora)
		db.session.commit()
	else:
		raise Exception('Editora não existe')

@app.route('/addEditora/remover/<int:index>')
def removerEditora(index):
	remover_editora(index)
	flash('Editora removida!')
	return redirect(url_for('addEditora')) 

#------------------------------ATUALIZAR EDITORA-------------------------------#
'''Funciona do mesmo jeito de atualizarLIvro'''

@app.route('/addEditora/atualizar/<id>', methods = ['GET', 'POST'])
def atualizarEditora(id):
	editora = models.Editora.query.get(id)
	if request.method == 'GET':
		return render_template('addEditora.html', editora = models.Editora.query.all()) 
	else:
		nome = request.form['nome']
		
		editora.nome = nome

		db.session.commit()
		flash('Editora atualizada!')
	return redirect(url_for('addEditora'))

#-----------------------------CATALOGO----------------------------------------#

@app.route('/catalogo') 
def catalogo():
	'''retorna a pagina de catalogo e a todos os livros do banco
	   através de livros = models.Livro.query.all()'''
	return render_template('catalogo.html', livros = models.Livro.query.all())

@app.route('/carrinho')
def carrinho():
	return render_template('cart.html')

