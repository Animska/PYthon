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

export async function crearPlantas(params) {
    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: { 
                "Content-Type": "application/json" 
            },
            // 1. Debes convertir el objeto params a una cadena JSON
            body: JSON.stringify(params) 
        });

        if (!response.ok) {
            // 2. Es buena práctica lanzar el status para saber qué falló (ej: 404, 500)
            throw new Error(`Error ${response.status}: No se pudo crear la planta`);
        }

        const data = await response.json();
        
        // 3. Importante: Retorna los datos para poder usarlos fuera de la función
        return data;

    } catch (error) {
        console.error("Hubo un problema en la petición:", error);
        // Opcional: re-lanzar el error si quieres manejarlo en la UI
        throw error; 
    }
}