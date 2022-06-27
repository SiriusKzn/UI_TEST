
from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators
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
