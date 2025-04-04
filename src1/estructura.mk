├── README.md
├── pyproject.toml
└── src
    ├── assets
    │   └── icon.png
    ├── main.py
    ├── frontend  # Capa de presentación
    │   ├── views
    │   │   ├── main_view.py  # Vista principal (Vista 1)
    │   │   ├── menu_view.py  # Vista del menú lateral (Vista 2)
    │   │   ├── settings_view.py  # Vista de ajustes (Vista 3)
    │   │   ├── proxy_view.py  # Subvista de ajustes - Proxy
    │   │   ├── system_notifications_view.py  # Subvista de ajustes - Sistema y notificaciones
    │   │   ├── change_password_view.py  # Subvista de ajustes - Cambiar contraseña
    │   ├── components
    │   │   ├── menu_component.py  # Menú lateral
    │   │   ├── header_component.py  # Encabezado común
    │   │   ├── button_component.py  # Botones reutilizables
    
    ├── backend  # Capa de lógica de negocio
    │   ├── services
    │   │   ├── proxy_service.py  # Lógica relacionada con la configuración del proxy
    │   │   ├── system_service.py  # Lógica de sistema y notificaciones
    │   │   ├── auth_service.py  # Gestión de autenticación y cambio de contraseña
    │   ├── models
    │   │   ├── user_model.py  # Modelo de usuario
    │   │   ├── config_model.py  # Modelo de configuración
    
    ├── data  # Capa de datos
    │   ├── config.json  # Archivo de configuración
    │   ├── database.sqlite  # Base de datos SQLite si es necesaria
    
    ├── utils  # Utilidades y helpers
    │   ├── logger.py  # Registro de eventos y errores
    │   ├── constants.py  # Variables constantes usadas en la app