FROM tiangolo/uwsgi-nginx-flask:python3.7

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "./server.py" ]