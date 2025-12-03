-- ### Evaluación del módulo ###

-- ## Objetivo ##

-- El objetivo de esta actividad es que puedas diseñar y desarrollar un sistema de gestión de inventario para una empresa que utiliza una base de datos relacional para almacenar y consultar información sobre productos, proveedores y transacciones. Además, aprenderás cómo manejar transacciones, restricciones de integridad referencial, y consultas complejas utilizando SQL.

-- ## Contexto ##

-- En una empresa de ventas, es necesario gestionar un inventario de productos que se van almacenando en diferentes proveedores, y a su vez, realizar transacciones de compra y venta. Para esto, se utiliza una base de datos relacional (RDBMS) para organizar toda la información de manera estructurada. El sistema debe permitir agregar productos, actualizar el inventario, registrar compras y ventas, y consultar los datos de manera eficiente.

-- 1. Diseño del Modelo Relacional
--     ○ Crea un modelo de datos para representar la siguiente información:
--         ■ Productos: nombre, descripción, precio, cantidad en inventario.
--         ■ Proveedores: nombre, dirección, teléfono, email.
--         ■ Transacciones: tipo (compra o venta), fecha, cantidad, id de producto, id de proveedor.
--     ○ Utiliza el modelo Entidad-Relación (ER) para abstraer las entidades y sus relaciones, y luego tradúcelas al modelo relacional.
--     ○ Asegúrate de identificar claves primarias y foráneas para establecer la integridad referencial entre las tablas.
        -- (archivo mwb)
-- 2. Creación de la Base de Datos y Tablas    
--     ○ Utiliza SQL para crear las tablas `productos`, `proveedores` y `transacciones` en la base de datos.
--     ○ Define las restricciones de nulidad, llaves primarias y llaves foráneas para garantizar la integridad de los datos.
--     ○ Establece el tipo de dato adecuado para cada atributo (por ejemplo, `VARCHAR`, `INT`, `DECIMAL`).

CREATE DATABASE IF NOT EXISTS M5_evaluacion_modulo;
USE M5_evaluacion_modulo;

-- Proveedores
CREATE TABLE proveedores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(200) NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    email VARCHAR(120) NOT NULL,
    UNIQUE (direccion, telefono, email)
);

-- Productos
CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(250),
    precio DECIMAL(10,2) NOT NULL,
    cantidad_inventario INT NOT NULL
);

-- Transacciones
CREATE TABLE transacciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo ENUM('compra', 'venta') NOT NULL,
    fecha DATE NOT NULL,
    cantidad INT NOT NULL,
    id_producto INT NOT NULL,
    id_proveedor INT,

    FOREIGN KEY (id_producto) REFERENCES productos(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,

    FOREIGN KEY (id_proveedor) REFERENCES proveedores(id)
        ON UPDATE CASCADE
        ON DELETE SET NULL
);  
            -- ******Por orden lógico, primero se hará el punto 4 antes del 3
-- 4. Manipulación de Datos (DML) 
--     ○ Inserta datos en las tablas `productos`, `proveedores` y `transacciones`.

-- PROVEEDORES
INSERT INTO proveedores (nombre, direccion, telefono, email)
VALUES
('TechSupply Ltda', 'Av. Central 123', '987654321', 'contacto@techsupply.com'),
('ElectroniChile', 'Calle Norte 45', '956321478', 'ventas@electronichile.cl'),
('GlobalParts Inc', 'Ruta 5 Sur Km 240', '945123789', 'info@globalparts.com');

--  PRODUCTOS
INSERT INTO productos (nombre, descripcion, precio, cantidad_inventario)
VALUES
('Notebook Lenovo', 'Notebook 14 pulgadas, 8GB RAM', 520000, 15),
('Impresora HP 2135', 'Impresora multifunción color', 45000, 30),
('Smartphone Samsung A10', 'Pantalla 6.0 pulgadas, 32GB', 120000, 20),
('Teclado Mecánico Redragon', 'Switch Blue, iluminación RGB', 35000, 40),
('Mouse Logitech M185', 'Mouse inalámbrico óptico', 12000, 50);

