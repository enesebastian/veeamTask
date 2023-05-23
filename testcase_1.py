
# TEST CASE 1 STEPS

# Launch browser and open website
# Choose Research & Development from the lists of departments
# Choose English from the languages
# Count the number of jobs found
# Verify that expected value = number of jobs found


from veeamPages.VacanciesPage import VacanciesPage
from config import config_params as cfg
from setup.Setup import setup

# Launch browser and open website
driver, wait = setup()
vp = VacanciesPage(driver, wait)
vp.navigate_to_page()
vp.accept_cookies() # accept the cookies

# Choose Research & Development from the lists of departments
vp.select_department(cfg.DEPARTMENT)

# Choose English from the languages dropdown
vp.select_language(cfg.LANGUAGE)

# Count the number of jobs found
jobs_found = vp.count_available_jobs()

# Verify that expected value = number of jobs found
assert jobs_found == cfg.EXPECTED_JOBS, "Assertion failed, jobs count differ !"

print ("Test finished")
# driver.quit()
