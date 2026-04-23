### Evaluación del módulo

Imagina que trabajas como desarrollador para una empresa que está creando una pequeña aplicación web para gestionar tareas. El sistema debe permitir a los usuarios autenticarse, gestionar tareas (crear, ver, eliminar) y ver una lista de sus tareas asignadas. Para esta actividad, se manejarán las tareas en memoria, sin conexión a una base de datos real.

**Parte 1: Configuración Inicial**

1. **Crear el Proyecto Django**:
    
    - Crea un proyecto Django llamado **`gestor_tareas`** en tu entorno virtual.
        
2. **Crear la Aplicación de Tareas**:
    
    - Dentro del proyecto **`gestor_tareas`**, crea una aplicación llamada **`tareas`**.
        
3. **Configura el Proyecto**:
    
    - Asegúrate de que la aplicación **`tareas`** esté registrada en `INSTALLED_APPS` en el archivo `settings.py`.
        
4. **Configuración de URLs**:
    
    - Crea un archivo `urls.py` dentro de la aplicación **`tareas`** y configura las rutas necesarias para las vistas principales.
        

**Parte 2: Vistas y Plantillas**

1. **Crear Vista de Lista de Tareas**:
    
    - Crea una vista para mostrar todas las tareas del usuario autenticado.
        
    - Las tareas se manejarán en memoria, usando una lista de diccionarios que almacene el título y la descripción de cada tarea.
        
    - La vista debe mostrar la lista de tareas en una página utilizando una plantilla HTML.
        
2. **Crear Vista para Detalles de Tarea**:
    
    - Crea una vista para mostrar los detalles de una tarea individual (solo la tarea seleccionada por el usuario).
        
    - Usa parámetros en la URL para mostrar los detalles de cada tarea.
        
3. **Crear Vista para Agregar Tarea**:
    
    - Crea una vista que permita a los usuarios agregar una nueva tarea.
        
    - El formulario debe ser creado con Django Forms. Usa `forms.Form` para recolectar el título y la descripción de la tarea.
        
    - Al agregar una tarea, se añadirá a la lista en memoria.
        
4. **Crear Vista para Eliminar Tarea**:
    
    - Crea una vista que permita a los usuarios eliminar una tarea existente.
        
    - Utiliza la URL para identificar la tarea a eliminar y eliminarla de la lista en memoria.
        
5. **Plantillas**:
    
    - Utiliza Bootstrap para diseñar las plantillas y asegurarte de que la interfaz sea responsiva.
        
    - Crea plantillas para las vistas: lista de tareas, detalle de tarea, agregar tarea y eliminar tarea.
        

**Parte 3: Autenticación y Seguridad**

1. **Autenticación de Usuarios**:
    
    - Implementa vistas para que los usuarios puedan **registrarse**, **iniciar sesión** y **cerrar sesión**.
        
    - Utiliza el sistema de autenticación de Django (`django.contrib.auth`).
        
    - Asegúrate de que los usuarios no autenticados no puedan acceder a la vista de lista de tareas. Usa el decorador `login_required` para proteger las vistas.
        
2. **Protección de Vistas**:
    
    - Asegúrate de que los usuarios solo puedan gestionar (agregar, eliminar, ver) las tareas que han creado.
        
    - La lista de tareas y las vistas de detalle deben ser privadas para cada usuario autenticado.
        

**Parte 4: Despliegue y Pruebas**

1. **Pruebas de Funcionalidad**:
    
    - Realiza pruebas para asegurarte de que las vistas y formularios funcionen correctamente. Verifica lo siguiente:
        
        - Las tareas se muestran correctamente en la vista de lista.
            
        - Los usuarios pueden agregar y eliminar tareas.
            
        - El sistema de autenticación funciona correctamente (registro, inicio de sesión, cierre de sesión).
            
        - Las tareas solo se pueden ver, agregar o eliminar por el usuario que las creó.
            
2. **Configuración de Servidor de Producción**:
    
    - Configura la aplicación para ejecutarse en un entorno de producción, asegurándote de que se utilicen configuraciones adecuadas de `ALLOWED_HOSTS`, `DEBUG`, etc.
        

**Parte 5: Entrega**

1. **Documentación**:
    
    - Redacta una breve documentación explicando cómo se estructura tu proyecto y las funcionalidades principales que implementaste.
        
    - Incluye instrucciones sobre cómo ejecutar el proyecto, configurar el entorno virtual y ejecutar las migraciones.
        
2. **Entrega**:
    
    - Entrega el código en un repositorio de GitHub o similar, con el README correctamente configurado.
