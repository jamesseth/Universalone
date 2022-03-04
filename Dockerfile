FROM python:3.8
ARG WORKDIR=/app
ENV PROJECT_NAME universal
ARG _PORT=8000
ENV PORT=$_PORT
# Set number of gunicorn workers .
ENV NUMBER_OF_GUNICORN_WORKERS=2
# Prevent Python io buffering.
ENV PYTHONUNBUFFERED=1
# Stop Python from creating *.pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get -qq update && apt-get -qq install build-essential -y
RUN apt-get -qq install libpq-dev python-dev
# Create non root user and django group
RUN groupadd -r django && useradd -r -s /bin/false -g django django

# Copy source code.
WORKDIR /app
COPY . ./

# Give django user read access to project source.
RUN chown -R django:django /app

# Install dependencies
RUN pip install --upgrade pip~=21.1.2 setuptools wheel
RUN pip install gunicorn
RUN pip install -r requirements.txt

# Change to django user.
USER django

# Kick-off Gunicorn
CMD exec gunicorn --bind :$PORT --workers $NUMBER_OF_GUNICORN_WORKERS universal.wsgi:application
