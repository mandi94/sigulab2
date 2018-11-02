# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# AppConfig configuration made easy. Look inside private/appconfig.ini
# Auth is for authenticaiton and access control
# -------------------------------------------------------------------------

###Bien mueble###
db.define_table(
    'bien_mueble',
    Field('bm_nombre','string',notnull=True,label=T('Nombre del Bien Mueble'),requires=IS_NOT_EMPTY()),
    Field('bm_num','string',notnull=True,unique=True,requires = IS_MATCH('^[0-9]{6}'), label = T('Número Bien Nacional')),
    Field('bm_placa','string', default="00000", label=T('Número de Placa del Bien'),requires = [IS_EMPTY_OR(IS_MATCH('^s/n$|^[0-9]{4,6}$')),IS_EMPTY_OR(IS_NOT_IN_DB(db,'bm_placa'))]),
    #No son obligatorios para mobiliario
    Field('bm_marca','string',label=T('Marca')),
    Field('bm_modelo','string',label=T('Modelo')),
    Field('bm_serial','string',label=T('Serial')),
    #
    Field('bm_descripcion','text', label=T('Descripción')),
    Field('bm_material','string',notnull=True,label=T('Material Predominante'), requires=IS_IN_SET(['Acero','Acrílico','Madera','Metal','Plástico','Tela','Vidrio', 'Otro'])),
    Field('bm_color','string',notnull=True,label=T('Color')),
    #Solo lo poseen los equipos
    Field('bm_calibrar', 'string', label = T('Requiere calibración'), requires = IS_EMPTY_OR(IS_IN_SET(['Si', 'No']))),
    Field('bm_fecha_calibracion','date',label=T('Fecha de Calibracion')),
    #
    Field('bm_unidad','string',label=T('Unidad de Medida'),requires=IS_EMPTY_OR(IS_IN_SET(['cm','m']))),
    Field('bm_ancho','double',label=T('Ancho'),requires=IS_EMPTY_OR(IS_FLOAT_IN_RANGE(0.1,999.99))),
    Field('bm_largo','double',label=T('Largo'),requires=IS_EMPTY_OR(IS_FLOAT_IN_RANGE(0.1,999.99))),
    Field('bm_alto','double',label=T('Alto'),requires=IS_EMPTY_OR(IS_FLOAT_IN_RANGE(0.1,999.99))),
    Field('bm_diametro','double',label=T('Diametro'),requires=IS_EMPTY_OR(IS_FLOAT_IN_RANGE(0.1,999.99))),

    Field('bm_movilidad','string',notnull=True,label=T('Movilidad'),requires=IS_IN_SET(['Fijo','Portátil'])),
    Field('bm_uso','string',notnull=True,label=T('Uso'),requires=IS_IN_SET(['Docencia','Investigación','Extensión','Apoyo administrativo'])),
    Field('bm_estatus','string',label=T('Estatus'),requires=IS_IN_SET(['Operativo','Inoperativo','En desuso','Inservible'])),
    Field('bm_categoria', 'string', notnull= True, label = T('Nombre de la categoría'), requires = IS_IN_SET(['Maquinaria y demás equipos de construcción, campo, industria y taller', 'Equipos de transporte, tracción y elevación', 'Equipos de comunicaciones y de señalamiento', 
    'Equipos médicos - quirúrgicos, dentales y veterinarios', 'Equipos científicos, religiosos, de enseñanza y recreación', 'Máquinas, muebles y demás equipos de oficina y de alojamiento'])),
    Field('bm_subcategoria', 'string', notnull= True, label = T('Nombre de la subcategoría')),
    Field('bm_codigo_localizacion','string',notnull=True,label=T('Código de Localización'), requires=IS_IN_SET(['150301','240107'])),
    Field('bm_localizacion','string',notnull=True,label=T('Localización'), requires=IS_IN_SET(['Edo Miranda, Municipio Baruta, Parroquia Baruta','Edo Vargas, Municipio Vargas, Parroquia Macuto'])),
    #Foraneas
    Field('bm_espacio_fisico', 'reference espacios_fisicos', notnull=True, label=T('Nombre del espacio fisico')),
    Field('bm_unidad_de_adscripcion', 'reference dependencias', notnull=True, label = T('Unidad de Adscripción')),
    Field('bm_depedencia', 'reference dependencias',notnull=True, label = T('Nombre de la dependencia')),
    Field('bm_crea_ficha', 'reference auth_user', notnull = True, label = T('Usuario que crea la ficha')),
    # Estado = -1 :Denegado
    # Estado = 0  :Por validación
    # Estado = 1  :Aceptado
    # Estado = 2  :Sin solicitud
    Field('bm_eliminar','integer', default=2, label=T('Estado de Solicitud de Eliminacion'), requires=IS_INT_IN_RANGE(-1,3)),
    Field('bm_desc_eliminar', 'string', length = 140, label = T('Razon de Eliminacion')),
    Field('bm_clasificacion', 'string', notnull = True, label = T('Clasificacion del bien mueble'), requires=IS_IN_SET(['Equipo','Mobiliario'])),
    # Estado = 0 : Visible
    # Estado = 1 : Oculto
    Field('bm_oculto','integer', default=0, label=T('Visibilidad del BM'), requires=IS_INT_IN_RANGE(0,2)),
    #Field('bm_uso_espacio_fisico', 'reference espacios_fisicos',notnull=True, label = T('Uso del espacio fisico'))
    )
    
db.bien_mueble.bm_placa.requires = IS_EMPTY_OR(IS_NOT_IN_DB(db(db.bien_mueble.bm_placa==request.vars.bm_placa), 'bien_mueble.bm_placa   '))
db.bien_mueble.bm_crea_ficha.requires = IS_IN_DB(db, db.auth_user, '%(first_name)s %(last_name)s | %(email)s')
db.bien_mueble.bm_espacio_fisico.requires = IS_IN_DB(db, db.espacios_fisicos.id,'%(codigo)s')
db.bien_mueble.bm_unidad_de_adscripcion.requires = IS_IN_DB(db, db.dependencias.id,'%(unidad_de_adscripcion)s')
db.bien_mueble.bm_depedencia.requires = IS_IN_DB(db, db.dependencias.id,'%(nombre)s')

###Modificacion de bien mueble###

