# Use an official Python runtime based on Alpine as a parent image
FROM python:3.12-alpine

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install python-frontmatter

# Make port 80 available to the world outside this container
EXPOSE 80

# Run the application when the container launches
CMD ["uvicorn", "fastapi_app:app", "--host", "0.0.0.0", "--port", "80"]