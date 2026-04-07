#!/usr/bin/env python3
"""
consulta_gemini.py — Carga los datos de los últimos 10 días
y hace preguntas agronómicas a la API de Gemini.
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.errors import ClientError

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


# ─── Llamada a la API ─────────────────────────────────────────────────────────

def consultar_gemini(pregunta: str) -> str:
    """
    Envía la pregunta junto con el contexto de datos a Gemini
    y devuelve la respuesta como texto.
    """
    prompt = construir_prompt(pregunta)

    print(f"\n{'─'*50}")
    print(f"Enviando consulta a Gemini ({MODELO})...")
    print("Contexto: últimos 10 días de sensores")
    print(f"{'─'*50}\n")

    try:
        resp = client.models.generate_content(
            model=MODELO,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
            ),
        )
        return resp.text or ""
    except ClientError as e:
        if e.code == 429:
            raise RuntimeError(
                "Cuota de la API de Gemini agotada. Espera unos minutos o revisa "
                "tu plan en https://ai.dev/rate-limit"
            ) from e
        raise


# ─── Punto de entrada interactivo ────────────────────────────────────────────

def main():
    print("=" * 50)
    print("  Consultor agronómico — Invernadero multi-planta (10 especies)")
    print("  Datos: últimos 10 días | Modelo: Gemini 3.1 Flash Lite Preview")
    print("=" * 50)
    print("Escribe 'salir' para terminar.\n")

    while True:
        pregunta = input("Tu pregunta: ").strip()

        if not pregunta:
            continue

        if pregunta.lower() == "salir":
            print("Cerrando el consultor. ¡Hasta pronto!")
            break

        respuesta = consultar_gemini(pregunta)

        print("\nRespuesta de Gemini:")
        print("─" * 50)
        print(respuesta)
        print("─" * 50 + "\n")


if __name__ == "__main__":
    main()