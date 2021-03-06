from selene.support.shared import browser
from selene import have
from selene.support.shared.jquery_style import s, ss
from demoqa_tests.resourse import resourse


def test_name(browser_config):

    browser.open('/automation-practice-form').driver.maximize_window()

    firstname = 'Anna'
    lastname = 'Hanna'
    email = '1@test.ru'
    gender = 'Other'
    phonenumber = '1111111111'
    month = 'April'
    year = '2000'
    # переменная day всегда должна быть обозначена двумя знаками: 01, 02, 15, 31
    day = '20'
    subject = 'English'
    hobby = 'Sports'
    picture = '1.jpg'
    address = 'my room'
    state = 'NCR'
    city = 'Delhi'

    s('#firstName').type(firstname)
    s('#lastName').type(lastname)
    s('#userEmail').type(email)
    s('[for="gender-radio-3"]').click()
    s('#userNumber').type(phonenumber)
    s('#dateOfBirthInput').click()
    s('.react-datepicker__month-select').type(month)
    s('.react-datepicker__year-select').type(year)
    s(f'.react-datepicker__day--0{day}').click()
    s('#subjectsInput').type(subject).press_enter()
    s('[for="hobbies-checkbox-1"]').click()
    s('#uploadPicture').send_keys(resourse(picture))
    s('#currentAddress').type(address)
    s('#react-select-3-input').set_value(state).press_enter()
    s('#react-select-4-input').set_value(city).press_enter()
    s('#submit').click()

    ss('table tbody tr').should(have.texts(
        f'{firstname} {lastname}',
        f'{email}',
        f'{gender}',
        f'{phonenumber}',
        f'{day} {month},{year}',
        f'Subjects {subject}',
        f'Hobbies {hobby}',
        f'Picture {picture}',
        f'Address {address}',
        f'State and City {state} {city}'))
