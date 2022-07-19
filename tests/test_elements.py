import time

import allure
from data.data import PersonInfo, Person
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage


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
            result_list = web_table_page.get_full_table()
            assert new_person in result_list

        @allure.feature("Check search person")
        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver,"https://demoqa.com/webtables")
            web_table_page.open()
            new_person = web_table_page.add_new_persons()[0]
            web_table_page.search_some_person(new_person)
            table_date = web_table_page.check_search_person()
            assert new_person in table_date, "Person was not found in table."
        @allure.feature("Check Update Person")
        def test_web_table_update(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            new_person = web_table_page.add_new_persons()
            web_table_page.search_some_person(new_person[0])
            updated_person_info = web_table_page.update_person_info()
            web_table_page.search_some_person(updated_person_info[0])
            result_data = web_table_page.check_search_person()
            assert updated_person_info == result_data, "Person card has not been changed"

        @allure.feature("Check delete person")
        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            email = web_table_page.add_new_persons()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_empty_table()
            assert text == "No rows found"

        @allure.feature("Check change count rows.")
        def test_web_table_change_count_rows(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            web_table_page.remove_footer()
            count = [5, 10, 20, 25, 50, 100]
            result_data = web_table_page.select_up_to_some_rows(count, driver)
            assert result_data == count, "The number of rows in the table has been changed or has been incorrectly"

    @allure.feature("ButtonsPage")
    class TestButtonsPage:
        @allure.feature("Check double click.")
        def test_double_click_on_the_buttons(self, driver):
            button_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            button_page.open()
            msg = button_page.click_on_different_button("double")
            assert msg == "You have done a double click"

        @allure.feature("Check right click.")
        def test_right_click_on_the_buttons(self, driver):
            button_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            button_page.open()
            msg = button_page.click_on_different_button("right")
            assert msg == "You have done a right click"

        @allure.feature("Check click.")
        def test_dynamic_click_on_the_buttons(self, driver):
            button_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            button_page.open()
            msg = button_page.click_on_different_button("click")
            assert msg == "You have done a dynamic click"






