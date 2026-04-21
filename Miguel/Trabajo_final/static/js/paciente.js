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

    if (viewId === 'view-patient-calendar') {
        inicializar_calendario_paciente();
    }
}

function inicializar_calendario_paciente() {
    const calendarEl = document.getElementById('calendar-paciente');
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
        slotLabelFormat: {
            hour: '2-digit',
            minute: '2-digit',
            hour12: false
        },
        allDaySlot: false,
        height: 'auto',
        events: [
            {
                title: 'Seguimiento Neurológico - Dra. Vance',
                start: '2023-10-24T10:00:00',
                end: '2023-10-24T11:00:00',
                backgroundColor: 'rgba(11, 94, 215, 0.1)',
                borderColor: '#0b5ed7',
                textColor: '#0b5ed7'
            },
            {
                title: 'Fisioterapia - Sala 3',
                start: '2026-04-27T14:00:00',
                end: '2026-04-27T15:30:00',
                backgroundColor: 'rgba(255, 193, 7, 0.1)',
                borderColor: '#ffc107',
                textColor: '#ffc107'
            }
        ]
    });

    calendar.render();
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
