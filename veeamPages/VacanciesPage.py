from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from config import config_params as cfg


class VacanciesPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def navigate_to_page(self):
        self.driver.get(cfg.VACANCIES_URL)  # navigate to the jobs list page
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "header-custom-spacer")))  # wait until page
        # loads
        self.driver.maximize_window()

    def accept_cookies(self):
        self.driver.find_element(By.ID, "cookiescript_accept").click()  # click Accept on the cookies menu

    def select_department(self, department_to_select=None):
        # dropdown_buttons = self.driver.find_elements(By.XPATH, "//button[@id='sl']")
        dropdown_buttons = self.wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//button[@id='sl']")
        ))
        departments_button = dropdown_buttons[0]  # departments is the first element in the list of dropdowns
        departments_button.click()
        # all_departments_list = self.driver.find_elements(By.XPATH, "//a[@class='dropdown-item']")
        all_departments_list = self.wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//a[@class='dropdown-item']")
        ))
        for department in all_departments_list:
            if department_to_select in department.text:
                department.click()

    def select_language(self, language_to_select=None):
        dropdown_buttons = self.driver.find_elements(By.XPATH, "//button[@id='sl']")
        languages_button = dropdown_buttons[1]  # languages is the 2nd element in the list of dropdowns
        languages_button.click()
        # all_languages_list = self.driver.find_elements(By.XPATH, "//label[@class='custom-control-label']")
        all_languages_list = self.wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//label[@class='custom-control-label']")
        ))
        for language in all_languages_list:
            if language_to_select in language.text:
                language.click()
        languages_button.click()  # close the dropdown

    def count_available_jobs(self):
        jobs = self.driver.find_elements(By.CLASS_NAME, "pb-2")  # get all jobs that are displayed on the page
        return len(jobs)
