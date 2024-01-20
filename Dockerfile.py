# Використовуйте офіційний образ Python
FROM python:3.8

# Встановлення залежностей
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt  


CMD ["python", "_main_.py"]