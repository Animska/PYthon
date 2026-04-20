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
