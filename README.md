# E-Commerce Website with Django-RESTAPI 

This project is an E-Commerce website developed using Django, with a robust API-driven architecture. It includes essential e-commerce functionalities such as product listing, shopping cart management, and comprehensive RESTful API endpoints.

Key Features
Product Listing: Users can browse and view detailed product listings.
Shopping Cart: Manages the shopping cart with features like subtotal, tax calculations, and total pricing.
API-Driven Backend: Provides RESTful API endpoints for product management, including listing, creation, and deletion.
Dynamic Pricing: Products can have dynamic pricing based on active sales, with real-time discount calculations.
Scalability: Designed with scalability in mind, making it easy to extend and integrate with other services.
Project Structure
views.py: Renders product lists, individual product details, and the shopping cart.
urls.py: Maps URLs to both standard views and API endpoints.
serializers.py: Manages the serialization and deserialization of product data.
api_views.py: Implements API endpoints using Django REST Framework.
models.py: Defines models for Product, ShoppingCart, and ShoppingCartItem, with methods for price calculations and sale management.
Requirements
Ensure you have the following installed to run the project:

Python: 3.10.x
Django: 4.2.x
Django REST Framework: 3.14.x
SQLite: 3.x (or any other supported database)
Pillow: 9.x (for image handling)
Django Filter: 23.x (for filtering in Django REST Framework)
Installation
Clone the repository:

bash
git clone https://github.com/yourusername/ecommerce-api.git
cd ecommerce-api
Create and activate a virtual environment:

bash

python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:

bash
pip install -r requirements.txt
Run migrations:

bash
python manage.py migrate
Start the development server:

bash
python manage.py runserver
Access the application:

Visit http://127.0.0.1:8000/ in your web browser to view the product listings and http://127.0.0.1:8000/api/v1/products/ to interact with the API.

Usage
Browse Products: Navigate to the homepage to view the list of available products.
View Product Details: Click on a product to view more details.
Manage Shopping Cart: Add items to your cart and view the calculated totals.
API Operations: Use the provided API endpoints to list, create, or delete products.
Future Enhancements
User Authentication: Implement user login and registration for a personalized shopping experience.
Order Processing: Add features for order management and payment integration.
Enhanced UI: Improve the user interface with modern design patterns and responsiveness.
