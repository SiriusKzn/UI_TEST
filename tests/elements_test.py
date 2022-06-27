
from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            full_name, email, cur_address, perm_address = text_box_page.fill_all_fieilds()
            output_name, output_email, output_cur_addr, out_per_addr = text_box_page.get_filled_form()
            assert full_name == output_name, "Full name is not match"
            assert email == output_email, "Email is not match"
            assert cur_address == output_cur_addr, "Current address is not match"
            assert perm_address == out_per_addr, "Permanent address is not match"
