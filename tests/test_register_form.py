import os

from selene import browser, have


def test_register_form():
    browser.open('/automation-practice-form')

    # заполнение текстовых полей
    browser.element('#firstName').type('Имя')
    browser.element('#lastName').type('Фамилия')
    browser.element('#userEmail').type('testmail@mail.gg')

    # ввод номера телефона
    browser.element('#userNumber').type('2589632147')

    # выбор радиобаттона (проверка, что можно выбрать любой из трех)
    browser.element('label[for="gender-radio-1').click()
    browser.element('label[for="gender-radio-2').click()
    browser.element('label[for="gender-radio-3').click()

    # выбор даты рождения
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click().element('option[value="2004"]').click()
    browser.element('.react-datepicker__month-select').click().element('option[value="10"]').click()
    browser.element('.react-datepicker__day--019').click()

    # выбор хобби (чекбокс)
    browser.element('label[for="hobbies-checkbox-1"]').click()

    # subject
    browser.element('#subjectsInput').type('P').press_enter().type('ar').press_enter()

    # добавление фото
    browser.element('#uploadPicture').send_keys(os.path.abspath('test_image/test_image.jpg'))

    # добавление адреса
    browser.element('#currentAddress').type('221b, Baker Street, London, NW1 6XE, UK.')

    # дропбоксы
    browser.element('#react-select-3-input').type('n').press_enter()
    browser.element('#react-select-4-input').type('d').press_enter()

    # submit
    browser.element('#submit').click()

    browser.element('.table').all('tr td:nth-child(2)').should(have.texts(
        'Имя Фамилия',
        'testmail@mail.gg',
        'Other',
        '2589632147',
        '19 November,2004',
        'Physics, Arts',
        'Sports',
        'test_image.jpg',
        '221b, Baker Street, London, NW1 6XE, UK.',
        'NCR Delhi'
    ))
