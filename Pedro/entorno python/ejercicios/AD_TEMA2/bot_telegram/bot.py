import logging
from datetime import date, timedelta, datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import acceso_datos
import config
from google import genai

# =================================================================
# ACTIVACIÓN DEL LOG
# =================================================================
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# =================================================================
# CONFIGURACIÓN DE API TOKENS
# =================================================================
TOKEN_BOT = config.TOKEN_BOT
GEMINI_API_KEY = config.GEMINI_API_KEY

# =================================================================
# FUNCIONES AUXILIARES PARA FORMATEAR MENSAJES PARA TELEGRAM
# =================================================================
def encender_aspersores():
    pass

def apagar_aspersores():
    pass

def formatear_mensaje(temp, humedad):
    return (
        "🌡️Temperatura (°C):\n"
        f"   • Media: {temp['mean']}\n"
        f"   • Min: {temp['min']}\n"
        f"   • Max: {temp['max']}\n"
        
        "💧Humedad Relativa (%):\n"
        f"   • Media: {humedad['mean']}\n"
        f"   • Min: {humedad['min']}\n"
        f"   • Max: {humedad['max']}\n"
    )

def formatear_mensaje_actual(temp, humedad):
    return (
        f"🌡️Temperatura: {temp}°C\n"
        f"💧Humedad Relativa {humedad}%:\n"
    )

# =================================================================
# FUNCIÓN PARA PEDIR CONSEJO A GEMINI
# =================================================================
def consejo_gemini(temperatura,humedad,planta)->str:
    client=genai.Client(api_key = GEMINI_API_KEY)
    prompt = (
        f"Se lo mas conciso y breve posible, que consejos darias para "
        f"cuidar esta planta:{planta} en estas condiciones: "
        f"Humedad: {humedad}% y temperatura: {temperatura}ºC"
        f"necesito que marques la humedad,temperatura y planta que te he dicho al principio de tu mensaje"
        f"formatealo y estilizalo para telegram y usa emojis si es necesario"
        f"no uses markdown para darle formato, no funciona"
    )

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error de API de Gemini: {e}"
    
def controlador_gemini(temperatura,humedad,planta)->str:
    client=genai.Client(api_key = GEMINI_API_KEY)
    prompt = (
        f"Devuelve solamente 'true' o una cadena vacia" 
        f"con esta planta:{planta} en estas condiciones: "
        f"Humedad: {humedad}% y temperatura: {temperatura}ºC"
        f"¿Encenderias los aspersores?"
        f"Si la respuesta es correcta devuelve true"
        f"si la respuesta es false devuelve una cadena vacia"

    )

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        if response.text:
            encender_aspersores()
            return f"Aspersores encendidos ✅"
        else:
            apagar_aspersores()
            return f"Aspersores apagados ❌"
    except Exception as e:
        return f"Error de API de Gemini: {e}"
# =================================================================
# VALIDACIÓN DE ARGUMENTO UBICACIÓN
# =================================================================
def validar_ubicacion(args: list[str]) -> str:
    """Valida que la ubicación del comando sea correcta y no tenga más argumentos."""
    if not args or len(args) > 2 or args[0].lower() not in ["huerto", "invernadero"]:
        return "" 
    
    return args[0] # Devuelve la ubicación

# =================================================================
# MANEJADORES DE CADA COMANDO DEL BOT TELEGRAM
# =================================================================

