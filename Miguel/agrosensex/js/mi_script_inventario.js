const API_URL = "api/plantas";

const formPlanta = document.querySelector('#modalNuevaPlanta')
let arrPlantas=[]

export async function consultarPlantas() {
    try {
        const response = await fetch(API_URL, {
            method: "GET",
            headers: { "Content-Type": "application/json" }
        });

        if (!response.ok) {
            throw new Error("Error al devolver datos de las plantas");
        }

        const data = await response.json();
        rellenarPlantas(data);
        return data
        
    } catch (error) {
        console.error("Hubo un problema:", error);
    }
}

function rellenarPlantas(plantas) {
    // CAPTURA LOS ELEMENTOS AQUÍ, CUANDO YA SE HAN CARGADO EN EL HTML
    const gridCartas = document.querySelector('#grid-cartas');
    const templateCartas = document.querySelector('#template-card');

    // Validación de seguridad
    if (!gridCartas || !templateCartas) {
        return;
    }
    gridCartas.innerHTML = "";

    plantas.forEach(planta => {
        const clone = templateCartas.content.cloneNode(true);

        const btnEditar = clone.querySelector('.btn-editar-planta');
        const btnEliminar = clone.querySelector('.btn-borrar-planta');
        
        // planta.id es el ID que viene de tu plantas.py
        btnEditar.dataset.id = planta.id;
        btnEliminar.dataset.id = planta.id;

        clone.querySelector('.card-img-top').setAttribute('src', planta.imagen_url || '');
        clone.querySelector('.nombre-planta').textContent = planta.nombre; // Asegúrate de usar .nombre
        clone.querySelector('.nombre-cientifico').textContent = planta.nombre_cientifico;
        clone.querySelector('.cantidad p').textContent = planta.cantidad;
        clone.querySelector('.temp p').textContent = `${planta.temperatura || 0}º`;
        clone.querySelector('.humedad p').textContent = `${planta.humedad || 0}%`;
        
        const img = clone.querySelector('.card-img-top');
        const icono = clone.querySelector('.bi-flower1');
        if (planta.imagen_url && planta.imagen_url.trim() !== "") {
        // Si hay imagen: mostrar img y ocultar icono
            img.src = planta.imagen_url;
            img.classList.remove('d-none');
            icono.classList.add('d-none');
        } else {
        // Si NO hay imagen: mostrar icono y ocultar img
            icono.classList.remove('d-none');
            img.classList.add('d-none');
        }
        
        gridCartas.appendChild(clone);
    });
}

export async function crearPlantas() {
    // Capturamos los VALORES de los inputs usando los IDs de index.html
    const paramsPlanta = {
        nombre: formPlanta.querySelector('#nombre-planta').value,
        nombre_cientifico: formPlanta.querySelector('#nombreCientifico-planta').value,
        descripcion: formPlanta.querySelector('#descripcion-planta').value,
        recinto_id: formPlanta.querySelector('#recinto-planta').value,
        cantidad: parseInt(document.querySelector('#cantidad-planta').value) || 0,
        imagen_url: document.querySelector('#urlImagen-planta').value,
        fecha_adquisicion: document.querySelector('#fechaAdquisicion-planta').value,
        ultimo_riego: document.querySelector('#ultimoRiego-planta').value,
        notas: document.querySelector('#notas-planta')?.value || "",
        necesita_trasplante: false
    };

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(paramsPlanta) // Enviamos el JSON limpio
        });

        if (!response.ok) throw new Error("Error en el servidor");

        const data = await response.json();
        
        // Limpiar y cerrar modal
        const modal = bootstrap.Modal.getInstance(document.getElementById('modalNuevaPlanta'));
        modal.hide();
        consultarPlantas(); // Refrescar la lista automáticamente
        
        return data;
    } catch (error) {
        console.error("Error en la petición:", error);
    }
}

async function borrarPlanta(id) {
    try {
        const response = await fetch(`${API_URL}/${id}`, {
            method: "DELETE"
        });

        if (response.ok) {
            consultarPlantas(); // Recarga la lista para actualizar la vista
        } else {
            const error = await response.json();
            alert("Error: " + error.detail);
        }
    } catch (error) {
        console.error("Error al eliminar:", error);
    }
}

