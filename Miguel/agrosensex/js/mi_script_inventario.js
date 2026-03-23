const API_URL = "http://127.0.0.1:8000/plantas";

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
        console.error("No se encontró el grid o el template en el DOM");
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

        clone.querySelector('.card-img-top').setAttribute('src', planta.imagen_url || 'https://via.placeholder.com/150');
        clone.querySelector('.nombre-planta').textContent = planta.nombre; // Asegúrate de usar .nombre
        clone.querySelector('.nombre-cientifico').textContent = planta.nombre_cientifico;
        clone.querySelector('.cantidad p').textContent = planta.cantidad;
        clone.querySelector('.temp p').textContent = `${planta.temperatura || 0}º`;
        clone.querySelector('.humedad p').textContent = `${planta.humedad || 0}%`;
        
        gridCartas.appendChild(clone);
    });
}

export async function crearPlantas() {
    // Capturamos los VALORES de los inputs usando los IDs de index.html
    const formPlanta = document.querySelector('#modalNuevaPlanta')

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
    const urlFinal = `${API_URL}/${id}`; 
    console.log("URL de borrado:", urlFinal); // Verifica esto en consola

    try {
        const response = await fetch(`${API_URL}/${id}`, {
            method: "DELETE"
        });

        if (response.ok) {
            alert("Planta eliminada correctamente");
            consultarPlantas(); // Recarga la lista para actualizar la vista
        } else {
            const error = await response.json();
            alert("Error: " + error.detail);
        }
    } catch (error) {
        console.error("Error al eliminar:", error);
    }
}

document.addEventListener('click', function (evento) {
    // Detectar clic en eliminar
    const botonEliminar = evento.target.closest('.btn-borrar-planta');
    if (botonEliminar) {
        const idPlanta = botonEliminar.dataset.id;
        console.log("Se quiere eliminar la planta:", idPlanta);
        borrarPlanta(idPlanta);
    }

    // Detectar clic en editar
    const botonEditar = evento.target.closest('.btn-editar-planta');
    if (botonEditar) {
        const idPlanta = botonEditar.dataset.id;
        console.log("Se quiere editar la planta:", idPlanta);
        // Aquí abrirías el modal con los datos para el PUT
    }
});