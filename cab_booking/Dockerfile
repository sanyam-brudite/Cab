FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY cab_booking/requirements.txt /app/

RUN pip install --upgrade pip setuptools
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "app.py", "sh","migrations.sh"]
