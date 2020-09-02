drop table if exists PNG;
drop sequence if exists id_png;
create sequence  id_png
start with 1
increment by 1
maxvalue 99999
minvalue 1;
CREATE TABLE PNG(
  pngid bigint default nextval('id_png') PRIMARY KEY,
  ruta varchar(500),
  moddate varchar(250),
  accesstime varchar(230),
  megapixels varchar(235),
  colortype varchar(235),
  imagesize varchar(335) 

);
INSERT INTO PNG (ruta , moddate , accesstime , megapixels , colortype , imagesize) VALUES ('path' ,'fecha' , 'access', 'megapixels' ,'colortype' , 'size' );
select * from PNG;
