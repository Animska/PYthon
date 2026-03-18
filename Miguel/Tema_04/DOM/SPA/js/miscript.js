// CONFIGURACIÓN: Mapa de rutas
const rutas = {
    "/": "vistas/inicio.html",
    "/servicios": "vistas/servicios.html",
    "/sobre-nosotros": "vistas/sobre-nosotros.html",
    "/contacto": "vistas/contacto.html"
};

// FUNCIÓN PRINCIPAL: Navegar a una ruta
async function navegarA(ruta) {
    // Obtener el elemento donde se cargará el contenido
    const app = document.querySelector('#app');

    // Mostrar indicador de carga
    app.innerHTML = '<div class="loading">Cargando...</div>';


    // Verificar si la ruta existe en nuestro mapa
    const archivo = rutas[ruta];

    if (!archivo) {
        // Si la ruta no existe, cargar página 404
        await cargar404();
        return;
    }

    // Cargar el contenido HTML de la vista
    const response = await fetch(archivo);

    // Verificar que la petición fue exitosa
    if (!response.ok) {
        throw new Error(`Error HTTP: ${response.status}`);
    }

    // Obtener el HTML como texto
    const html = await response.text();

    // Inyectar el HTML en el contenedor principal
    app.innerHTML = html;

    // Actualizar la clase "active" en los enlaces de navegación
    actualizarNavegacionActiva(ruta);

    // Hacer scroll al inicio de la página
    window.scrollTo(0, 0);
}

// FUNCIÓN: Cargar página 404
async function cargar404() {
    const app = document.querySelector('#app');

    const response = await fetch('vistas/404.html');
    const html = await response.text();
    app.innerHTML = html;
}


// FUNCIÓN: Actualizar navegación activa
function actualizarNavegacionActiva(ruta) {
    // Obtener todos los enlaces de navegación
    const enlaces = document.querySelectorAll('.nav-link');

    // Recorrer cada enlace
    enlaces.forEach(enlace => {
        // Remover la clase 'active' de todos
        enlace.classList.remove('active');

        // Obtener el href del enlace
        const href = enlace.getAttribute('href');

        // Si el href coincide con la ruta actual, añadir 'active'
        if (href == ruta) {
            enlace.classList.add('active');
        }
    });
}

// FUNCIÓN: Manejar clicks en enlaces
function manejarClick(evento) {
    // Verificar si el elemento clickeado tiene el atributo data-link
    if (evento.target.hasAttribute('data-link')) {
        // Prevenir el comportamiento por defecto (recargar página)
        evento.preventDefault();

        // Obtener la ruta del atributo href
        const ruta = evento.target.getAttribute('href');

        // Navegar a la nueva ruta
        navegarA(ruta);
    }
}

// Agregar listener para clicks en TODA la página
const barraNav = document.querySelector("nav")
barraNav.addEventListener('click', manejarClick);

const app = document.querySelector('#app');
app.addEventListener('click', manejarFormularioContacto);

// Cargar la ruta inicial (la página actual)
navegarA("/");



// Contacto.html

function manejarFormularioContacto(evento) {
    // Verificar si es el formulario de contacto
    if (evento.target.id == 'btnEnviar') {
        // Prevenir el envío tradicional del formulario
        evento.preventDefault();

        // Obtener los valores del formulario
        const nombre = document.getElementById('nombre').value;
        const email = document.getElementById('email').value;
        const mensaje = document.getElementById('mensaje').value;

        // Mostrar alerta con los datos
        alert(`Mensaje enviado!\n\nNombre: ${nombre}\nEmail: ${email}\nMensaje: ${mensaje}`);

        // Opcional: Limpiar el formulario después de enviar
        evento.target.reset();
    }
}

