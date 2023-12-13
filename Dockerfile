FROM python:3.11.3-slim-bullseye


WORKDIR /app


COPY backend-lab2/requirements.txt .


RUN python -m pip install -r requirements.txt


COPY backend-lab2 /app
CMD ["python", "main.py"]