

from tests.logger import LOG


def test_main(browser):
    LOG.info('Open page')
    browser.page.goto('https://alib.com.ua')
    assert 'Alib1' in browser.page.title()


def test_search(browser):
    browser.page.goto("https://alib.com.ua/")
    browser.page.get_by_role("textbox").fill("knut")
    browser.page.get_by_role("textbox").press("Enter")
    text = "Если ничего не найдено, укажите только автора или одно слово из названия. Примеры поиска"
    LOG.info('Check text')
    browser.set_expect_timeout(5000).expect(browser.locator("//p[3]")).to_contain_text(text)

