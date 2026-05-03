/**
 * app.js - SPA Controller with Dynamic View Loading
 */

const AppState = {
    usuarioActual: null,
    rolActual: 'patient',
    layoutActivo: 'auth', // 'auth' o 'app'
    vistas: {
        'view-patient-dashboard': 'views/paciente_dashboard.html',
        'view-patient-request': 'views/paciente_request.html',
        'view-patient-calendar': 'views/paciente_calendar.html',
        'view-patient-history': 'views/paciente_history.html',
        'view-doctor-dashboard': 'views/medico_dashboard.html',
        'view-admin-calendar': 'views/admin_calendar.html',
        'view-admin-manage-doctors': 'views/admin_manage_doctors.html'
    }

};

// --- Inicialización ---
document.addEventListener('DOMContentLoaded', () => {
    configurar_login();
    mostrar_layout('auth');
});

// --- Gestión de Layouts ---
function mostrar_layout(layout) {
    AppState.layoutActivo = layout;
    const authEl = document.getElementById('layout-auth');
    const appEl = document.getElementById('layout-app');

    if (layout === 'auth') {
        authEl.classList.remove('d-none');
        appEl.classList.add('d-none');
    } else {
        authEl.classList.add('d-none');
        appEl.classList.remove('d-none');
        inicializar_sidebar();
        // Carga vista por defecto según rol
        const vistaInicial = AppState.rolActual === 'doctor' ? 'view-doctor-dashboard' :
            (AppState.rolActual === 'admin' ? 'view-admin-calendar' : 'view-patient-dashboard');
        navegar_a(vistaInicial);
        configurar_perfil(); // Inicializar lógica de perfil si es necesario
    }
}

// --- Router Dinámico (Carga Externa) ---
async function navegar_a(viewId) {
    const container = document.getElementById('view-container');
    const titleEl = document.getElementById('current-view-title');
    const path = AppState.vistas[viewId];

    if (!path) {
        console.error("Vista no encontrada:", viewId);
        return;
    }

    try {
        // 1. Mostrar estado de carga (opcional)
        container.innerHTML = '<div class="d-flex justify-content-center p-5"><div class="spinner-border text-primary" role="status"></div></div>';

        // 2. Cargar HTML externo
        const response = await fetch(path);
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        const html = await response.text();

        // 3. Inyectar contenido
        container.innerHTML = html;

        // 4. Actualizar Título (Traducción manual para mayor precisión)
        const titulos = {
            'view-patient-dashboard': 'Panel de Control',
            'view-patient-request': 'Solicitud de Consulta',
            'view-patient-calendar': 'Mi Calendario',
            'view-patient-history': 'Historial Médico',
            'view-doctor-dashboard': 'Agenda Diaria',
            'view-admin-calendar': 'Calendario Global',
            'view-admin-manage-doctors': 'Gestión de Personal'
        };
        titleEl.textContent = titulos[viewId] || 'Inicio';

        // 5. Actualizar Estado del Sidebar (Active / Text-Muted)
        document.querySelectorAll('#sidebar-nav .nav-link').forEach(link => {
            if (link.dataset.view === viewId) {
                link.classList.add('active');
                link.classList.remove('text-muted');
            } else {
                link.classList.remove('active');
                if (link.dataset.view) link.classList.add('text-muted');
            }
        });

        // 6. Re-adjuntar eventos específicos de la vista
        adjuntar_eventos_vista(viewId);

    } catch (error) {
        console.error("Error cargando vista:", error);
        container.innerHTML = `
            <div class="alert alert-danger m-4">
                <h5>Error de Carga</h5>
                <p>No se pudo cargar la vista desde <code>${path}</code>.</p>
                <small>Asegúrate de estar ejecutando un servidor local (ej. <code>python3 -m http.server</code>).</small>
            </div>
        `;
    }
}

