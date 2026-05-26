# FeedbackSDK API

API desarrollada con FastAPI para recolectar:
- reportes de errores
- opiniones de usuarios
- feedback de aplicaciones

Cada proyecto posee su propia API Key para enviar y visualizar reportes.

---

# Tecnologías

- FastAPI
- PostgreSQL
- SQLAlchemy
- Supabase
- JWT Authentication
- Docker (próximamente)
- Flutter (cliente)

---

# Características

✅ Registro de usuarios  
✅ Login con JWT  
✅ Creación de proyectos  
✅ API Key por proyecto  
✅ Envío de reportes  
✅ Visualización de reportes  
✅ Soporte multi-proyecto  

---

# Instalación

## Clonar repositorio

```bash
git clone https://github.com/tuusuario/feedback-sdk.git
```

---

## Crear entorno virtual

```bash
python -m venv .venv
```

---

## Activar entorno

### Windows

```bash
.venv\Scripts\activate
```

### Linux/Mac

```bash
source .venv/bin/activate
```

---

## Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Variables de entorno

Crear archivo `.env`

```env
DATABASE_URL=
SECRET_KEY=
APP_NAME=
DEBUG=
```

---

# Ejecutar servidor

```bash
uvicorn app.main:app --reload
```

---

# Documentación API

Swagger UI:

```text
http://localhost:8000/docs
```

---

# Endpoints principales

## Auth

- POST `/auth/register`
- POST `/auth/login`

## Projects

- POST `/projects`
- GET `/projects`

## Reports

- POST `/reports`
- GET `/admin/reports`

---

# Deploy

Backend desplegado con:
- Render
- Supabase PostgreSQL

---

# Futuras mejoras

- Upload de imágenes
- IA para clasificación automática
- Dashboard avanzado
- Métricas con Prometheus + Grafana

---

# Autor

Andre Haris
