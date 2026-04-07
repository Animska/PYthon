import csv
import json
from collections import defaultdict
from pathlib import Path


def resumir_csv_diario(ruta_csv: Path) -> dict:
    """
    Lee un CSV de un día completo y devuelve estadísticas por planta
    más un resumen global, todo listo para incluir en el prompt de Gemini.
    """
    with open(ruta_csv, "r", encoding="utf-8") as f:
        registros = list(csv.DictReader(f))

    if not registros:
        return {}

    # Ignorar CSVs con formato antiguo (sin nombre_planta)
    if "nombre_planta" not in registros[0]:
        return {}

    fecha       = registros[0]["timestamp"][:10]
    total       = len(registros)
    alertas_tot = sum(1 for r in registros if r["alerta"] == "ALERTA")

    def stats(campo: str, subset: list) -> dict:
        valores = [float(r[campo]) for r in subset]
        return {
            "min":   round(min(valores), 1),
            "max":   round(max(valores), 1),
            "media": round(sum(valores) / len(valores), 1),
        }

    # Resumen por planta
    por_planta = defaultdict(list)
    for r in registros:
        por_planta[r["nombre_planta"]].append(r)

    plantas_resumen = {}
    for nombre, filas in sorted(por_planta.items()):
        alertas_p = sum(1 for r in filas if r["alerta"] == "ALERTA")
        plantas_resumen[nombre] = {
            "lecturas":             len(filas),
            "alertas":              alertas_p,
            "temperatura_c":        stats("temperatura_c", filas),
            "humedad_aire_pct":     stats("humedad_aire_pct", filas),
            "humedad_sustrato_pct": stats("humedad_sustrato_pct", filas),
            "luz_lux":              stats("luz_lux", filas),
            "ce_ms_cm":             stats("ce_ms_cm", filas),
        }

    # Hora crítica global (más alertas)
    alertas_hora = defaultdict(int)
    for r in registros:
        if r["alerta"] == "ALERTA":
            alertas_hora[r["timestamp"][11:13]] += 1
    hora_critica = (
        max(alertas_hora, key=lambda h: alertas_hora[h])
        if alertas_hora else None
    )

    return {
        "fecha":          fecha,
        "total_lecturas": total,
        "alertas_total":  alertas_tot,
        "alertas_pct":    round(alertas_tot / total * 100, 1),
        "hora_critica":   f"{hora_critica}:00" if hora_critica else "ninguna",
        "por_planta":     plantas_resumen,
    }


def obtener_csvs_recientes(directorio: Path, n_dias: int = 10) -> list[Path]:
    """
    Devuelve los n CSV más recientes del directorio, del más antiguo al más reciente.
    """
    archivos = sorted(directorio.glob("sensores_*.csv"))
    return archivos[-n_dias:]


def construir_contexto(directorio: Path, n_dias: int = 10) -> str:
    """
    Carga los últimos n CSV, resume cada uno por planta y construye
    el bloque de contexto que se incluirá en el prompt de Gemini.
    """
    archivos = obtener_csvs_recientes(directorio, n_dias)

    if not archivos:
        return "No hay datos disponibles en el directorio especificado."

    resumenes = [resumir_csv_diario(f) for f in archivos]
    resumenes = [r for r in resumenes if r]

    texto  = f"DATOS DEL INVERNADERO — ÚLTIMOS {len(resumenes)} DÍAS\n"
    texto += "=" * 50 + "\n\n"
    texto += json.dumps(resumenes, ensure_ascii=False, indent=2)

    return texto