# /menu
async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja el comando /menu para mostrar ayuda."""
    ayuda_mensaje = (
        "🌱 Bot de Monitoreo Ambiental\n\n"
        "Comandos disponibles (requieren ubicación: `huerto` o `invernadero`):\n"
        "• `/actual [ubicación]`: Muestra valores actuales. Ej: `/actual huerto`\n"
        "• `/diario [ubicación]`: Resumen de un día anterior. Ej: `/diario invernadero`\n"
        "• `/semanal [ubicación]`: Resumen de la última semana. Ej: `/semanal huerto`\n"
        "• `/consejo [ubicación]`: Consejo de Gemini para tus plantas. Ej: `/consejo huerto`\n"
    )
    await update.message.reply_text(ayuda_mensaje, parse_mode='Markdown')

# /diario <ubicación>
async def diario_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja el comando /diario [ubicacion]."""
    chat_id = update.effective_chat.id
    
    # 1. Validar Ubicación
    ubicacion = validar_ubicacion(context.args)
    if not ubicacion:
        error = f"❌ Ubicación no válida. Usa 'huerto' o 'invernadero'.\nEj: /diario huerto"
        await context.bot.send_message(chat_id=chat_id, text=error)
    
    else:
        # 2. Obtenemos Fecha actual para mostrarla
        hoy = date.today()
        ayer = hoy - timedelta(days=1)
        fecha = f"{ayer.strftime('%Y-%m-%d')}"    
        await context.bot.send_message(chat_id=chat_id, text=f"🔍 Consultando datos del {ubicacion} de {fecha}.")

        # 3. Obtenemos los datos
        if ubicacion == 'huerto':
            humedad = acceso_datos.diario_huerto_humedad()
            temp = acceso_datos.diario_huerto_temperatura()
        else: 
            # Solo hay opcion de que sea invernadero
            humedad = acceso_datos.diario_invernadero_humedad()
            temp = acceso_datos.diario_invernadero_temperatura()
            
        # 4. Formateamos el mensaje
        mensaje = formatear_mensaje(temp, humedad)
        
        # 5. Enviar la respuesta
        await context.bot.send_message(chat_id=chat_id, text=mensaje)

# /semanal <ubicación>
async def semanal_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja el comando /semanal [ubicacion]."""
    chat_id = update.effective_chat.id
    
    # 1. Validar Ubicación
    ubicacion = validar_ubicacion(context.args)
    if not ubicacion:
        error = f"❌ Ubicación no válida. Usa 'huerto' o 'invernadero'.\nEj: /semanal huerto"
        await context.bot.send_message(chat_id=chat_id, text=error)
    
    else:
        # 2. Obtenemos Fecha actual para mostrarla
        hoy = date.today()
        ayer = hoy - timedelta(days=1)
        fecha = f"{ayer.strftime('%Y-%m-%d')}"    
        await context.bot.send_message(chat_id=chat_id, text=f"🔍 Consultando datos del {ubicacion} de {fecha}.")

        # 3. Obtenemos los datos
        if ubicacion == 'huerto':
            humedad = acceso_datos.semanal_huerto_humedad()
            temp = acceso_datos.semanal_huerto_temperatura()
        else: 
            # Solo hay opcion de que sea invernadero
            humedad = acceso_datos.semanal_invernadero_humedad()
            temp = acceso_datos.semanal_invernadero_temperatura()
            
        # 4. Formateamos el mensaje
        mensaje = formatear_mensaje(temp, humedad)
        
        # 5. Enviar la respuesta
        await context.bot.send_message(chat_id=chat_id, text=mensaje)

# /actual <ubicación>
async def actual_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja el comando /actual [ubicacion]."""
    chat_id = update.effective_chat.id
    
    # 1. Validar Ubicación
    ubicacion = validar_ubicacion(context.args)
    if not ubicacion:
        error = f"❌ Ubicación no válida. Usa 'huerto' o 'invernadero'.\nEj: /actual huerto"
        await context.bot.send_message(chat_id=chat_id, text=error)
    
    else:
        # 2. Obtenemos Fecha actual para mostrarla
        hoy = date.today()
        ayer = hoy - timedelta(days=1)
        fecha = f"{ayer.strftime('%Y-%m-%d')}"    
        await context.bot.send_message(chat_id=chat_id, text=f"🔍 Consultando datos del {ubicacion} actual.")

        # 3. Obtenemos los datos
        if ubicacion == 'huerto':
            humedad = acceso_datos.actual_huerto_humedad()
            temp = acceso_datos.actual_huerto_temperatura()
        else: 
            # Solo hay opcion de que sea invernadero
            humedad = acceso_datos.actual_invernadero_humedad()
            temp = acceso_datos.actual_invernadero_temperatura()
            
        # 4. Formateamos el mensaje
        mensaje = formatear_mensaje_actual(temp, humedad)
        
        # 5. Enviar la respuesta
        await context.bot.send_message(chat_id=chat_id, text=mensaje)


