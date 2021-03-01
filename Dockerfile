FROM python:3.8.2

COPY "app/web_app.py" "/opt/app/web_app.py"
COPY "requirements.txt" "tmp"

RUN pip install -r /tmp/requirements.txt

ENTRYPOINT ["python", "/opt/app/web_app.py"]

