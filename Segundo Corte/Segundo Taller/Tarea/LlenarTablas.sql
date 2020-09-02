--Rodrigo Castillo Camargo

--insertar cuidadores

insert into Cuidador values('42995854', 'Maria Mendez', 'Diurno');
insert into Cuidador values('9733201', 'Pedro Perez', 'Nocturno');
insert into Cuidador values('100029981', 'Cecilia Cubillos', 'Nocturno');
insert into Cuidador values('80943410', 'Álvaro Álvarez', 'Diurno');


--insertar Familias

insert into Familia values(01, 'Camelidae');
insert into Familia values(02, 'Felidae');
insert into Familia values(03, 'Lemuridae');
insert into Familia values(04, 'Canidae');
insert into Familia values(05, 'Cheirogaleidae');

--insertar especialidadCuidador

insert into especialidadCuidador values(04, '42995854', 04);
insert into especialidadCuidador values(02, '42995854', 02);

insert into especialidadCuidador values(02, '9733201', 02);
insert into especialidadCuidador values(01, '9733201', 01);

insert into especialidadCuidador values(01, '100029981', 01);
insert into especialidadCuidador values(05, '100029981', 05);

insert into especialidadCuidador values(03, '80943410', 03);
insert into especialidadCuidador values(05, '80943410', 05);


--Insertar Animales

insert into Animal values(01,'Camelus Dromedarius', 'Camello Dromedario','Camelidae','Grande')
insert into Animal values(02,'Lama Glama', 'Llama','Camelidae','Grande')
insert into Animal values(03,'Leopardus Pardalis', 'Ocelote','Felidae','Medio')
insert into Animal values(04,'Lepilemur Sahamalazensis', 'Lemur de Sahamaiza','Lemuridae','Pequeño')
insert into Animal values(05,'Lycalopex Griseus', 'Zorro Gris Suramericano','Canidae','Media')
insert into Animal values(06,'Lycalopex Sechuare', 'Zorro del Desierto Peruano','Canidae','Media')
insert into Animal values(07,'Microcebus Myonixus', 'Lemur Ratón Pigmeo','Cheirogaleidae','Muy Pequeño')
insert into Animal values(08,'Mirza Coquereli', 'Lemur Ratón Gigante','Cheirogaleidae','Medio')
insert into Animal values(09,'Otocyon Megalotis', 'Zorro Orejas de Murcielago','Canidae','Media')
insert into Animal values(10,'Panthera Leo', 'Leon','Felidae','Muy Grande')
insert into Animal values(11,'Panthera Onca', 'Jaguar','Felidae','Medio')
insert into Animal values(12,'Panthera Pardus', 'Leopardo','Felidae','Grande')
insert into Anicreate table comportamientoAnimales(
  actividadAnimales_ID int not null,
  Animal_ID int not null,
  dieta_ID int not null,
  comportamiento int,
  primary key(actividadAnimales_ID),
  foreign key(Animal_ID) references Animal,
  foreign key(dieta_ID) references dieta,
  foreign key(comportamiento) references Actividad(actividad_ID)
);mal values(13,'Prionalirius Rubiginosus', 'Gato Manchado Oxidado','Felidae','Medio')
insert into Animal values(14,'Vicugna Pacos', 'Alpaca','Camelidae','Grande')
insert into Animal values(15,'Vicugna Vicugna', 'Vicuña','Camelidae','Media')
insert into Animal values(16,'Vulpes Vulpes', 'Zorro Rojo','Canidae','Media')


-- Insertar Dieta CAMBIAR VALORES DIETA DE 69, 07 Y 50

insert into Dieta values(01, 'Herbivora',30,33,3,12,33)--Pequeño
insert into Dieta values(06, 'Frugivora',10,100,25,40,80)--Medio
insert into Dieta values(03, 'Carnivora',33,6,25,30,8)--Pequeño
insert into Dieta values(02, 'Herbivora',30,300,23,38,270)--Grande
insert into Dieta values(11, 'Carnivora',375,75,270,105,45)--Grande
insert into Dieta values(04, 'Insectivoro',44,10,33,17,3)--Pequeño
insert into Dieta values(15, 'Carnivora',150,75,85,65,24)--Medio


-- Insertar Actividad
create table comportamientoAnimales(
  actividadAnimales_ID int not null,
  Animal_ID int not null,
  dieta_ID int not null,
  comportamiento int,
  primary key(actividadAnimales_ID),
  foreign key(Animal_ID) references Animal,
  foreign key(dieta_ID) references dieta,
  foreign key(comportamiento) references Actividad(actividad_ID)
);create table comportamientoAnimales(
  actividadAnimales_ID int not null,
  Animal_ID int not null,
  dieta_ID int not null,
  comportamiento int,
  primary key(actividadAnimales_ID),
  foreign key(Animal_ID) references Animal,
  foreign key(dieta_ID) references dieta,
  foreign key(comportamiento) references Actividad(actividad_ID)
);
insert into Actividad values(01,'Diurno')
insert into Actividad values(02,'Nocturno')

-- Insertar Comportamiento Animales

insert into comportamientoAnimales values(01,01,02,01)
insert into comportamientoAnimales values(02,02,02,01)
insert into comportamientoAnimales values(03,03,15,01)
insert into comportamientoAnimales values(04,04,04,02)
insert into comportamientoAnimales values(05,05,15,01)
insert into comportamientoAnimales values(06,06,15,01)
insert into comportamientoAnimales values(07,07,69,02)
insert into comportamientoAnimales values(08,08,07,02)
insert into comportamientoAnimales values(09,09,15,02)
insert into comportamientoAnimales values(10,10,50,01)
insert into comportamientoAnimales values(11,11,15,01)
insert into comportamientoAnimales values(12,12,11,02)
insert into comportamientoAnimales values(13,13,15,02)
insert into comportamientoAnimales values(14,14,02,01)
insert into comportamientoAnimales values(15,15,12,01)
insert into comportamientoAnimales values(16,16,11,01)
