from connections import sqlServerCnx, postgresServer

def productCategory():

    # Instantiate database object:
    miSqlConx = sqlServerCnx()
    postgresConx = postgresServer()

    # Create a cursor
    cursor = miSqlConx.cursor()
    cursorpg = postgresConx.cursor()

    # Execute a query
    cursor.execute('''SELECT c.ID_CATEGORIA, c.categoria_padre, c.DESCRIPCION from CATEGORIA c;''')

    # Store category, parent_id, description in a dictionary. The format is {'n(id_categoria)': int, 'a(categoria_padre)': int, 'm(descripcion)': str}
    catrelation = {i : dict(zip(f'name{i}', row)) for i, row in enumerate(cursor.fetchall()) if row[1] != None}

    #for i in catrelation.items():
    #    print(f'{i[1].get("n")}, {i[1]["a"]}')

    # Insert products categories with out parent_id
    cursor.execute('''SELECT c.ID_CATEGORIA, c.categoria_padre, c.DESCRIPCION from CATEGORIA c;''')
    for i in cursor:
        cursorpg.execute('''INSERT INTO public.product_category(name, complete_name, parent_path, create_uid, write_uid)
	                        VALUES (%s, %s, %s, %s, %s);''', (i[0], i[0], str(f'{i[0]}/'), 2, 2))
        postgresConx.commit()

    postgresConx.close()      

    # Update rows to specify new parent_id values
    postgresConxII = postgresServer()
    cursorpgUpdate = postgresConxII.cursor()
    for i in catrelation.items():
        cursorpgUpdate.execute('''UPDATE product_category SET parent_id=subquery.id FROM (SELECT id FROM product_category WHERE name= %s) as subquery WHERE name= %s;''', 
                                (str(i[1].get("a")), str(i[1].get("n"))))
        updated_rows = cursorpgUpdate.rowcount
        postgresConxII.commit()

    miSqlConx.close()

