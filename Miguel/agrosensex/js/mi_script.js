async function loadHTML(url, element) {
    const respuesta = await fetch(url);
    objetivo.innerHTML = await respuesta.text()
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



