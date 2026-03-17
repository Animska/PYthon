const API_URL = "http://0.0.0.0:8000";
const gridCartas = document.querySelector('#grid-cartas')

async function consultarplantas(){
    const response = await fetch(
        `${API_URL}`,
        {
            method: "GET",
            headers: {
                "Content-Type": "application/json"
            }
        }
    )
    if(!response.ok){
        throw new Error("Error al devolver datos de las plantas");
    }
    const data = await response.json();
    console.log(data)
}

consultarplantas()