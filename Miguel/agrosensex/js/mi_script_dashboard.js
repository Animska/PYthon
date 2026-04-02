import { consultarPlantas } from './mi_script_inventario.js'

export function rellenarTablaDashboard(plantas) {
    const cuerpoTabla = document.querySelector('#tabla-dashboard-cuerpo');
    const templateFila = document.querySelector('#template-fila-dashboard');

    if (!cuerpoTabla || !templateFila) return;

    cuerpoTabla.innerHTML = "";

    // Variables para las estadísticas
    let totalPlantas = plantas.length;
    let recintosUnicos = new Set();
    let plantasEnAtencion = 0;

    plantas.forEach(planta => {
        const clone = templateFila.content.cloneNode(true);

        // 1. Datos reales del JSON
        clone.querySelector('.nombre-planta').textContent = planta.nombre;
        clone.querySelector('.nombre-cientifico').textContent = planta.nombre_cientifico;
        clone.querySelector('.ubicacion-planta').textContent = planta.recinto_id || "Sin ubicación";
        
        // Guardar recinto para el conteo (si existe)
        if (planta.recinto_id) recintosUnicos.add(planta.recinto_id);

        // 2. Datos "a mano"
        clone.querySelector('.temp-planta').textContent = "20.5ºC";
        clone.querySelector('.hum-planta').textContent = "60%";
        
        // 3. Lógica del Badge de Estado
        const badge = clone.querySelector('.badge-estado');
        if (planta.cantidad <= 0 || planta.necesita_trasplante) {
            badge.textContent = "Atención";
            badge.className = "badge rounded-pill bg-warning text-dark px-3 py-2";
            plantasEnAtencion++; // Sumamos al contador de atención
        } else {
            badge.textContent = "OK";
            badge.className = "badge rounded-pill bg-success px-3 py-2";
        }

        cuerpoTabla.appendChild(clone);
    });

    // 4. Rellenar los contadores del Dashboard
    // Usamos ?. por si algún ID no existe en el HTML actual
    if (document.querySelector('#numPlantas')) document.querySelector('#numPlantas').textContent = totalPlantas;
    if (document.querySelector('#numRecintos')) document.querySelector('#numRecintos').textContent = recintosUnicos.size;
    if (document.querySelector('#numSensores')) document.querySelector('#numSensores').textContent = totalPlantas * 2; // Ejemplo: 2 sensores por planta
    if (document.querySelector('#numAtencion')) document.querySelector('#numAtencion').textContent = plantasEnAtencion;
}