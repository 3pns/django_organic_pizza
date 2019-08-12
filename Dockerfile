FROM python:3.7.4-stretch
ENV PATH="/home/app/.local/bin:${PATH}"
RUN useradd -ms /bin/bash app
USER app
WORKDIR /app
COPY ./requirements ./requirements
RUN pip install --user --no-cache-dir -r requirements/production.txt 
COPY . .
EXPOSE 8000
CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "django_organic_pizza.wsgi:application"]
