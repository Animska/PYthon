API_BASE = "/api";
// Etiquetas legibles para cada tipo de conversion
const ETIQUETAS = {
  temperatura: {
    "c-f": "°C → °F",
    "f-c": "°F → °C",
    "c-k": "°C → K",
    "k-c": "K → °C",
  },
  longitud: {
    "km-mi": "km → millas",
    "mi-km": "millas → km",
    "m-ft": "metros → pies",
    "ft-m": "pies → metros",
  },
  peso: {
    "kg-lb": "kg → libras",
    "lb-kg": "libras → kg",
    "g-oz": "gramos → onzas",
    "oz-g": "onzas → gramos",
  },
};
let categoriaActual = "temperatura";
// Rellena el <select> con los tipos de la categoría activa
function cargarTipos(categoria) {
  const sel = document.querySelector("#selectTipo");
  sel.innerHTML = "";
  Object.entries(ETIQUETAS[categoria]).forEach(([tipo, label]) => {
    const opt = document.createElement("option");
    opt.value = tipo;
    opt.textContent = label;
    sel.appendChild(opt);
  });
}

// Cambia de pestaña
document.querySelectorAll(".tab").forEach((btn) => {
  btn.addEventListener("click", () => {
    document
      .querySelectorAll(".tab")
      .forEach((b) => b.classList.remove("activa"));
    btn.classList.add("activa");
    categoriaActual = btn.dataset.cat;
    cargarTipos(categoriaActual);
    document.querySelector("#resultado").classList.add("oculto");
  });
});
// Llamada a la API al pulsar Convertir
document.querySelector("#btnConvertir").addEventListener("click", async () => {
  const tipo = document.querySelector("#selectTipo").value;
  const valor = parseFloat(document.querySelector("#inputValor").value);
  if (isNaN(valor)) {
    alert("Introduce un valor numérico.");
    return;
  }

  // Llamada: /api/convertir/<categoria>/<tipo>/<valor>
  // Nginx elimina /api/ y Gunicorn recibe /convertir/<categoria>/<tipo>/<valor>
  const url = `${API_BASE}/convertir/${categoriaActual}/${tipo}/${valor}`;
  const res = await fetch(url);
  const datos = await res.json();
  if (datos.error) {
    alert("Error: " + datos.error);
    return;
  }
  // Mostrar resultado
  const etiqueta = ETIQUETAS[categoriaActual][tipo];
  document.querySelector("#resValorEntrada").textContent =
    `${datos.entrada} ${etiqueta.split("→")[0].trim()}`;
  document.querySelector("#resValorSalida").textContent =
    `${datos.resultado} ${datos.unidad}`;
  document.querySelector("#resFormula").textContent =
    `Fórmula: ${datos.formula}`;
  document.querySelector("#resultado").classList.remove("oculto");
});

// Inicializar la pestaña por defecto al cargar la página
cargarTipos(categoriaActual);
