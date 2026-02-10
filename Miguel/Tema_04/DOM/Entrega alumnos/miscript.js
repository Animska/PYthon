/**
* Datos de entrada: Array de productos serializados (Simulando una fuente externa)
* Formato: "IDProducto;Nombre;Precio;Descripción;URL_Imagen"
*/
const arrayProductos = [
    "123;Monitor UltraWide;349.99;Monitor curvo de 34 pulgadas ideal para programar.;https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500",
    "245;Teclado Mecánico;120.50;Teclado RGB con switches blue para una escritura táctil.;https://images.unsplash.com/photo-1511467687858-23d96c32e4ae?w=500",
    "367;Ratón Ergonómico;55.00;Ratón inalámbrico diseñado para largas jornadas de trabajo.;https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500",
    "423;Auriculares Studio;89.00;Cancelación de ruido activa y sonido de alta fidelidad.;https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500",
    "518;Silla Gaming;199.00;Comodidad extrema para tus sesiones de código.;https://www.powerplanetonline.com/cdnassets/silla_gaming_813_blanco_negro_001v2_l.jpg",
    "696;Webcam 4K;75.25;Resolución Ultra HD para tus reuniones de equipo.;https://resource.logitech.com/w_80,h_50,c_limit,q_auto,f_auto,dpr_2.0/d_transparent.gif/content/dam/logitech/en/products/webcams/brio/gallery/brio-gallery-2.png?v=1"
];

const productosObjetos = arrayProductos.map(producto => {
    const [id, nombre, precio, descripcion, imagen] = producto.split(';');

    return {
        id: parseInt(id),           
        nombre: nombre,
        precio: parseFloat(precio), 
        descripcion: descripcion,
        imagen: imagen
    };
});

const contenido = document.querySelector('#productGrid')
const temp_contenido = document.querySelector('#plantillaTarjeta')

productosObjetos.forEach(producto => {
    const clon = temp_contenido.content.cloneNode(true);

    clon.querySelector('.product-title').textContent = producto.nombre;
    clon.querySelector('.product-desc').textContent = producto.descripcion;
    clon.querySelector('.product-price').textContent = `${producto.precio}€`;
    clon.querySelector('.product-image').setAttribute('src', producto.imagen);
    clon.querySelector('.add-btn').setAttribute('data-id', producto.id);
    contenido.append(clon);
});

const botones_contenido = contenido.querySelectorAll('.add-btn');

botones_contenido.forEach(boton => {
    boton.addEventListener('click', (e) => {
        idProducto = e.target.getAttribute('data-id')
        anadirCarrito(idProducto)
    });
});

//objeto que tiene {producto:cantidad}
let array_carrito = []

function rellenarCarrito(){
    const carrito = document.querySelector('#cartItems');
    carrito.innerHTML = '';
    const temp_carrito = document.querySelector('#elementoCarrito');
    let numProductos = 0
    let valorTotal = 0
    document.querySelector('#cartBadge').innerHTML = ''
    document.querySelector('#totalValue').innerHTML = ''

    array_carrito.forEach(productoCarrito =>{
        let idNum = parseInt(productoCarrito.id);
        let productoBase = productosObjetos.find(p => p.id === idNum);

        const clon_carrito = temp_carrito.content.cloneNode(true);
        clon_carrito.querySelector('.cart-item-title').textContent = productoBase.nombre;
        clon_carrito.querySelector('.cart-item-price').textContent = `${productoBase.precio}€`;
        clon_carrito.querySelector('.cart-item-img').setAttribute('src', productoBase.imagen);
        clon_carrito.querySelector('.remove-btn').setAttribute('data-id', productoBase.id);
        carrito.append(clon_carrito);
    
        numProductos+= parseInt(productoCarrito.cantidad);
        parseFloat(valorTotal+= (parseInt(productoCarrito.cantidad)*parseFloat(productoBase.precio)));

    })
    document.querySelector('#cartBadge').textContent = numProductos;
    document.querySelector('#totalValue').textContent = `${valorTotal.toFixed(2)}€`;
}

function anadirCarrito(id) {
    //buscamos si esta en array_carrito
    const idNum = parseInt(id);
    let productoExistente = array_carrito.find(item => item.id === idNum);
    if (productoExistente) {
        productoExistente.cantidad+=1;
    } else {    
            array_carrito.push({
                id: idNum,
                cantidad: 1
            });

    }
    rellenarCarrito(array_carrito)
}

function borrarDelCarrito(id){
    const idNum = parseInt(id);
    let productoExistente = array_carrito.find(item => item.id === idNum);
    let index_producto = array_carrito.indexOf(productoExistente)
    array_carrito.splice(index_producto, 1)
    rellenarCarrito()
}

cart = document.querySelector('#sidebar')
document.querySelector('.cart-icon').addEventListener('click', ()=>{
    cart.classList.add('active')
})
cart.addEventListener('click', (e) =>{
    if (e.target.classList.contains('close-cart')){
        cart.classList.remove('active')
    }

    if (e.target.classList.contains('clear-btn')){
        array_carrito = []
        rellenarCarrito()
    }

    if (e.target.classList.contains('remove-btn')){
        idProducto = e.target.getAttribute('data-id')
        borrarDelCarrito(idProducto)
    }

    if (e.target.classList.contains('comprar-btn')){
        mensaje=""
        array_carrito.forEach(productoCarrito =>{
            let idNum = parseInt(productoCarrito.id);
            let productoBase = productosObjetos.find(p => p.id === idNum);
            mensaje += `${productoBase.nombre} (x${productoCarrito.cantidad}) - ${(productoCarrito.cantidad * productoBase.precio).toFixed(2)}€\n`;
    })
        alert(mensaje)
}
})





