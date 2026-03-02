let array_tareas = [];
let cont_id = 1;
const template = document.querySelector('#templateTarea')
const listaTareas = document.querySelector('.lista-tareas')
class Tarea{
    constructor(descripcion, tipo, completada=false, fechaCompletada=null) {
        this.id= cont_id;
        this.descripcion = descripcion;
        this.tipo = tipo;
        this.completada = completada;
        this.fechaCompletada = fechaCompletada;
        cont_id++
    }

    
}

let btn_tarea = document.querySelector('#btnAnadir');
btn_tarea.addEventListener("click", anadir_tarea);



function anadir_tarea(){
    const nombreTarea = document.querySelector('#inputTarea').value;
    const tipoTarea = document.querySelector('#selectTipo').value;

    if (nombreTarea == ''){
        alert("ERROR! Debe mostrar una ciudad")
        return;
    }

    const tarea = new Tarea(nombreTarea, tipoTarea);
    array_tareas.push(tarea)

    document.querySelector('#inputTarea').value = ""
    dibujarTareas()
}

function dibujarTareas(){
    listaTareas.innerHTML=""
    array_tareas.forEach( e =>{
        clonTemplateTarea = template.content.cloneNode(true);
        clonTemplateTarea.querySelector('.tarea-desc').textContent = e.descripcion
        clonTemplateTarea.querySelector('.tarea-tipo').textContent = e.tipo
        clonTemplateTarea.querySelector('.tarea-fecha').textContent = e.fecha

        if(e.fecha == null){
            clonTemplateTarea.querySelector('.tarea-fecha').remove()
        }

        if (e.completada){
            clonTemplateTarea.classList.add("completada")
            clonTemplateTarea.querySelector('.btn-completar')
        }

        listaTareas.append(clonTemplateTarea)
    })

    }
