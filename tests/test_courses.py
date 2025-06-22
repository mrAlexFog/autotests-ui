import pytest
from playwright.sync_api import expect, Page


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(
    chromium_page_with_state: Page
):
    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    _locator_title = chromium_page_with_state.get_by_test_id("courses-list-toolbar-title-text")
    expect(_locator_title).to_contain_text("Courses")

    _locator_sub_title = chromium_page_with_state.get_by_test_id("courses-list-empty-view-title-text")
    expect(_locator_sub_title).to_contain_text("There is no results")


@pytest.mark.parametrize(
    "email, password",
    [
        pytest.param("user.name@gmail.com", "password", id="Проверяем, что пользователь не может войти в систему с невалидными email и password"),
        pytest.param("user.name@gmail.com", "  ", id="Проверяем, что пользователь не может войти в систему с невалидным email, и пустым password"),
        pytest.param("  ", "password", id="Проверяем, что пользователь не может войти в систему с пустым email, и невалидным password")
    ]
)
def test_wrong_email_or_password_authorization(
    chromium_page: Page,
    email,
    password
): 
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
    email_input.fill(email)

    password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
    password_input.fill(password)

    login_button = chromium_page.get_by_test_id('login-page-login-button')
    login_button.click()

    wrong_email_or_password_alert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")