# /consejo <ubicación> <planta>
async def consejo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja el comando /consejo [ubicacion]."""
    # SIGUE ESTRUCTURA SIMILAR AL MANEJADOR FACILITADO
    # Guardar el chat_id
    chat_id = update.effective_chat.id
    ubicacion = validar_ubicacion(context.args)
    # Validar Ubicación
    if not ubicacion:
        error = f"❌ Ubicación no válida. Usa 'huerto' o 'invernadero'.\nEj: /actual huerto"
        await context.bot.send_message(chat_id=chat_id, text=error)
    
    else:
    # Obtenemos los datos según ubicación
        planta=context.args[1]
        if ubicacion == 'huerto':
            humedad = acceso_datos.actual_huerto_humedad()
            temp = acceso_datos.actual_huerto_temperatura()
        else: 
            # Solo hay opcion de que sea invernadero
            humedad = acceso_datos.actual_invernadero_humedad()
            temp = acceso_datos.actual_invernadero_temperatura()
            
        
    # Formateamos el mensaje
        mensaje=consejo_gemini(temp,humedad,planta)
    # Enviar la respuesta
        await context.bot.send_message(chat_id=chat_id, text=mensaje)

async def control_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja el comando /consejo [ubicacion]."""
    # SIGUE ESTRUCTURA SIMILAR AL MANEJADOR FACILITADO
    # Guardar el chat_id
    chat_id = update.effective_chat.id
    ubicacion = validar_ubicacion(context.args)
    # Validar Ubicación
    if not ubicacion:
        error = f"❌ Ubicación no válida. Usa 'huerto' o 'invernadero'.\nEj: /actual huerto"
        await context.bot.send_message(chat_id=chat_id, text=error)
    
    else:
    # Obtenemos los datos según ubicación
        planta=context.args[1]
        if ubicacion == 'huerto':
            humedad = acceso_datos.actual_huerto_humedad()
            temp = acceso_datos.actual_huerto_temperatura()
        else: 
            # Solo hay opcion de que sea invernadero
            humedad = acceso_datos.actual_invernadero_humedad()
            temp = acceso_datos.actual_invernadero_temperatura()
            
        
    # Formateamos el mensaje
        mensaje=controlador_gemini(temp,humedad,planta)
    # Enviar la respuesta
        await context.bot.send_message(chat_id=chat_id, text=mensaje)

# =================================================================
# FUNCIÓN PRINCIPAL Y REGISTRO DE MANEJADORES
# =================================================================
def main():
    if not TOKEN_BOT:
        print("ERROR: Por favor, reemplaza 'TOKEN' en el archivo config.py.")
        return

    # Se crea la clase que controla del Bot con el TOKEN
    appbot = ApplicationBuilder().token(TOKEN_BOT).build()

    # Registro de funciones manejadoras de comandos
    appbot.add_handler(CommandHandler("menu", menu_handler))
    appbot.add_handler(CommandHandler("diario", diario_handler))
    appbot.add_handler(CommandHandler("semanal", semanal_handler))
    appbot.add_handler(CommandHandler("actual", actual_handler))
    appbot.add_handler(CommandHandler("consejo", consejo_handler))
    appbot.add_handler(CommandHandler("control", control_handler))

    # Se inicia el sondeo de comandos a servidores de Telegram
    print("El bot de monitoreo está corriendo...")
    appbot.run_polling()

if __name__ == '__main__':
    main()