db.define_table(
    'modificacion_bien_mueble',
    Field('mbn_nombre','string',label=T('Nombre del Bien Mueble')),
    Field('mbn_num','string',notnull=True,unique=True,requires = IS_MATCH('^[0-9]{6}'), label = T('Número Bien Nacional')),
    Field('mbn_placa','string',label=T('Número de Placa del Bien'),requires = IS_EMPTY_OR(IS_MATCH('^s/n$|^[0-9]{4,6}$'))),
    #No son obligatorios para mobiliario
    Field('mbn_marca','string',label=T('Marca')),
    Field('mbn_modelo','string',label=T('Modelo')),
    Field('mbn_serial','string',label=T('Serial')),
    #
    Field('mbn_descripcion','text',label=T('Descripción')),
    Field('mbn_material','string',label=T('Material Predominante'), requires=IS_EMPTY_OR(IS_IN_SET(['Acero','Acrílico','Madera','Metal','Plástico','Tela','Vidrio']))),
    Field('mbn_color','string',label=T('Color')),
    #Solo lo poseen los equipos
    Field('mbn_calibrar', 'string', label = T('Requiere calibración'), requires = IS_EMPTY_OR(IS_IN_SET(['Si', 'No']))),
    Field('mbn_fecha_calibracion','date',label=T('Fecha de Calibracion'), requires = IS_EMPTY_OR(IS_DATE(format=('%d-%m-%Y')))),
    #
    Field('mbn_unidad','string',label=T('Unidad de Medida'),requires=IS_EMPTY_OR(IS_IN_SET(['cm','m']))),
    Field('mbn_ancho','double',label=T('Ancho'),requires=IS_EMPTY_OR(IS_FLOAT_IN_RANGE(0.1,999.99))),
    Field('mbn_largo','double',label=T('Largo'),requires=IS_EMPTY_OR(IS_FLOAT_IN_RANGE(0.1,999.99))),
    Field('mbn_alto','double',label=T('Alto'),requires=IS_EMPTY_OR(IS_FLOAT_IN_RANGE(0.1,999.99))),
    Field('mbn_diametro','double',label=T('Diametro'),requires=IS_EMPTY_OR(IS_FLOAT_IN_RANGE(0.1,999.99))),

    Field('mbn_movilidad','string',label=T('Movilidad'),requires=IS_EMPTY_OR(IS_IN_SET(['Fijo','Portátil']))),
    Field('mbn_uso','string',label=T('Uso'),requires=IS_EMPTY_OR(IS_IN_SET(['Docencia','Investigación','Extensión','Apoyo administrativo']))),
    Field('mbn_estatus','string',label=T('Estatus'),requires=IS_EMPTY_OR(IS_IN_SET(['Operativo','Inoperativo','En desuso','Inservible']))),
    Field('mbn_categoria', 'string', label = T('Nombre de la categoría'), requires = IS_EMPTY_OR(IS_IN_SET(['Maquinaria Construccion',
                        'Equipo Transporte', 'Equipo Comunicaciones', 'Equipo Medico', 'Equipo Cientifico Religioso', 'Equipo Oficina']))),
    Field('mbn_subcategoria', 'string', label = T('Nombre de la subcategoría')),
    Field('mbn_codigo_localizacion','string',label=T('Código de Localización'), requires=IS_EMPTY_OR(IS_IN_SET(['150301','240107']))),
    Field('mbn_localizacion','string',label=T('Localización'), requires=IS_EMPTY_OR(IS_IN_SET(['Edo Miranda, Municipio Baruta, Parroquia Baruta','Edo Vargas, Municipio Vargas, Parroquia Macuto']))),
    Field('mbn_desc', 'string', length = 140, label = T('Razon de modificación')),
    Field('mbn_modifica_ficha', 'reference auth_user', label = T('Usuario que modifica la ficha')),
    Field('mbn_motivo', 'string', length = 140, label = T('Motivo de la modificacion')),
    # Estado = -1 :Denegado
    # Estado = 0  :Por validación
    # Estado = 1  :Aceptado
    Field('estado','integer', default=0, label=T('Estado de Solicitud de Modificacion'), requires=IS_INT_IN_RANGE(-1,2))
    )

db.modificacion_bien_mueble.mbn_placa.requires = IS_EMPTY_OR(IS_NOT_IN_DB(db(db.bien_mueble.bm_placa==request.vars.mbn_placa), 'modificacion_bien_mueble.mbn_placa'))
db.modificacion_bien_mueble.mbn_num.requires = IS_IN_DB(db, db.bien_mueble.id, '%(bm_num)s')
db.modificacion_bien_mueble.mbn_modifica_ficha.requires = IS_IN_DB(db, db.auth_user, '%(first_name)s %(last_name)s | %(email)s')


#####No se implementa una tabla para datos de adquisicion#####

### Mantenimiento ###
#Hay que preguntar cuales son obligatorios
db.define_table(
    'mantenimiento',
    Field('m_NroBM', 'reference bien_mueble', unique=True, notnull=True, label = T('Número Bien Nacional')),
    #Claves
    Field('m_dependencia','reference dependencias',notnull=True,requires=IS_IN_DB(db,db.dependencias.nombre,'%(nombre)s'),label=T('Dependencia')),
    Field('m_anio','integer',unique=True,notnull=True,label=T('Año'),requires=IS_INT_IN_RANGE(1,100)),
    Field('m_num_correlativo','integer',unique=True,notnull=True,label=T('Número de registro'),requires=IS_INT_IN_RANGE(1,1000)),
    #
    Field('m_fecha','date',notnull=True,label=T('Fecha'), requires = IS_DATE(format=('%d-%m-%Y'))), ###Hay que ver el formato, se quiere dd/mm/aaaa
    Field('m_O_S','string',label=T('O/S'),requires=IS_LENGTH(8)),
    Field('m_proveedor','string',label=T('Proveedor')),
    Field('m_tipo_servicio','string',label=T('Tipo de servicio'), requires=IS_IN_SET(['Mantenimiento preventivo','Mantenimiento correctivo','Calibración','Verificación','Otro'])),
    Field('m_descripcion','text',label=T('Descripción')),
    Field('m_fecha_inicio','date',label=T('Fecha de inicio'),requires=IS_DATE(format=('%d-%m-%Y'))),
    Field('m_fecha_fin','date',label=T('Fecha de culminación'), requires=IS_DATE(format=('%d-%m-%Y'))),
    Field('m_observaciones','text',label=T('Observaciones'))
    )
db.mantenimiento.m_NroBM.requires = IS_IN_DB(db,db.bien_mueble.id,'%(first_name)s %(last_name)s | %(email)s') 

