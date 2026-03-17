// URL base de la API. Al estar en el mismo servidor que el frontend
// no hace falta poner la IP ni el puerto.
// Apache se encarga de reenviar /api/ a Uvicorn eliminando el prefijo.
const API_BASE = '/api';
// Saludo personalizado
document.querySelector('#btnSaludar').addEventListener('click', async () => {
    const nombre = document.querySelector('#inputNombre').value.trim();
    if (!nombre) {
        document.querySelector('#respuestaSaludo').textContent = 'Escribe un nombre primero.';
    return;
    }

    try {
        const respuesta = await fetch(`${API_BASE}/saludo/${nombre}`);
        const datos = await respuesta.json();
        document.querySelector('#respuestaSaludo').textContent = datos.mensaje;
    } catch (error) {
        document.querySelector('#respuestaSaludo').textContent = 'Error al conectar con la API.';
        console.error(error);
    }
});

// Listado de productos
document.querySelector('#btnProductos').addEventListener('click', async () => {
    const lista = document.querySelector('#listaProductos');
    lista.innerHTML = '';
    try {
        const respuesta = await fetch(`${API_BASE}/productos`);
        const datos = await respuesta.json();
        datos.productos.forEach(producto => {
            const item = document.createElement('li');
            item.innerHTML = `
                <span>${producto.nombre}</span>
                <span class='precio'>${producto.precio.toFixed(2)} EUR</span>`;
            lista.appendChild(item);
        });
    } catch (error) {
        lista.innerHTML = '<li>Error al cargar los productos.</li>';
        console.error(error);
    }
});