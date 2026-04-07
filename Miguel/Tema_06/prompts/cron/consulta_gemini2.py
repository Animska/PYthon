#!/usr/bin/env python3
"""
consulta_gemini.py — Carga los datos de los últimos 10 días
y hace preguntas agronómicas a la API de Gemini.
"""
import json
import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from google.genai import types
from modelos import AnalisisInvernadero

# Importamos las funciones de carga de datos
from datos_contexto import construir_contexto

# ─── Configuración ────────────────────────────────────────────────────────────

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("No se encontró GEMINI_API_KEY en el archivo .env")

client = genai.Client(api_key=GEMINI_API_KEY)

BASE_DIR = Path(__file__).resolve().parent
DIR_DATOS = Path(BASE_DIR / "datos")
MODELO = "gemini-3-flash-preview"

# ─── System prompt del agente agronómico ─────────────────────────────────────

SYSTEM_PROMPT = """
Eres un agrónomo experto en cultivos de invernadero.
El invernadero contiene 10 tipos de plantas: Lechuga, Tomate, Albahaca,
Fresa, Pepino, Pimiento, Espinaca, Cilantro, Menta y Perejil.

Recibirás datos de sensores de los últimos días organizados por planta,
con las siguientes variables para cada una:

- temperatura_c: temperatura del aire en °C.
- humedad_aire_pct: humedad relativa del aire en %.
- humedad_sustrato_pct: humedad del sustrato en %.
- luz_lux: nivel de luz en lux.
- ce_ms_cm: conductividad eléctrica de la solución nutritiva en mS/cm.
- alertas: número de lecturas fuera del rango óptimo de esa planta.
- hora_critica: hora del día con mayor concentración de alertas globales.

Cada planta tiene rangos óptimos distintos. Analiza las tendencias por
planta, identifica cuáles presentan más estrés, explica las consecuencias
agronómicas y propón acciones correctoras concretas y priorizadas.
Responde siempre en español y de forma clara y estructurada.
""".strip()

PROMPT_JSON = """
Analiza los datos del invernadero y responde ÚNICAMENTE con un objeto JSON
válido con esta estructura exacta, sin texto antes ni después:

{
  "plantas": [
    {
      "nombre": "Nombre de la planta",
      "descripcion": "2-3 frases sobre el estado de esta planta concreta",
      "salud_pct": número entero entre 0 y 100,
      "nivel_alerta": "BUENO" o "MEDIO" o "PELIGRO"
    }
  ]
}

Incluye una entrada por cada una de las 10 plantas: Lechuga, Tomate, Albahaca,
Fresa, Pepino, Pimiento, Espinaca, Cilantro, Menta y Perejil.

Criterios para nivel_alerta de cada planta:
- BUENO: menos del 10% de lecturas con alerta, variables dentro de rango.
- MEDIO: entre 10% y 30% de alertas, o desviaciones moderadas.
- PELIGRO: más del 30% de alertas, o desviaciones severas.
""".strip()


# ─── Construcción del prompt ──────────────────────────────────────────────────

def construir_prompt(pregunta: str) -> str:
    """
    Combina el contexto de datos con la pregunta del usuario
    para formar el prompt completo que se envía a Gemini.
    """
    contexto = construir_contexto(DIR_DATOS, n_dias=10)

    prompt = f"""
{contexto}

---

PREGUNTA DEL TÉCNICO:
{pregunta}
""".strip()

    return prompt

def consultar_gemini(pregunta: str = PROMPT_JSON) -> AnalisisInvernadero:
    prompt = construir_prompt(pregunta)

    try:
        resp = client.models.generate_content(
            model=MODELO,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
            ),
        )

        # Limpiamos posibles bloques markdown que Gemini añade a veces
        texto = resp.text.strip()
        texto = texto.removeprefix("```json").removeprefix("```").removesuffix("```").strip()

        datos = json.loads(texto)
        return AnalisisInvernadero(**datos)

    except json.JSONDecodeError as e:
        raise RuntimeError(f"Gemini no devolvió JSON válido: {e}") from e
    except Exception as e:
        raise RuntimeError(f"Error al procesar la respuesta: {e}") from e

def main():
    print("=" * 50)
    print("  Consultor agronómico — Invernadero multi-planta (10 especies)")
    print("=" * 50)

    resultado = consultar_gemini()

    for planta in resultado.plantas:
        print(f"\n[{planta.nivel_alerta}] {planta.nombre} — salud: {planta.salud_pct}%")
        print(f"  {planta.descripcion}")

    # El objeto completo como JSON, listo para enviar a un frontend
    print("\nJSON completo:")
    print(resultado.model_dump_json(indent=2))

if __name__ == "__main__":
    main()