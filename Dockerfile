FROM python:3

WORKDIR /usr/src/app

COPY requirements ./
RUN pip install --no-cache-dir -r requirements/testing.txt
RUN pip install xknx
RUN pre-commit install

COPY . .

CMD [ "python", "./monitor.py" ]