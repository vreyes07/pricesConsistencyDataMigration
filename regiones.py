from connections import postgresServer, sqlServerCnx

def regiones():

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

    cursor.execute('''SELECT s.FOLIOCADEM, r.REGION_NOMBRE, r.REGION_ID, c.DESCRIPCION
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
        cursorpg.execute('''UPDATE salas SET state_id=%s WHERE folio=%s;''', (i[2], str(i[0])))
        postgresConx.commit()
        print(i)

    exit()
    postgresConx.close()      
    miSqlConx.close()