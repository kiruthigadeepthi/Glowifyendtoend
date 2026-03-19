from pages.chatbot import ChatBot

def test_chatbot(driver):
    chat=ChatBot(driver)
    chat.load()
    chat.chatbot("Lipsticks")
    driver.save_screenshot("screenshots/chatbot.png")
    