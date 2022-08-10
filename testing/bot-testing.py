# Imports
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import selenium.common.exceptions

import random
import time


def build_driver():
    return webdriver.Chrome(ChromeDriverManager().install())


def click_through(driver):
    # Clicks the "next" button
    driver.find_element_by_tag_name('button').click()


def demo_page(driver):
    time.sleep(2)
    question_boxes = driver.find_elements_by_class_name('mb-3.bg-light.border.pt-2.pb-2.px-2') # get all question boxes
    for box in question_boxes:
        inputs = box.find_elements_by_tag_name('input') # get the possible answers for each question
        if len(inputs) > 1: # if there's more than one option
            random_choice = random.randint(0,len(inputs)-1)
            try:
                inputs[random_choice].click()
            except selenium.common.exceptions.ElementClickInterceptedException:
                inputs[0].click() # todo: does this really work ?
                # print('    Asserting that the demo page error handling actually works')
        else: # if there's only one option, then we know that it's the age question
            random_year = random.randint(1952,2004)
            inputs[0].send_keys(str(random_year))

    # Click next
    try:
        click_through(driver)
    except selenium.common.exceptions.ElementClickInterceptedException:
        time.sleep(1)
        click_through(driver)


def baldeology(driver):
    question_boxes = driver.find_elements_by_class_name('mb-3.bg-light.border.pt-2.pb-2.px-2')
    for box in question_boxes:
        tables = box.find_elements_by_tag_name('table')
        if len(tables) > 1:
            for table in tables:
                inputs = table.find_elements_by_tag_name('input')
                random_choice = random.randint(0, len(inputs)-1)
                try:
                    inputs[random_choice].click()
                except selenium.common.exceptions.ElementClickInterceptedException:
                    time.sleep(1)
                    try:
                        inputs[0].click()
                    except selenium.common.exceptions.ElementClickInterceptedException:
                        time.sleep(1)
                        # todo: does this need another click?
                        # print('    Asserting that the error handling for baldeolgy actually works')

        else:
            inputs = box.find_elements_by_tag_name('input')
            random_choice = random.randint(0, len(inputs)-1)
            try:
                inputs[random_choice].click()
            except selenium.common.exceptions.ElementClickInterceptedException:
                time.sleep(1)
                inputs[0].click()
    # CLick next
    driver.find_element_by_tag_name('button').click()


def dumb_option(driver):
    inputs = driver.find_elements_by_tag_name('input')
    for inp in inputs:
        try:
            inp.click()
        except selenium.common.exceptions.ElementClickInterceptedException:
            time.sleep(2) # was 3, does it actually need to be this long?
            outer_html = inp.get_attribute('outerHTML')
            if 'type="text"' in outer_html:
                inp.send_keys('response')
            else:
                inp.click()
        except selenium.common.exceptions.ElementNotInteractableException:
            pass

    try:
        click_through(driver)
    except selenium.common.exceptions.ElementClickInterceptedException:
        time.sleep(1)
        click_through(driver)


def one_question(driver):
    # for the case in which there is only one radio question on the page
    inputs = driver.find_elements_by_tag_name('input')
    random_choice = random.randint(0, len(inputs)-1)

    try:
        inputs[random_choice].click()
    except selenium.common.exceptions.ElementClickInterceptedException:
        inputs[0].click()
    except selenium.common.exceptions.ElementNotInteractableException:
        time.sleep(1)
        try:
            driver.find_element_by_xpath('//*[@id="group3"]/input[1]').click()
        except selenium.common.exceptions.ElementClickInterceptedException:
            time.sleep(1)
            # driver.find_element_by_xpath('//*[@id="group3"]/input[1]').click()
            options = driver.find_elements_by_name('ba_ballot_pic1')
            if len(options)>0:
                options[0].click()
            else:
                ch_check_qs = driver.find_elements_by_name('ch_check_question')
                ch_check_qs[0].click()
        except selenium.common.exceptions.NoSuchElementException:
            options = driver.find_elements_by_name('ba_ballot_pic1')
            if len(options) > 0:
                options[0].click()
            else:
                ch_check_qs = driver.find_elements_by_name('ch_check_question')
                ch_check_qs[0].click()

    try:
        click_through(driver)
    except selenium.common.exceptions.ElementClickInterceptedException:
        time.sleep(1)
        driver.find_element_by_tag_name('button').click()


