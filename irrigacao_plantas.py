from flask import Flask, render_template, redirect, url_for
import psutil
import datetime
import water
import os

app = Flask(__name__)

def template(title = "Jardim Automático!", text = ""):
    horario = datetime.datetime.now()
    dia = horario.strftime("%d")
    mes = horario.strftime("%m")
    ano = horario.strftime("%Y")
    hora = horario.strftime("%H")
    minuto = horario.strftime("%M")
    tempoString = "Hoje é " + dia + "-" + mes + "-" + ano + "  " + hora + ":" + minuto
    
    templateDate = {
        'title' : title,
        'time' : tempoString,
        'text' : text
        }
    return templateDate

@app.route("/")
def hello():
    templateData = template()
    return render_template('main.html', **templateData)

@app.route("/ultima_irrigacao")
def check_ultima_irrigacao():
    templateData = template(text = water.get_ultima_irrigacao())
    return render_template('main.html', **templateData)

@app.route("/sensor")
def action():
    status = water.get_status()
    message = status

    templateData = template(text = message)
    return render_template('main.html', **templateData)

@app.route("/water")
def action2():
    water.irrigador_on()
    templateData = template(text = "Irrigado")
    return render_template('main.html', **templateData)

@app.route("/auto/water/<toggle>")
def auto_water(toggle):
    running = False
    if toggle == "ON":
        templateData = template(text = "Auto Irrigação Ligada")
        for process in psutil.process_iter():
            try:
                if process.cmdline()[1] == 'auto_water.py':
                    templateData = template(text = "Já está rodando")
                    running = True
            except:
                pass
        if not running:
            os.system("python3.7 auto_water.py&")
    else:
        templateData = template(text = "Auto Irrigação Desligada")
        os.system("pkill -f water.py")

    return render_template('main.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)