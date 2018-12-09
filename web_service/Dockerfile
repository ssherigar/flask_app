FROM python:3.6-alpine

RUN adduser -D tigflask
WORKDIR /home/tigflask

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app app
COPY tests tests
COPY run.py ./

ENV FLASK_APP run.py
ENV FLASK_CONFIG development

RUN chown -R tigflask:tigflask ./
USER tigflask

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
