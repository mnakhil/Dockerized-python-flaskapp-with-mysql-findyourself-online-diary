from python:3

RUN pip install --no-cache-dir --upgrade pip

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["main.py"]