def table_many_questions(driver):
    trs =  driver.find_elements_by_tag_name('tr')
    for tr in trs:
        inputs =  tr.find_elements_by_tag_name('input')
        if len(inputs) > 0:
            random_choice = random.randint(0, len(inputs)-1)
            try:
                inputs[random_choice].click()
            except selenium.common.exceptions.ElementClickInterceptedException:
                time.sleep(2)
                inputs[0].click()
    try:
        driver.find_element_by_tag_name('button').click()
    except selenium.common.exceptions.ElementClickInterceptedException:
        time.sleep(1)
        click_through(driver)


def audio(driver):
    time.sleep(37)
    try:
        driver.find_element_by_tag_name('button').click()
    except selenium.common.exceptions.ElementClickInterceptedException:
        time.sleep(2)
        click_through(driver)


def cv_demo(driver):
    trs = driver.find_elements_by_tag_name('tr')
    for tr in trs:
        inputs = tr.find_elements_by_tag_name('input')
        if len(inputs) > 0:
            random_choice = random.randint(0, len(inputs)-1)
            try:
                inputs[random_choice].click()
            except selenium.common.exceptions.ElementClickInterceptedException:
                time.sleep(1)
                inputs[0].click()

    eligibility_qs = driver.find_elements_by_name('eligibility')
    eligibility_choice = random.randint(0,len(eligibility_qs)-1)
    eligibility_qs[eligibility_choice].click()

    participation_qs = driver.find_elements_by_name('participation')
    participation_choice = random.randint(0, len(participation_qs)-1)
    participation_qs[participation_choice].click()

    driver.find_element_by_tag_name('button').click()


def cv_demo_pg3(driver):
    boxes = driver.find_elements_by_class_name('mb-3.bg-light.border.pt-2.pb-2.px-2')
    # print(f"    Number of boxes: {len(boxes)}")
    for box in boxes:
        inputs = box.find_elements_by_tag_name('input')
        random_choice = random.randint(0, len(inputs) - 1)
        outer_html = inputs[random_choice].get_attribute('outerHTML')
        if 'type="radio"'in outer_html:
            try:
                inputs[random_choice].click()
            except selenium.common.exceptions.ElementClickInterceptedException:
                time.sleep(1)
                inputs[0].click()
        else:
            pass
    # todo: need to accomodate the text here
    ba_immigration_qs = driver.find_elements_by_name('ba_immigration1')
    for quest in ba_immigration_qs:
        quest.send_keys('response')
    try:
        driver.find_element_by_tag_name('button').click()
    except selenium.common.exceptions.ElementClickInterceptedException:
        time.sleep(1)
        click_through(driver)


def multi_radio_questions(driver):
    boxes = driver.find_elements_by_class_name('mb-3.bg-light.border.pt-2.pb-2.px-2')
    # print(f"    Number of boxes: {len(boxes)}")
    for box in boxes:
        inputs = box.find_elements_by_tag_name('input')
        random_choice = random.randint(0, len(inputs)-1)
        try:
            inputs[random_choice].click()
        except selenium.common.exceptions.ElementClickInterceptedException:
            time.sleep(1)
            inputs[0].click()

    try:
        driver.find_element_by_tag_name('button').click()
    except selenium.common.exceptions.ElementClickInterceptedException:
        time.sleep(1)
        click_through(driver)


def order_Ba_Ballot(driver):
    if 'BaIdeology' in driver.current_url:  # Check if the next page is BaIdeology
        print('-- BaIdeology first --')
        # Baldeology
        try:
            baldeology(driver)
        except Exception as e:
            # print('    ... Using dumb option')
            dumb_option(driver)

        try:
            # ballot example
            one_question(driver)
        except Exception as e:
            print('    ... Using dumb option')
            dumb_option(driver)
    if 'Ballot' in driver.current_url:
        print('-- Ballot example first --')
        try:
            # ballot example
            one_question(driver)
        except Exception as e:
            print('    ... Using dumb option')
            dumb_option(driver)

        # Baldeology
        try:
            baldeology(driver)
        except Exception as e:
            print('    ... Using dumb option')
            dumb_option(driver)


