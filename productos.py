from openpyxl import Workbook
from connections import sqlServerCnx

def productos():
    
    # Create final xls to contain all the data
    wb = Workbook()
    wb.create_sheet("Items3")
    sheet = wb.active

    # Instantiate database object:
    miSqlConx = sqlServerCnx()

    # Create a cursor
    cursor = miSqlConx.cursor()

    # Execute a query and print results
    cursor.execute('''SELECT i.EAN, i.ID_CATEGORIA, app.ID_CATEGORIA as AppCategoria, i.DESCRIPCION, i.MARCA, i.FABRICANTE, i.VOLUMEN, i.ALTO, i.LARGO, i.ANCHO, i.PESO,
                      i.ID_CLIENTE, c.NOMBRECLIENTE
                      FROM ITEM i 
                      INNER JOIN CLIENTE c on i.ID_CLIENTE = c.ID_CLIENTE
                      RIGHT JOIN ALARMA_PRODUCTO_POSICION app on i.ID_CATEGORIA = app.ID_CATEGORIA
                      ORDER BY I.EAN
                      OFFSET 150000 ROWS 
                      FETCH NEXT 15000 ROWS ONLY;''')
    
    # Retrieve Columns header names
    columns = cursor.description
    result = [i[0] for i in cursor.description]
    sheet.append(result)

    for i in cursor:
       sheet.append(tuple(i))

    wb.save('Items.xlsx')

    miSqlConx.close()