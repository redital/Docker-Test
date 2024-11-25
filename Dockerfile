FROM python:3.8-slim
RUN apt-get update 
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","app.py"]
#CMD ["flask", "run", "--debug"]
