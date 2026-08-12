# Tripwise (Pure Django)

A full-stack travel booking site built entirely in Django — no separate frontend framework.
Django handles everything: pages, styling, forms, and data, all in one project.

Comes with 4 sample destinations pre-loaded automatically.

## Prerequisites
- Python 3.10+

## Run it

Open a terminal in this folder:

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open **http://127.0.0.1:8000/** in your browser. That's it — one server, one terminal.

## What's built
- Homepage with hero section
- Destinations page — lists all destinations (4 pre-loaded: Santorini, Kyoto, Banff, Lisbon)
- Destination detail page — description + a real booking form (writes to the database)
- Django admin at **http://127.0.0.1:8000/admin/** for managing destinations and viewing bookings
  (create a login with `python manage.py createsuperuser` if you want to use this)

## Why pure Django (no React)
Simpler to build, simpler to deploy — one Python project, one server. When we deploy this to AWS,
it's a single EC2 instance running Django, instead of juggling a separate S3+CloudFront frontend
and an EC2 backend. Fewer moving pieces, easier to explain in an interview, easier to actually finish.

## Coming next
- Deploy to AWS EC2 (single instance running Django via Gunicorn + Nginx)
- Swap SQLite for a real database (PostgreSQL on RDS, or DynamoDB)
- S3 for destination images instead of external URLs
- SNS to email you when a new booking comes in
