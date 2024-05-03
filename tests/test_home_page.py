

def test_main(browser):
    browser.page.goto('https://alib.com.ua')
    assert 'Alib' in browser.page.title()
    print(browser.page.title())


def test_search(browser):
    browser.page.goto("https://alib.com.ua/")
    browser.page.get_by_role("textbox").fill("knut")
    browser.page.get_by_role("textbox").press("Enter")
    text = "Если ничего не найдено, укажите только автора или одно слово из названия. Примеры поиска"
    browser.set_expect_timeout(5000).expect(browser.locator("//p[3]")).to_contain_text(text)

