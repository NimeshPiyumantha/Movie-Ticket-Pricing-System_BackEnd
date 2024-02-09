FROM python:3.10.7
 
WORKDIR /code
 
COPY . .
 
RUN pip install -v --no-cache-dir --upgrade -r /code/requirements.txt
 
COPY . /code
 
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","80"]
