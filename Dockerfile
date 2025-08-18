# === Build a small Python image ===
FROM python:3.11-slim

# 1) System deps (optional but useful for TLS/certs)
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    ca-certificates curl && \
    rm -rf /var/lib/apt/lists/*

# 2) Set workdir
WORKDIR /app

# 3) Copy requirements and install (layer caching)
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir gunicorn

# 4) Copy source code
COPY src/ /app/src/

# 5) Expose port and run with Gunicorn (production-ready)
EXPOSE 5000
# app.py defines: app = Flask(__name__)
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "src.app:app"]
