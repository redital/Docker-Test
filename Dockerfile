# syntax=docker/dockerfile:1
FROM python:3.10
WORKDIR /usr/src/app
COPY . .
RUN pip install — no-cache-dir -r requirements.txt
EXPOSE 5000
RUN cd ..
CMD ["python3","main.py"]
#CMD ["flask", "run", "--debug"]