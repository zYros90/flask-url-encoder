FROM python:alpine3.16

WORKDIR /srv

COPY . .

# Install dependencies:
RUN pip install -r requirements.txt

CMD ["python", "main.py"]
