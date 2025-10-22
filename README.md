---Django Ecommerce Backend (DRF)

This is a sample ecommerce backend built with Django and Django REST Framework. It demonstrates modular architecture, custom user models, and RESTful APIs.

---Features

- Modular apps: products, cart, orders, payments
- Django REST Framework APIs
- Custom user model with signals
- PostgreSQL integration
- Optional: JWT authentication, rate-limiting

---Tech Stack

- Django 4.x
- Django REST Framework
- PostgreSQL
- Python 3.13

---Setup

```bash
git clone https://github.com/yourusername/ecommerce-backend.git
cd ecommerce-backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
