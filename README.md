1) Redis 
docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
2) RabbitMQ
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.11-management
3) Poetry
curl -sSL https://install.python-poetry.org | python3 -
export PATH=$PATH:/Users/teoshuqi/.local/bin (add to path)
poetry init
poetry add fastapi
poetry add celery
poetry add redis
4) Run celery
celery -A worker.celery worker --loglevel=info
to shutown celery worker: celery control shutdown
5) run fastapi
uvicorn main:app --host 0.0.0.0 --reload