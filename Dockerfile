FROM python:3.9-slim

WORKDIR /home/app

COPY ./requirements.txt /home/app/requirements.txt
COPY ./api.py /home/app/api.py
#COPY ./.env /home/app/.env

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000

CMD ["python", "api.py"]