def run_bot( url):
    # Setup
    driver = build_driver()
    driver.get(url)

    # Action
    click_through(driver)  # First page
    demo_page(driver)  # Demo page
    print('-- Generic setup --')

    if 'screenout' in driver.current_url:  # Check if we're screened out
        print('Screened out')
        driver.close()
        return 'SUCCESS'

    if 'quotasfull' in driver.current_url:
        print('Full quota')
        driver.close()
        return 'SUCCESS'
    click_through(driver)  # Another welcome pg

    order_Ba_Ballot(driver) # Do the BaIdeology and the ballot example, depending on the order

    print('-- Starting SM section --')
    # another welcome page
    click_through(driver)
    try:
        # sm treatment page
        one_question(driver)
    except Exception as e:
        print('    Exception')
        dumb_option(driver)
    try:
        # sm_participation page
        table_many_questions(driver)
    except Exception as e:
        dumb_option(driver)
    # sm political page
    table_many_questions(driver)
    try:
        # sm demonstration page
        table_many_questions(driver)
    except selenium.common.exceptions.ElementClickInterceptedException:
        dumb_option(driver)

    print('-- Starting CH section --')
    # ch intro
    click_through(driver)
    try:
        # ch picture audio
        # print(f'---- Doing the CH audio page: {driver.current_url}')
        audio(driver)
    except selenium.common.exceptions.ElementClickInterceptedException:
        dumb_option(driver)
    # ch check rede
    print(f'---- Doing the CH check rede page: {driver.current_url}')
    one_question(driver)

    if 'ChSurvey_Charisma' in driver.current_url:
        print(f'---- Ch Survey Charisma: {driver.current_url}')
        # I think this is one table but im not sure
        table_many_questions(driver)
    else:
        pass
    if 'ChSurvey_Charisma' in driver.current_url:
        print(f'---- Ch Survey Charisma: {driver.current_url}')
        # I think this is one table but im not sure
        table_many_questions(driver)
    else:
        pass
    if 'ChEndPage' in driver.current_url:
        try:
            # ch end page
            print(f'---- Doing the CH end page: {driver.current_url}')
            click_through(driver)
        except selenium.common.exceptions.ElementClickInterceptedException:
            time.sleep(1)
            click_through(driver)
    else:
        print(f'---- Unknown page: {driver.current_url}')
        dumb_option(driver)

    print('-- Starting CV section --')
    print(f'---- CV demo page: {driver.current_url}')
    try:
        cv_demo(driver)  # Cv Demo
    except Exception as e:
        dumb_option(driver)
    if 'CvDemoPage2' in driver.current_url:
        print(f'---- CV demo page 2: {driver.current_url}')
        try:
            multi_radio_questions(driver)
        except Exception as e:
            print('    ... Using dumb option')
            dumb_option(driver)

        print(f'---- CV demo page 3: {driver.current_url}')
        cv_demo_pg3(driver)
        print(f'---- CV click through: {driver.current_url}')
        click_through(driver)
    else:
        print(f'---- CV demo page 3: {driver.current_url}')
        try:
            cv_demo_pg3(driver)  # Cv demo page 2
        except Exception as e:
            dumb_option(driver)
        print(f'---- CV click through: {driver.current_url}')
        try:
            click_through(driver)
        except Exception:
            time.sleep(1)
            click_through(driver)

    if 'complete' in driver.current_url:
        print(driver.current_url)
        driver.close()
        return '--SUCCESS--'
    else:
        driver.close()
        return f"Final Url: {driver.current_url}"

num_bots = 900
link = 'http://localhost:8000/join/denehize'
print(run_bot(link))


for i in range(num_bots):
    print(f"Number {i}")
    start = time.time()
    try:
        run_bot( link)
    except Exception as e:
        print(f'Exception: {e}')
        print('UNSUCCESSFUL')
    end = time.time()
    print(f"TOOK {end - start} seconds")
