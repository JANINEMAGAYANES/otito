from selenium import webdriver
from django.test import SimpleTestCase, TestCase, Client, RequestFactory
from core.models import ( Item, OrderItem, Order, Address, Payment, Coupon, Refund, UserProfile )
from core.views import ( HomeView, ItemDetailView, CheckoutView, ShopView, OrderSummaryView, add_to_cart, remove_from_cart, remove_single_item_from_cart, PaymentView,  AddCouponView, RequestRefundView )
from core.forms import ( CheckoutForm, CouponForm, RefundForm, PaymentForm )
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse, resolve, reverse_lazy
import time

# Login Page Test
class TestLoginPage(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('functional_test/chromedriver.exe')
        self.link = "http://127.0.0.1:8000/accounts/login/"
        self.csrf_client = Client(enforce_csrf_checks=True)
        self.browser.get(self.link)
        time.sleep(5)
    
    def tearDown(self):
        self.browser.close()

    # Sign Up Link Test
    def test_signuplink(self):
        # WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-signup"))).click()
        self.browser.get(self.link)
        element = self.browser.find_element_by_class_name('signin')
        element.find_elements_by_tag_name('a')[0].click()
        signup = "http://127.0.0.1:8000/accounts/signup/"
        self.assertEquals(
            self.browser.current_url,
            signup
        )
    
    # Login Process Test
    def testlogin(self):
        self.browser.get(self.link)
        self.csrf_client = Client(enforce_csrf_checks=True)
        useremail = self.browser.find_element_by_name("login")
        password = self.browser.find_element_by_name("password")
        login = self.browser.find_element_by_class_name("signinbtn")
        useremail.send_keys("jin") 
        password.send_keys("Onedirection143")
        login.click()
        actualurl="http://127.0.0.1:8000/"
        self.assertEquals(self.browser.find_element_by_class_name("shoppingcart").text, "Cart")
        self.assertEquals(self.browser.current_url,actualurl);
    