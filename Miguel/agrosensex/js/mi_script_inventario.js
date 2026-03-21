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
        
        // Corregido: Acceder a las propiedades del objeto planta
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