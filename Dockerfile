FROM python:3.10-slim
ENV BOT_TOKEN=""
ENV API_ID=""
ENV API_HASH=""
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN mkdir /app/logger/log
RUN mkdir /app/saved
RUN mkdir /app/saved/sessions
CMD ["python", "main.py"]