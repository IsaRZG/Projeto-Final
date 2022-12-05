from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

#produtos_farmaceuticos = [
    #{'name': 'Estudar', 'finished': False}, 
    #{'name': 'Comer', 'finished': True}
#]
produtos_farmaceuticos=[]
@app.route('/')
def home():
    with open("app.json", 'r') as f:
        produtos_farmaceuticos = json.load(f)
    return render_template('home.html', produtos_farmaceuticos=produtos_farmaceuticos)

@app.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    produtos = {'name': name, 'finished': False}
    with open("app.json", 'r') as f:
        produtos_farmaceuticos = json.load(f)
    produtos_farmaceuticos.append(produtos)
    with open("app.json", 'w') as f:
        json.dump(produtos_farmaceuticos, f, indent= 2)
    return redirect(url_for('home'))
    
@app.route('/Deletar/<name>')
def deletar(name):
    with open("app.json", 'r') as f:
        produtos_farmaceuticos = json.load(f)
    produtos = {'name': name, 'finished': False}
    produtos_farmaceuticos.remove(produtos)
    with open("app.json", 'w') as f:
        json.dump(produtos_farmaceuticos, f, indent= 2)
    return redirect(url_for('home'))
app.run(debug=True)
