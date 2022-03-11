FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


######################################### to run container using terminal ######################################
# run on docker without gunicorn
# terminal: docker run -p 8000:5000 <image name>
# browser: http://localhost:8000/
#CMD ["python", "books.py"]

# run on docker with gunicorn
# terminal: docker run -p 8000:5000 <image name>
# browser: http://localhost:8000/
#CMD ["gunicorn"  , "--bind", "0.0.0.0:5000", "app:app"]
################################################################################################################



######################################### to run container using docker-compose ################################
# you probably do everything in docker-compose.yml itself.