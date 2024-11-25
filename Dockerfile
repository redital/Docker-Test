FROM python:3.8-slim
RUN apt-get update 
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
RUN pwd
RUN ls
CMD ["python","app/main.py"]
#CMD ["flask", "run", "--debug"]
