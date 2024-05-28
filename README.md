### Setup

## Docker Setup

Make sure your Docker engine is running. Then run the following commands to build the image and start up the container:

```
docker build -t coding_challenge .
docker run -d -p 4000:4000 coding_challenge
```

## Local Setup

Make sure you have Python installed on your system. Then run the following.

1. Create the virtual environment:

```
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

2. Start the application:

```
python wsgi.py
```

3. Navigate to the API documentation: [http://localhost:4000/docs#/](hhttp://localhost:4000/docs#/)
