"""
	Tutorial de CRUD con MySQL y Python 3
	parzibyte.me/blog
"""
import pymysql
try:
	conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='peliculas')
	try:
		with conexion.cursor() as cursor:
			
			consulta = "SELECT id, titulo, anio FROM peliculas WHERE anio > %s;"
			cursor.execute(consulta, (2000))

			# Con fetchall traemos todas las filas
			peliculas = cursor.fetchall()

			# Recorrer e imprimir
			for pelicula in peliculas:
				print(pelicula)
	finally:
		conexion.close()
	
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)