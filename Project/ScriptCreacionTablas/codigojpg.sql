drop table if exists JPG;
drop sequence if exists id_jpg;
create sequence  id_jpg
start with 1
increment by 1
maxvalue 99999
minvalue 1;
CREATE TABLE JPG(
  jpgid bigint default nextval('id_jpg') PRIMARY KEY,
  ruta varchar(50),
  modtime   varchar(120),
  camera   varchar(120),
  flash   varchar(110),
  GPSLatituderef   varchar(130),
  GPSAltituderef   varchar(310),
  GPSLongituderef   varchar(310),
  GPSDatestamp   varchar(301),
  GPSTimestamp   varchar(301),
  GPSAltitude  varchar(301),
  GPSLatitude   varchar(301),
  GPSLongitude   varchar(310),
  GPSPosition   varchar(312)
  

);
INSERT INTO jpg (ruta, modtime , camera, flash, GPSLatituderef , GPSAltituderef, GPSLongituderef, GPSDatestamp , GPSTimestamp , GPSAltitude, GPSLatitude ,GPSLongitude ,GPSPosition) 
VALUES ('RUTA' ,'MODTIME' , 'camera', 'flash' ,'gps latitude ref' , 'gps altitude ref' ,'gps longitude ref' ,'gps date stamp' ,'gps time stamp','gps altitude','gps latitude','gps longitude', 'Gps Position');
select * from jpg;
