let array_tareas = []
let cont_id = 0
class Tarea{
    constructor(descripcion, tipo, completada=false, fechaCompletada=null) {
        this.id= cont_id
        this.descripcion = descripcion;
        this.tipo = tipo;
        this.completada = completada;
        this.fechaCompletada = fechaCompletada;
        cont_id++
    }

    
}

form_tarea = document.querySelector('.')

