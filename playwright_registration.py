from playwright.sync_api import sync_playwright, expect

"""
Откроет страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration
Заполнит поле "Email" значением "user.name@gmail.com"
Заполнит поле "Username" значением "username"
Заполнит поле "Password" значением "password"
Нажмет на кнопку "Registration". После нажатия кнопки "Registration" произойдет редирект на страницу "Dashboard"
Проверит, что на странице "Dashboard" отображается заголовок "Dashboard"
"""

# Открываем браузер с использованием Playwright
with sync_playwright() as playwright:
    # Запускаем Chromium браузер в обычном режиме (не headless)
    browser = playwright.chromium.launch(headless=False)
    # Создаем новый контекст браузера (новая сессия, которая изолирована от других)
    context = browser.new_context()
    # Открываем новую страницу в рамках контекста
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    _locator_dashboard = page.get_by_test_id("dashboard-toolbar-title-text")

    expect(_locator_dashboard).to_contain_text("Dashboard")