### Servicios ###
db.define_table(
    'servicio_bien_mueble',
    Field('s_NroBM', 'reference bien_mueble', unique=True, notnull=True, label = T('Número Bien Nacional')),
    Field('s_fecha','reference historial_solicitudes',notnull=True,label=T('Fecha'),requires=IS_IN_DB(db,db.historial_solicitudes.registro_solicitud,'%(registro_solicitud)s')),
    Field('s_dependencia','reference dependencias',notnull=True,requires=IS_IN_DB(db,db.dependencias.nombre,'%(nombre)s'),label=T('Dependencia')),
    Field('s_cliente_final','reference solicitudes',requires=IS_IN_DB(db,db.solicitudes.proposito_cliente_final,'%(proposito_cliente_final)s'), notnull=True,label=T('Cliente final')),
    #Fecha de inicio y fecha de culminacion deben preguntarse pues en historial de solicitudes aparecen 3 fechas
    #En servicios no se tiene nada sobre horas, hay que preguntar esto
    )
db.servicio_bien_mueble.s_NroBM.requires = IS_IN_DB(db,db.bien_mueble.id,'%(bm_num)s') 

### Tabla general para bienes muebles que no poseen numero de bien nacional ###
db.define_table(
	'sin_bn',
	Field('sb_nombre', 'string', notnull = True, label = T('Nombre del elemento')),
	Field('sb_marca', 'string', label = T('Marca del elemento')),
	Field('sb_modelo', 'string', label = T('Modelo/código del elemento')),
	Field('sb_cantidad', 'integer', notnull = True, label = T('Cantidad'), requires = IS_INT_IN_RANGE(0,99999999)),
	Field('sb_espacio', 'reference espacios_fisicos', notnull = True, label = T('Espacio físico al que pertenece')), 
	Field('sb_ubicacion', 'string', notnull = True, label = T('Ubicacion interna')),
	Field('sb_descripcion', 'text', label = T('Descripción del elemento')),
	Field('sb_aforado', 'string', label = T('Condición de aforado'), requires = IS_EMPTY_OR(IS_IN_SET(['Si', 'No', 'N/A']))),
	Field('sb_calibrar', 'string', label = T('Requiere calibración'), requires = IS_EMPTY_OR(IS_IN_SET(['Si', 'No']))),
	Field('sb_capacidad', 'string', label = T('Capacidad'), requires = IS_EMPTY_OR(IS_MATCH('^[0-9]{5},[0-9]{2}$'))),
	Field('sb_unidad', 'string', label = T('Unidad de medida de capacidad'), requires = IS_EMPTY_OR(IS_IN_SET(['m³','l','ml','μl','kg','g','mg','μg','galón','oz','cup','lb']))),
	Field('sb_unidad_dim', 'string', label = T('Unidad de medida de dimensiones'), requires = IS_EMPTY_OR(IS_IN_SET(['m', 'cm']))),
    Field('sb_ancho','double',label=T('Ancho'),requires=IS_EMPTY_OR(IS_FLOAT_IN_RANGE(0.1,999.99))),
    Field('sb_largo','double',label=T('Largo'),requires=IS_EMPTY_OR(IS_FLOAT_IN_RANGE(0.1,999.99))),
    Field('sb_alto','double',label=T('Alto'),requires=IS_EMPTY_OR(IS_FLOAT_IN_RANGE(0.1,999.99))),
    Field('sb_diametro','double',label=T('Diametro'),requires=IS_EMPTY_OR(IS_FLOAT_IN_RANGE(0.1,999.99))),
    Field('sb_material', 'string', label = T('Material predominante')),
    Field('sb_material_sec', 'string', label = T('Material secundario'), requires = IS_EMPTY_OR(IS_IN_SET(['Acero', 'Acrílico', 'Cerámica', 'Cuarzo', 'Madera',
                                                                                                        'Metal', 'Plástico', 'Tela', 'Vidrio', 'Otro']))),
   	Field('sb_presentacion', 'string', label = T('Presentación')),
	Field('sb_unidades', 'string', label = T('Unidades por presentación'), requires = IS_EMPTY_OR(IS_MATCH('^[0-9]{5}$'))),
	Field('sb_total', 'integer', label = T('Total de unidades')),
    
    Field('sb_unidad_de_adscripcion', 'reference dependencias', notnull=True, label = T('Unidad de Adscripción')),
    Field('sb_depedencia', 'reference dependencias',notnull=True, label = T('Nombre de la dependencia')),
    Field('sb_crea_ficha', 'reference auth_user', notnull = True, label = T('Usuario que crea la ficha')),
    # Estado = -1 :Denegado
    # Estado = 0  :Por validación
    # Estado = 1  :Aceptado
    # Estado = 2  :Sin solicitud
    Field('sb_eliminar','integer', default=2, label=T('Estado de Solicitud de Eliminacion'), requires=IS_INT_IN_RANGE(-1,3)),
    Field('sb_desc_eliminar', 'string', length = 140, label = T('Razon de Eliminacion')),
    Field('sb_clasificacion', 'string', notnull = True, label = T('Clasificacion del consumible/material'), requires=IS_IN_SET(['Material de Laboratorio','Consumible'])),
	# Estado = 0 : Visible
    # Estado = 1 : Oculto
    Field('sb_oculto','integer', default=0, label=T('Visibilidad del BM'), requires=IS_INT_IN_RANGE(0,2)),
    )

db.sin_bn.sb_espacio.requires = IS_IN_DB(db, db.espacios_fisicos.id,'%(codigo)s')
db.sin_bn.sb_nombre.requires=IS_NOT_IN_DB(db(db.sin_bn.sb_espacio==request.vars.sb_espacio),'sin_bn.sb_nombre')
db.sin_bn.sb_crea_ficha.requires = IS_IN_DB(db, db.auth_user, '%(first_name)s %(last_name)s | %(email)s')
db.sin_bn.sb_unidad_de_adscripcion.requires = IS_IN_DB(db, db.dependencias.id,'%(unidad_de_adscripcion)s')
db.sin_bn.sb_depedencia.requires = IS_IN_DB(db, db.dependencias.id,'%(nombre)s')


###Modificacion de muebles sin número de bien nacional###

