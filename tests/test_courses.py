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

