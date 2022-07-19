import random
import time

from selenium.webdriver.common.by import By

from data.data import PersonInfo
from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fieilds(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        cur_address = person_info.current_address
        perm_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(cur_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(perm_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, cur_address, perm_address

    def get_filled_form(self):
        full_name = self.element_is_presence(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_presence(self.locators.CREATED_EMAIL).text.split(':')[1]
        cur_address = self.element_is_presence(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        perm_address = self.element_is_presence(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, cur_address, perm_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()
    T = ['Home',
         [['Desktop',
           ['Notes', 'Commands']],
          ['Documents',
           ['WorkSpace', 'Office']],
          ['Downloads',
           ['Word File.doc', 'Excel File.doc']]]]

    def open_full_list(self):
        self.element_is_visible(self.locators.BTN_EXPAND_ALL).click()

    def get_item_list(self):
        return self.elements_are_visible(self.locators.ITEM_LIST)

    def click_random_checkbox(self):
        item_list = self.get_item_list()
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_elements(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_elements(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEM_LIST)
        data = []
        for item in checked_list:
            title_item = item.find_element_by_xpath(self.locators.TITLE_ITEM)
            data.append(title_item.text.replace(' ', '').replace('doc', '').replace('.', '').lower())
        return data

    def get_output_checked(self):
        output_result = self.elements_are_present(self.locators.SUCCESS_TITLE)
        data = []
        for item in output_result:
            data.append(item.text.replace(' ', '').lower())
        return data

    def print_tree(self):
        item_list = self.T
        self.print_tree_rec(item_list[1])

    def print_tree_rec(self, item_list):
        if type(item_list) == list:
            for i in range(len(item_list)):
                self.print_tree(item_list[i])
        else:
            print(item_list)

    def element_is_checked(self, element):
        checked_list = self.elements_are_visible(self.locators.CHECKED_ITEM_LIST)
        for checked in checked_list:
            if checked.text == element:
                return True
        return False


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def click_on_the_radio_button(self, choice):
        choices = {
            'Yes': self.locators.YES_RADIOBUTTON,
            'Impressive': self.locators.IMPRESSIVE_RADIOBUTTON,
            'No': self.locators.NO_RADIOBUTTON
        }
        element = self.element_is_visible(choices[choice])
        self.go_to_elements(element)
        element.click()

    def get_output_result(self):
        return self.element_is_presence(self.locators.SUCCESS_TEXT).text


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    def add_new_persons(self):
        add_button = self.element_is_visible(self.locators.ADD_BUTTON)
        person_info = next(generated_person())
        first_name = person_info.first_name
        last_name = person_info.last_name
        email = person_info.email
        age = person_info.age
        salary = person_info.salary
        department = person_info.department
        add_button.click()
        self.element_is_visible(self.locators.FIRSTNAME_FORM).send_keys(person_info.first_name)
        self.element_is_visible(self.locators.LASTNAME_FORM).send_keys(person_info.last_name)
        self.element_is_visible(self.locators.EMAIL_FORM).send_keys(person_info.email)
        self.element_is_visible(self.locators.AGE_FORM).send_keys(person_info.age)
        self.element_is_visible(self.locators.SALARY_FORM).send_keys(person_info.salary)
        self.element_is_visible(self.locators.DEPARTMENT_FORM).send_keys(person_info.department)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return [first_name, last_name, str(age), email, str(salary), department]

    def get_full_table(self):
        person_list = self.elements_are_present(self.locators.FULL_PERSON_TABLE)
        data_list = []
        for item in person_list:
            data_list.append(item.text.splitlines())
        return data_list

    def search_some_person(self, keyword):
        self.element_is_visible(self.locators.SEARCH_BOX).clear()
        self.element_is_visible(self.locators.SEARCH_BOX).send_keys(keyword)

    def check_search_person(self):
        delete_button = self.element_is_visible(self.locators.DELETE_BUTTON)
        row = delete_button.find_element_by_xpath(self.locators.ROW_PARENT)
        return row.text.splitlines()

    def update_person_info(self):
        update_button = self.element_is_visible(self.locators.EDIT_BUTTON)
        update_button.click()
        person_info = next(generated_person())
        first_name = person_info.first_name
        last_name = person_info.last_name
        email = person_info.email
        age = person_info.age
        salary = person_info.salary
        department = person_info.department
        self.element_is_visible(self.locators.FIRSTNAME_FORM).clear()
        self.element_is_visible(self.locators.FIRSTNAME_FORM).send_keys(first_name)
        self.element_is_visible(self.locators.LASTNAME_FORM).clear()
        self.element_is_visible(self.locators.LASTNAME_FORM).send_keys(last_name)
        self.element_is_visible(self.locators.EMAIL_FORM).clear()
        self.element_is_visible(self.locators.EMAIL_FORM).send_keys(email)
        self.element_is_visible(self.locators.AGE_FORM).clear()
        self.element_is_visible(self.locators.AGE_FORM).send_keys(age)
        self.element_is_visible(self.locators.SALARY_FORM).clear()
        self.element_is_visible(self.locators.SALARY_FORM).send_keys(salary)
        self.element_is_visible(self.locators.DEPARTMENT_FORM).clear()
        self.element_is_visible(self.locators.DEPARTMENT_FORM).send_keys(department)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return [first_name, last_name, str(age), email, str(salary), department]

    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    def check_empty_table(self):
        return self.element_is_presence(self.locators.EMPTY_TABLE_TEXT).text

    def select_up_to_some_rows(self, count, driver):
        count = [5, 10, 20, 25, 50, 100]
        capture_path = 'C:/capture/your_desired_filename.png'
        driver.save_screenshot(capture_path)
        data = []
        count_row_button = self.element_is_visible(self.locators.SELECTOR_SIZE_TABLE)
        for i in count:
            self.go_to_elements(count_row_button)
            count_row_button.click()
            self.element_is_visible((By.CSS_SELECTOR, f'option[value="{i}"]')).click()
            driver.save_screenshot(capture_path)
            data.append(len(self.get_full_table()))
        return data



