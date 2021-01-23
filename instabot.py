from pages import StartPage
from selenium import webdriver

def press_likes(login, password, request):

    browser = webdriver.Firefox(executable_path=r'/usr/bin/geckodriver')
    browser.implicitly_wait(5)

    home_page = StartPage(browser)

    login_page = home_page.go_to_login_page()
    login_page.login(login, password)

    hub_page = home_page.go_to_hub_page()
    search_page = hub_page.search_for(request)
    search_page.click_on_post()

    for like in range(100):
        search_page.press_like()
        search_page.next_post()

#browser.close()


press_likes('YOUR LOGIN HERE', 'YOUR PASSWORD HERE', 'YOUR REQUEST HERE')
