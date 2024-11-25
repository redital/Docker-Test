# syntax=docker/dockerfile:1
FROM python:3.10
COPY . .
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","-u","main.py"]