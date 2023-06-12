# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep
driver = webdriver.Chrome()
site_sbis_ru = 'https://sbis.ru/'
title_site_sbis = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'
site_tensor = 'https://tensor.ru/'

try:  # Закрываем браузер если что-то пошло не так
    driver.maximize_window()
    driver.get(site_sbis_ru)  # Переходим на сайт (проверка URL, title)
    sleep(1)
    print('Проверить адрес и заголовок сайта')
    assert driver.current_url == site_sbis_ru, 'Не верно открыт сайт'
    assert driver.title == title_site_sbis, 'Не верный заголовок'

    print('Проверить отображение 4 вкладок')
    tabs = driver.find_elements(By.CSS_SELECTOR, '.sbisru-Header__menu-item')
    assert len(tabs) == 4, 'Должно быть 4 вкладки'

    print('Проверить текст, атрибут и видимость кнопки "Контакты"')
    contact_button = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item-1')
    assert contact_button.text == 'Контакты', 'Не верный текст кнопки'
    assert contact_button.get_attribute('title') == '', 'Лишние данные'
    assert contact_button.is_displayed(), 'Кнопка не отображается'
    contact_button.click()
    sleep(2)

    print('Проверить отображение 4 вкладок в новом окне')
    tabs_on_new_page = driver.find_elements(By.CSS_SELECTOR, '.sbisru-Header__menu-item')
    assert len(tabs_on_new_page) == 4, 'Должно быть 4 вкладки'

    print('Проверить текст и отображение кнопки "Контакты"')
    contact_in_new_page = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-link--selected')  # Ищем кнопку "Контакты"
    assert contact_in_new_page.text == 'Контакты', 'Не верный текст'
    assert contact_in_new_page.is_displayed(), 'Кнопка не отображается'

    print('Проверить атрибут и отображение баннера "Тензор"')
    tenzor_bunner = driver.find_element(By.CSS_SELECTOR,'.sbisru-Contacts__logo-tensor.mb-8')
    assert tenzor_bunner.get_attribute('title') == 'tensor.ru', 'Не верные данные'
    assert tenzor_bunner.is_displayed(), 'Баннер отображается'
    sleep(2)
    tenzor_bunner.click()

    print('Проверить адрес и заголовок сайта')
    driver.switch_to.window(driver.window_handles[1])
    sleep(2)
    assert driver.current_url == site_tensor, 'Не верно открыт сайт'
    assert driver.title == 'Тензор — IT-компания', 'Не верный текст'

    print('Проскролить страницу и проверить, что в новостях есть блок "Сила в людях"')
    strength_in_people = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content.tensor_ru-Index__card')
    sleep(2)
    strength_in_people.location_once_scrolled_into_view  # Скролим до нужного блока новостей
    assert strength_in_people.is_displayed(), 'Блок "Сила в людях" не отображается'
    sleep(3)

    print('Проверить текст и наличие кнопки "Подробнее" в блоке "Сила в людях"')
    more_button = driver.find_element(By.CSS_SELECTOR, '[href="/about"].tensor_ru-link.tensor_ru-Index__link')
    assert more_button.text == 'Подробнее', 'Должен быть текст "Подробнее"'
    assert more_button.is_displayed(), 'Кнопка "Подробнее отображается"'

    print('Проверить адрес  заголовок сайта')
    more_button.click()
    sleep(3)
    assert driver.current_url == 'https://tensor.ru/about', 'Не верный сайт'
    assert driver.title == 'О компании | Тензор — IT-компания', 'Не верный текст'
finally:
    driver.quit()