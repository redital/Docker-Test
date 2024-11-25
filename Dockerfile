FROM python:3.11.10-bookworm
RUN apt-get update 
WORKDIR /app
COPY . .
RUN  pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python","app.py"]
#CMD ["flask", "run", "--debug"]
