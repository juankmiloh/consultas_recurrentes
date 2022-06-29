----------------------------
-- EJECUTAR PROCEDURE EN SQL Developer
----------------------------
VARIABLE USERCUR REFCURSOR; -- Ejecutar X linea
EXECUTE SP_CONS_SERVICIOS(:usercur); -- Ejecutar X linea
PRINT USERCUR -- Ejecutar X linea
