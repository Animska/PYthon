import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve.parent
fichero = Path(BASE_DIR / "data/informes/2026/ventas")

os.makedirs(fichero, exist_ok=True)
print(f"Directorio creado en: {fichero}")

fichero_informe = fichero / "informe_fina.txt"
fichero_informe.write_text("Informe Creado", encoding="utf-8")