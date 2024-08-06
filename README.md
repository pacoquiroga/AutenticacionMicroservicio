<p align="center">
  <a href="https://fastapi.tiangolo.com"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI"></a>
</p>
<p align="center">
    <em>FastAPI framework, high performance, easy to learn, fast to code, ready for production</em>
</p>
<p align="center">
<a href="https://pypi.org/project/fastapi" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058" alt="Supported Python versions">
</a>
</p>

---

**Documentation**: <a href="https://fastapi.tiangolo.com" target="_blank">https://fastapi.tiangolo.com</a>

**Source Code**: <a href="https://github.com/fastapi/fastapi" target="_blank">https://github.com/fastapi/fastapi</a>

---


# Microservicio de Autenticación

Este proyecto implementa un microservicio de autenticación usando FastAPI y MySQL.

## Requisitos

- Docker
- Docker Compose (opcional, pero recomendado)
- Python 3.9+
- FastAPI
---
## Crear y correr contenedores
Para crear y correr los contenedores se ejecuta el comando completo, unas vez creados podemos usar el comando sin --build o unicamente encender los contenedores desde Docker Desktop
```bash
docker-compose up --build
```

## Servidor corriendo
 ╭────────── FastAPI  ────────────────────────────────────────────────────────╮
 │                                                                            │
 │  INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit) │
 │  INFO:     Started reloader process [14256] using WatchFiles               │
 │  INFO:     Started server process [1880]                                   │
 │  INFO:     Waiting for application startup.                                │
 │  INFO:     Application startup complete.                                   │
 │                                                                            │
 ╰────────────────────────────────────────────────────────────────────────────╯

```

</div>


### API docs

Ahora, ve a <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a>. Podrás ver la documentación automática de FastAPI.

![Documentación de la API](./img/FastAPIdocs.png)


