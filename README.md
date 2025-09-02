# PRODIGY_FS_03
# 🛍️ Local Store – Django Project

A simple e-commerce style project built with **Django**, featuring products, reviews, orders, and customer support.

## 🚀 Features

* ✅ Product catalog with categories and images
* ✅ Product reviews with ratings
* ✅ Customer orders with status tracking (Pending, Shipped, Delivered)
* ✅ Customer support queries
* ✅ Admin panel to manage everything
* ✅ Media file support for product images

---

## 📂 Project Structure

```
localstore_project/
│── shop/                # Main Django app  
│   ├── models.py        # Product, Review, Order, Support models  
│   ├── views.py         # Business logic  
│   ├── urls.py          # App routes  
│   ├── templates/shop/  # HTML templates  
│   └── fixtures/        # Dummy data (optional)  
│
│── localstore_project/  # Project config  
│   ├── settings.py  
│   ├── urls.py  
│   └── asgi.py / wsgi.py  
│
│── media/               # Uploaded images (auto-created)  
│── manage.py  
```

---

## ⚙️ Installation

1. **Clone repo**

   ```bash
   git clone https://github.com/your-username/localstore_project.git
   cd localstore_project
   ```

2. **Create & activate virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install django pillow
   ```

4. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create superuser (for admin panel)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run development server**

   ```bash
   python manage.py runserver
   ```

7. Visit in browser:

   ```
   http://127.0.0.1:8000/
   http://127.0.0.1:8000/admin/  (for admin panel)
   ```

---

## 📸 Adding Products with Images

* Go to **Admin Panel** → Products → Add Product.
* Upload image (stored in `/media/products/`).
* To display product images in templates:

```html
<img src="{{ product.image.url }}" alt="{{ product.name }}">
```

If no image, you can show a placeholder:

```html
{% if product.image %}
  <img src="{{ product.image.url }}" alt="{{ product.name }}">
{% else %}
  <img src="/static/images/placeholder.png" alt="No image">
{% endif %}
```

---

## 📊 Models

### Product

* `name`, `description`, `price`, `category`, `image`, `created_at`

### Review

* `product`, `user_name`, `rating`, `comment`, `created_at`

### Order

* `name`, `email`, `address`, `items`, `total`, `status`, `created_at`

### SupportQuery

* `name`, `email`, `message`, `resolved`, `created_at`

---

## 🛠️ Optional Features to Try

* Add **cart system** (session-based)
* Add **search & filter** for products
* Add **payment integration** (Stripe, Razorpay, etc.)
* Add **user login/signup** for real customers

---
##ScreenShots



## 📜 License

This project is open-source and available under the MIT License.

