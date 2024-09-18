FROM python:3.11-slim
WORKDIR /code
COPY requirements.txt /code/dev-requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/dev-requirements.txt
COPY app.py /code/
CMD ["python", "app.py"]
