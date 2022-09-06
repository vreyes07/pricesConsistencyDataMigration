from connections import postgresServer, sqlServerCnx

'''
En SUPI la tabla tiene los sgtes atributos:
  FOLIOHISTORICO
  FOLIOCADEM
  ID_COMUNA: Llave foránea tabla comuna
  DIRECCION
  GPS_LATITUD
  GPS_LONGITUDve 
  ACTIVO
  ID_CADENA
  ID_FORMATO
  ID_CANAL
  PRIORIDAD

En SUPI+ se usan los sgtes:
  NAME
  ADDRESS
  FOLIO
  COMUNA_ID
  STATE_ID: QUÉ ES ESTO?
  LAT
  LONG
  ** unos cuantos campos no tienen match en la data vieja. Son columnas repetidas? Ex: lat moved0 --> lat?

* Atributos de Odoo?

INSERT INTO public.salas
("name", address, folio, comuna_id, state_id, lat_moved0, long_moved0, geo, create_uid, create_date, write_uid, write_date, retail_cod_local, cadena, bandera, cod_local, canal, formato, id_sala_supi, lat, long)
VALUES('', '', '', 0, 0, '', '', 0, 0, '', 0, '', '', '', '', '', '', '', '', 0, 0);
'''

def salas():

    # Instantiate database object:
    miSqlConx = sqlServerCnx()
    postgresConx = postgresServer()

    # Create a cursor
    cursor = miSqlConx.cursor()
    cursorpg = postgresConx.cursor()

    # Execute a query and print results
    cursor.execute('''SELECT s.FOLIOCADEM, s.ID_COMUNA, s.DIRECCION, s.GPS_LATITUD, s.GPS_LONGITUD, s.ID_CADENA, s.ID_COMUNA from SALA s;''')

    for i in cursor:
        cursorpg.execute('''INSERT INTO public.comunas ("name", state_id, create_uid, write_uid,)
                            VALUES(%s, %s, %s, %s, %s, %s)''', (int(i[0]), int(i[1]), int(i[2])))
        postgresConx.commit()

    postgresConx.close()      
    miSqlConx.close()