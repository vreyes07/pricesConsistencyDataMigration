from connections import postgresServer, sqlServerCnx

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