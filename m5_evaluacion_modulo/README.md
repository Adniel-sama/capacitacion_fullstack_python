# Sistema de Gestión de Inventario – Documentación del Proyecto

## Descripción General
Este proyecto implementa un sistema de gestión de inventario utilizando un modelo de base de datos relacional. Su finalidad es registrar, consultar y administrar productos, proveedores y transacciones mediante instrucciones SQL, manteniendo integridad y consistencia en los datos.

## Modelo de Datos
El sistema se basa en tres entidades principales: productos, proveedores y transacciones. Se desarrolló un modelo Entidad–Relación que posteriormente se tradujo al modelo relacional, incorporando claves primarias, claves foráneas, restricciones de integridad, controles de nulidad y selección de tipos de datos adecuados.

## Implementación SQL
El script SQL incluye:

- Creación de tablas con restricciones (PK, FK, UNIQUE, NOT NULL, CHECK).
- Inserción, actualización y eliminación de registros.
- Consultas básicas y consultas con agregaciones.
- Consultas utilizando operaciones JOIN entre las tablas principales.

También se incorpora el cálculo y ajuste del inventario según las transacciones registradas.

## Manejo de Transacciones
Se emplearon transacciones SQL para asegurar la atomicidad en operaciones críticas. Se utilizaron instrucciones como `START TRANSACTION`, `COMMIT` y `ROLLBACK` para garantizar consistencia en caso de errores.

## Normalización
El diseño aplicado sigue los principios de normalización hasta Tercera Forma Normal (3NF), evitando redundancia y posibles anomalías de actualización. No se requirió desnormalización dada la naturaleza del sistema.

## Documentación y Archivos
El proyecto incluye:
- Archivo del modelo ER en formato `.mwb`.
- Archivo SQL con la creación de tablas, operaciones DML y consultas.
- Archivo README con una descripción general del proyecto.
