from datetime import datetime

def es_par(num):
  return int(num) % 2 == 0

def es_generacion_z(anio):
  return int(anio) >= 2000


def es_bisiesto(anio):
  anio = int(anio)  
  return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def obtener_edad_actual(anio_nacimiento):
  anio_actual = datetime.now().year

  return anio_actual - int(anio_nacimiento)