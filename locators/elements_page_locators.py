from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # TextBox Form
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')
    # created
    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')


# CheckBox
class CheckBoxPageLocators:
    BTN_EXPAND_ALL = (By.CSS_SELECTOR, "button[title='Expand all']")
    BTN_COLLAPSE_ALL = (By.CSS_SELECTOR, "button[title='Collapse all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEM_LIST = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    SUCCESS_TITLE = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonPageLocators:
    YES_RADIOBUTTON = (By.CSS_SELECTOR, "label[for='yesRadio']")
    IMPRESSIVE_RADIOBUTTON = (By.CSS_SELECTOR, "label[for='impressiveRadio']")
    NO_RADIOBUTTON = (By.CSS_SELECTOR, "label[for='noRadio']")
    SUCCESS_TEXT = (By.CSS_SELECTOR, "span[class='text-success']")

class WebTablePageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")
    FIRSTNAME_FORM = (By.CSS_SELECTOR, "input[id='firstName']")
    LASTNAME_FORM = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL_FORM = (By.CSS_SELECTOR, "input[id='userEmail']")
    AGE_FORM = (By.CSS_SELECTOR, "input[id='age']")
    SALARY_FORM = (By.CSS_SELECTOR, "input[id='salary']")
    DEPARTMENT_FORM = (By.CSS_SELECTOR, "input[id='department']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[id='submit']")

    #tables
    FULL_PERSON_TABLE = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    SEARCH_BOX = (By.CSS_SELECTOR, "input[id='searchBox']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "div[class='input-group-append']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"

