# Features

This is a very basic Ecommerce application. I have developed following features.

## Catalogue of Products.

The catalogue of products is created using the app - `ecommerce.apps.catalogue`. Product have category, additional images, base image and few other featues. All the data have been added from Magento.

1. The products can be listed by category by viewing the category page. e.g. [http://ec2-52-91-71-216.compute-1.amazonaws.com/catalogue/items/hoodies--sweatshirts/](http://ec2-52-91-71-216.compute-1.amazonaws.com/catalogue/items/hoodies--sweatshirts/). The category page is paginated.
2. Each product has a detail page. e.g. [http://ec2-52-91-71-216.compute-1.amazonaws.com/catalogue/crown-summit-backpack/](http://ec2-52-91-71-216.compute-1.amazonaws.com/catalogue/crown-summit-backpack/).
3. Search page: A basic search page is created to browse products.  For e.g [http://ec2-52-91-71-216.compute-1.amazonaws.com/catalogue/search/?q=shirt](http://ec2-52-91-71-216.compute-1.amazonaws.com/catalogue/search/?q=shirt).


## Cart

The cart is developed with the app - `ecommerce.apps.cart`. When a user adds a product, its added to a cart. Non-logged in user can also add a product to the cart but it before checking out i.e. buying the user needs to create an account.

1. A single item can be added to the cart.
2. Multiple items can also be added to the cart.
3. Items can be removed from cart.
4. When User clicks checkout, the status of cart is changed to `submitted`


## User management

Features to Signup, login, change password and other basic user management have been added to the application.

## Admin

For agility in development, I have used Django's default admin page. It can be accessed via. /admin/ url. The admin page provides following facilities:

1. Admin can add a new product, update it or delete it.
2. Admin can add a new category, update it or delete it.
3. Admin can also view items which has been submitted by user for checkout and change the status after processing.
