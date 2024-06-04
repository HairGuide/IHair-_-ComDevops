from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def pag_inicial():
    return render_template('pag_inicial.html')

@app.route('/pag_2')
def pag_2():
    return render_template('pag_2.html')

@app.route('/ir_para_pag_2')
def ir_para_pag_2():
    return redirect(url_for('pag_2'))

if __name__ == '__main__':
    app.run(debug=True)
