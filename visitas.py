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

def visitas():

    # Instantiate database object:
    miSqlConx = sqlServerCnx()
    postgresConx = postgresServer()

    # Create a cursor
    cursor = miSqlConx.cursor()
    cursorpg = postgresConx.cursor()

    # Execute a query and print results
    cursor.execute('''SELECT v.ID_VISITA, v.ID_ESTUDIOSALA, v.ID_AUDITOR, v.ESTADO, v.HORAINICIO, v.HORAFIN from VISITA v;''')

    for i in cursor:
        print(i)
        cursorpg.execute('''INSERT INTO public.planning_salas(planning_id, place_id, auditor_id, state, create_uid, write_uid, date_start, date_end)
	                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''', (i[0], i[1], i[2], str(i[3]), 2, 2, i[4], i[5]))  
        #cursorpg.execute('''INSERT INTO public.comunas (id, "name", create_uid, write_uid)
        #                    VALUES(%s, %s, %s, %s)''', (i[0], i[1], i[2], i[3]))
        #postgresConx.commit()

    postgresConx.close()      
    miSqlConx.close()

