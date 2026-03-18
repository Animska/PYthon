const API_URL = "http://127.0.0.1:8000/plantas";
const gridCartas = document.querySelector('#grid-cartas');
const templateCartas = document.querySelector('#template-card');

async function consultarPlantas() {
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
    // Clear the grid before adding new items
    gridCartas.innerHTML = "";

    plantas.forEach(planta => {
        // 1. Clone the template content
        const clone = templateCartas.content.cloneNode(true);
        clone.querySelector('.card-img-top').setAttribute('src', planta.imagen_url);
        clone.querySelector('.nombre-planta').textContent = planta
        clone.querySelector('.nombre-cientifico').textContent = planta
        clone.querySelector('.cantidad p').textContent = planta
        clone.querySelector('.temp p').textContent = planta
        clone.querySelector('.humedad p').textContent = planta
        
        // 3. Append to the grid
        gridCartas.appendChild(clone);
    });
}


consultarPlantas();
