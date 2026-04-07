# main.py — Conversor de unidades desplegado en GCP Compute Engine
from flask import Flask, jsonify
#from flask_cors import CORS

app = Flask(__name__)
app.json.ensure_ascii = False
#CORS(app)

# Diccionario de conversiones cada entrada tiene: funcion de conversion,
# nombre de la unidad resultado y la formula en texto (para mostrarla al usuario)

CONVERSIONES = {
    "temperatura": {
        "c-f": {
            "fn": lambda v: v * 9 / 5 + 32,
            "unidad": "°F",
            "formula": "°C × 9/5 + 32",
        },
        "f-c": {
            "fn": lambda v: (v - 32) * 5 / 9,
            "unidad": "°C",
            "formula": "(°F − 32) × 5/9",
        },
        "c-k": {"fn": lambda v: v + 273.15, "unidad": "K", "formula": "°C + 273.15"},
        "k-c": {"fn": lambda v: v - 273.15, "unidad": "°C", "formula": "K − 273.15"},
    },
    "longitud": {
        "km-mi": {
            "fn": lambda v: v * 0.621371,
            "unidad": "millas",
            "formula": "km × 0.621371",
        },
        "mi-km": {
            "fn": lambda v: v * 1.60934,
            "unidad": "km",
            "formula": "mi × 1.60934",
        },
        "m-ft": {
            "fn": lambda v: v * 3.28084,
            "unidad": "pies",
            "formula": "m × 3.28084",
        },
        "ft-m": {
            "fn": lambda v: v * 0.3048,
            "unidad": "metros",
            "formula": "ft × 0.3048",
        },
    },
    "peso": {
        "kg-lb": {
            "fn": lambda v: v * 2.20462,
            "unidad": "libras",
            "formula": "kg × 2.20462",
        },
        "lb-kg": {
            "fn": lambda v: v * 0.453592,
            "unidad": "kg",
            "formula": "lb × 0.453592",
        },
        "g-oz": {
            "fn": lambda v: v * 0.035274,
            "unidad": "onzas",
            "formula": "g × 0.035274",
        },
        "oz-g": {
            "fn": lambda v: v * 28.3495,
            "unidad": "gramos",
            "formula": "oz × 28.3495",
        },
    },
}


@app.route("/")
def inicio():
    """Endpoint raiz: devuelve las categorias disponibles."""
    return jsonify(
        {
            "app": "Conversor de unidades",
            "categorias": list(CONVERSIONES.keys()),
            "uso": "/convertir/{categoria}/{tipo}/{valor}",
        }
    )


@app.route("/convertir/<categoria>/<tipo>/<valor>")
def convertir(categoria, tipo, valor):
    """Realiza la conversion solicitada y devuelve el resultado."""

    # Convertir el valor de texto a numero
    try:
        valor = float(valor)
    except ValueError:
        return jsonify({"error": f"Valor no numerico: {valor}"}), 400

    if categoria not in CONVERSIONES:
        return jsonify({"error": f"Categoria desconocida: {categoria}"}), 404

    if tipo not in CONVERSIONES[categoria]:
        return jsonify({"error": f"Tipo desconocido: {tipo}"}), 404

    datos = CONVERSIONES[categoria][tipo]
    resultado = round(datos["fn"](valor), 4)

    return jsonify(
        {
            "entrada": valor,
            "resultado": resultado,
            "unidad": datos["unidad"],
            "formula": datos["formula"],
            "categoria": categoria,
            "tipo": tipo,
        }
    )


@app.route("/tipos/<categoria>")
def tipos(categoria):
    """Devuelve los tipos de conversion disponibles para una categoria."""
    if categoria not in CONVERSIONES:
        return jsonify({"error": f"Categoria desconocida: {categoria}"}), 404
    return jsonify(
        {"categoria": categoria, "tipos": list(CONVERSIONES[categoria].keys())}
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
