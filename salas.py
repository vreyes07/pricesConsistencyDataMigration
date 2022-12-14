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
    #cursor.execute('''SELECT c.DESCRIPCION, s.DIRECCION, s.FOLIOCADEM, s.ID_COMUNA, s.ID_CADENA, s.ID_CANAL, s.GPS_LATITUD, s.GPS_LONGITUD
    #                  FROM SALA s 
    #                  LEFT JOIN CADENA c ON s.ID_CADENA = c.ID_CADENA;''')

    cursor.execute('''SELECT s.FOLIOCADEM, r.REGION_NOMBRE, c.DESCRIPCION
                      FROM SALA s LEFT JOIN CADENA c ON s.ID_CADENA = c.ID_CADENA 
                      INNER JOIN COMUNA c2 on s.ID_COMUNA = c2.COMUNA_ID 
                      INNER JOIN PROVINCIA p on c2.COMUNA_PROVINCIA_ID = p.PROVINCIA_ID 
                      INNER join REGION r on p.PROVINCIA_REGION_ID = r.REGION_ID
                      WHERE c.DESCRIPCION IS NOT NULL;''')
            
    for i in cursor:
        #print(f'Inserting room {i[0]}')
        #cursorpg.execute('''INSERT INTO public.salas(name, address, folio, comuna_id, cadena, canal, lat, long, create_uid, write_uid)
	      #                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);''',(i[0], i[1], i[2], i[3], i[4], i[5],
        #                    float(i[6].replace(',','.')), float(i[7].replace(',','.')), 2, 2))
        print(f'Updating region for room {i[0]}')
        cursorpg.execute('''UPDATE salas SET state_id=%s WHERE folio=%s;''', (str(i[1]), str(i[0])))
        postgresConx.commit()
        print(i)

    exit()
    postgresConx.close()      
    miSqlConx.close()