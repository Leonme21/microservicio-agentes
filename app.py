from flask import Flask, jsonify, request
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
error_msg = None

try:
    if url and key:
        supabase: Client = create_client(url, key)
    else:
        supabase = None
        error_msg = f"Faltan variables de entorno. URL={bool(url)}, KEY={bool(key)}"
except Exception as e:
    supabase = None
    error_msg = str(e)
    print(f"Error conectando a Supabase: {e}")

@app.route('/')
def home():
    return jsonify({"mensaje": "Microservicio de Agentes Activo. Visita /api/agentes"})

@app.route('/api/agentes', methods=['GET'])
def obtener_agentes():
    if not supabase:
        return jsonify({"error": "No se pudo conectar a la base de datos en la nube (Supabase).", "detalle": error_msg}), 500
        
    try:
        response = supabase.table('agentes').select("*").execute()
        return jsonify(response.data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Para probar local
    app.run(debug=True, port=5000)
