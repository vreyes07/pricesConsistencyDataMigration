from connections import sqlServerCnx, postgresServer
from datetime import date

def planograma102():

    # Instantiate database object:
    miSqlConx = sqlServerCnx()
    postgresConx = postgresServer()

    # Create a cursor
    cursor = miSqlConx.cursor()
    cursorpg = postgresConx.cursor()

    # Execute a query and print results
    cursor.execute('''SELECT 102 as Id_planograma, s.FOLIOCADEM foliocadem, 2 as userid, '01/01/1900' as fecha from TOMA t 
                    INNER JOIN VISITA v on t.ID_VISITA = v.ID_VISITA 
                    INNER JOIN ESTUDIOSALA es on v.ID_ESTUDIOSALA = es.ID_ESTUDIOSALA 
                    INNER JOIN SALA s on s.ID_SALA = es.ID_SALA WHERE t.ID_VARIABLE = 3 GROUP BY s.FOLIOCADEM;''')

    for i in cursor:
        cursorpg.execute('''INSERT INTO public.lolo (Id_planograma, foliocadem, userid, fecha)
                            VALUES(%s, %s, %s, %s)''', (int(i[0]), int(i[1]), int(i[2]), i[3]))
        postgresConx.commit()

    postgresConx.close()      
    miSqlConx.close()

