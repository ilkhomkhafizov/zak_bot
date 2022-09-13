# Pull base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /zakovat_bot

# Install dependencies
COPY requirements.txt /zakovat_bot/
RUN pip install -r requirements.txt

# Copy project
COPY . /zakovat_bot/
