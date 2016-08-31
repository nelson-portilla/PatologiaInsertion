CREATE TEMP TABLE tmp_table AS SELECT * FROM muestra_html WITH NO DATA;
COPY tmp_table FROM '/home/registro/Vídeos/prueba_cargar/scripts/texto_plano/registro.csv' DELIMITER '|' CSV HEADER;
INSERT INTO muestra_html SELECT * FROM tmp_table t1
where not exists
(select numeroregistro from muestra_html t2 
where t2.numeroregistro=t1.numeroregistro);
DROP TABLE tmp_table;