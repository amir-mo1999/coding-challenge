# base python image for custom image
FROM python:3.12

# create working directory and install pip dependencies
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# copy python project files from local to /hello-py image working directory
COPY . .

# Make port 80 available to the world outside this container
EXPOSE 4000

# Run app.py when the container launches
CMD ["python", "wsgi.py"]