db.define_table(
    'modificacion_sin_bn',
    #El nombre no se puede modificar, referencia al bm que se quiere cambiar
    Field('msb_nombre', 'string', notnull = True, label = T('Nombre del elemento')),
    Field('msb_marca', 'string', label = T('Marca del elemento')),
    Field('msb_modelo', 'string', label = T('Modelo/código del elemento')),
    Field('msb_cantidad', 'integer', label = T('Cantidad'), requires = IS_EMPTY_OR(IS_INT_IN_RANGE(0,99999999))),
    Field('msb_espacio', 'reference espacios_fisicos', notnull = True, label = T('Espacio físico al que pertenece')), 
    Field('msb_ubicacion', 'string', label = T('Ubicacion interna')),
    Field('msb_descripcion', 'string', label = T('Descripción del elemento')),
    Field('msb_aforado', 'string', label = T('Condición de aforado'), requires = IS_EMPTY_OR(IS_IN_SET(['Si', 'No', 'N/A']))),
    Field('msb_calibrar', 'string', label = T('Requiere calibración'), requires = IS_EMPTY_OR(IS_IN_SET(['Si', 'No']))),
    Field('msb_capacidad', 'string', label = T('Capacidad'), requires = IS_EMPTY_OR(IS_MATCH('^[0-9]{5},[0-9]{2}$'))),
    Field('msb_unidad', 'string', label = T('Unidad de medida de capacidad'), requires = IS_EMPTY_OR(IS_IN_SET(['m³','l','ml','μl','kg','g','mg','μg','galón','oz','cup','lb']))),
    Field('msb_unidad_dim', 'string', label = T('Unidad de medida de dimensiones'), requires = IS_EMPTY_OR(IS_IN_SET(['m', 'cm']))),
    Field('msb_ancho','double',label=T('Ancho'),requires=IS_EMPTY_OR(IS_FLOAT_IN_RANGE(0.1,999.99))),
    Field('msb_largo','double',label=T('Largo'),requires=IS_EMPTY_OR(IS_FLOAT_IN_RANGE(0.1,999.99))),
    Field('msb_alto','double',label=T('Alto'),requires=IS_EMPTY_OR(IS_FLOAT_IN_RANGE(0.1,999.99))),
    Field('msb_diametro','double',label=T('Diametro'),requires=IS_EMPTY_OR(IS_FLOAT_IN_RANGE(0.1,999.99))),
    Field('msb_material', 'string', label = T('Material predominante')),
    Field('msb_material_sec', 'string', label = T('Material secundario'), requires = IS_EMPTY_OR(IS_IN_SET(['Acero', 'Acrílico', 'Cerámica', 'Cuarzo', 'Madera',
                                                                                                        'Metal', 'Plástico', 'Tela', 'Vidrio', 'Otro']))),
    Field('msb_presentacion', 'string', label = T('Presentación')),
    Field('msb_unidades', 'string', label = T('Unidades por presentación'), requires = IS_EMPTY_OR(IS_MATCH('^[0-9]{5}$'))),
    Field('msb_total', 'integer', label = T('Total de unidades')),
    Field('msb_desc', 'string', length = 140, label = T('Razon de modificacion')),
    Field('msb_modifica_ficha', 'reference auth_user', notnull = True, label = T('Usuario que modifica la ficha')),
    Field('msb_motivo', 'string', length = 140, label = T('Motivo de la modificacion')),
    # Estado = -1 :Denegado
    # Estado = 0  :Por validación
    # Estado = 1  :Aceptado
    Field('estado','integer', default=0, label=T('Estado de Solicitud de Modificacion'), requires=IS_EMPTY_OR(IS_INT_IN_RANGE(-1,2)))
    )

db.modificacion_sin_bn.msb_nombre.requires =IS_IN_DB(db, db.sin_bn.id, '%(sb_nombre)s')
db.modificacion_sin_bn.msb_espacio.requires = IS_IN_DB(db, db.espacios_fisicos.id,'%(codigo)s')
#db.modificacion_sin_bn.msb_nombre.requires=IS_NOT_IN_DB(db(db.modificacion_sin_bn.msb_espacio==request.vars.msb_espacio),'modificacion_sin_bn.msb_nombre')
db.modificacion_sin_bn.msb_modifica_ficha.requires = IS_IN_DB(db, db.auth_user, '%(first_name)s %(last_name)s | %(email)s')

# Nota: Cantidad para consumibles debe tener una longitud de 4 dígitos
#		Colocar la opción de especificar dede el front para el field "prsentacion" en sin_bn y en "material" en sin_bn
# 		Calculo de la cantidad total de unidades que se hace multiplicando el número de unidades por la cantidad 
#		sb_unidad es obligatorio si se rellena sb_capacidad


###Tabla para herramientas###
db.define_table(
    'herramienta',
    Field('hr_nombre','string',notnull=True,label=T('Nombre del Bien Mueble'),requires=IS_NOT_EMPTY()),
    Field('hr_num','string',requires=IS_EMPTY_OR(IS_MATCH('^[0-9]{6}')), label = T('Número Bien Nacional')),
    Field('hr_marca','string',label=T('Marca')),
    Field('hr_modelo','string',label=T('Modelo')),
    Field('hr_serial','string',label=T('Serial')),
    #
    Field('hr_presentacion','string',notnull=True,label=T('Presentación'),requires=IS_IN_SET(['Unidad','Conjunto'])),
    Field('hr_numpiezas','string',notnull=True,label=T('Nro de piezas'),default='1',length=3),
    Field('hr_contenido','text',label=T('Contenido')),
    Field('hr_descripcion','text',label=T('Descripción de Presentación')),
    Field('hr_material','string',notnull=True,label=T('Material Predominante'), requires=IS_IN_SET(['Acero','Acrílico','Madera','Metal','Plástico','Tela','Vidrio', 'Otro'])),
    #
    Field('hr_unidad','string',label=T('Unidad de Medida'),requires=IS_EMPTY_OR(IS_IN_SET(['cm','m']))),
    Field('hr_ancho','double',label=T('Ancho'),requires=IS_EMPTY_OR(IS_FLOAT_IN_RANGE(0.1,999.99))),
    Field('hr_largo','double',label=T('Largo'),requires=IS_EMPTY_OR(IS_FLOAT_IN_RANGE(0.1,999.99))),
    Field('hr_alto','double',label=T('Alto'),requires=IS_EMPTY_OR(IS_FLOAT_IN_RANGE(0.1,999.99))),
    Field('hr_diametro','double',label=T('Diametro'),requires=IS_EMPTY_OR(IS_FLOAT_IN_RANGE(0.1,999.99))),

    Field('hr_ubicacion','string',notnull=True,label=T('Ubicacion interna'),requires=IS_NOT_EMPTY()),
    Field('hr_observacion','text',label=T('Observaciones')),
   
    Field('hr_espacio_fisico', 'reference espacios_fisicos', notnull=True, label=T('Nombre del espacio fisico')),
    Field('hr_unidad_de_adscripcion', 'reference dependencias', notnull=True, label = T('Unidad de Adscripción')),
    Field('hr_depedencia', 'reference dependencias',notnull=True, label = T('Nombre de la dependencia')),
    Field('hr_crea_ficha', 'reference auth_user', notnull = True, label = T('Usuario que crea la ficha')),
    Field('hr_desc_eliminar', 'string', length = 140, label = T('Razon de Eliminacion')),
    # Estado = -1 :Denegado
    # Estado = 0  :Por validación
    # Estado = 1  :Aceptado
    # Estado = 2  :Sin solicitud
    Field('hr_eliminar','integer', default=2, label=T('Estado de Solicitud de Eliminacion'), requires=IS_INT_IN_RANGE(-1,3)),
    # Estado = 0 : Visible
    # Estado = 1 : Oculto
    Field('hr_oculto','integer', default=0, label=T('Visibilidad del BM'), requires=IS_INT_IN_RANGE(0,2)),
    )

