from pages.signup import Signup


def test_signup(driver):
    signup=Signup(driver)
    signup.load()
    signup.signup("Kiruthiga Ajith","kiruthigasns16@gmail.com","123456")
    