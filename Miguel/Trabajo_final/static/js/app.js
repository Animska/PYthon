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
        'view-doctor-dashboard': 'views/medico_dashboard.html',
        'view-admin-calendar': 'views/admin_calendar.html',
        'view-admin-manage-doctors': 'views/admin_manage_doctors.html'
    },
    // Datos Mock de Médicos
    medicos: [
        { id: 1, nombre: 'Dra. Eleanor Vance', especialidad: 'Neurología', email: 'e.vance@clinical.com', estado: 'Activo', fecha: '2023-01-15' },
        { id: 2, nombre: 'Dr. Marcus Holloway', especialidad: 'Cardiología', email: 'm.holloway@clinical.com', estado: 'Activo', fecha: '2023-03-10' },
        { id: 3, nombre: 'Dra. Sarah Jenkins', especialidad: 'Pediatría', email: 's.jenkins@clinical.com', estado: 'De Baja', fecha: '2022-11-20' },
        { id: 4, nombre: 'Dr. Robert Chen', especialidad: 'Medicina General', email: 'r.chen@clinical.com', estado: 'Activo', fecha: '2023-05-04' }
    ]
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
            <hr>
            <a href="#" class="nav-link text-muted" id="btn-open-profile"><i class="bi bi-person-gear me-2"></i> Ajustes de Perfil</a>
        `;
    } else if (role === 'doctor') {
        menuHtml = `
            <a href="#" class="nav-link" data-view="view-doctor-dashboard"><i class="bi bi-calendar2-check me-2"></i> Agenda de Hoy</a>
            <a href="#" class="nav-link text-muted"><i class="bi bi-journal-medical me-2"></i> Informes</a>
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
        btnProfile.onclick = (e) => {
            e.preventDefault();
            const profileModal = new bootstrap.Modal(document.getElementById('profileModal'));
            profileModal.show();
        };
    }

    // Logout global
    document.getElementById('btn-global-logout').onclick = () => mostrar_layout('auth');
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

    document.getElementById('login-form').onsubmit = (e) => {
        e.preventDefault();
        // Simular login exitoso
        actualizar_interfaz_usuario();
        mostrar_layout('app');
    };

    // Eventos de Registro de Paciente
    const btnOpenRegister = document.getElementById('btn-open-register');
    const registerModalEl = document.getElementById('patientRegisterModal');
    const registerForm = document.getElementById('register-patient-form');

    if (btnOpenRegister && registerModalEl) {
        const modal = new bootstrap.Modal(registerModalEl);
        btnOpenRegister.onclick = (e) => {
            e.preventDefault();
            modal.show();
        };
    }

    if (registerForm) {
        registerForm.onsubmit = (e) => {
            e.preventDefault();
            // Simulación de registro
            const nombre = document.getElementById('reg-name').value;
            alert(`¡Bienvenido, ${nombre}! Tu cuenta de paciente ha sido creada con éxito. Ahora puedes iniciar sesión.`);
            bootstrap.Modal.getInstance(registerModalEl).hide();
            registerForm.reset();
        };
    }
}

function actualizar_interfaz_usuario() {
    const name = document.getElementById('global-user-name');
    const roleLab = document.getElementById('global-user-role');

    if (AppState.rolActual === 'doctor') {
        name.textContent = "Dra. Eleanor Vance";
        roleLab.textContent = "Neuróloga Senior";
    } else if (AppState.rolActual === 'admin') {
        name.textContent = "Control de Admin";
        roleLab.textContent = "Administrador Clínico";
    } else {
        name.textContent = "Alex Thompson";
        roleLab.textContent = "Paciente";
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
