# InjectKit - GitHub Template Boilerplate

A scalable Python project boilerplate using manual dependency injection with `injector`. It includes a structured layout with environment-based configuration, centralized logging, database access using SQLAlchemy, and support for Apache Airflow (locally via Docker and on production via MWAA).

---

## 📦 Features

- Manual Dependency Injection using `injector`
- Modular separation: `core/`, `services/`, and `entrypoints/`
- Environment variable support via `.env`
- Unit-test friendly structure
- SQLAlchemy-based database module
- Centralized logging service with file/console output
- 🌀 Apache Airflow DAG integration (local & MWAA-compatible)

---

## 🗂️ Project Structure

```
injectkit/
├── app/
│   ├── core/
│   │   ├── logging_service.py
│   │   └── database.py
│   ├── services/
│   │   ├── greeting_service.py
│   │   └── user_service.py
│   ├── config.py
│   ├── container.py
│   └── __init__.py
├── entrypoints/
│   ├── cli.py            # Optional command-line entrypoint
│   └── main.py           # Main script entry
├── tasks/
│   └── sample_task.py    # Can be used for cron jobs, workers, etc.
├── airflow/
│   └── dags/
│       └── example_dag.py  # Airflow DAG using app logic
├── tests/
│   └── test_user_service.py
├── .env.example
├── .gitignore
├── LICENSE
├── requirements.txt / pyproject.toml
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/injectkit.git
cd injectkit
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Copy `.env.example` to `.env` and update values:

```dotenv
ENVIRONMENT=development
API_KEY=changeme
FEATURE_FLAG=true
LOG_LEVEL=debug
LOG_TO_FILE=false
LOG_FILE_PATH=app.log
DATABASE_URL=postgresql://user:pass@localhost:5432/db
```

### 5. Run the app

```bash
python -m entrypoints.main
```

---

## 🧪 Running Tests

```bash
pytest
```

---

## 🌀 Airflow Support

### Local Airflow (Docker)

Add `airflow/docker-compose.yml` (not included here) and mount:

- `./airflow/dags`
- `./injectkit.zip` (zipped `app/` directory for imports)

Then run:
```bash
cd airflow
docker compose up -d
```

### MWAA (Production)

1. Upload `injectkit.zip` to your MWAA DAGs S3 bucket
2. Use `airflow/dags/example_dag.py`
3. Configure environment variables in MWAA console
4. Add dependencies to `requirements.txt`

---

## ➕ Extending

### Add a New Service

1. Create a new file in `app/services/`
2. Use `@inject` if it depends on other services
3. Register it in `app/container.py`

### Add a Shared Utility

1. Place it in `app/core/`
2. Wire it into the DI container

---

## 📚 Dependencies

- `injector`
- `python-dotenv`
- `SQLAlchemy`
- `psycopg2-binary`
- `pytest`
- `apache-airflow`

Install them using:

```bash
pip install -r requirements.txt
```

---

## 📝 License

MIT — free to use for personal or commercial projects.
