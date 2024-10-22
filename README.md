# KICKIN' IT 
[Link to Live Site](https://kickin-it-744f171f0d02.herokuapp.com)

## Mockup
![AmIResponsive Mockup](documentation/kickin-it-amiresponsive.png)

## Introduction

Kickin' It is a full-stack e-commerce web application. The site allows user to browse and purchase high end sneakers online.
Users can create an account, add items to their bag, add items to their wishlist and checkout.
Administrators can add, edit, and delete sneakers to/from the site.

The site has been developed as a part of an educational project, 
my MS4 project for the web application development course @ Code Institute.

This project relies on Stripe for payment processing, however is only set up for development purposes.

If you wish to test payments, please use the test details:

- Card Number: 4242 4242 4242 4242
- Expiration Date: Any using MM/YY format
- CVC/CVN: Any 3 digits
- Postcode/ZIP: Any 5 digits

Any payments made will not be charged to your account and no orders will be fulfilled.

If you have the relevant log-in details
 for the Django Admin panel, log-in [HERE](https://kickin-it-744f171f0d02.herokuapp.com/admin/)

## Overview

Kickin' It is a full-stack e-commerce web application: 

Users can:

- View the store anonymously
- Register for an account
- Wishlist desired products to save for later
- Browse products and sort by Brand, Gender, Price
- Add items to the shopping bag
- Edit and view items in the shopping bag
- View order history if signed in
- Subscribe to the newsletter

The site is available on all web browsers at various screensizes.

## UX

### Target Audience

- Sneaker Collectors
- Gift Givers
- Anyone who wants to buy high end shoes

### Colour Scheme

I opted to not use a main colour scheme for the site, I wanted to keep the design simple, but these were the main colours I used for the site:

![Colour Scheme](documentation/kickin-it.png)

Generated via [Coolers](https://coolors.co/)

### Typography

For the main font on the site, I used [Outfit](https://fonts.google.com/specimen/Outfit) from GoogleFonts.

For the text in the Hero, I used [Bebas Neue](https://fonts.google.com/specimen/Bebas+Neue) from GoogleFonts to make that text stand out from the rest.

### Project Goals

#### Site Owner

- Offer a seamless shopping experience
- Provide a user-friendly interface
- Maintain an up-to-date inventory
- Facilitate user engagement via the wishlist and account features

#### External User

- Easily browse and find desired sneakers
- Experience a smooth checkout process
- Personalise the shopping experience through account creation and wishlist functionality

### User Stories

| Role             | User Story Description                                                                                   |
| ---------------- | ------------------------------------------------------------------------------------------------------- |
| Site Visitor/Shopper | I want to be able to search for sneakers by name, brand or descriptor. |
| | I want to add sneakers to my bag to purchase. |
| | I want to be able to create an account so that I can utilise the full features of the website. |
| | I want to be able to filter products by category, gender, brand, price and name. |
| | I want to be given visual feedback when performing actions on the site. |
| Registered Shopper | I want to be able to add products to my wishlist. |
| | I want to be able to checkout securely. |
| | I want to be able to log-in to see my wishlist and account. |
| | I want to be able to view my order history. |
| | I want to be able to subscribe to the newsletter. |
| | I want to save my delivery information to my profile for easy checkout next time I purchase. |
| Admin | I want to be able to add, edit and delete products. |
| | I want to be able to access the admin panel, to manually remove multiple products at once, add categories to the database and overview the website from a "dashboard". |

### User Feedback

"**The website layout is clean and well organised, making it easy for me to find the shoes I was looking for.
Navigating through the site was smooth and I was able to move between categories without any issues. I particularly liked the ‘back to top’ button as this made it easier to go back to the top of the page without the time consuming task of scrolling from the bottom.
The product pages were detailed and clear. The option of adding items to my wishlist was helpful for when I was browsing and was something I could go back to when I was ready to buy something.
The checkout process was simple and hassle-free.
I would suggest adding a ‘quick buy’ button to each product to make the overall shopping experience that little bit faster.**" - Mica Ali

## Features

### Existing Features

<details>
<summary>Click Me</summary>

#### General

| Feature | Description | Image |
|:---|:---|:---|
| Favicon | | |
| Site Logo | | |
| Navigation Bar | | |
| Search Dropdown | | |
| Profile Dropdown | | |
| Products Dropdown | | |
| Mobile Nav Bar | | |
| Hero | | |
| Featured Products | | |
| Info Cards | | |
| Top Brands | | |
| Newsletter | | |
| Footer | | |

#### Products Pages

| Feature | Description | Image |
|:---|:---|:---|
| Products Page | | |
| Product Detail Page | | |
| Product Information | | |
| Size Selection | | |
| Quanitity Selection | | |
| Add to Bag | | |
| Add to Wish List | | |

#### Profile

| Feature | Description | Image |
| :---|:---|:---|
| Profile Page | | |
| Default Information | | |
| Order History | | |

#### Wishlist

| Feature | Description | Image |
|:---|:---|:---|
| Wishlist Page | | |
| Product | | |

#### Shopping Bag

| Feature | Description | Image |
|:---|:---|:---|
| Bag Page | | |
| Product | | |
| Summary & Buttons | | |

#### Checkout

| Feature | Description | Image |
|:---|:---|:---|
| Checkout Page | | |
| Order Confirmation | | |

#### Product Management(Admin)

| Feature | Description | Image |
|:---|:---|:---|
| Product Form | | |

#### Newsletter

| Feature | Description | Image |
|:---|:---|:---|
| Newsletter Email | | |
| Newsletter Confirmation | | |
| Newsletter Unsubscribe | | |

</details>

### Future Features

- Stock Levels: Add a feature that allows the admin to set the stock level for each item. And display on the product page when the stock level is low or if the item is out of stock.
- User reviews and ratings: Add a feature that allows users to leave reviews and ratings for each product.
- Quick Buy Button: Add a feature that allows users to quickly add a product to their bag without having to navigate to the product page.
- Blog/Articles: Add weekly articles to the site created by admin, so that users can read the latest news and product drops from the sneaker world.

## Structure

### DB

The Django backend is connected to a PostgreSQL database hosted on [AWS](https://aws.amazon.com/).

As Kickin' It tailors to just sneakers, I have changed the product model to add some features to the site.

Below are the custom models for wishlist, newsletter and FAQ sections and updated the updated Product model, which are all custom from the Boutique Ado walkthrough project.

**Product model**

```python
class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    # Custom fields below
    colourway = models.CharField(max_length=254, null=True, blank=True)
    gender = models.CharField(max_length=254, null=True, blank=True)
    brand = models.CharField(max_length=254, null=True, blank=True)
    release_year = models.IntegerField(null=True, blank=True)
    is_featured = models.BooleanField(default=False, null=True, blank=True)
    is_sale = models.BooleanField(default=False, null=True, blank=True)
    is_new = models.BooleanField(default=False, null=True, blank=True)

```

**FAQ model**

```python
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
```

**Wishlist model**

```python
class Wishlist(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                                     null=False, blank=False,
                                     related_name='user_wishlist',
                                     default=None)
    description = models.TextField(null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE, default=None)
```

**Newsletter model**

```python
class Subscriber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='subscription', null=True, blank=True)
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)
```

### Databse Schema

For easy visualisation of the database, I used Lucid Chart to build an Entity Relationship Diagram.

![ERD](documentaion/ERD.png)

### Technology and Languages Used

- HTML
- CSS
- Javascript
- Python
- [Git](https://git-scm.com) for version control
- [Github](https://github.com) to store the codebase
- Gitpod as an online development environment
- [Django](https://www.djangoproject.com) was used as the Python framework
- [Heroku](https://www.heroku.com) to host the application
- [AWS](https://aws.amazon.com) to host the database

Please refer to the [requirements.txt](https://github.com/cambboyle/Kickin-it-v1/blob/main/requirements.txt) file for more information on libraries/frameworks and their versions that were used in the project.

### Testing

For all testing, please refer to the [TESTING.md]() file.

### Deployment

#### Local Deployment

*1. Fork or Clone the repository*

1. Log-in to Github and locate to the [Kickin' It](https://github.com/cambboyle/Kickin-it-v1) repository.

2. From here, either:
   - Clone the repository to your Github
     1. Go to the repository page and click the "Code" button.
     2. Select your preferred method of cloning and copy the url.
     3. In your development environment, run the following command: `git clone https://github.com/cambboyle/Kickin-it-v1`
     4. Once the repository is cloned, navigate to the cloned directory: `cd Kickin-it-v1`
     5. Now in your terminal, you can run the app by running the following command: `python manage.py runserver`
   - Fork the repository by clicking the Fork button on the top right of the repository page.

3. For either option, you will need to install the packages found in the requirements.txt file. In your terminal, run the following command to install the packages:

    ```terminal
    pip3 install -r requirements.txt
    ```

4. Additionally, you will need to set some Environment Variables, you can do this by creating an env.py files at the root directory (Make sure to add this to .gitignore) OR you can set the environment variables in your gitpod environment in your user settings.

    ```python
    import os

    os.environ["SECRET_KEY"] = "your_secret_key"
    os.environ["LOCAL_HOST"] = "your_local_host"
    os.environ["STRIPE_PUBLIC_KEY"] = "your_stripe_public_key"
    os.environ["STRIPE_SECRET_KEY"] = "your_stripe_secret_key"
    os.environ["STRIPE_WH_SECRET"] = "your_stripe_webhook_secret"

    ```

5. Now you need to run the initial migrations and create a "Superuser"

   1. Run the migrations to create the database:

        ```terminal
        python manage.py migrate
        ```

   2. Create a superuser:

        ```terminal
        python manage.py createsuperuser
        ```

6. Now load any fixtures you might have using: `python manage.py loaddata file-name.json`
7. Run your application: `python manage.py runserver`

#### Heroku Deployment

*Setup a PostgreSQL Database*

1. You can setup a postgres database using a web service like AWS, however my project uses a PostgreSQL database from Code Institute and is only available to students.
2. Keep note of the databse URL.

*Heroku Setup*

1. Log in to Heroku and create a new app.
2. Set the name of the app and choose your nearest region.
3. In the app settings, in Config Vars, add the following:

| Key | Value |
| --- | --- |
| `AWS_ACCESS_KEY_ID` | user's own value |
| `AWS_SECRET_ACCESS_KEY` | user's own value |
| `DATABASE_URL` | user's own value |
| `EMAIL_HOST_PASS` | user's own value |
| `EMAIL_HOST_USER` | user's own value |
| `SECRET_KEY` | user's own value |
| `STRIPE_PUBLIC_KEY` | user's own value |
| `STRIPE_SECRET_KEY` | user's own value |
| `STRIPE_WH_SECRET` | user's own value |
| `USE_AWS` | True |

*Configure the DB*

1. In settings.py, set up the database:

  ```python
  import dj_database_url

  DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
  }
  ```

2. In your terminal, run the following command: `python manage.py showmigrations`, this should show you a list of migrations that aren't checked.
3. Migrate these using the following command: `python manage.py migrate`
4. Create a superuser using the following command: `python manage.py createsuperuser`
5. In your environment variables add: `os.environ[DEVELOPMENT] = "True"`
6. Remove the `DATABASE_URL` from your settings.py file and replace it with this block of code:

    ```python
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
        }
    ```

7. Finally, push your changes to Github.

*Deploying to Heroku*

Create a Procfile and add the following: `web: gunicorn kickin_it.wsgi:application` with a blank line at the bottom of the file.

For Heroku deployment, you can follow these steps to connect to the new app.

- Select Automatic Deployment from the Heroku App.

Or:

- In the Terminal connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a <your_app_name>`
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type: `git push heroku main`

#### GMAIL Setup

#### AWS Setup

1. **Create an AWS S3 bucket**
   - Log-in to your AWS account, and navigate to the service "S3".
   - Click "Create Bucket", name it the same as your Heroku app, and choose your region.
   - Make sure "Block All Public Access" is unchecked.
   - Create the Bucket.

2. **Enable static website hosting**
   - In the newly created S3 bucket, click on the "Properties" tab.
   - Scroll to Static Website Hosting, click "Edit" and select "Enable".
   - Use 'index.html' as the index file and 'error.html' as the error file.
   - Save your changes

3. **Setup Permissions**
   

#### Stripe Setup

### References

https://purepng.com/photo/1717/logos-nike-logo#google_vignette

<div>Icons made by <a href="https://www.flaticon.com/authors/pixel-perfect" title="Pixel perfect">Pixel perfect</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div><div>Icons made by <a href="https://www.flaticon.com/authors/vectors-tank" title="Vectors Tank">Vectors Tank</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div><div>Icons made by <a href="https://www.flaticon.com/authors/revolutionizzed-1" title="revolutionizzed_1">revolutionizzed_1</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

<a href="https://www.flaticon.com/free-icons/sneakers" title="sneakers icons">Sneakers icons created by Nhor Phai - Flaticon</a>

All Sneaker Images are from <a href="https://thesneakerdatabase.com/sneakers" title="sneakers">The Sneaker Database</a>

#### Acknowledgements