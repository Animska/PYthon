from fastapi import FastAPI, HTTPException, status
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from mysql.connector import Error as MySQLError
import os
import uvicorn

from api.database import initialize_database, get_db_connection
from api.schemas import (
    LoginRequest, LoginResponse, RegisterPatientRequest, PatientProfileResponse, 
    UpdateProfileRequest, RegisterDoctorRequest, DoctorResponse, DoctorUpdate,
    AppointmentCreate, AppointmentUpdate, PatientReportCreate, PatientReportResponse
)
from api.repository import (
    authenticate_user, create_patient, get_patient_profile, update_patient_profile, 
    get_all_doctors, create_doctor, update_doctor, delete_doctor,
    create_appointment, get_pending_appointments, update_appointment_status, 
    get_all_appointments, get_active_appointments_by_patient, get_all_appointments_by_patient, 
    get_doctor_appointments_by_day, create_or_update_patient_report, get_available_slots, 
    get_latest_report_by_patient
)

# Inicializar Base de Datos al arrancar el script
initialize_database()

app = FastAPI(title="Clinica Rodriguez API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)

# Endpoints de Autenticación
@app.post("/api/login", response_model=LoginResponse, status_code=status.HTTP_200_OK)
async def login(request: LoginRequest):
    """
    Endpoint para iniciar sesión. Valida las credenciales contra la base de datos.
    """
    user_data = authenticate_user(request.email, request.password, request.role)
    
    if not user_data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas o rol no autorizado"
        )
        
    return LoginResponse(
        message="Inicio de sesión exitoso",
        user_data=user_data
    )

@app.post("/api/register", status_code=status.HTTP_201_CREATED)
async def register(request: RegisterPatientRequest):
    """
    Endpoint para registrar un nuevo paciente.
    """
    try:
        data = request.model_dump()
        create_patient(data)
        return {"message": "Paciente registrado exitosamente"}
    except MySQLError as e:
        if e.errno == 1062:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El correo electrónico o DNI ya está registrado."
            )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error al procesar el registro."
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@app.get("/api/profile/{usuario_id}", response_model=PatientProfileResponse)
async def get_profile(usuario_id: int):
    """Obtiene los datos del perfil del paciente."""
    profile = get_patient_profile(usuario_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Perfil no encontrado")
    return profile

@app.put("/api/profile/{usuario_id}")
async def update_profile(usuario_id: int, request: UpdateProfileRequest):
    """Actualiza los datos del perfil del paciente."""
    success = update_patient_profile(usuario_id, request.model_dump())
    if not success:
        raise HTTPException(status_code=500, detail="Error al actualizar el perfil")
    return {"message": "Perfil actualizado correctamente"}

@app.get("/api/doctors", response_model=list[DoctorResponse])
async def list_doctors():
    """Lista todos los médicos de la base de datos."""
    return get_all_doctors()

@app.post("/api/doctors", status_code=status.HTTP_201_CREATED)
async def add_doctor(request: RegisterDoctorRequest):
    """Crea un nuevo médico."""
    try:
        success = create_doctor(request.model_dump())
        if not success:
            raise HTTPException(status_code=500, detail="No se pudo crear el médico.")
        return {"message": "Médico creado exitosamente"}
    except MySQLError as e:
        if e.errno == 1062:
            raise HTTPException(status_code=400, detail="El email ya está registrado.")
        raise HTTPException(status_code=500, detail="Error de base de datos.")

@app.put("/api/doctors/{id}")
async def update_doc(id: int, request: DoctorUpdate):
    """Actualiza un médico existente."""
    success = update_doctor(id, request.model_dump())
    if not success:
        raise HTTPException(status_code=500, detail="Error al actualizar el médico.")
    return {"message": "Médico actualizado correctamente"}

@app.delete("/api/doctors/{id}")
async def delete_doc(id: int):
    """Elimina un médico."""
    success = delete_doctor(id)
    if not success:
        raise HTTPException(status_code=500, detail="Error al eliminar el médico.")
    return {"message": "Médico eliminado correctamente"}

@app.post("/api/appointments", status_code=status.HTTP_201_CREATED)
async def add_appointment(request: AppointmentCreate):
    """Crea una nueva cita."""
    success = create_appointment(request.model_dump())
    if not success:
        raise HTTPException(status_code=500, detail="Error al programar la cita.")
    return {"message": "Cita programada exitosamente"}

@app.get("/api/appointments/pending")
async def list_pending_appointments():
    """Lista todas las citas pendientes."""
    return get_pending_appointments()

@app.get("/api/appointments/patient/{paciente_id}")
async def list_patient_appointments(paciente_id: int):
    """Lista todas las citas de un paciente específico."""
    return get_active_appointments_by_patient(paciente_id)

@app.get("/api/appointments/patient/{paciente_id}/history")
async def list_patient_appointment_history(paciente_id: int):
    """Lista el historial completo de citas de un paciente."""
    return get_all_appointments_by_patient(paciente_id)

@app.get("/api/appointments/doctor/{medico_id}")
async def list_doctor_appointments(medico_id: int, fecha: str):
    """Lista todas las citas de un médico para un día específico."""
    return get_doctor_appointments_by_day(medico_id, fecha)

@app.get("/api/appointments/available_slots")
async def available_slots(fecha: str, motivo: str):
    """Devuelve los huecos disponibles basados en las citas existentes y la duración del motivo."""
    slots = get_available_slots(fecha, motivo)
    return {"available_slots": slots}

@app.get("/api/appointments")
async def list_all_appointments():
    """Lista todas las citas aceptadas (para el calendario)."""
    return get_all_appointments()

@app.patch("/api/appointments/{id}")
async def update_appointment(id: int, request: AppointmentUpdate):
    """Actualiza el estado y/o el médico de una cita."""
    success = update_appointment_status(id, request.estado, request.medico_id)
    if not success:
        raise HTTPException(status_code=500, detail="Error al actualizar la cita.")
    return {"message": "Cita actualizada correctamente"}

@app.post("/api/reports", status_code=status.HTTP_201_CREATED)
async def save_report(request: PatientReportCreate):
    """Guarda o actualiza el informe de un paciente."""
    success = create_or_update_patient_report(request.model_dump())
    if not success:
        raise HTTPException(status_code=500, detail="Error al guardar el informe.")
    return {"message": "Informe guardado correctamente"}

@app.get("/api/reports/patient/{paciente_id}/latest", response_model=PatientReportResponse)
async def get_latest_report(paciente_id: int):
    """Obtiene el último informe médico de un paciente."""
    report = get_latest_report_by_patient(paciente_id)
    if not report:
        raise HTTPException(status_code=404, detail="No se encontró ningún informe para este paciente")
    return report

# Montar las carpetas estáticas y vistas
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/views", StaticFiles(directory="views"), name="views")

@app.get("/")
async def read_index():
    """Sirve el index.html principal (Single Page Application)."""
    index_path = os.path.join(os.path.dirname(__file__), "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    raise HTTPException(status_code=404, detail="Index no encontrado")

@app.get("/health")
async def health_check():
    """Endpoint de estado para comprobar la conexión a BD."""
    conn = get_db_connection()
    if conn:
        conn.close()
        return {"status": "ok", "database": "connected"}
    
    raise HTTPException(status_code=500, detail="Database connection failed")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
