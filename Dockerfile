FROM python:3.11.5
EXPOSE 8000

WORKDIR /app

COPY requirements.txt /app

# # Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update

# Copy the rest of the application code into the container at /app
COPY . /app

# Command to run when the container is started
CMD ["python", "app.py"]