-- INSERTAR TRANSACCIONES
INSERT INTO transacciones (tipo, fecha, cantidad, id_producto, id_proveedor)
VALUES
('venta',  '2025-01-10', 2, 1, 1),
('compra', '2025-01-12', 10, 2, 2),
('venta',  '2025-01-15', 1, 3, 3),
('compra', '2025-02-05', 20, 4, 1),
('venta',  '2025-02-15', 50, 5, 2);

--     ○ Actualiza la cantidad de inventario de un producto después de una venta o compra.

-- Actualizar inventario según transacciones
SET SQL_SAFE_UPDATES = 0;

UPDATE productos
SET cantidad_inventario = cantidad_inventario
    + (
        SELECT COALESCE(SUM(cantidad), 0)
        FROM transacciones
        WHERE transacciones.id_producto = productos.id
        AND tipo = 'compra'
      )
    - (
        SELECT COALESCE(SUM(cantidad), 0)
        FROM transacciones
        WHERE transacciones.id_producto = productos.id
        AND tipo = 'venta'
      );


--     ○ Elimina un producto de la base de datos si ya no está disponible.

SELECT id, nombre, cantidad_inventario -- Buscamos si hay productos con 0 inventario
FROM productos
WHERE cantidad_inventario <= 0;

DELETE FROM productos -- Se elimina el 5 por estar sin stock
WHERE id = 5;

--     ○ Asegúrate de aplicar integridad referencial al actualizar o eliminar registros relacionados.

-- Al hacer las tablas se considero "ON DELETE CASCADE"

-- 3. Consultas Básicas

--     ○ Realiza consultas básicas utilizando el lenguaje SQL:
        
--         ■ Recupera todos los productos disponibles en el inventario.
SELECT *
FROM productos;
--         ■ Recupera todos los proveedores que suministran productos específicos.
SELECT DISTINCT proveedores.*
FROM proveedores
JOIN transacciones ON transacciones.id_proveedor = proveedores.id
WHERE transacciones.id_producto = 2
AND transacciones.tipo = 'compra';
--         ■ Consulta las transacciones realizadas en una fecha específica.
SELECT *
FROM transacciones
WHERE fecha = '2025-02-15';
--         ■ Realiza consultas de selección con funciones de agrupación, como `COUNT()` y `SUM()`, para calcular el número total de productos vendidos o el valor total de las compras.
SELECT SUM(cantidad) AS total_productos_vendidos
FROM transacciones
WHERE tipo = 'venta';

SELECT tipo, COUNT(*) AS cantidad
FROM transacciones
GROUP BY tipo;
        
-- 5. Transacciones SQL
    
--     ○ Realiza una transacción para registrar una compra de productos. Utiliza el comando `BEGIN TRANSACTION`, `COMMIT` y `ROLLBACK` para asegurar que los cambios se apliquen correctamente.

--     ○ Asegúrate de que los cambios en la cantidad de inventario y las transacciones se realicen de forma atómica.
        
--     ○ Utiliza el modo `AUTOCOMMIT` para manejar operaciones individuales si es necesario.
        
START TRANSACTION;

-- Registrar la transacción
INSERT INTO transacciones (tipo, fecha, cantidad, id_producto, id_proveedor)
VALUES ('compra', '2025-03-01', 15, 3, 1);

-- Actualizar el inventario
UPDATE productos
SET cantidad_inventario = cantidad_inventario + 15
WHERE id = 3; 

-- Confirmar
COMMIT;

START TRANSACTION;
 
-- Inserción válida
INSERT INTO transacciones (tipo, fecha, cantidad, id_producto, id_proveedor)
VALUES ('compra', '2025-03-10', 10, 1, 1);

-- Inserción incorrecta: id_producto = 999 NO EXISTE 

