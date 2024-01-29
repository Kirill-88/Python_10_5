import os

from selene import browser, by, have


def test_contact_information():
    browser.open('/')
    browser.element('#firstName').type('Kirill').press_tab()
    browser.element('#lastName').type('Lyutkin').press_tab()
    browser.element('#userEmail').type('Kirill@mail.ru')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('8901372384')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select').click().element(by.text("2001")).click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select').element(by.text('November')).click()
    browser.element('.react-datepicker__day--026').click()

    browser.element('#subjectsInput').type('Arts').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('input[type="file"').send_keys(os.path.abspath('qa-2-min.jpeg'))
    browser.element('#currentAddress').type('п. Хатанга, ул. Безымянная, д. 7/6 стр. 53, 606814')
    browser.element('#state').click()
    browser.element(by.text('Haryana')).click()
    browser.element('#city').click()
    browser.element(by.text('Karnal')).click()
    browser.element('#submit').click()

    browser.element('.table').all('td:nth-child(2)').should(have.texts(
        'Kirill Lyutkin',
        'Kirill@mail.ru',
        'Male',
        '8901372384',
        '26 November,2001',
        'Arts',
        'Sports, Reading, Music',
        'qa-2-min.jpeg',
        'п. Хатанга, ул. Безымянная, д. 7/6 стр. 53, 606814',
        'Haryana Karnal'
    ))
