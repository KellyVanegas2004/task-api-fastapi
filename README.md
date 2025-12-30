# Technical Test API

API REST construida con FastAPI para la gestión de tareas, con autenticación JWT, persistencia en PostgreSQL y migraciones con Alembic.

El objetivo del proyecto es demostrar una solución funcional end-to-end, segura y mantenible, ejecutable en un entorno local usando Docker.

---

## 🧱 Tecnologías utilizadas

- Python 3.11.8
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic (migraciones)
- JWT (JSON Web Tokens)
- Passlib (bcrypt)
- Docker & Docker Compose

---

## 📁 Estructura del proyecto
rest_project/
├── alembic/
│ ├── versions/
│ │ ├── create_users_table.py
│ │ ├── seed_initial_admin_user.py
│ │ └── create_tasks_table.py
│ └── env.py
│
├── app/
│ ├── api/
│ │ ├── auth.py # Endpoints de autenticación
│ │ └── tasks.py # Endpoints CRUD de tareas
│ │
│ ├── core/
│ │ ├── auth.py # JWT y dependencias de seguridad
│ │ ├── config.py # Configuración y variables de entorno
│ │ └── security.py # Hash y verificación de contraseñas
│ │
│ ├── db/
│ │ └── session.py # Conexión y sesión de base de datos
│ │
│ ├── models/
│ │ ├── user.py # Modelo SQLAlchemy User
│ │ └── task.py # Modelo SQLAlchemy Task
│ │
│ ├── schemas/
│ │ ├── user_dto_input.py
│ │ ├── user_dto_output.py
│ │ ├── user_login_dto.py
│ │ ├── task_dto_input.py
│ │ ├── task_dto_output.py
│ │ └── token_dto.py
│ │
│ ├── services/
│ │ ├── user_service.py # Lógica de negocio de usuarios
│ │ └── task_service.py # Lógica de negocio de tareas
│ │
│ └── main.py # Punto de entrada de la aplicación
│
├── docker-compose.yml
├── Dockerfile
├── alembic.ini
├── requirements.txt
├── .env
└── README.md

**Decisión clave:**  
- Se separa **API / Services / Models / Schemas** para facilitar escalabilidad, testing y mantenimiento.

---

## 🗄️ Base de datos

- PostgreSQL ejecutándose **exclusivamente en Docker**
- Migraciones gestionadas con **Alembic**
- Tablas creadas mediante migraciones versionadas

### Variables de entorno (`.env`)

```env
DB_HOST=postgres
DB_PORT=5432
DB_NAME=technical_test
DB_USER=postgres
DB_PASSWORD=postgres

JWT_SECRET_KEY=super-secret-key
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=30

🐳 Uso de Docker

El proyecto está completamente dockerizado para garantizar una ejecución reproducible.

Contenedores utilizados
Servicio	Descripción
api	Aplicación FastAPI (Python 3.11)
postgres	Base de datos PostgreSQL
▶️ Levantar el proyecto

Desde la raíz del proyecto ejecutar:

docker-compose up --build


La API quedará disponible en:

http://localhost:8000


Documentación Swagger:

http://localhost:8000/docs

⏹️ Detener los contenedores
docker-compose down

🗂️ Migraciones de base de datos (Alembic)

Las migraciones se ejecutan dentro del contenedor de la API.

Migraciones incluidas

Creación de tabla users

Creación de tabla tasks

Seed automático del usuario administrador

▶️ Ejecutar migraciones
docker-compose exec api alembic upgrade head

🆕 Crear una nueva migración
docker-compose exec api alembic revision -m "descripcion de la migracion"


Luego ejecutar:

docker-compose exec api alembic upgrade head

🔐 Autenticación

La autenticación está basada en JWT.

Usuario inicial

El usuario administrador se crea automáticamente al ejecutar las migraciones.

username: admin
password: admin123


⚠️ Credenciales solo para pruebas locales.

Login

Endpoint:

POST /auth/login


Body (x-www-form-urlencoded):

username=admin
password=admin123


Respuesta:

{
  "access_token": "<jwt_token>",
  "token_type": "bearer"
}


Usar el token en el header:

Authorization: Bearer <jwt_token>

📝 Tareas (Task)

Todos los endpoints están protegidos por JWT.

Endpoints
Método	Endpoint	Descripción
POST	/tasks/	Crear tarea
GET	/tasks/	Listar tareas (paginado)
GET	/tasks/{id}	Obtener tarea
PUT	/tasks/{id}	Actualizar tarea
DELETE	/tasks/{id}	Eliminar tarea
📄 Paginación
GET /tasks?page=1&page_size=10


page: número de página (default: 1)

page_size: tamaño de página (default: 10)

⚖️ Decisiones técnicas (Trade-offs)

JWT stateless para evitar sesiones persistentes

Arquitectura por capas para escalabilidad

PostgreSQL solo en Docker (sin dependencias locales)

Alembic para control total del esquema

Alcance acotado (sin refresh tokens) según requerimientos

✅ Estado del proyecto

✔ Autenticación JWT
✔ CRUD completo de tareas
✔ Paginación real
✔ Migraciones versionadas
✔ Usuario inicial automático
✔ Docker end-to-end