INSERT INTO transacciones (tipo, fecha, cantidad, id_producto, id_proveedor)
VALUES ('compra', '2025-03-10', 25, 999, 1);

ROLLBACK;
        
-- 6. Consultas Complejas
    
--     ○ Realiza una consulta que recupere el total de ventas de un producto durante el mes anterior.

SELECT 
    productos.nombre AS nombre_producto,
    SUM(transacciones.cantidad) AS total_vendido
FROM transacciones
INNER JOIN productos
    ON transacciones.id_producto = productos.id
WHERE transacciones.tipo = 'venta'
    AND MONTH(transacciones.fecha) = MONTH(CURRENT_DATE - INTERVAL 1 MONTH)
    AND YEAR(transacciones.fecha) = YEAR(CURRENT_DATE - INTERVAL 1 MONTH)
    AND productos.id = 3
GROUP BY productos.nombre;

--     ○ Utiliza JOINs (INNER, LEFT) para obtener información relacionada entre las tablas `productos`, `proveedores` y `transacciones`.
SELECT 
    transacciones.id AS id_transaccion,
    transacciones.tipo,
    transacciones.fecha,
    transacciones.cantidad,
    productos.nombre AS nombre_producto,
    proveedores.nombre AS nombre_proveedor
FROM transacciones
LEFT JOIN productos 
    ON transacciones.id_producto = productos.id
LEFT JOIN proveedores
    ON transacciones.id_proveedor = proveedores.id;

--     ○ Implementa una consulta con subconsultas (subqueries) para obtener productos que no se han vendido durante un período determinado.
SELECT productos.*
FROM productos
LEFT JOIN transacciones
    ON productos.id = transacciones.id_producto
    AND transacciones.tipo = 'venta'
    AND transacciones.fecha BETWEEN '2025-01-01' AND '2025-02-28'
WHERE transacciones.id IS NULL;

-- 7. Normalización y Desnormalización
    
--     ○ Asegúrate de que las tablas estén normalizadas hasta la tercera forma normal (3NF) para evitar redundancias y asegurar la integridad de los datos.
		-- Las tablas están normalizadas desde el diseño
--     ○ Si es necesario, discute en tu informe los casos en los que la desnormalización podría ser útil para mejorar el rendimiento de las consultas.
        -- En este caso, no creo que sea necesario, podría ser útil si sólo se enfocara en las ventas o una situación similar
-- 8. Manejo de restricciones
    
--     ○ Implementa restricciones en los campos de las tablas para garantizar que los datos ingresados sean válidos (por ejemplo, asegurando que la cantidad de inventario no sea negativa o que los precios sean mayores que cero).

-- Evitar precios negativos:
ALTER TABLE productos
ADD CONSTRAINT chk_precio_positivo
CHECK (precio > 0);

-- Evitar stock negativo:
ALTER TABLE productos
ADD CONSTRAINT chk_inventario_no_negativo
CHECK (cantidad_inventario >= 0);

-- 9. Documentación
    
--     ○ Documenta el proceso de creación del modelo de datos y las decisiones tomadas al diseñar las tablas, restricciones y relaciones entre entidades.
	-- el diseño de las tablas obedece a los requerimientos del ejercicio y los criterios de normalización. Se usó NOT NULL para evitar campos vacíos, PK para indicar los ID, AUTO_INCREMENT como buena práctica de estos, y se agregó CHECK para evitar algunos campos numéricos negativos que no tienen lógica en el mundo real
        
--     ○ Incluye una breve explicación de la normalización aplicada en el modelo de datos y su impacto en la estructura de la base de datos.
      -- La normalización reduce redundancia, mejora integridad de datos, facilita actualizaciones consistentes, y evita anomalías en inserción, actualización y eliminación.
--     ○ Presenta ejemplos de las consultas SQL utilizadas y explica cómo funcionan.
	-- los ejemplos están en los items correspondientes, select elige los datos, los JOIN ayudan a cruzar la información de dos o más tablas. 


