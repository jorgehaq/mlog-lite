# MLOG-Lite

![CI](https://github.com/<user>/<repo>/actions/workflows/ci.yml/badge.svg)
![Coverage](https://img.shields.io/badge/coverage-85%25-green)

Centralized **logging and lightweight analytics microservice**.  
Part of the backend portfolio along with [AXI-Lite](../axi-lite), [ADTECH-Lite](../adtech-lite), and [MINT-Lite](../mint-lite).

---

## 🎯 Purpose

MLOG-Lite acts as the **auditing hub** of the ecosystem:
- Receives JSON events (`service`, `user_id`, `action`, `metadata`).
- Stores them in MongoDB with timestamps.
- Exposes endpoints to query recent logs and usage summaries.

This allows **AXI**, **ADTECH**, and **MINT** to centralize their telemetry for traceability and cross-service metrics.

---

## ⚙️ Tech Stack

- **FastAPI** for the asynchronous HTTP API and OpenAPI docs.  
- **MongoDB** for event storage.  
- **Docker** + **docker-compose** for local orchestration.  
- **pytest** + **httpx** for async integration and end-to-end tests.  

---

## 🚀 Local Development

1. Create a `.env.local` file with the service configuration:

```env
   MONGO_URI=mongodb://mongo:27017/mlog
   PORT=8000       # internal container port
   HOST_PORT=8008  # host exposed port
```

2. Start the stack:

   ```bash
   make mlog-dev
   ```

   The API is available at [http://localhost:8008/docs](http://localhost:8008/docs)
   MongoDB at `localhost:27017`.

3. Run the test suite:

   ```bash
   make mlog-test
   ```

   > CI/CD pipeline runs pytest with coverage on every push (GitHub Actions).

Stop the stack when you are done:

```bash
make mlog-down
```

---

## 📡 API Endpoints

### Healthcheck

```bash
curl http://localhost:8008/health
```

### Create Event

```bash
curl -X POST http://localhost:8008/events/ \
  -H "Content-Type: application/json" \
  -d '{"service": "axi", "user_id": "u1", "action": "login"}'
```

### List Recent Events

```bash
curl http://localhost:8008/events/
```

### Summary of Actions

```bash
curl http://localhost:8008/analytics/summary
```

---

## 🔄 Example Flow

* AXI-Lite uploads a dataset → `{"service": "axi", "user_id": "u42", "action": "upload_csv"}`
* ADTECH-Lite logs a click → `{"service": "adtech", "user_id": "u99", "action": "click"}`
* MINT-Lite generates a report → `{"service": "mint", "user_id": "u15", "action": "generate_report"}`

The summary endpoint responds with:

```json
{
  "by_action": {
    "upload_csv": 1,
    "click": 1,
    "generate_report": 1
  },
  "total": 3
}
```

---

## ☁️ Deployment (Cloud Run)

Build and push the container image:

```bash
docker build -t gcr.io/<PROJECT_ID>/mlog-lite:latest -f docker/Dockerfile .
docker push gcr.io/<PROJECT_ID>/mlog-lite:latest
```

Deploy to Cloud Run:

```bash
gcloud run deploy mlog-lite \
  --image gcr.io/<PROJECT_ID>/mlog-lite:latest \
  --platform managed \
  --allow-unauthenticated \
  --region us-central1
```

---

## 🗂️ Portfolio Context

```
 AXI-Lite       ADTECH-Lite       MINT-Lite
     \              |               /
      \             |              /
       --->      MLOG-Lite      --->   MongoDB + Analytics
```

* **AXI-Lite (8000):** CSV dataset analytics.
* **ADTECH-Lite (8001):** Multi-tenant advertising metrics.
* **MINT-Lite (8002):** SaaS platform with schema-per-tenant PostgreSQL.
* **MLOG-Lite (8008):** Central logging and lightweight analytics → auditing hub.

---

## 📌 Nota en Español

Este proyecto forma parte de mi portafolio técnico.
Lo desarrollé para demostrar patrones de arquitectura modernos aplicados en entornos startup y cloud,
con un enfoque en microservicios, escalabilidad y buenas prácticas de desarrollo.

MLOG-Lite centraliza los eventos de **AXI, ADTECH y MINT**, ofreciendo trazabilidad y métricas unificadas.