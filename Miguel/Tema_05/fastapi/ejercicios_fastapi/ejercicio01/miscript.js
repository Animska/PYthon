const API_URL = "http://0.0.0.0:8000";
const btnConsultar = document.querySelector('#btnConsultar');
const inputCiudad = document.querySelector('#city');
const template = document.querySelector("#weatherTemplate");
const divResultado = document.querySelector('#resultado')
const templateError = document.querySelector("#errorTemplate")
consultarTiempo();
btnConsultar.addEventListener("click", consultarTiempo);

async function consultarTiempo(){
    const ciudad = inputCiudad.value.trim();
    if (ciudad == ''){
        mostrarError("ERROR! Debe mostrar una ciudad")
        return;
    }

    const params = new URLSearchParams({ciudad});
    const response = await fetch(
        `${API_URL}/api/weather?${params}`,
        {
            method: "GET",
            headers: {
                "Content-Type": "application/json"
            }
        }
    )
    if(!response.ok){
        throw new Error("Error al devolver datos de la previsión");
    }
    const data = await response.json();
    mostrarResultado(data);
}

function mostrarResultado(data){
    const clon = template.content.cloneNode(true);
    clon.querySelector('.city-name').textContent = data.ciudad;
    clon.querySelector('.temperature').textContent = `${data.temperatura}ºC`;
    clon.querySelector('.description').textContent = data.descripcion;
    clon.querySelector('.feels-like').textContent = `${data.sensacion}ºC`;
    clon.querySelector('.humidity').textContent = `${data.humedad}%`;
    clon.querySelector('.wind').textContent = `${data.viento}km/h`;
    clon.querySelector('.weather-icon').src=`https://openweathermap.org/payload/api/media/file/${data.icono}.png`;

    divResultado.innerHTML = ""
    divResultado.appendChild(clon)
}

function mostrarError(mensaje){
    const clonError = templateError.content.cloneNode(true)
    clonError.querySelector(".error-message").textContent = mensaje
    divResultado.innerHTML = ""
    divResultado.appendChild(clonError)
}