// --- Lógica de Sidebar Dinámico ---
function inicializar_sidebar() {
    const nav = document.getElementById('sidebar-nav');
    const role = AppState.rolActual;

    let menuHtml = '';

    if (role === 'patient') {
        menuHtml = `
            <a href="#" class="nav-link" data-view="view-patient-dashboard"><i class="bi bi-grid-1x2 me-2"></i> Dashboard</a>
            <a href="#" class="nav-link" data-view="view-patient-request"><i class="bi bi-plus-circle me-2"></i> Nueva Cita</a>
            <a href="#" class="nav-link" data-view="view-patient-calendar"><i class="bi bi-calendar4-event me-2"></i> Mi Calendario</a>
            <a href="#" class="nav-link" data-view="view-patient-history"><i class="bi bi-clock-history me-2"></i> Historial Médico</a>
            <hr>
            <a href="#" class="nav-link text-muted" id="btn-open-profile"><i class="bi bi-person-gear me-2"></i> Ajustes de Perfil</a>
        `;
    } else if (role === 'doctor') {
        menuHtml = `
            <a href="#" class="nav-link" data-view="view-doctor-dashboard"><i class="bi bi-calendar2-check me-2"></i> Agenda de Hoy</a>
        `;
    } else if (role === 'admin') {
        menuHtml = `
            <a href="#" class="nav-link" data-view="view-admin-calendar"><i class="bi bi-calendar3 me-2"></i> Calendario Global</a>
            <a href="#" class="nav-link" data-view="view-admin-manage-doctors"><i class="bi bi-person-badge me-2"></i> Gestionar Personal</a>
        `;
    }

    nav.innerHTML = menuHtml;

    // Eventos del Sidebar
    nav.querySelectorAll('.nav-link[data-view]').forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            nav.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
            link.classList.add('active');
            navegar_a(link.dataset.view);
        });
    });

    // Evento para el modal de perfil
    const btnProfile = document.getElementById('btn-open-profile');
    if (btnProfile) {
        btnProfile.onclick = async (e) => {
            e.preventDefault();

            // Cargar datos reales si es un paciente
            if (AppState.rolActual === 'patient') {
                try {
                    const response = await fetch(`/api/profile/${AppState.usuarioActual.id}`);
                    if (response.ok) {
                        const data = await response.json();
                        // Rellenar modal
                        document.getElementById('profile-name').value = data.nombre || '';
                        document.getElementById('profile-email').value = data.email || '';
                        document.getElementById('profile-phone').value = data.telefono || '';
                        document.getElementById('profile-dni').value = data.dni || '';
                        document.getElementById('profile-address').value = data.direccion || '';
                        document.getElementById('profile-blood').value = data.grupo_sanguineo || 'O+';
                        document.getElementById('profile-allergies').value = data.alergias || '';
                    }
                } catch (error) {
                    console.error("Error al cargar perfil:", error);
                }
            }

            const modalEl = document.getElementById('profileModal');
            document.body.appendChild(modalEl);
            const profileModal = new bootstrap.Modal(modalEl);
            profileModal.show();
        };
    }

    // Logout global
    document.getElementById('btn-global-logout').onclick = () => {
        const loginForm = document.getElementById('login-form');
        if (loginForm) loginForm.reset();

        const errorMsgEl = document.getElementById('login-error-msg');
        if (errorMsgEl) errorMsgEl.classList.add('d-none');

        mostrar_layout('auth');
    };
}

