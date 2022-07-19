import time

import allure
from data.data import PersonInfo, Person
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage


@allure.suite("Test Elements")
class TestElements:
    @allure.feature("TextBox")
    class TestTextBox:
        @allure.title("Check TestBox")
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            full_name, email, cur_address, perm_address = text_box_page.fill_all_fieilds()
            output_name, output_email, output_cur_addr, out_per_addr = text_box_page.get_filled_form()
            assert full_name == output_name, "Full name is not match"
            assert email == output_email, "Email is not match"
            assert cur_address == output_cur_addr, "Current address is not match"
            assert perm_address == out_per_addr, "Permanent address is not match"

    @allure.feature("CheckBox")
    class TestCheckBox:
        @allure.title("Check CheckBox")
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            checked_box_elements = check_box_page.get_checked_elements()
            check_box_elements_out = check_box_page.get_output_checked()
            assert checked_box_elements == check_box_elements_out, "Checked elements and output data is not match"

    @allure.feature("RadioButtons")
    class TestRadioButton:
        @allure.title("Check RadioButton")
        def test_radio_click(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('Yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('No')
            output_no = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('Impressive')
            output_impressive = radio_button_page.get_output_result()
            with allure.step("Check 'Yes' button"):
                assert output_yes == 'Yes', "'Yes' is not selected"
            with allure.step("Check 'Impressive' button"):
                assert output_impressive == 'Impressive', "'Impressive' is not selected"
            with allure.step("Check 'No' button"):
                assert output_no == 'No', "'No' is not selected"

    @allure.feature("WebTables")
    class TestWebTables:
        @allure.feature("Check Fill Form")
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            new_person = web_table_page.add_new_persons()
            result_list = web_table_page.check_add_new_person()
            assert new_person in result_list

        @allure.feature("Check search person")
        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver,"https://demoqa.com/webtables")
            web_table_page.open()
            new_person = web_table_page.add_new_persons()[0]
            web_table_page.search_some_person(new_person)
            table_date = web_table_page.check_search_person()
            assert new_person in table_date, "Person was not found in table."


