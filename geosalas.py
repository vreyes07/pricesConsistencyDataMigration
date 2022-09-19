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

def geosalas():

    # Instantiate database object:
    miSqlConx = sqlServerCnx()
    postgresConx = postgresServer()

    # Create a cursor
    cursor = miSqlConx.cursor()
    cursorpgUpdate = postgresConx.cursor()

    # Execute a query and print results
    cursor.execute('''SELECT s.FOLIOCADEM, s.GPS_LATITUD, s.GPS_LONGITUD FROM SALA s;''')
                      
    for i in cursor:
        print(i)
        #UPDATE salas SET lat=-29.9624953 WHERE folio='22087001';
        print(f'Executing query for {i[0]}')
        cursorpgUpdate.execute('''UPDATE salas SET long=%s WHERE folio=%s;''', (i[2], str(i[0])))
        #cursorpg.execute('''INSERT INTO public.salas(name, address, folio, comuna_id, cadena, canal, lat, long, create_uid, write_uid)
	      #                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);''',(i[0], i[1], i[2], i[3], i[4], i[5],
        #                    float(i[6].replace(',','.')), float(i[7].replace(',','.')), 2, 2))
        postgresConx.commit()

    postgresConx.close()      
    miSqlConx.close()