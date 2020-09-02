drop table if exists PDF;
drop sequence if exists id_pdf;

create sequence  id_pdf
start with 1
increment by 1
maxvalue 99999
minvalue 1;
CREATE TABLE PDF(
pdfid bigint default nextval('id_pdf') PRIMARY KEY,
nombre VARCHAR(300),              
creationDate VARCHAR(320),
fulbanner VARCHAR(350),
trapped VARCHAR(350),
modDate VARCHAR(350),
creator VARCHAR(350)
);
INSERT INTO PDF (nombre,creationdate,fulbanner,trapped,moddate,creator) VALUES ('Balcon', '17/05/2020', 'Sevilla','asdsa','16/8/2019','Jhon Sabogal');
select * from PDF;
