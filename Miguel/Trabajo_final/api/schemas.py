from pydantic import BaseModel
from typing import Dict, Any, Optional

class LoginRequest(BaseModel):
    email: str
    password: str
    role: str

class LoginResponse(BaseModel):
    message: str
    user_data: Dict[str, Any]

class RegisterPatientRequest(BaseModel):
    nombre: str
    dni: str
    telefono: str
    email: str
    password: str

class PatientProfileResponse(BaseModel):
    id: int
    usuario_id: int
    nombre: str
    dni: str
    email: str
    telefono: Optional[str] = None
    direccion: Optional[str] = None
    grupo_sanguineo: Optional[str] = None
    alergias: Optional[str] = None

class UpdateProfileRequest(BaseModel):
    nombre: str
    email: str
    telefono: str
    direccion: Optional[str] = None
    grupo_sanguineo: Optional[str] = None
    alergias: Optional[str] = None

class RegisterDoctorRequest(BaseModel):
    nombre: str
    especialidad: str
    email: str
    password: str
    estado: str = "Activo"

class DoctorResponse(BaseModel):
    id: int
    usuario_id: int
    nombre: str
    especialidad: str
    email: str
    estado: str
    fecha: str # Usaremos string para simplificar el envío desde la BD

class AppointmentCreate(BaseModel):
    paciente_id: int
    medico_id: int
    fecha_hora: str
    motivo: str
    sintomas: Optional[str] = None
    prioridad_alta: bool = False

class AppointmentUpdate(BaseModel):
    estado: str
    medico_id: Optional[int] = None
