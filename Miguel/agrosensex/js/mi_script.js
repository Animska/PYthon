import { consultarPlantas } from './mi_script_inventario.js'
import { crearPlantas } from './mi_script_inventario.js'

// Modifica tu loadHTML para que devuelva la promesa
async function loadHTML(url, element) {
    try {
        const respuesta = await fetch(url);
        if (!respuesta.ok) throw new Error("Error al cargar");
        element.innerHTML = await respuesta.text();
        
        if (url === "inventario.html") {
            consultarPlantas(); 
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
const formPlanta = document.querySelector('#modalNuevaPlanta')
const botonGuardarPlanta = document.querySelector('#btn-guardar-planta');
const paramsPlanta = {
        nombre: formPlanta.querySelector('#nombre-planta'),
        nombre_cientifico: formPlanta.querySelector('#nombreCientifico-planta'),
        descripcion: formPlanta.querySelector('#descripcion-planta'),
        recinto_id: formPlanta.querySelector('#recinto-planta'),
        cantidad: formPlanta.querySelector('#cantidad-planta'),
        imagen_url: formPlanta.querySelector('#fechaAdquisicion-planta'),
        fecha_adquisicion: formPlanta.querySelector('#ultimoRiego-planta'),
        ultimo_riego: formPlanta.querySelector('#urlImagen-planta'),
        necesita_trasplante: false,
        notas: formPlanta.querySelector('#notas')
}

botonGuardarPlanta.addEventListener('click', function (){
    crearPlantas(paramsPlanta)
})


