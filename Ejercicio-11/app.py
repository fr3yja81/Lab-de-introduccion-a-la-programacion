from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guardar_datos', methods=['POST'])
def guardar_datos():
    data = request.json
    print(f"Código recibido: {data.get('codigo')}")
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    # Render asigna un puerto dinámico, por eso usamos os.environ
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)