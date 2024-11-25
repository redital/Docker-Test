# syntax=docker/dockerfile:1
FROM python:3.10
WORKDIR /content
ADD . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["flask", "run", "--debug"]