db.herramienta.hr_num.requires = IS_EMPTY_OR(IS_NOT_IN_DB(db(db.herramienta.hr_num==request.vars.hr_num), 'herramienta.hr_num'))
db.herramienta.hr_nombre.requires=IS_NOT_IN_DB(db(db.herramienta.hr_ubicacion==request.vars.hr_ubicacion and db.herramienta.hr_espacio_fisico==request.vars.hr_espacio_fisico),'herramienta.hr_nombre')
db.herramienta.hr_crea_ficha.requires = IS_IN_DB(db, db.auth_user, '%(first_name)s %(last_name)s | %(email)s')
db.herramienta.hr_espacio_fisico.requires = IS_IN_DB(db, db.espacios_fisicos.id,'%(codigo)s')
db.herramienta.hr_unidad_de_adscripcion.requires = IS_IN_DB(db, db.dependencias.id,'%(unidad_de_adscripcion)s')
db.herramienta.hr_depedencia.requires = IS_IN_DB(db, db.dependencias.id,'%(nombre)s')

db.define_table(
	'modificacion_herramienta',
    Field('mhr_nombre','string',label=T('Nombre del Bien Mueble'),requires=IS_NOT_EMPTY()),
    Field('mhr_num','string',requires=IS_EMPTY_OR(IS_MATCH('^[0-9]{6}')), label = T('Número Bien Nacional')),
    #
    Field('mhr_marca','string',label=T('Marca')),
    Field('mhr_modelo','string',label=T('Modelo')),
    Field('mhr_serial','string',label=T('Serial')),
    #
    Field('mhr_presentacion','string',label=T('Presentación'),requires=IS_IN_SET(['Unidad','Conjunto'])),
    Field('mhr_numpiezas','string',label=T('Nro de piezas'),default='1',length=3),
    Field('mhr_contenido','text',label=T('Contenido')),
    Field('mhr_descripcion','text',label=T('Descripción de Presentación')),
    Field('mhr_material','string',label=T('Material Predominante'), requires=IS_IN_SET(['Acero','Acrílico','Madera','Metal','Plástico','Tela','Vidrio', 'Otro'])),
    #
    Field('mhr_unidad','string',label=T('Unidad de Medida'),requires=IS_EMPTY_OR(IS_IN_SET(['cm','m']))),
    Field('mhr_ancho','double',label=T('Ancho'),requires=IS_EMPTY_OR(IS_FLOAT_IN_RANGE(0.1,999.99))),
    Field('mhr_largo','double',label=T('Largo'),requires=IS_EMPTY_OR(IS_FLOAT_IN_RANGE(0.1,999.99))),
    Field('mhr_alto','double',label=T('Alto'),requires=IS_EMPTY_OR(IS_FLOAT_IN_RANGE(0.1,999.99))),
    Field('mhr_diametro','double',label=T('Diametro'),requires=IS_EMPTY_OR(IS_FLOAT_IN_RANGE(0.1,999.99))),

    Field('mhr_ubicacion','string',label=T('Ubicacion interna'),requires=IS_NOT_EMPTY()),
    Field('mhr_observacion','text',label=T('Observaciones')),
   
    Field('mhr_espacio_fisico', 'reference espacios_fisicos', label=T('Nombre del espacio fisico')),
    Field('mhr_unidad_de_adscripcion', 'reference dependencias', label = T('Unidad de Adscripción')),
    Field('mhr_depedencia', 'reference dependencias', label = T('Nombre de la dependencia')),
    Field('mhr_crea_ficha', 'reference auth_user', label = T('Usuario que crea la ficha')),
    Field('mhr_modifica_ficha', 'reference auth_user', notnull = True, label = T('Usuario que modifica la ficha')),
    Field('mhr_motivo', 'string', length = 140, label = T('Motivo de la modificacion')),
    # Estado = -1 :Denegado
    # Estado = 0  :Por validación
    # Estado = 1  :Aceptado
    Field('mhr_estado','integer', default=0, label=T('Estado de Solicitud de Modificacion'), requires=IS_EMPTY_OR(IS_INT_IN_RANGE(-1,2)))
	)
db.modificacion_herramienta.mhr_ubicacion.requires = IS_NOT_IN_DB(db(db.herramienta.hr_nombre==request.vars.mhr_nombre and db.herramienta.hr_espacio_fisico==request.vars.mhr_espacio_fisico),'modificacion_herramienta.mhr_ubicacion')
db.modificacion_herramienta.mhr_modifica_ficha.requires = IS_IN_DB(db, db.auth_user, '%(first_name)s %(last_name)s | %(email)s')
db.modificacion_herramienta.mhr_espacio_fisico.requires = IS_IN_DB(db, db.espacios_fisicos.id,'%(codigo)s')
db.modificacion_herramienta.mhr_unidad_de_adscripcion.requires = IS_IN_DB(db, db.dependencias.id,'%(unidad_de_adscripcion)s')
db.modificacion_herramienta.mhr_depedencia.requires = IS_IN_DB(db, db.dependencias.id,'%(nombre)s')
db.modificacion_herramienta.mhr_num.requires = IS_EMPTY_OR(IS_NOT_IN_DB(db(db.herramienta.hr_num==request.vars.hr_num), 'herramienta.hr_num'))

