from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan_result', methods=['POST'])
def scan_result():
    data = request.json
    codigo = data.get('code')
    print(f"✅ Código recibido en el servidor: {codigo}")
    return jsonify({"status": "success"})

if __name__ == '__main__':
    # Importante: host 0.0.0.0 para que el iPhone pueda entrar
    app.run(host='0.0.0.0', port=5000)