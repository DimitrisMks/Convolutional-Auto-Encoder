![image](https://github.com/user-attachments/assets/1dc45d9f-b3b0-49f9-9a86-3073a9ca1f7d)


# 🌌 AstroFlow ETL

**Project Summary**  
Design and implementation of a daily ETL pipeline using Apache Airflow to automate the extraction of NASA’s Astronomy Picture of the Day (APOD) metadata, transform it into a normalized format, and load it into a PostgreSQL database—all containerized with Docker for consistency and portability.

---

## 🚀 Key Contributions

- **Orchestrated Workflows:**  
  - Defined a modular Airflow DAG (`@task` + `SimpleHttpOperator`) with clear dependencies:  
    1. Create target table (idempotent `CREATE TABLE IF NOT EXISTS`)  
    2. Extract JSON from NASA APOD API  
    3. Transform into flat records (`title`, `explanation`, `url`, `date`, `media_type`)  
    4. Load into Postgres with safe upserts (`ON CONFLICT DO NOTHING`)

- **API Integration & Data Handling:**  
  - Consumed a public REST endpoint, parsed JSON, handled rate limits/keys via Airflow Connections  
  - Employed XCom for passing structured data between tasks

- **Containerization & Deployment:**  
  - Composed Airflow scheduler, webserver, and Postgres services in `docker-compose.yml`  
  - Ensured persistent storage via Docker volumes and reproducible environment

- **Reliability & Observability:**  
  - Configured retry policies, logging (`log_response=True`), and error handling to avoid pipeline failures on duplicates or transient network issues  
  - Monitored runs in Airflow UI, stored historical runs and logs

---

## 🛠️ Technology Stack

- **Orchestration:** Apache Airflow (TaskFlow API, SimpleHttpOperator, PostgresHook)  
- **Containerization:** Docker & Docker Compose  
- **Database:** PostgreSQL (Dockerized, persistent volumes, SQL upserts)  
- **API:** NASA APOD REST API (JSON)  
- **Languages & Tools:** Python 3, SQL, Bash  