db.define_table(
    'historial_mantenimiento_bm',
    Field('hmbm_nro', 'references bien_mueble', label = T('Numero de bien nacional')),
    Field('hmbm_fecha_sol', 'date', notnull = True, label = T('Fecha de solicitud')),
    Field('hmbm_codigo', 'string', label = T('Codigo de Solicitud')),
    Field('hmbm_tipo', 'string', notnull = True, label = T('Tipo de Mantenimiento'), requires = IS_IN_SET(['Correctivo', 'Predictivo', 'Preventivo'])),
    Field('hmbm_servicio', 'string', notnull = True, label = T('Servicio Ejecutado'),requires = IS_IN_SET(['Ajuste', 'Calibración', 'Inspección','Limpieza','Reparación','Sustitución de Partes','Verificación','Otro'])),
    Field('hmbm_accion', 'string', notnull = True, label = T('Acción'),requires = IS_IN_SET(['Periódica', 'Extraordinaria', 'Urgente'])),
    Field('hmbm_descripcion', 'string', notnull = True, label = T('Motivo de ejecución, desperfecto o falla.')),
    Field('hmbm_proveedor', 'string', notnull = True, label = T('Proveedor del servicio')),
    Field('hmbm_fecha_inicio', 'date', notnull = True, label = T('Fecha de inicio')),
    Field('hmbm_fecha_fin', 'date', notnull = True, label = T('Fecha de culminación')),
    Field('hmbm_tiempo_ejec', 'integer', notnull = True, label = T('Tiempo de ejecución')),
    Field('hmbm_fecha_cert', 'date', notnull = True, label = T('Fecha de certificación')),
    Field('hmbm_observacion', 'text', label = T('Observaciones'))
    )

db.historial_mantenimiento_bm.hmbm_nro.requires = IS_IN_DB(db, db.bien_mueble.id, '%(bm_num)s')

db.define_table(
    'historial_mantenimiento_sin_bn',
    Field('hmsb_espacio_fisico', 'references espacios_fisicos', label = T('Espacio fisico')),
    Field('hmsb_nombre', 'references sin_bn', label = T('Nombre del consumible o material de laboratorio')),
    Field('hmsb_fecha_sol', 'date', notnull = True, label = T('Fecha de solicitud')),
    Field('hmsb_codigo', 'string', label = T('Codigo de Solicitud')),
    Field('hmsb_tipo', 'string', notnull = True, label = T('Tipo de Mantenimiento'), requires = IS_IN_SET(['Correctivo', 'Predictivo', 'Preventivo'])),
    Field('hmsb_servicio', 'string', notnull = True, label = T('Servicio Ejecutado')),
    Field('hmsb_accion', 'string', notnull = True, label = T('Acción'),requires = IS_IN_SET(['Periódica', 'Extraordinaria', 'Urgente'])),
    Field('hmsb_descripcion', 'string', notnull = True, label = T('Motivo de ejecución, desperfecto o falla.')),
    Field('hmsb_proveedor', 'string', notnull = True, label = T('Proveedor del servicio')),
    Field('hmsb_fecha_inicio', 'date', notnull = True, label = T('Fecha de inicio')),
    Field('hmsb_fecha_fin', 'date', notnull = True, label = T('Fecha de culminación')),
    Field('hmsb_tiempo_ejec', 'integer', notnull = True, label = T('Tiempo de ejecución')),
    Field('hmsb_fecha_cert', 'date', notnull = True, label = T('Fecha de certificación')),
    Field('hmsb_observacion', 'text', label = T('Observaciones'))
    )

db.historial_mantenimiento_sin_bn.hmsb_espacio_fisico.requires = IS_IN_DB(db, db.sin_bn.id, '%(sb_espacio)s')
db.historial_mantenimiento_sin_bn.hmsb_nombre.requires = IS_IN_DB(db, db.sin_bn.id, '%(sb_nombre)s')

