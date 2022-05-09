import time

link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_es_basket_button(browser):
    browser.get(link)
    # time.sleep(30) # time.sleep for check language
    button_add_to_basket = browser.find_elements_by_css_selector("button.btn-add-to-basket")
    assert button_add_to_basket, 'Basket button not found'