// --- Configuración de Login ---
function configurar_login() {
    const roleBtns = document.querySelectorAll('.role-selector-btn');
    roleBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            roleBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            AppState.rolActual = btn.dataset.role;
        });
    });

    // Toggle Mostrar Contraseña
    const togglePass = document.getElementById('toggle-login-password');
    const passInput = document.getElementById('login-password');
    if (togglePass && passInput) {
        togglePass.addEventListener('click', () => {
            const isPassword = passInput.type === 'password';
            passInput.type = isPassword ? 'text' : 'password';

            // Cambiar icono
            const icon = togglePass.querySelector('i');
            icon.classList.toggle('bi-eye');
            icon.classList.toggle('bi-eye-slash');
        });
    }

    document.getElementById('login-form').onsubmit = async (e) => {
        e.preventDefault();

        const email = document.getElementById('login-email').value;
        const password = document.getElementById('login-password').value;
        const role = AppState.rolActual;
        const errorMsgEl = document.getElementById('login-error-msg');

        // Ocultar mensaje previo
        errorMsgEl.classList.add('d-none');

        try {
            const response = await fetch('/api/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ email, password, role })
            });

            if (response.ok) {
                const data = await response.json();
                AppState.usuarioActual = data.user_data;
                actualizar_interfaz_usuario();
                mostrar_layout('app');
            } else {
                const errorData = await response.json();
                errorMsgEl.textContent = `Error: ${errorData.detail || 'Credenciales incorrectas'}`;
                errorMsgEl.classList.remove('d-none');
            }
        } catch (error) {
            console.error('Error durante el inicio de sesión:', error);
            errorMsgEl.textContent = 'Error de conexión con el servidor.';
            errorMsgEl.classList.remove('d-none');
        }
    };

    // Eventos de Registro de Paciente
    const btnOpenRegister = document.getElementById('btn-open-register');
    const registerModalEl = document.getElementById('patientRegisterModal');
    const registerForm = document.getElementById('register-patient-form');

    if (btnOpenRegister && registerModalEl) {
        document.body.appendChild(registerModalEl);
        const modal = new bootstrap.Modal(registerModalEl);
        btnOpenRegister.onclick = (e) => {
            e.preventDefault();
            modal.show();
        };
    }

    if (registerForm) {
        registerForm.onsubmit = async (e) => {
            e.preventDefault();

            const nombre = document.getElementById('reg-name').value;
            const dni = document.getElementById('reg-dni').value;
            const telefono = document.getElementById('reg-phone').value;
            const email = document.getElementById('reg-email').value;
            const password = document.getElementById('reg-password').value;

            try {
                const response = await fetch('/api/register', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ nombre, dni, telefono, email, password })
                });

                if (response.ok) {
                    alert(`¡Bienvenido, ${nombre}! Tu cuenta de paciente ha sido creada con éxito. Ahora puedes iniciar sesión.`);
                    bootstrap.Modal.getInstance(registerModalEl).hide();
                    registerForm.reset();
                } else {
                    const errorData = await response.json();
                    alert(`Error al registrar: ${errorData.detail || 'Por favor verifica los datos.'}`);
                }
            } catch (error) {
                console.error('Error durante el registro:', error);
                alert('Error de conexión con el servidor al registrar.');
            }
        };
    }
}

function actualizar_interfaz_usuario() {
    const name = document.getElementById('global-user-name');
    const roleLab = document.getElementById('global-user-role');

    if (AppState.usuarioActual) {
        name.textContent = AppState.usuarioActual.nombre || AppState.usuarioActual.email;

        const rolesMap = {
            'patient': 'Paciente',
            'doctor': AppState.usuarioActual.especialidad ? `Médico - ${AppState.usuarioActual.especialidad}` : 'Médico',
            'admin': 'Administrador'
        };
        roleLab.textContent = rolesMap[AppState.usuarioActual.rol] || 'Usuario';
    } else {
        name.textContent = "Usuario Desconocido";
        roleLab.textContent = "Sin Rol";
    }
}

function configurar_perfil() {
    const profileForm = document.getElementById('profile-form');
    if (profileForm) {
        profileForm.onsubmit = async (e) => {
            e.preventDefault();

            const data = {
                nombre: document.getElementById('profile-name').value,
                email: document.getElementById('profile-email').value,
                telefono: document.getElementById('profile-phone').value,
                direccion: document.getElementById('profile-address').value,
                grupo_sanguineo: document.getElementById('profile-blood').value,
                alergias: document.getElementById('profile-allergies').value
            };

            try {
                const response = await fetch(`/api/profile/${AppState.usuarioActual.id}`, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });

                if (response.ok) {
                    alert("¡Perfil actualizado con éxito!");
                    // Actualizar nombre en la interfaz global
                    document.getElementById('global-user-name').textContent = data.nombre;
                    // Cerrar modal
                    const modalEl = document.getElementById('profileModal');
                    const modal = bootstrap.Modal.getInstance(modalEl);
                    if (modal) modal.hide();
                } else {
                    alert("Error al actualizar el perfil.");
                }
            } catch (error) {
                console.error("Error al actualizar perfil:", error);
                alert("Error de conexión al guardar el perfil.");
            }
        };
    }
}

// --- Eventos Específicos de Vistas ---
function adjuntar_eventos_vista(viewId) {
    // Delegar a módulos según el prefijo de la vista o el rol
    if (viewId.startsWith('view-patient-')) {
        adjuntar_eventos_paciente(viewId);
    } else if (viewId.startsWith('view-doctor-')) {
        adjuntar_eventos_medico(viewId);
    } else if (viewId.startsWith('view-admin-')) {
        adjuntar_eventos_admin(viewId);
    }
}
