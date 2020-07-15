The steps below serves as a guide to clone the project repository and run in a local machine:

1. Download the Git repository and go to the main directory where manage.py is.

2. Create virtual env by typing “virtualenv venv” on the command line.

3. Activate the Virtual Environment. Type “source venv/bin/activate” on the command line.

4. Open the requirements.txt then  install the dependencies. Type “pip install -r requirements.txt” on the command line.

7. Run python manage.py makemigrations 

8. Run python manage.py migrate

9. Run python manage.py createsuperuser (enter your email and set your password)

10. Run python manage.py runserver


The steps below serves as a guide to navigate the app once its running on the local host:

1. Once the file is running at local host: http://127.0.0.1:8000/ , you will be directed in the homepage. Click on the Log In button to sign in on the app. 

2. Click on the Shop link to view all the Items on the menu and click on the photo to view the description.

3. On the Item Page, there is an option to add the Item on the cart.

4. The Cart Page is where you can view all the Items added on the Cart. This is also where the Checkout option is located.

5. After the checkout option is clicked, the page will be directed to the checkout page where the delivery, billing address and payment option must be selected. Once done, you can click on the Continue to Checkout that will route the page to the payment details.

6. The credit card details must be provided to be able to submit the order.

7. If the payment was successful, the page will be routed to the Shop Page, with the success message.

8. Once done, sign out on the app by clicking on the Log out page.

