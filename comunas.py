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

def comunas():

    # Instantiate database object:
    miSqlConx = sqlServerCnx()
    postgresConx = postgresServer()

    # Create a cursor
    cursor = miSqlConx.cursor()
    cursorpg = postgresConx.cursor()

    # Execute a query and print results
    cursor.execute('''SELECT c.COMUNA_ID, c.COMUNA_NOMBRE, 2 as createuid, 2 as writeuid from COMUNA c inner join PROVINCIA p on c.COMUNA_PROVINCIA_ID = p.PROVINCIA_ID;''')

    for i in cursor:
        cursorpg.execute('''INSERT INTO public.comunas (id, "name", create_uid, write_uid)
                            VALUES(%s, %s, %s, %s)''', (i[0], i[1], i[2], i[3]))
        postgresConx.commit()

    postgresConx.close()      
    miSqlConx.close()

