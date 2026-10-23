FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt ./

RUN printf 'gunicorn==26.2.0\n' > /tmp/gunicorn-constraints.txt \
    && pip install --no-cache-dir --constraint /tmp/gunicorn-constraints.txt -r requirements.txt \
    && rm /tmp/gunicorn-constraints.txt

RUN addgroup --system app \
    && adduser --system --ingroup app app

COPY --chown=app:app app.py ./
COPY --chown=app:app templates/ ./templates/
COPY --chown=app:app static/ ./static/

USER app

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--no-control-socket", "app:app"]
