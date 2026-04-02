import { consultarPlantas } from './mi_script_inventario.js'
import { rellenarTablaDashboard } from './mi_script_dashboard.js';

// Usaremos esta variable para no pedir los datos al servidor cada vez que cambiemos de pestaña
let datosPlantas = [];

async function loadHTML(url, element) {
    try {
        const respuesta = await fetch(url);
        if (!respuesta.ok) throw new Error("Error al cargar " + url);
        
        // Esperamos a que el HTML se descargue y se inserte en el DOM
        element.innerHTML = await respuesta.text();
        
        if (url === "inventario.html") {
            // Esperamos a que las plantas lleguen antes de seguir
            datosPlantas = await consultarPlantas();
            
        } else if (url === "dashboard.html" || url === "dashboard.html") {
            // 1. Obtenemos los datos (usando await)
            datosPlantas = await consultarPlantas();
            
            // 2. Ahora que tenemos los datos reales, rellenamos la tabla
            rellenarTablaDashboard(datosPlantas);
        }

    } catch (error) {
        console.error("Error en loadHTML:", error);
    }
}



const contenido = document.querySelector("#contenido");
loadHTML("dashboard.html", contenido);
document.addEventListener('click', function (evento){
    const elementosValidos = ['dashboard', 'recintos', 'inventario', 'reportes', 'configuracion'];
    if (elementosValidos.includes(evento.target.id)) {
        document.querySelectorAll(".nav .nav-link").forEach(link => {
            link.classList.remove("active");
        })
        evento.target.classList.add("active");
        loadHTML(`${evento.target.id}.html`, contenido);
    }
})



