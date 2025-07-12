from flask import Flask , render_template, request, redirect, url_for

app = Flask(__name__)

usuariosac = []
contraseñasac = []


@app.route('/')
def inicio():
    return render_template('login.html')

@app.route('/sesion' , methods=['POST'])
def sesion():
    global usuariosac, contraseñasac


    usuario = request.form['usuario']
    contraseña = request.form['contraseña']

    if usuario in usuariosac:
        indice = usuariosac.index(usuario) 
        if contraseñasac[indice] == contraseña:
            return redirect(url_for('calculadora'))

        return render_template('login.html' ,iniciado='usuario invalido')

    else:
        inicio = 'usuario invalido'
        return render_template('login.html', iniciado = 'usuario invalido')
    
@app.route('/crear')
def crear():
    return render_template('crear.html')

@app.route('/c_usuario', methods=['POST'])
def c_usuario():
        global usuariosac, contraseñasac

        c_usuario = request.form['c_usuario']
        c_contraseña = request.form['c_contraseña'] 


        if c_usuario in usuariosac:
            men = 'el usuario ya existe'
        else:
            usuariosac.append(c_usuario)
            contraseñasac.append(c_contraseña)
            men = 'Se ha creado exitosamente'

        return render_template('crear.html', men = men)



@app.route('/calculadora')
def calculadora():
    return render_template('1.html')

@app.route('/calcular', methods=['POST'])
def calcular():


    n1 = float(request.form['n1'])
    n2 = float(request.form['n2'])

    suma = n1 + n2
    resta = n1 - n2
    multiplicacion = n1 * n2
    division = n1 / n2


    opcion = int(request.form['opcion'])

    if opcion == 1:
        resultado = suma
    elif opcion == 2:
        resultado = resta
    elif opcion == 3:
        resultado = multiplicacion
    elif opcion == 4:
        resultado = division

    else:
        resultado = 'error'

    return render_template('1.html', resultado = resultado )

if __name__ == '__main__':
    app.run(debug=True)
    
    
