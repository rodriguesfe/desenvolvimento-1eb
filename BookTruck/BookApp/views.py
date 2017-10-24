from BookApp import app
from flask import render_template, redirect, url_for, request

@app.route('/')    
@app.route('/home')
def homepage():
	return render_template('index.html')

#ROTA DE TESTE
@app.route('/homeC')
def homeC():
	return render_template('homeC.html')

@app.route('/login')  
def login(): 
	return render_template('login.html')

#ROTA DE TESTE
@app.route('/loginM')
def loginM():
	return render_template('loginM.html')

@app.route('/registrar')
def registro():
	return render_template('registrar.html')

@app.route('/catalogo') 
def catalogo():
	return render_template('catalogo.html')

@app.route('/carrinho')
def carrinho():
	return render_template('carrinho.html')


@app.route('/perfil')
def perfil():
	return render_template('perfil.html')

