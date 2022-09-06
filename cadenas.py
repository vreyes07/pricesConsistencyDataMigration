from connections import sqlServerCnx, postgresServer
from datetime import date

'''
En SUPI la tabla tiene los sgtes atributos:
  COMUNA_ID
  COMUNA_NOMBRE
  COMUNA_PROVINCIA_ID: llave foránea a la tabla PROVINCIA
  lat
  lot

En SUPI+ se usan los sgtes:
  NAME
  STATE_ID
  CREATE_UID
  CREATE_DATE*
  WRITE_UID
  WRITE_DATE*

* Atributos de Odoo?

public.comunas insert script
INSERT INTO public.comunas
("name", state_id, create_uid, create_date, write_uid, write_date)
VALUES('', 0, 0, '', 0, '');
'''

def cadenas():

    # Instantiate database object:
    miSqlConx = sqlServerCnx()
    postgresConx = postgresServer()

    # Create a cursor
    cursor = miSqlConx.cursor()
    cursorpg = postgresConx.cursor()

    # Execute a query and print results
    cursor.execute('''SELECT TOP 10 c.DESCRIPCION FROM CADENA c;;''')

    for i in cursor:
        cursorpg.execute('''INSERT INTO public.cadenas_supi(name, create_uid, write_uid)
	                        VALUES (%s, %s, %s);''', (str(i[0]), int(2), int(2)))
        postgresConx.commit()

    postgresConx.close()      
    miSqlConx.close()

