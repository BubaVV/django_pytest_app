""" Note that there should be a pytest.ini within the project root

[pytest]
DJANGO_SETTINGS_MODULE = test_project.settings
python_files = tests.py test_*.py *_tests.py
"""

from django.urls import reverse

import pytest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


from test_app.models import Product




@pytest.fixture
def product():
    return Product.objects.create(name='Hose')


@pytest.fixture
def browser(request):
    def finalizer():
        driver.close()
    request.addfinalizer(finalizer)

    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)

    return driver


@pytest.mark.django_db()
def test_product():
    product = Product.objects.create(name='Hose')
    assert product.name == 'Hose'


@pytest.mark.selenium
@pytest.mark.django_db()
def test_add_product_with_click(live_server, browser):
    browser.get(live_server.url + reverse('test_app:product-create'))

    input = browser.find_element_by_id('id_name')
    input.send_keys('Product 1')

    button = browser.find_element_by_id('create-product')
    button.click()

    p = Product.objects.first()

    assert Product.objects.count() == 1
    assert p.name == 'Product 1'


@pytest.mark.selenium
@pytest.mark.django_db()
def test_add_product_by_enter(live_server, browser):
    browser.get(live_server.url + reverse('test_app:product-create'))

    input = browser.find_element_by_id('id_name')
    input.send_keys('Product 2')
    input.send_keys(Keys.RETURN)

    p = Product.objects.first()

    assert Product.objects.count() == 1
    assert p.name == 'Product 2'


@pytest.mark.selenium
@pytest.mark.django_db()
def test_delete_product(live_server, browser, product):
    browser.get(live_server.url + reverse('test_app:product-detail', kwargs={'pk': product.pk}))
    delete_link = browser.find_element_by_xpath("//a[text()='Delete']")
    delete_link.click()

    confirm_button = browser.find_element_by_xpath("//input[@value='Confirm']")
    confirm_button.click()

    assert Product.objects.count() == 0


@pytest.mark.selenium
@pytest.mark.django_db()
def test_product_list(live_server, browser):
    browser.get(live_server.url + reverse('test_app:product-list'))
    'No objects yet.' in browser.page_source

    Product.objects.create(name="Hose")
    browser.get(live_server.url + reverse('test_app:product-list'))
    'Hose' in browser.page_source
    'No objects yet.' not in browser.page_source