async function editarPlanta(id) {
    const paramsPlanta = {
        //id: id,
        nombre: formPlanta.querySelector('#nombre-planta').value,
        nombre_cientifico: formPlanta.querySelector('#nombreCientifico-planta').value,
        descripcion: formPlanta.querySelector('#descripcion-planta').value,
        recinto_id: formPlanta.querySelector('#recinto-planta').value,
        cantidad: parseInt(document.querySelector('#cantidad-planta').value) || 0,
        imagen_url: document.querySelector('#urlImagen-planta').value,
        fecha_adquisicion: document.querySelector('#fechaAdquisicion-planta').value,
        ultimo_riego: document.querySelector('#ultimoRiego-planta').value,
        notas: document.querySelector('#notas-planta')?.value || "",
        necesita_trasplante: false
    };

    try {
        const response = await fetch(`${API_URL}/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(paramsPlanta)
        });

        //if (!response.ok) throw new Error("Error en el servidor");
        if (!response.ok) {
            const errorDetalle = await response.json();
            console.error("Detalle del error de validación:", errorDetalle); // <-- ESTO TE DIRÁ EL CAMPO EXACTO
            throw new Error("Error en el servidor");
        }
        // Limpiar y cerrar modal
        const modal = bootstrap.Modal.getInstance(document.getElementById('modalNuevaPlanta'));
        modal.hide();
        consultarPlantas(); // Refrescar la lista automáticamente
        
    } catch (error) {
        console.error("Error en la petición:", error);
    }

    
}

async function ejecutarFiltro(tipo) {
    // 1. Añadimos 'await' para que espere a que los datos lleguen de verdad
    const plantasObtenidas = await consultarPlantas();
    
    // 2. Nos aseguramos de que sea un array (por si el JSON viene como objeto)
    const arrPlantas = Array.isArray(plantasObtenidas) ? plantasObtenidas : Object.values(plantasObtenidas);

    if (tipo === 'todas') {
        rellenarPlantas(arrPlantas);
    } else if (tipo === 'sin-ubicacion') {
        // 3. Ahora .filter() sí funcionará porque arrPlantas ya es un array real
        const filtradas = arrPlantas.filter(p => 
            !p.recinto_id || 
            p.recinto_id === "" || 
            p.recinto_id === "--Sin asignar--" || 
            p.recinto_id === "null"
        );
        rellenarPlantas(filtradas);
    }
}

const modalElement = document.querySelector('#modalNuevaPlanta');
const botonGuardarModal = document.querySelector('#btn-guardar-planta');

// 1. Gestionar qué se muestra cuando se abre el modal
modalElement.addEventListener('show.bs.modal', async function (event) {
    const botonDisparador = event.relatedTarget; // El botón que abrimos (Añadir o Editar)
    const modo = botonDisparador.dataset.set; // "guardar" o "editar"
    const idPlanta = botonDisparador.dataset.id;

    // Guardamos el modo y el ID en el propio modal para leerlo luego
    modalElement.dataset.modoActual = modo;
    modalElement.dataset.idActual = idPlanta || "";

    if (modo === 'editar') {
        arrPlantas = await consultarPlantas();
        const plantaPorId = arrPlantas.find(p => p.id == idPlanta);
        
        if (plantaPorId) {
            modalElement.querySelector('#nombre-planta').value = plantaPorId.nombre;
            modalElement.querySelector('#nombreCientifico-planta').value = plantaPorId.nombre_cientifico;
            modalElement.querySelector('#descripcion-planta').value = plantaPorId.descripcion;
            modalElement.querySelector('#recinto-planta').value = plantaPorId.recinto_id;
            modalElement.querySelector('#cantidad-planta').value = plantaPorId.cantidad;
            modalElement.querySelector('#urlImagen-planta').value = plantaPorId.imagen_url;
            modalElement.querySelector('#fechaAdquisicion-planta').value = plantaPorId.fecha_adquisicion;
            modalElement.querySelector('#ultimoRiego-planta').value = plantaPorId.ultimo_riego;
            modalElement.querySelector('#notas-planta').value = plantaPorId.notas;
        }
    } else {
        // Si es "guardar" (Nueva Planta), reseteamos el formulario
        modalElement.querySelector('form')?.reset(); 
    }
});

// 2. UN SOLO Event Listener para el botón de guardar (Fuera del evento show)
botonGuardarModal.addEventListener('click', function () {
    const modo = modalElement.dataset.modoActual;
    const id = modalElement.dataset.idActual;

    if (modo === 'editar') {
        editarPlanta(id);
    } else {
        crearPlantas();
    }
});

// 3. Delegación de eventos para borrar (Ya lo tenías bien)
document.addEventListener('click', function (evento) {
    const botonEliminar = evento.target.closest('.btn-borrar-planta');
    if (botonEliminar) {
        if(confirm("¿Estás seguro de eliminar esta planta?")) {
            borrarPlanta(botonEliminar.dataset.id);
        }
    }
});



document.addEventListener('click', (evento) => {
    // 1. Busca el botón más cercano con la clase .btn-filtro (con punto)
    const boton = evento.target.closest('.btn-filtro');

    // 2. IMPORTANTE: Solo si 'boton' NO es null, ejecutamos la lógica
    if (boton) {
        const contenedor = document.querySelector('#filtros');
        const botones = contenedor.querySelectorAll('.btn-filtro');

        // 2. Quitamos la clase 'active' de TODOS los botones del grupo
        botones.forEach(btn => btn.classList.remove('active'));

        // 3. Se la ponemos solo al botón que acabamos de pulsar
        boton.classList.add('active');
        //alert(boton.dataset.filter)
        ejecutarFiltro(boton.dataset.filter);
    } 
});