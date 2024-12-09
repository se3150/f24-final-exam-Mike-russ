from behave import given, when, then
from selenium.webdriver.common.by import By
import time

@given('I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"')
def step_impl(context):
    context.behave_driver.get("https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder")
    time.sleep(2)  # Wait for page to load

@when("when I enter a valid message")
def step_impl(context):
    type = context.behave_driver.find_element(By.ID, "decoder-setting")
    shift = context.behave_driver.find_element(By.ID, "shift-amount")
    message = context.behave_driver.find_element(By.ID, "letters")
    submit_button = context.behave_driver.find_element(By.ID, "submit")

    # Enter values
    type.select_by_index(0)
    shift.select_by_index(4)
    message.send_keys("Secret Message To Decode")
    submit_button.click()
    time.sleep(2)  # Wait for results to load

@then("I should get an encoded message")
def step_impl(context):
    result = context.behave_driver.find_element(By.ID, "decoded_message").text
    assert result == "Vhfuhw Phvvdjh Wr Ghfrgh"

@when("I enter an encoded message")
def step_impl(context):
    type = context.behave_driver.find_element(By.ID, "decoder-setting")
    shift = context.behave_driver.find_element(By.ID, "shift-amount")
    message = context.behave_driver.find_element(By.ID, "letters")
    submit_button = context.behave_driver.find_element(By.ID, "submit")

    # Enter values
    type.select_by_index(1)
    shift.select_by_index(4)
    message.send_keys("Vhfuhw Phvvdjh Wr Ghfrgh")
    submit_button.click()
    time.sleep(2)  # Wait for results to load

@then("then I should get a decoded message")
def step_impl(context):
    result = context.behave_driver.find_element(By.ID, "decoded_message").text
    assert result == "Secret Message To Decode"