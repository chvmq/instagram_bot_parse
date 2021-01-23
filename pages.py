from time import sleep


class SearchPage:
    def __init__(self, browser):
        self.browser = browser

    def click_on_post(self):
        post = self.browser.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div")
        post.click()
        sleep(2)

    def press_like(self):
        like_button = self.browser.find_element_by_xpath(
            "/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button/div")
        like_button.click()
        sleep(2)

    def next_post(self):
        next_button = self.browser.find_element_by_css_selector("._65Bje")
        next_button.click()
        sleep(2)


class HubPage:
    def __init__(self, browser):
        self.browser = browser

    def search_for(self, request):
        text_request = self.browser.find_element_by_tag_name("input")
        text_request.send_keys(request)

        submit_button = self.browser.find_element_by_css_selector(
            "a.yCE8d:nth-child(1) > div:nth-child(1) > div:nth-child(2)")
        submit_button.click()

        return SearchPage(self.browser)


class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        username_input = self.browser.find_element_by_css_selector("input[name='username']")
        password_input = self.browser.find_element_by_css_selector("input[name='password']")

        username_input.send_keys(username)
        password_input.send_keys(password)

        login_button = self.browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()

        sleep(2)

    # confirm_button = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
    # confirm_button.click()
    #
    # confirm_button_2 = self.browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
    # confirm_button_2.click()


class StartPage:
    def __init__(self, browser):
        self.browser = browser

    def go_to_login_page(self):
        self.browser.get("https://instagram.com/")
        sleep(5)

        return LoginPage(self.browser)

    def go_to_hub_page(self):
        hub_button = self.browser.find_element_by_xpath(
            "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]")
        hub_button.click()

        sleep(2)

        return HubPage(self.browser)
