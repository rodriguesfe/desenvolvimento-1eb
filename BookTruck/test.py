import unittest
from App import db, models, modelsDAO

def compareObjects(obj1, obj2):
	if obj1 == None:
		return False
	dic1 = vars(obj1)
	for atributo in dic1:
		atributo1 = getattr(obj1, atributo)
		atributo2 = getattr(obj2, atributo)
		if atributo == 'id' or atributo.startswith('_') or type(atributo1) == list or type(atributo1) == object:
			continue
		#print(atributo)
		if atributo1 != atributo2:
			#print(atributo1)
			#print(atributo2)
			return False

	return True


class AppTestCase(unittest.TestCase):

	def setUp(self):
		db.drop_all()
		db.create_all()
		print('Setup completo')

	def test_obter_usuarios(self):
		db.drop_all()
		db.create_all()
		db.session.add(models.Usuario('Augusto', 'augusto', '1234', 1))
		db.session.add(models.Usuario('Fernanda', 'fernanda', '1234', 2))
		db.session.commit()
		usuarios = modelsDAO.obter_usuarios()
		self.assertEqual(usuarios, models.Usuario.query.all())

	def test_obter_usuario_por_user(self):
		db.drop_all()
		db.create_all()
		db.session.add(models.Usuario('Augusto', 'augusto', '1234', 1))
		db.session.add(models.Usuario('Fernanda', 'fernanda', '1234', 2))
		db.session.commit()
		self.assertEqual(modelsDAO.obter_usuario_por_user('augusto'), models.Usuario.query.filter_by(user = 'augusto').first())

	def test_inserir_usuario(self):
		db.drop_all()
		db.create_all()
		nome = 'Augusto'
		user = 'augusto'
		senha = '1234'
		tipo = 1
		db.session.add(models.Usuario('Fernanda', 'fernanda', '1234', 2))
		userTest = models.Usuario(nome, user, senha, tipo)
		modelsDAO.inserir_usuario(userTest.nome, userTest.user, userTest.senha, userTest.tipo)
		usuario = models.Usuario.query.filter_by(user = 'augusto').first()
		self.assertEqual(compareObjects(usuario, userTest), True)

	def test_atualizar_usuario(self):
		db.drop_all()
		db.create_all()
		usuario = models.Usuario('Augusto', 'augusto', '1234', 1)
		db.session.add(usuario)
		db.session.commit()
		userTest = models.Usuario('novo nome', usuario.user, 'nova senha', usuario.tipo)
		modelsDAO.atualizar_usuario(usuario.id, userTest.nome, userTest.senha)
		self.assertEqual(compareObjects(usuario, userTest), True)

	def test_remover_usuario(self):
		db.drop_all()
		db.create_all()
		usuario = models.Usuario('Augusto', 'augusto', '1234', 1)
		db.session.add(usuario)
		db.session.commit()
		idUsuario = usuario.id
		modelsDAO.remover_usuario(usuario.id)
		self.assertEqual(models.Usuario.query.get(idUsuario), None)

	def test_obter_autores(self):
		db.drop_all()
		db.create_all()
		db.session.add(models.Autor('Jose'))
		db.session.add(models.Autor('Francisco'))
		db.session.commit()
		autor = modelsDAO.obter_autores()
		self.assertEqual(autor, models.Autor.query.all())

	def test_inserir_autor(self):
		db.drop_all()
		db.create_all()
		nome = 'Jose'
		autorTest = models.Autor(nome)
		modelsDAO.inserir_autor(autorTest.nome)
		autor = models.Autor.query.filter_by(nome = 'Jose').first()
		self.assertEqual(compareObjects(autor, autorTest), True)

	def test_obter_autor_por_nome(self):
		db.drop_all()
		db.create_all()
		db.session.add(models.Autor('Jose'))
		db.session.commit()
		self.assertEqual(modelsDAO.obter_autor_por_nome('Jose'), models.Autor.query.filter_by(nome = 'Jose').first())

	def test_atualizar_autor(self):
		db.drop_all()
		db.create_all()
		autor = models.Autor('Jose')
		db.session.add(autor)
		db.session.commit()
		autorTest = models.Autor('novo nome')
		modelsDAO.atualizar_autor(autor.id, autorTest.nome)
		self.assertEqual(compareObjects(autor, autorTest), True)

	def test_remover_autor(self):
		db.drop_all()
		db.create_all()
		autor = models.Autor('Jose')
		db.session.add(autor)
		db.session.commit()
		idAutor = autor.id
		modelsDAO.remover_autor(autor.id)
		self.assertEqual(models.Autor.query.get(idAutor), None)

	def test_obter_editoras(self):
		db.drop_all()
		db.create_all()
		db.session.add(models.Editora('Alfa'))
		db.session.add(models.Editora('Omega'))
		db.session.commit()
		editora = modelsDAO.obter_editoras()
		self.assertEqual(editora, models.Editora.query.all())


	def test_inserir_editora(self):
		db.drop_all()
		db.create_all()
		nome = 'Amago'
		editoraTest = models.Editora(nome)
		modelsDAO.inserir_editora(editoraTest.nome)
		editora = models.Editora.query.filter_by(nome = 'Amago').first()
		self.assertEqual(compareObjects(editora, editoraTest), True)

	def test_obter_editora_por_nome(self):
		db.drop_all()
		db.create_all()
		db.session.add(models.Editora('Amago'))
		db.session.commit()
		self.assertEqual(modelsDAO.obter_editora_por_nome('Amago'), models.Editora.query.filter_by(nome = 'Amago').first())


	def test_atualizar_editora(self):
		db.drop_all()
		db.create_all()
		editora = models.Editora('Alfa')
		db.session.add(editora)
		db.session.commit()
		editoraTest = models.Editora('novo nome')
		modelsDAO.atualizar_editora(editora.id, editoraTest.nome)
		self.assertEqual(compareObjects(editora, editoraTest), True)


	def test_remover_editora(self):
		db.drop_all()
		db.create_all()
		editora = models.Editora('Omega')
		db.session.add(editora)
		db.session.commit()
		idEditora = editora.id
		modelsDAO.remover_editora(editora.id)
		self.assertEqual(models.Editora.query.get(idEditora), None)

	def test_obter_livro(self):
		db.drop_all()
		db.create_all()
		db.session.add(models.Autor('Jose'))
		db.session.add(models.Editora('Alfa'))
		autor = models.Autor.query.filter_by(nome = 'Jose').first()
		editora = models.Editora.query.filter_by(nome = 'Alfa').first()
		db.session.add(models.Livro(123456, 'A volta dos que não foram', 'Drama', 1, 2007, 'Esse livro é um drama sobra a volta dos que não foram', 2, editora.id, autor.id))
		db.session.commit()
		livro = modelsDAO.obter_livros()
		self.assertEqual(livro, models.Livro.query.all())

	def test_inserir_livro(self):
		db.drop_all()
		db.create_all()
		db.session.add(models.Autor('Jose'))
		db.session.add(models.Editora('Alfa'))
		db.session.commit()
		autor = models.Autor.query.filter_by(nome = 'Jose').first()
		editora = models.Editora.query.filter_by(nome = 'Alfa').first()
		livroTest = models.Livro(123456, 'A volta dos que não foram', 'Drama', 1, 2007, 'Esse livro é um drama sobra a volta dos que não foram', 2, editora.id, autor.id)
		modelsDAO.inserir_livro(123456, 'A volta dos que não foram', 'Drama', 1, 2007, 'Esse livro é um drama sobra a volta dos que não foram', 2, editora.id, autor.id)
		livro = models.Livro.query.filter_by(isbn = livroTest.isbn).first()
		self.assertEqual(compareObjects(livro, livroTest), True)

	def test_obter_livro_por_titulo(self):
		db.drop_all()
		db.create_all()
		db.session.add(models.Autor('Jose'))
		db.session.add(models.Editora('Alfa'))
		autor = models.Autor.query.filter_by(nome = 'Jose').first()
		editora = models.Editora.query.filter_by(nome = 'Alfa').first()
		db.session.add(models.Livro(123456, 'A volta dos que não foram', 'Drama', 1, 2007, 'Esse livro é um drama sobra a volta dos que não foram', 2, editora.id, autor.id))
		db.session.commit()
		livro = modelsDAO.obter_livro_por_titulo('A volta dos que não foram')
		self.assertEqual(modelsDAO.obter_livro_por_titulo('A volta dos que não foram'), models.Livro.query.filter_by(titulo = 'A volta dos que não foram').first())


	def test_atualizar_livro(self):
		db.drop_all()
		db.create_all()
		db.session.add(models.Autor('Jose'))
		db.session.add(models.Editora('Alfa'))
		autor = models.Autor.query.filter_by(nome = 'Jose').first()
		editora = models.Editora.query.filter_by(nome = 'Alfa').first()
		livro = models.Livro(123456, 'A volta dos que não foram', 'Drama', 1, 2007, 'Esse livro é um drama sobra a volta dos que não foram', 2, editora.id, autor.id)
		db.session.add(livro)
		db.session.commit()
		livroTest = models.Livro(123456, 'A volta', 'Drama', 1, 2007, 'Esse livro é um drama sobra a volta dos que não foram', 2, editora.id, autor.id)
		modelsDAO.atualizar_livro(livro.id, livroTest.titulo)
		self.assertEqual(compareObjects(livro, livroTest), True)
		

	def test_remover_livro(self):
		db.drop_all()
		db.create_all()
		db.session.add(models.Autor('Jose'))
		db.session.add(models.Editora('Alfa'))
		autor = models.Autor.query.filter_by(nome = 'Jose').first()
		editora = models.Editora.query.filter_by(nome = 'Alfa').first()
		livro = models.Livro(123456, 'A volta dos que não foram', 'Drama', 1, 2007, 'Esse livro é um drama sobra a volta dos que não foram', 2, editora.id, autor.id)
		db.session.add(livro)
		db.session.commit()
		idLivro = livro.id
		modelsDAO.remover_livro(livro.id)
		self.assertEqual(models.Livro.query.get(idLivro), None)
		

		
if __name__ == '__main__':
	unittest.main()










