from flask import Flask
import os

app = Flask(__name__)

@app.route('/sonar')
def sonar():
    print("📲 Dispositivo 1: Recibió alerta. Activando sonido...")

    # Si estás en Windows
    os.system("start sonidos/alarma.mp3")

    # En Linux / Termux (usa solo uno según tu sistema)
    # os.system("mpg123 sonidos/alarma.mp3")
    # os.system("termux-media-player play sonidos/alarma.mp3")

    return "Alarma sonando", 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)
