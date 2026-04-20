/**
 * paciente.js - Lógica específica para el rol de Paciente
 */

function adjuntar_eventos_paciente(viewId) {
    if (viewId === 'view-patient-dashboard') {
        const btnRequest = document.getElementById('btn-nav-request');
        if (btnRequest) btnRequest.onclick = () => navegar_a('view-patient-request');

        const btnCalendar = document.getElementById('btn-nav-calendar');
        if (btnCalendar) btnCalendar.onclick = () => navegar_a('view-patient-calendar');
    }

    if (viewId === 'view-patient-request') {
        const btnBack = document.getElementById('btn-back-to-dashboard');
        if (btnBack) btnBack.onclick = () => navegar_a('view-patient-dashboard');

        const form = document.getElementById('consultation-form');
        if (form) form.onsubmit = (e) => {
            e.preventDefault();
            alert("Solicitud enviada con éxito!");
        };
    }
}

function configurar_perfil() {
    const profileForm = document.getElementById('profile-form');
    if (profileForm) {
        profileForm.onsubmit = (e) => {
            e.preventDefault();
            const nuevoNombre = document.getElementById('profile-name').value;
            // Simular guardado
            alert("¡Perfil actualizado con éxito!");
            // Actualizar nombre en la interfaz global si es el paciente
            if (AppState.rolActual === 'patient') {
                document.getElementById('global-user-name').textContent = nuevoNombre;
            }
            bootstrap.Modal.getInstance(document.getElementById('profileModal')).hide();
        };
    }
}
