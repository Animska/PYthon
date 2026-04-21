/**
 * medico.js - Lógica específica para el rol de Médico
 */

// Datos Mock de Citas y Pacientes
const citasMock = [
    {
        id: 1,
        paciente: "Alex Thompson",
        hora: "10:00 AM",
        motivo: "Seguimiento Neurológico",
        estado: "Activo",
        genero: "Hombre",
        edad: 32,
        sangre: "O+ Positivo",
        alergias: "Polen, Penicilina",
        vitals: { altura: 182, peso: 78, respiracion: 16, presion: "120/80" },
        observaciones: "El paciente muestra una mejora significativa en la movilidad después de la sesión de fisioterapia. La medicación Lisinopril 10mg se está tolerando bien."
    },
    {
        id: 2,
        paciente: "Sarah Jenkins",
        hora: "11:30 AM",
        motivo: "Consulta de Migraña",
        estado: "Pendiente",
        genero: "Mujer",
        edad: 28,
        sangre: "A- Negativo",
        alergias: "Nueces, Aspirina",
        vitals: { altura: 165, peso: 55, respiracion: 18, presion: "110/70" },
        observaciones: "Migrañas recurrentes en la zona frontal. Se recomienda llevar un diario de cefaleas y reducir el consumo de cafeína."
    },
    {
        id: 3,
        paciente: "Marcus Holloway",
        hora: "12:15 PM",
        motivo: "Chequeo Post-operatorio",
        estado: "Pendiente",
        genero: "Hombre",
        edad: 45,
        sangre: "B+ Positivo",
        alergias: "Ninguna conocida",
        vitals: { altura: 178, peso: 82, respiracion: 14, presion: "130/85" },
        observaciones: "Recuperación favorable tras la cirugía de rodilla. La inflamación ha disminuido un 40%."
    },
    {
        id: 4,
        paciente: "Elena Rodríguez",
        hora: "01:00 PM",
        motivo: "Control de Diabetes",
        estado: "Completado",
        genero: "Mujer",
        edad: 52,
        sangre: "O- Negativo",
        alergias: "Látex",
        vitals: { altura: 160, peso: 68, respiracion: 16, presion: "125/82" },
        observaciones: "Niveles de glucosa estables. Se ajusta la dosis de insulina basal según los nuevos resultados de laboratorio."
    }
];

let citaSeleccionadaId = 1;

function adjuntar_eventos_medico(viewId) {
    if (viewId === 'view-doctor-dashboard') {
        renderizar_agenda();
        configurar_busqueda();
        
        // Mostrar el primero por defecto si existe
        if (citasMock.length > 0) {
            mostrar_detalle_paciente(citasMock[0].id);
        }
    } else if (viewId === 'view-doctor-reports') {
        renderizar_lista_pacientes_informes();
        configurar_busqueda_informes();
        
        // Mostrar el primero por defecto si existe
        if (citasMock.length > 0) {
            mostrar_formulario_informe(citasMock[0].id);
        }
    }
}

function renderizar_agenda(filtro = '') {
    const contenedor = document.getElementById('contenedor-agenda');
    if (!contenedor) return;

    const citasFiltradas = citasMock.filter(c => 
        c.paciente.toLowerCase().includes(filtro.toLowerCase()) || 
        c.motivo.toLowerCase().includes(filtro.toLowerCase())
    );

    if (citasFiltradas.length === 0) {
        contenedor.innerHTML = '<div class="text-center p-4 text-muted small">No se encontraron pacientes</div>';
        return;
    }

    contenedor.innerHTML = citasFiltradas.map(cita => {
        const isActive = cita.id === citaSeleccionadaId;
        const statusBadgeClass = cita.estado === 'Activo' ? 'bg-primary bg-opacity-10 text-primary' : 'bg-light text-muted';
        const borderClass = isActive ? 'border-primary border-start border-4 shadow-sm' : 'border-light cursor-pointer transition-hover';
        
        return `
            <div class="border rounded-4 p-3 bg-white ${borderClass} agenda-item" data-id="${cita.id}">
                <div class="d-flex justify-content-between mb-2">
                    <span class="badge ${statusBadgeClass} rounded-pill px-3 py-1 fw-bold">${cita.hora}</span>
                    ${isActive ? '<span class="small text-muted fw-bold">Activo</span>' : ''}
                </div>
                <h6 class="mb-1 fw-bold">${cita.paciente}</h6>
                <p class="small text-muted mb-0">${cita.motivo}</p>
            </div>
        `;
    }).join('');

    // Adjuntar eventos de clic
    contenedor.querySelectorAll('.agenda-item').forEach(item => {
        item.onclick = () => {
            const id = parseInt(item.dataset.id);
            mostrar_detalle_paciente(id);
        };
    });
}

function configurar_busqueda() {
    const inputBusqueda = document.getElementById('buscar-paciente');
    if (inputBusqueda) {
        inputBusqueda.oninput = (e) => {
            renderizar_agenda(e.target.value);
        };
    }
}

