import enum as enum
import components.database_byd as database_byd

#teclados


reply_keyboard = [
    ['📄 Totales', '❓ Help']
]

total_keyboard = [
    ['gasolina', 'electricidad', 
     'kilometros']
]

help_text = f"""
       ℹ️ *Centro de ayuda - Byd-bot*

Aquí tienes las opciones disponibles:

/start - Inicia el bot  
/help - Muestra este mensaje  

📌 *Consultas sobre el bot:*

🏖️ premio - Información  

💬 Puedes escribir el comando o simplemente preguntar con tus propias palabras.
    """
    

texto_start = f"""👋 ¡Hola equipo!

Soy *Byd-bot*, vuestro asistente.

Estoy aquí para facilitaros el día a día:

🔧 Consultas rápidas  

💬 Escríbeme lo que necesites o usa los botones de abajo 👇"""

text_continue_help = f"""¿En qué más puedo ayudarte?"""
text_km_total = f"""Los kilometros totales recorridos son: {database_byd.trip_km_total}"""
text_fuel_total = f"""El gasto total en gasolina es: {database_byd.fuel_total}"""
text_elec_total = f"""El gasto total en electricidad es: {database_byd.elec_total}"""

