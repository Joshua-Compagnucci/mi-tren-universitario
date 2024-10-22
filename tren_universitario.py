import streamlit as st
from datetime import datetime

# Título de la aplicación
st.title("MI TREN UNIVERSITARIO")

# Elegir entre Tren Universitario o Colectivo Universitario
opcion_transporte = st.selectbox("Elige el tipo de transporte:", ["Tren Universitario", "Colectivo Universitario"])

if opcion_transporte == "Tren Universitario":
    # Subtítulo y descripción
    st.subheader("Selecciona la dirección del tren:")
    direction = st.selectbox("Dirección", ["La Plata", "Hospital San Juan de Dios"])

    # Crear los datos de los trenes y horarios por paradas (paradas y horarios omitidos)
    data_to_sjd = {
        "701": ["La Plata", "Arquitectura", "Informática", "Medicina", "Periodismo", "Diagonal 73", "Policlínico", "Avenida 7", "Circunvalacion", "Meridiano V", "Hospital San Juan de Dios"],
        "703": ["La Plata", "Arquitectura", "Informática", "Medicina", "Periodismo", "Diagonal 73", "Policlínico", "Avenida 7", "Circunvalacion", "Meridiano V", "Hospital San Juan de Dios"],
        "705": ["La Plata", "Arquitectura", "Informática", "Medicina", "Periodismo", "Diagonal 73", "Policlínico", "Avenida 7", "Circunvalacion", "Meridiano V", "Hospital San Juan de Dios"],
        "707": ["La Plata", "Arquitectura", "Informática", "Medicina", "Periodismo", "Diagonal 73", "Policlínico", "Avenida 7", "Circunvalacion", "Meridiano V", "Hospital San Juan de Dios"],
        "709": ["La Plata", "Arquitectura", "Informática", "Medicina", "Periodismo", "Diagonal 73", "Policlínico", "Avenida 7", "Circunvalacion", "Meridiano V", "Hospital San Juan de Dios"],
        "711": ["La Plata", "Arquitectura", "Informática", "Medicina", "Periodismo", "Diagonal 73", "Policlínico", "Avenida 7", "Circunvalacion", "Meridiano V", "Hospital San Juan de Dios"],
        "713": ["La Plata", "Arquitectura", "Informática", "Medicina", "Periodismo", "Diagonal 73", "Policlínico", "Avenida 7", "Circunvalacion", "Meridiano V", "Hospital San Juan de Dios"],
        "715": ["La Plata", "Arquitectura", "Informática", "Medicina", "Periodismo", "Diagonal 73", "Policlínico", "Avenida 7", "Circunvalacion", "Meridiano V", "Hospital San Juan de Dios"],
        "717": ["La Plata", "Arquitectura", "Informática", "Medicina", "Periodismo", "Diagonal 73", "Policlínico", "Avenida 7", "Circunvalacion", "Meridiano V", "Hospital San Juan de Dios"]
    }

    data_to_lp = {
        "702": ["Hospital San Juan de Dios", "Meridiano V", "Circunvalacion", "Avenida 7", "Policlínico", "Diagonal 73", "Periodismo", "Medicina", "Informática", "Arquitectura", "La Plata"],
        "704": ["Hospital San Juan de Dios", "Meridiano V", "Circunvalacion", "Avenida 7", "Policlínico", "Diagonal 73", "Periodismo", "Medicina", "Informática", "Arquitectura", "La Plata"],
        "706": ["Hospital San Juan de Dios", "Meridiano V", "Circunvalacion", "Avenida 7", "Policlínico", "Diagonal 73", "Periodismo", "Medicina", "Informática", "Arquitectura", "La Plata"],
        "708": ["Hospital San Juan de Dios", "Meridiano V", "Circunvalacion", "Avenida 7", "Policlínico", "Diagonal 73", "Periodismo", "Medicina", "Informática", "Arquitectura", "La Plata"],
        "710": ["Hospital San Juan de Dios", "Meridiano V", "Circunvalacion", "Avenida 7", "Policlínico", "Diagonal 73", "Periodismo", "Medicina", "Informática", "Arquitectura", "La Plata"],
        "712": ["Hospital San Juan de Dios", "Meridiano V", "Circunvalacion", "Avenida 7", "Policlínico", "Diagonal 73", "Periodismo", "Medicina", "Informática", "Arquitectura", "La Plata"],
        "714": ["Hospital San Juan de Dios", "Meridiano V", "Circunvalacion", "Avenida 7", "Policlínico", "Diagonal 73", "Periodismo", "Medicina", "Informática", "Arquitectura", "La Plata"],
        "716": ["Hospital San Juan de Dios", "Meridiano V", "Circunvalacion", "Avenida 7", "Policlínico", "Diagonal 73", "Periodismo", "Medicina", "Informática", "Arquitectura", "La Plata"],
        "718": ["Hospital San Juan de Dios", "Meridiano V", "Circunvalacion", "Avenida 7", "Policlínico", "Diagonal 73", "Periodismo", "Medicina", "Informática", "Arquitectura", "La Plata"]
    }

    # Horarios correspondientes (omitidos)
    data_times_to_sjd = {
        "701": ["07:17", "07:20", "07:23", "07:27", "07:30", "07:34", "07:39", "07:43", "07:46", "07:50", "07:55"],
        "703": ["09:03", "09:06", "09:09", "09:13", "09:16", "09:20", "09:25", "09:29", "09:32", "09:36", "09:41"],
        "705": ["10:54", "10:57", "11:00", "11:04", "11:07", "11:11", "11:16", "11:20", "11:23", "11:27", "11:32"],
        "707": ["12:38", "12:41", "12:44", "12:48", "12:51", "12:55", "13:00", "13:04", "13:07", "13:11", "13:16"],
        "709": ["14:22", "14:25", "14:28", "14:32", "14:35", "14:39", "14:44", "14:48", "14:51", "14:55", "15:00"],
        "711": ["16:06", "16:09", "16:12", "16:16", "16:19", "16:23", "16:28", "16:32", "16:35", "16:39", "16:44"],
        "713": ["17:54", "17:57", "18:00", "18:04", "18:07", "18:11", "18:16", "18:20", "18:23", "18:27", "18:32"],
        "715": ["19:42", "19:45", "19:48", "19:52", "19:55", "19:59", "20:04", "20:08", "20:11", "20:15", "20:20"],
        "717": ["21:26", "21:29", "21:32", "21:36", "21:39", "21:43", "21:48", "21:52", "21:55", "21:59", "22:04"]
    }

    data_times_to_lp = {
        "702": ["08:05", "08:09", "08:12", "08:16", "08:20", "08:24", "08:29", "08:32", "08:37", "08:40", "08:43"],
        "704": ["09:51", "09:55", "09:58", "10:02", "10:06", "10:10", "10:15", "10:18", "10:23", "10:26", "10:29"],
        "706": ["11:40", "11:44", "11:47", "11:51", "11:55", "11:59", "12:04", "12:07", "12:12", "12:15", "12:18"],
        "708": ["13:24", "13:28", "13:31", "13:35", "13:39", "13:43", "13:48", "13:51", "13:56", "13:59", "14:02"],
        "710": ["15:08", "15:12", "15:15", "15:19", "15:23", "15:27", "15:32", "15:35", "15:40", "15:43", "15:46"],
        "712": ["16:54", "16:58", "17:01", "17:05", "17:09", "17:13", "17:18", "17:21", "17:26", "17:29", "17:32"],
        "714": ["18:42", "18:46", "18:49", "18:53", "18:57", "19:01", "19:06", "19:09", "19:14", "19:17", "19:20"],
        "716": ["20:28", "20:32", "20:35", "20:39", "20:43", "20:47", "20:52", "20:55", "21:00", "21:03", "21:06"],
        "718": ["22:12", "22:16", "22:19", "22:23", "22:27", "22:31", "22:36", "22:39", "22:44", "22:47", "22:50"]
    }

    # Seleccionar los datos según la dirección elegida
    if direction == "Hospital San Juan de Dios":
        data_stations = data_to_sjd
        data_times = data_times_to_sjd
    else:
        data_stations = data_to_lp
        data_times = data_times_to_lp

    # Seleccionar el tren
    train_number = st.selectbox("Selecciona el tren:", list(data_stations.keys()))

    # Obtener las paradas y horarios del tren seleccionado
    train_stations = data_stations[train_number]
    train_times = data_times[train_number]

    # Función para calcular la estación actual del tren
    def get_train_position(current_time, times):
        current_time = datetime.strptime(current_time, "%H:%M")
        for i, time in enumerate(times):
            station_time = datetime.strptime(time, "%H:%M")
            if current_time < station_time:
                return i-1  # Retorna el índice de la parada anterior
        return len(times) - 1  # Retorna la última parada si ya las ha pasado todas

    # Obtener la hora actual
    current_time = datetime.now().strftime("%H:%M")

    # Obtener la estación actual del tren
    current_station_index = get_train_position(current_time, train_times)

    # Mostrar las estaciones con el tren que se mueve hacia abajo
    for i, time in enumerate(train_times):
        col1, col2, col3 = st.columns([2, 1, 1])  # Tres columnas: estación, tren, hora
        
        with col1:
            st.markdown(f"**{train_stations[i]}**")
        
        with col2:
            if i == current_station_index:
                # Mostrar el tren en la estación actual
                st.markdown('<div style="font-size: 24px;">🚆</div>', unsafe_allow_html=True)
            else:
                # Estaciones pasadas o futuras
                st.markdown('<div style="font-size: 24px;">⬤</div>', unsafe_allow_html=True)

        with col3:
            st.markdown(f"{time}")

# Incluir el código de JavaScript para refrescar la página automáticamente cada 10 segundos
st.markdown(
    """
    <script>
    function refresh() {
        setTimeout(function(){
           window.location.reload(1);
        }, 10000);  // Refrescar cada 10 segundos (10000 ms)
    }
    refresh();
    </script>
    """,
    unsafe_allow_html=True
)
