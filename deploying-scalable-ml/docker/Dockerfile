FROM python:3.7-alpine

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000
COPY . .

WORKDIR /model
ENV FLASK_APP=model.py
ENV FLASK_RUN_HOST=0.0.0.0
#ENV ml_debug_level=1
#ENV environment PRODUCTION

CMD ["flask", "run"]
