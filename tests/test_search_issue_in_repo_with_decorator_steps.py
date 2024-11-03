from selene import browser, have, be
import allure

@allure.epic('github')
@allure.feature('github issues')
@allure.story('find issue in github')
@allure.title("Test find issue in repo. Decorator steps")
@allure.description("This test find issue in repo issues. With allure steps as decorators")
@allure.feature("Issues in repo")
@allure.tag("Issue", "Github" "Decorators")
@allure.severity(allure.severity_level.MINOR)
@allure.label("owner", "Pavel Sukhanov")
@allure.link("https://github.com/SuhanovPV", name="Github")
@allure.testcase("HW10-2")
def test_search_issue_in_repo_with_decorator_steps():
    open_page()

    open_repositories_list()
    open_required_repository()
    open_issues()

    should_have_issue('issue_for_test')


@allure.step('Open page https://github.com/SuhanovPV')
def open_page():
    browser.open('/')

@allure.step('go to repositories list')
def open_repositories_list():
    browser.all('[data-tab-item="repositories"]').element_by(be.visible).click()

@allure.step('open required repository')
def open_required_repository():
    browser.element('[href$="qa_guru_hw10"]').click()

@allure.step('open_isseues')
def open_issues():
    browser.element('#issues-tab').click()

@allure.step('issues should have issue with text {issue}')
def should_have_issue(issue):
    browser.element('#issue_1 a').should(have.exact_text(issue))