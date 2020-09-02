--Rodrigo Castillo Camargo


create table Cuidador(
  cuidador_ID varchar not null,
  cuidador_nombre varchar(80),
  preferencia_horario varchar(10),
  primary key(cuidador_ID)
);

create table especialidadCuidador(
  especialidadCuidador_ID int not null,
  cuidador_ID varchar,
  familia_ID int,
  primary key(especialidadCuidador_ID),
  foreign key(cuidador_ID) references Cuidador,
  foreign key(familia_ID) references Familia
);

create table Familia(
  familia_ID int not null,
  nom_familia varchar(50),
  primary key(familia_ID)

);

create table Animal(
  Animal_ID int not null,
  animal_nombre_tecnico varchar(50),
  animal_nombre_comun varchar(50),
  familia_ID int not null,
  tamano varchar(10),
  primary key(Animal_ID) ,
  foreign key(familia_ID) references Familia
);

create table comportamientoAnimales(
  actividadAnimales_ID int not null,
  Animal_ID int not null,
  dieta_ID int not null,
  comportamiento int,
  primary key(actividadAnimales_ID),
  foreign key(Animal_ID) references Animal,
  foreign key(dieta_ID) references dieta,
  foreign key(comportamiento) references Actividad(actividad_ID)
);

create table Actividad(
  actividad_ID int not null,
  jornada varchar,
  horaAlimentacion datetime,
  primary key(actividad_ID)
);

create table Dieta(
  dieta_ID int not null,
  tipo_Dieta varchar(20),
  proteina_gr int,
  carbohidratos_gr int,
  grasa_gr int,
  mineRALES_gr int,
  fibra_gr int,
  primary key(dieta_ID)

);