###Vehiculo###
db.define_table(
    'vehiculo',
    # Datos de identificación
    Field('vh_num', 'string', notnull=True, unique=True, requires=IS_MATCH('^[0-9]{6}'), label=T('Número Bien Nacional')),
    Field('vh_propietario', 'string', notnull=True, label=T('Nombre del propietario'), requires=IS_NOT_EMPTY()),
    Field('vh_marca', 'string', notnull=True, label=T('Marca del Vehículo'), requires=IS_NOT_EMPTY()),
    Field('vh_modelo', 'string', notnull=True, label=T('Modelo del Vehículo'), requires=IS_NOT_EMPTY()),
    Field('vh_ano', 'integer', notnull=True, label=T('Año del Vehículo'), requires=IS_NOT_EMPTY()),
    Field('vh_serial_motor', 'string', notnull=True, unique=True, label = T('Serial del Motor'), requires =IS_NOT_EMPTY()),
    Field('vh_serial_carroceria', 'string', notnull=True, unique=True, label = T('Serial de Carrocería'), requires =IS_NOT_EMPTY()),
    Field('vh_serial_chasis', 'string', notnull=True, unique=True, label = T('Serial de Chasis'), requires=[IS_NOT_EMPTY(), IS_LENGTH(17)]),
    Field('vh_placa', 'string', notnull=True, unique=True, label=T('Placa del Vehículo'), requires=IS_NOT_EMPTY()),
    Field('vh_intt', 'string', notnull=True, unique=True, label=T('Nº. Autorización INTT')),
    Field('vh_sede', 'string', notnull=True, default="Sartenejas", label=T('Sede de adscripción'), requires=IS_IN_SET(['Sartenejas', 'Litoral'])),

    # Descripción de uso
    Field('vh_observaciones', 'text', default="", label=T('Observaciones')),
    Field('vh_lugar_pernocta', 'string', notnull=True, default="", label=T('Lugar de pernocta')),
    Field('vh_color', 'string', label=T('Color')),

    # Categorias
    Field('vh_clase', 'string', notnull=True, label=T('Clase')),
    Field('vh_tipo', 'string', notnull=True, label=T('Tipo')),
    Field('vh_clasificacion', 'string', notnull=True, label=T('Clasificación')),
    Field('vh_uso', 'string', notnull=True, label=T('Uso'), requires=IS_IN_SET(['Público', 'Privado'])),
    Field('vh_servicio', 'string', notnull=True, label=T('Servicio')),
    
    Field('vh_tara', 'double', label=T('Tara')),
    Field('vh_tara_md', 'string', default="kg", label=T('Tara (medida)'), requires=IS_IN_SET(['kg', 'ton'])),

    # Capacidades
    Field('vh_nro_puestos', 'integer', notnull=True, default=0, label = T('Nº de Puestos'), requires=IS_MATCH('^[0-9]{2}')),
    Field('vh_nro_ejes', 'integer', default=0, label = T('Nº de Ejes')),
    Field('vh_capacidad_carga', 'double', default=0, label = T('Capacidad de Carga')),
    Field('vh_capacidad_carga_md', 'string', default="kg", label=T('Capacidad de Carga (medida)'), requires=IS_IN_SET(['kg', 'ton'])),

    Field('vh_rines', 'string', default="", label=T('Rines')),

    # Datos del responsable
    # PENDIENTE: Referenciar usuarios de la BD aquí
    Field('vh_responsable', 'string', notnull=True, label=T('Nombre del responsable patrimonial'), requires=IS_NOT_EMPTY()),
    Field('vh_telf_responsable', 'string', label=T('Número de teléfono del responsable patrimonial'), requires=[IS_NOT_EMPTY(), IS_MATCH('^(0[0-9]{3}) [0-9]{3}-[0-9]{4}')]),
    Field('vh_custodio', 'string', notnull=True, defaut="", label=T('Nombre del custodio'), requires=IS_NOT_EMPTY()),
    Field('vh_ubicacion_custodio', 'string', notnull=True, defaut="", label=T('Ubicación del custodio'), requires=IS_NOT_EMPTY()),
    Field('vh_telf_custodio', 'string', default="", label=T('Número de teléfono del custodio'), requires=[IS_NOT_EMPTY(), IS_MATCH('^(0[0-9]{3}) [0-9]{3}-[0-9]{4}')]),
    Field('vh_extension', 'integer', default=0, label=T('Extensión de teléfono del custodio'), requires=IS_MATCH('^[0-9]{4}')),


    # Datos SUDEBIP
    Field('vh_sudebip_localizacion', 'string', notnull=True, label=T('SUDEBIP: Localización')),
    Field('vh_sudebip_codigo_localizacion', 'string', notnull=True, default="", label=T('SUDEBIP: Código de Localización')),
    Field('vh_sudebip_categoria', 'string', notnull=True, default="(15000-0000) Equipos de transporte, tracción y elevación", label=T('SUDEBIP: Categoría')),
    Field('vh_sudebip_subcategoria', 'string', notnull=True, label=T('SUDEBIP: Subcategoría')),
    Field('vh_sudebip_categoria_especifica', 'string', notnull=True, label=T('SUDEBIP: Categoría específica')),

    # Datos Adquisición
    Field('vh_fecha_adquisicion', 'date', notnull=True, label=T('Fecha de adquisición')),
    Field('vh_origen', 'string', notnull=True, default="", label=T('Origen'), requires=IS_IN_SET(['Compra', 'Donación'])),
    Field('vh_nro_factura', 'string', default="", label=T('Número de Factura')),
    Field('vh_fecha_factura', 'date', label=T('Fecha de Factura')),
    Field('vh_nro_oficio', 'string', default="", label=T('Número de Oficio')),
    Field('vh_proveedor', 'string', default="", label=T('Proveedor')),
    Field('vh_proveedor_rif', 'string', default="", label=T('RIF del Proveedor')),
    Field('vh_nro_donacion', 'integer', label=T('Nº Donación')),
    Field('vh_donante', 'string', default="", label=T('Donante')),
    Field('vh_contacto_donante', 'string', default="", label=T('Contacto del donante'), requires=IS_MATCH('^[-()+0-9]*')),

    # Estatus de préstamo o mantenimiento
    Field('vh_estatus', 'string', label=T('Estatus'), default='Disponible', requires=IS_IN_SET(['Disponible','En préstamo','En mantenimiento','En uso','Averiado'])),

    # Estado = 0 : No es particular
    # Estado = 1 : Es particular
    Field('vh_es_particular', 'integer', default=0, label=T('Vehículo particular'), requires=IS_INT_IN_RANGE(0,2)),

    # Estado = 0 : Visible
    # Estado = 1 : Oculto
    Field('vh_oculto', 'integer', default=0, label=T('Visibilidad del vehículo'), requires=IS_INT_IN_RANGE(0,2)),

    # Foráneas
    Field('vh_dependencia', 'reference dependencias', notnull=True, label = T('Nombre de la dependencia asociada')),
    Field('vh_crea_ficha', 'reference auth_user', notnull = True, label = T('Usuario que crea la ficha')),

    # Eliminación
    # Estado = -1 :Denegado
    # Estado = 0  :Por validación
    # Estado = 1  :Aceptado
    # Estado = 2  :Sin solicitud
    Field('vh_eliminar','integer', default=2, label=T('Estado de Solicitud de Eliminacion'), requires=IS_INT_IN_RANGE(-1,3)),
    Field('vh_desc_eliminar', 'string', length = 140, label = T('Razon de Eliminacion')),
    )
    
db.vehiculo.vh_crea_ficha.requires = IS_IN_DB(db, db.auth_user, '%(first_name)s %(last_name)s | %(email)s')
db.vehiculo.vh_dependencia.requires = IS_IN_DB(db, db.dependencias.id,'%(nombre)s')

