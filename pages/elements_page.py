import random
import time

from selenium.webdriver.common.by import By

from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators
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
