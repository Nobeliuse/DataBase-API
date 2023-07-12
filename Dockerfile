FROM python:latest
ENV FLASK_APP=web_app/app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY req.txt req.txt
RUN pip install -r req.txt
COPY . .
CMD ["flask", "run", "--host=0.0.0.0"]
