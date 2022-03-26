from flask import Flask, render_template, request, redirect
app = Flask('app')

todos = [] 

# Deixar a lista vazia

@app.route('/')
def index():
  return render_template(
    'index.html',
    todos = todos
  )

@app.route('/create', methods=['POST'])
def inicio():
  nome = request.form.get('name')
  todos.append({'title': nome})
  return redirect('/')
  
if __name__ == '__main__':
    app.run(host='0.0.0.0')