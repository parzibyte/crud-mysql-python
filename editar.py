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
			
			consulta = "UPDATE peliculas SET titulo = %s WHERE id = %s;"
			nuevo_titulo = "Ready Player One: comienza el juego"
			id_editar = 2
			cursor.execute(consulta, (nuevo_titulo, id_editar))

		# No olvidemos hacer commit cuando hacemos un cambio a la BD
		conexion.commit()
	finally:
		conexion.close()
	
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)