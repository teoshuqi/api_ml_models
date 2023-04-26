#!/bin/bash
docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.11-management
celery -A fast-api-celery.worker worker -l INFO
uvicorn fast-api-celery.api.main:app --host 0.0.0.0 --port 8000 --reload