db.define_table(
    'modificacion_vehiculo',
    # Datos de identificación
    Field('mvh_marca', 'string', notnull=True, label=T('Marca del Vehículo'), requires=IS_NOT_EMPTY()),
    Field('mvh_modelo', 'string', notnull=True, label=T('Modelo del Vehículo'), requires=IS_NOT_EMPTY()),
    Field('mvh_ano', 'integer', notnull=True, label=T('Año del Vehículo'), requires=IS_NOT_EMPTY()),
    Field('mvh_serial_motor','string', notnull=True, unique=True, label = T('Serial del Motor'), requires =IS_NOT_EMPTY()),
    Field('mvh_serial_carroceria', 'string', notnull=True, unique=True, label = T('Serial de Carrocería'), requires =IS_NOT_EMPTY()),
    Field('mvh_placa','string', notnull=True, unique=True, label=T('Placa del Vehículo'), requires=IS_NOT_EMPTY()),
    Field('mvh_intt', 'string', notnull=True, unique=True, label=T('Nº. Autorización INTT')),
    Field('mvh_sede', 'string', notnull=True, default="Sartenejas", label=T('Sede de adscripción'), requires=IS_IN_SET(['Sartenejas', 'Litoral'])),

    # Descripción de uso
    Field('mvh_descripcion','text', notnull=True, default="", label=T('Descripción')),
    Field('mvh_lugar_pernocta','string', notnull=True, default="", label=T('Lugar de pernocta')),
    Field('mvh_color', 'string', label=T('Color')),

    # Categorias
    Field('mvh_clase', 'string', notnull=True, label=T('Clase')),
    Field('mvh_uso', 'string', notnull=True, label=T('Uso')),
    Field('mvh_servicio', 'string', notnull=True, label=T('Servicio')),
    Field('mvh_tara', 'string', label=T('Tara')),

    # Capacidades
    Field('mvh_nro_puestos', 'integer', notnull=True, default=0, label = T('Nº de Puestos')),
    Field('mvh_nro_ejes', 'integer', notnull=True, default=0, label = T('Nº de Ejes')),
    Field('mvh_capacidad_carga', 'double', notnull=True, default=0, label = T('Capacidad de Carga')),

    # Datos del responsable
    # PENDIENTE: Referenciar usuarios de la BD aquí
    Field('mvh_propietario', 'string', notnull=True, label=T('Nombre del propietario'), requires=IS_NOT_EMPTY()),
    Field('mvh_responsable', 'string', notnull=True, label=T('Nombre del responsable patrimonial'), requires=IS_NOT_EMPTY()),
    Field('mvh_telf_responsable', 'string', notnull=True, label=T('Número de teléfono del responsable patrimonial'), requires=[IS_NOT_EMPTY(), IS_MATCH('^[-()+0-9]*')]),
    Field('mvh_custodio', 'string', notnull=True, defaut="", label=T('Nombre del custodio'), requires=IS_NOT_EMPTY()),
    Field('mvh_telf_custodio', 'string', notnull=True, default="", label=T('Número de teléfono del custodio'), requires=[IS_NOT_EMPTY(), IS_MATCH('^[-()+0-9]*')]),
    
     # Datos SUDEBIP
    Field('mvh_sudebip_localizacion', 'string', notnull=True, label=T('SUDEBIP: Localización')),
    Field('mvh_sudebip_codigo_localizacion', 'string', notnull=True, default="", label=T('SUDEBIP: Código de Localización')),
    Field('mvh_sudebip_categoria', 'string', notnull=True, label=T('SUDEBIP: Categoría')),
    Field('mvh_sudebip_subcategoria', 'string', notnull=True, label=T('SUDEBIP: Subcategoría')),
    Field('mvh_sudebip_categoria_especifica', 'string', notnull=True, label=T('SUDEBIP: Categoría específica')),
   
   # Datos Adquisición
    Field('mvh_fecha_adquisicion', 'date', notnull=True, label=T('Fecha de adquisición')),
    Field('mvh_origen', 'string', notnull=True, default="", label=T('Origen'), requires=IS_IN_SET(['Compra', 'Donación'])),
    Field('mvh_nro_factura', 'string', label=T('Número de Factura')),
    Field('mvh_fecha_factura', 'date', label=T('Fecha de Factura')),
    Field('mvh_nro_oficio', 'string', label=T('Número de Oficio')),
    Field('mvh_proveedor', 'string', label=T('Proveedor')),
    Field('mvh_proveedor_rif', 'string', label=T('RIF del Proveedor')),
    Field('mvh_nro_donacion', 'integer', label=T('Nº Donación')),
    Field('mvh_donante', 'string', label=T('Donante')),
    Field('mvh_contacto_donante', 'string', label=T('Contacto del donante'), requires=IS_MATCH('^[-()+0-9]*')),

    # Estatus de préstamo o mantenimiento
    Field('mvh_estatus', 'string',label=T('Estatus'), default='Disponible', requires=IS_IN_SET(['Disponible', 'En préstamo', 'En mantenimiento','En uso','Averiado'])),

    # Estado = 0 : No es particular
    # Estado = 1 : Es particular
    Field('mvh_es_particular','integer', default=0, label=T('Vehículo particular'), requires=IS_INT_IN_RANGE(0,2)),

    # Estado = 0 : Visible
    # Estado = 1 : Oculto
    Field('mvh_oculto','integer', default=0, label=T('Visibilidad del vehículo'), requires=IS_INT_IN_RANGE(0,2)),

    # Foráneas
    Field('mvh_dependencia', 'reference dependencias', notnull=True, label = T('Nombre de la dependencia asociada')),
    Field('mvh_modifica_ficha', 'reference auth_user', notnull = True, label = T('Usuario que modifica la ficha')),
    Field('mvh_motivo', 'string', length = 140, label = T('Motivo de la modificacion')),
    # Estado = -1 :Denegado
    # Estado = 0  :Por validación
    # Estado = 1  :Aceptado
    Field('mvh_estado','integer', default=0, label=T('Estado de Solicitud de Modificacion'), requires=IS_EMPTY_OR(IS_INT_IN_RANGE(-1,2)))
    )

db.modificacion_vehiculo.mvh_modifica_ficha.requires = IS_IN_DB(db, db.auth_user, '%(first_name)s %(last_name)s | %(email)s')
db.modificacion_vehiculo.mvh_dependencia.requires = IS_IN_DB(db, db.dependencias.id,'%(nombre)s')
# PENDIENTE: Verificar la siguiente restriccion
db.modificacion_vehiculo.mvh_placa.requires = IS_IN_DB(db, db.vehiculo.vh_placa, '%(vh_placa)s')

db.define_table(
    'historial_mantenimiento_vh',
    Field('hmvh_placa', 'references vehiculo', label = T('Placa del vehiculo')),
    Field('hmvh_fecha_sol', 'date', notnull = True, label = T('Fecha de solicitud')),
    Field('hmvh_codigo', 'string', label = T('Codigo de Solicitud')),
    Field('hmvh_tipo', 'string', notnull = True, label = T('Tipo de Mantenimiento'), requires = IS_IN_SET(['Correctivo', 'Predictivo', 'Preventivo'])),
    Field('hmvh_servicio', 'string', notnull = True, label = T('Servicio Ejecutado'),requires = IS_IN_SET(['Ajuste', 'Calibración', 'Inspección','Limpieza','Reparación','Sustitución de Partes','Verificación','Otro'])),
    Field('hmvh_accion', 'string', notnull = True, label = T('Acción'),requires = IS_IN_SET(['Periódica', 'Extraordinaria', 'Urgente'])),
    Field('hmvh_descripcion', 'string', notnull = True, label = T('Motivo de ejecución, desperfecto o falla.')),
    Field('hmvh_proveedor', 'string', notnull = True, label = T('Proveedor del servicio')),
    Field('hmvh_fecha_inicio', 'date', notnull = True, label = T('Fecha de inicio')),
    Field('hmvh_fecha_fin', 'date', notnull = True, label = T('Fecha de culminación')),
    Field('hmvh_tiempo_ejec', 'integer', notnull = True, label = T('Tiempo de ejecución')),
    Field('hmvh_fecha_cert', 'date', notnull = True, label = T('Fecha de certificación')),
    Field('hmvh_observacion', 'text', label = T('Observaciones')),
    Field('hmvh_responsable', 'string', label = T('Responsable de mantenimiento')),
    Field('hmvh_crea_mantenimiento', 'reference auth_user', notnull = True, label = T('Usuario que crea la entrada de mantenimiento')),
    )

# PENDIENTE: Verificar la siguiente restriccion
db.historial_mantenimiento_vh.hmvh_placa.requires = IS_IN_DB(db, db.vehiculo.vh_placa, '%(vh_placa)s')
db.historial_mantenimiento_vh.hmvh_crea_mantenimiento.requires = IS_IN_DB(db, db.auth_user, '%(first_name)s %(last_name)s | %(email)s')