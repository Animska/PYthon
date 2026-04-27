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
        if (form) {
            // Lógica para los botones visuales de motivo de visita
            const visitTypeRadios = form.querySelectorAll('input[name="visitType"]');
            visitTypeRadios.forEach(radio => {
                radio.addEventListener('change', () => {
                    // Limpiar clases de todos los labels
                    visitTypeRadios.forEach(r => {
                        const label = r.closest('label');
                        label.classList.remove('border-primary', 'bg-primary', 'bg-opacity-10');
                        label.classList.add('text-muted');
                        label.querySelector('i').classList.remove('text-primary');
                        label.querySelector('span').classList.remove('fw-semibold', 'text-primary');
                        label.querySelector('span').classList.add('fw-medium');
                    });

                    // Añadir clases al seleccionado
                    const activeLabel = radio.closest('label');
                    activeLabel.classList.add('border-primary', 'bg-primary', 'bg-opacity-10');
                    activeLabel.classList.remove('text-muted');
                    activeLabel.querySelector('i').classList.add('text-primary');
                    activeLabel.querySelector('span').classList.add('fw-semibold', 'text-primary');
                    activeLabel.querySelector('span').classList.remove('fw-medium');
                });
            });

            form.onsubmit = async (e) => {
                e.preventDefault();
                
                // Recopilar datos
                const motivoInput = form.querySelector('input[name="visitType"]:checked');
                const motivo = motivoInput ? motivoInput.value : "Examen General";
                const fecha = document.getElementById('appointment-date').value;
                const hora = document.getElementById('appointment-time').value;
                const sintomas = document.getElementById('appointment-symptoms').value;
                const prioridadAlta = document.getElementById('appointment-priority').checked;

                const data = {
                    paciente_id: AppState.usuarioActual.paciente_id,
                    medico_id: 1, // Por ahora fijo a Dra. Eleanor Vance
                    fecha_hora: `${fecha} ${hora}`,
                    motivo: motivo,
                    sintomas: sintomas,
                    prioridad_alta: prioridadAlta
                };

                try {
                    const response = await fetch('/api/appointments', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(data)
                    });

                    if (response.ok) {
                        alert("¡Solicitud enviada con éxito!");
                        navegar_a('view-patient-dashboard');
                    } else {
                        const err = await response.json();
                        alert("Error al enviar la solicitud: " + (err.detail || "Error desconocido"));
                    }
                } catch (error) {
                    console.error("Error enviando cita:", error);
                    alert("Error de conexión al enviar la solicitud.");
                }
            };
        }
    }

    if (viewId === 'view-patient-calendar') {
        inicializar_calendario_paciente();
    }
}

function inicializar_calendario_paciente() {
    const calendarEl = document.getElementById('calendar-paciente');
    if (!calendarEl) return;

    const calendar = new FullCalendar.Calendar(calendarEl, {
        themeSystem: 'bootstrap5',
        initialView: 'timeGridWeek',
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek'
        },
        locale: 'es',
        slotMinTime: '08:00:00',
        slotMaxTime: '20:00:00',
        slotDuration: '00:30:00',
        slotLabelInterval: '01:00:00',
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
