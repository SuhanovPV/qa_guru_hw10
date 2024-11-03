from selene import browser, have, be
import allure


@allure.epic('github')
@allure.feature('github issues')
@allure.story('find issue in github')
@allure.title("Test find issue in repo. No steps")
@allure.description("This test find issue in repo issues. No allure steps.")
@allure.feature("Issues in repo")
@allure.tag("Issue", "Github" "NoSteps")
@allure.severity(allure.severity_level.MINOR)
@allure.label("owner", "Pavel Sukhanov")
@allure.link("https://github.com/SuhanovPV", name="Github")
@allure.testcase("HW10-1")
def test_search_issue_in_repo_selene_only():
    browser.open('/')

    browser.all('[data-tab-item="repositories"]').element_by(be.visible).click()
    browser.element('[href$="qa_guru_hw10"]').click()
    browser.element('#issues-tab').click()

    browser.element('#issue_1 a').should(have.exact_text('issue_for_test'))
