from selene import browser, have, be
import allure

@allure.epic('github')
@allure.feature('github issues')
@allure.story('find issue in github')
@allure.title("Test find issue in repo. Decorator steps")
@allure.description("This test find issue in repo issues. With allure steps as lambda")
@allure.feature("Issues in repo")
@allure.tag("Issue", "Github" "Lambda")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Pavel Sukhanov")
@allure.link("https://github.com/SuhanovPV", name="Github")
@allure.testcase("HW10-3")
def test_search_issue_in_repo_with_lambda_steps():
    with allure.step('Open page https://github.com/SuhanovPV'):
        browser.open('/')

    with allure.step('go to repositories list'):
        browser.all('[data-tab-item="repositories"]').element_by(be.visible).click()

    with allure.step('open required repository'):
        browser.element('[href$="qa_guru_hw10"]').click()

    with allure.step('open_isseues'):
        browser.element('#issues-tab').click()

    with allure.step('issues should have issue with text "issue_for_test"'):
        browser.element('#issue_1 a').should(have.exact_text('issue_for_test'))