function mostrar_detalle_paciente(id) {
    const cita = citasMock.find(c => c.id === id);
    if (!cita) return;

    citaSeleccionadaId = id;
    
    // Actualizar clases de la agenda para feedback visual
    document.querySelectorAll('.agenda-item').forEach(item => {
        const itemId = parseInt(item.dataset.id);
        if (itemId === id) {
            item.classList.add('border-primary', 'border-start', 'border-4', 'shadow-sm');
            item.classList.remove('border-light', 'cursor-pointer', 'transition-hover');
        } else {
            item.classList.remove('border-primary', 'border-start', 'border-4', 'shadow-sm');
            item.classList.add('border-light', 'cursor-pointer', 'transition-hover');
        }
    });

    const contenedor = document.getElementById('detalle-paciente-contenido');
    const template = document.getElementById('template-informe-paciente');
    
    if (!contenedor || !template) return;

    // Limpiar contenido anterior
    contenedor.innerHTML = '';
    
    // Clonar el template
    const clone = template.content.cloneNode(true);
    
    // Rellenar los datos en el fragmento clonado usando las clases de plantilla
    clone.querySelector('.t-nombre-paciente').textContent = cita.paciente;
    clone.querySelector('.t-info-genero-edad').innerHTML = 
        `<i class="bi bi-gender-${cita.genero === 'Hombre' ? 'male' : 'female'} me-1"></i> ${cita.genero}, ${cita.edad}`;
    clone.querySelector('.t-info-sangre').innerHTML = 
        `<i class="bi bi-droplet me-1"></i> ${cita.sangre}`;
    clone.querySelector('.t-alergias-paciente').textContent = cita.alergias;
    
    clone.querySelector('.t-vital-altura').textContent = cita.vitals.altura;
    clone.querySelector('.t-vital-peso').textContent = cita.vitals.peso;
    clone.querySelector('.t-vital-respiracion').textContent = cita.vitals.respiracion;
    clone.querySelector('.t-vital-presion').textContent = cita.vitals.presion;
    
    clone.querySelector('.t-observaciones-paciente').textContent = cita.observaciones;

    // Inyectar el fragmento en el DOM
    contenedor.appendChild(clone);

    // Adjuntar evento al botón de editar informe
    const btnEditar = contenedor.querySelector('.t-btn-editar-informe');
    if (btnEditar) {
        btnEditar.onclick = () => abrir_modal_informe(id);
    }

    // Gestionar visibilidad de los estados del panel
    document.getElementById('detalle-paciente-vacio').classList.add('d-none');
    contenedor.classList.remove('d-none');
}

function abrir_modal_informe(id) {
    const cita = citasMock.find(c => c.id === id);
    if (!cita) return;

    const modalBody = document.getElementById('modal-report-body');
    const template = document.getElementById('template-formulario-informe');
    
    if (!modalBody || !template) return;

    // Limpiar contenido anterior
    modalBody.innerHTML = '';
    
    // Clonar el template
    const clone = template.content.cloneNode(true);
    
    // Rellenar los datos
    clone.querySelector('.t-nombre-paciente').textContent = cita.paciente;
    clone.querySelector('.t-info-genero-edad').innerHTML = 
        `<i class="bi bi-gender-${cita.genero === 'Hombre' ? 'male' : 'female'} me-1"></i> ${cita.genero}, ${cita.edad}`;
    clone.querySelector('.t-info-sangre').innerHTML = 
        `<i class="bi bi-droplet me-1"></i> ${cita.sangre}`;
    clone.querySelector('.t-alergias-paciente').textContent = cita.alergias;
    
    // Rellenar inputs
    clone.querySelector('.t-input-altura').value = cita.vitals.altura;
    clone.querySelector('.t-input-peso').value = cita.vitals.peso;
    clone.querySelector('.t-input-respiracion').value = cita.vitals.respiracion;
    clone.querySelector('.t-input-presion').value = cita.vitals.presion;
    
    clone.querySelector('.t-textarea-observaciones').value = cita.observaciones;

    // Manejar envío del formulario
    const form = clone.querySelector('#form-actualizar-informe');
    form.onsubmit = (e) => {
        e.preventDefault();
        
        // Actualizar datos en citasMock
        cita.vitals.altura = parseInt(form.querySelector('.t-input-altura').value);
        cita.vitals.peso = parseInt(form.querySelector('.t-input-peso').value);
        cita.vitals.respiracion = parseInt(form.querySelector('.t-input-respiracion').value);
        cita.vitals.presion = form.querySelector('.t-input-presion').value;
        cita.observaciones = form.querySelector('.t-textarea-observaciones').value;
        
        // Cerrar modal
        const modalEl = document.getElementById('reportModal');
        const modal = bootstrap.Modal.getInstance(modalEl);
        if (modal) modal.hide();

        // Refrescar detalle en el dashboard
        mostrar_detalle_paciente(id);
        
        alert(`Informe de ${cita.paciente} actualizado con éxito.`);
    };

    // Inyectar el fragmento en el modal
    modalBody.appendChild(clone);

    // Mostrar modal (Reutilizando instancia de Bootstrap si existe para evitar problemas de backdrop)
    const modalEl = document.getElementById('reportModal');
    let modal = bootstrap.Modal.getInstance(modalEl);
    if (!modal) {
        modal = new bootstrap.Modal(modalEl);
    }
    modal.show();
}


// --- Lógica de Informes (OBSOLETO: Ahora integrado en Dashboard vía Modal) ---
// Se han eliminado las funciones renderizar_lista_pacientes_informes, configurar_busqueda_informes y mostrar_formulario_informe
// ya que la funcionalidad ahora reside en abrir_modal_informe dentro de la vista del dashboard.


