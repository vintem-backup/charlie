FROM python:3.7
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD . /worker
WORKDIR /worker
COPY code/* worker/
CMD python worker/app.py