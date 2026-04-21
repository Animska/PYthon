/**
 * admin.js - Lógica específica para el rol de Administrador
 */

function adjuntar_eventos_admin(viewId) {
    if (viewId === 'view-admin-manage-doctors') {
        renderizar_tabla_medicos();

        // Buscador
        const searchInput = document.getElementById('doctor-search');
        if (searchInput) {
            searchInput.oninput = (e) => {
                renderizar_tabla_medicos(e.target.value);
            };
        }

        // Botón Añadir
        const btnAdd = document.getElementById('btn-add-doctor');
        if (btnAdd) {
            btnAdd.onclick = () => {
                const modalEl = document.getElementById('doctorModal');
                document.body.appendChild(modalEl);
                document.getElementById('doctor-form').reset();
                document.getElementById('edit-index').value = "";
                document.getElementById('modalTitle').textContent = "Añadir Nuevo Médico";
                new bootstrap.Modal(modalEl).show();
            };
        }

        // Submit Formulario (Add/Edit)
        const docForm = document.getElementById('doctor-form');
        if (docForm) {
            docForm.onsubmit = (e) => {
                e.preventDefault();
                const editIndex = document.getElementById('edit-index').value;
                const nuevoMedico = {
                    nombre: document.getElementById('doctor-name').value,
                    especialidad: document.getElementById('doctor-specialty').value,
                    email: document.getElementById('doctor-email').value,
                    estado: document.getElementById('doctor-status').value,
                    fecha: new Date().toISOString().split('T')[0]
                };

                if (editIndex === "") {
                    nuevoMedico.id = AppState.medicos.length + 1;
                    AppState.medicos.push(nuevoMedico);
                } else {
                    nuevoMedico.id = AppState.medicos[editIndex].id;
                    AppState.medicos[editIndex] = nuevoMedico;
                }

                bootstrap.Modal.getInstance(document.getElementById('doctorModal')).hide();
                renderizar_tabla_medicos();
            };
        }
    }

    if (viewId === 'view-admin-calendar') {
        inicializar_calendario_admin();
    }
}

function inicializar_calendario_admin() {
    const calendarEl = document.getElementById('calendar-admin');
    if (!calendarEl) return;

    const calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'timeGridWeek',
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek'
        },
        locale: 'es',
        slotMinTime: '08:00:00',
        slotMaxTime: '20:00:00',
        allDaySlot: false,
        height: 'auto',
        slotLabelFormat: {
            hour: '2-digit',
            minute: '2-digit',
            hour12: false
        },
        events: [
            {
                title: 'Ronda de Cardiología',
                start: '2026-04-26T08:00:00',
                end: '2026-04-26T10:00:00',
                backgroundColor: 'rgba(255, 193, 7, 0.1)',
                borderColor: '#ffc107',
                textColor: '#ffc107'
            },
            {
                title: 'Thompson (Consul)',
                start: '202-10-24T10:00:00',
                end: '2023-10-24T11:30:00',
                backgroundColor: 'rgba(40, 167, 69, 0.1)',
                borderColor: '#28a745',
                textColor: '#28a745'
            },
            {
                title: 'Quirófano #2 - Apén.',
                start: '2023-10-26T10:30:00',
                end: '2023-10-26T14:00:00',
                backgroundColor: 'rgba(220, 53, 69, 0.1)',
                borderColor: '#dc3545',
                textColor: '#dc3545'
            }
        ]
    });

    calendar.render();
}

// --- Funciones de Gestión de Médicos ---
function renderizar_tabla_medicos(filtro = '') {
    const tbody = document.getElementById('doctors-table-body');
    const template = document.getElementById('doctor-row-template');
    if (!tbody || !template) return;

    tbody.innerHTML = '';

    const medicosFiltrados = AppState.medicos.filter(m =>
        m.nombre.toLowerCase().includes(filtro.toLowerCase()) ||
        m.especialidad.toLowerCase().includes(filtro.toLowerCase())
    );

    medicosFiltrados.forEach(m => {
        const originalIndex = AppState.medicos.findIndex(med => med.id === m.id);
        const clone = template.content.cloneNode(true);

        clone.querySelector('.row-name').textContent = m.nombre;
        clone.querySelector('.row-specialty').textContent = m.especialidad;
        clone.querySelector('.row-email').textContent = m.email;
        clone.querySelector('.row-date').textContent = m.fecha;

        const statusBadge = clone.querySelector('.row-status');
        statusBadge.textContent = m.estado;
        statusBadge.className = `badge rounded-pill row-status ${m.estado === 'Activo' ? 'bg-success-subtle text-success' :
            m.estado === 'De Baja' ? 'bg-warning-subtle text-warning' :
                'bg-danger-subtle text-danger'
            }`;

        clone.querySelector('.btn-edit').onclick = () => window.editar_medico(originalIndex);
        clone.querySelector('.btn-delete').onclick = () => window.eliminar_medico(originalIndex);

        tbody.appendChild(clone);
    });

    const totalEl = document.getElementById('stat-total-doctors');
    if (totalEl) totalEl.textContent = AppState.medicos.length;
}

window.editar_medico = (index) => {
    const m = AppState.medicos[index];
    const modalEl = document.getElementById('doctorModal');
    document.body.appendChild(modalEl);

    document.getElementById('doctor-name').value = m.nombre;
    document.getElementById('doctor-specialty').value = m.especialidad;
    document.getElementById('doctor-email').value = m.email;
    document.getElementById('doctor-status').value = m.estado;
    document.getElementById('edit-index').value = index;
    document.getElementById('modalTitle').textContent = "Editar Perfil Médico";
    new bootstrap.Modal(modalEl).show();
};

window.eliminar_medico = (index) => {
    if (confirm(`¿Estás seguro de que deseas eliminar a ${AppState.medicos[index].nombre}?`)) {
        AppState.medicos.splice(index, 1);
        renderizar_tabla_medicos();
    }
};
