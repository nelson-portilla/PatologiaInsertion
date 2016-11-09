CREATE TABLE muestra_html
(
  numeroregistro character varying(20) NOT NULL,
  historiaclinica bigint,
  cedula integer,
  descmacro text,
  descmicro text,
  diagnostico text,
  texto text,
  CONSTRAINT muestra_html_pkey PRIMARY KEY (numeroregistro)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE muestra_html
  OWNER TO postgres;
