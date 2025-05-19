# Deployment

This project can be deployed locally using Docker or run directly with Python.

## Docker

Build and run the Docker image:

```bash
docker build -t financial-analyzer .
docker run -p 8501:8501 financial-analyzer
```

Then open `http://localhost:8501` to access the app.

## GitHub Actions

The repository includes a simple CI workflow located at `.github/workflows/ci.yml`.
It installs dependencies and runs the unit tests on every push.

