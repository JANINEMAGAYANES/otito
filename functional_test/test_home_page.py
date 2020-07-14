from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from core.models import ( Item, OrderItem, Order, Address, Payment, Coupon, Refund, UserProfile )
from core.views import ( HomeView, ItemDetailView, CheckoutView, ShopView, OrderSummaryView, add_to_cart, remove_from_cart, remove_single_item_from_cart, PaymentView,  AddCouponView, RequestRefundView )
from core.forms import ( CheckoutForm, CouponForm, RefundForm, PaymentForm )
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse, resolve, reverse_lazy
import time

# Home Page Test
class TestHomePage(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('functional_test/chromedriver.exe')
        self.link = "http://127.0.0.1:8000/"
        self.browser.get(self.link)
        time.sleep(5)
    
    def tearDown(self):
        self.browser.close()
    
    # Check Home Title
    def test_title(self):
        self.browser.get(self.link)
        title= self.browser.find_element_by_class_name("banner-title")
        self.assertEquals(title.find_element_by_tag_name("h1").text, "Otito Berlin")
    
    # # Check Home Link
    def test_homelink(self):
        self.browser.get(self.link)
        self.browser.find_element_by_class_name("otito").click()
        self.assertEquals(
            self.browser.current_url,
            self.link
        )

    # # def test_shoplink(self):
        self.browser.get(self.link)
        self.browser.find_element_by_class_name("shop").click()
        shop = self.link + "shop"
        self.assertEquals(
            self.browser.current_url,
            shop
        )

    
    # def test_loginlink(self):
        self.browser.get(self.link)
        self.browser.find_element_by_class_name("loggin").click()
        login = self.link + "accounts/login/"
        self.assertEquals(
            self.browser.current_url,
            login
        )
    
    
