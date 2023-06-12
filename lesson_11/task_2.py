# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from time import sleep
from selenium import webdriver
driver = webdriver.Chrome()
fix_site = 'https://fix-online.sbis.ru/'
autorization_site = 'https://fix-sso.sbis.ru/auth-online/?ret=fix-online.sbis.ru/'
title_fix_site = 'Вход в личный кабинет'

try:
    driver.maximize_window()
    driver.get(fix_site)
    sleep(2)
    print('Проверить адрес и заголовок сайта')
    assert driver.current_url == autorization_site, 'Не верный сайт'
    assert driver.title == title_fix_site, 'Не верный заголовок'

    print('Авторизация на сайте. Проверка корректности ввода логина/пароля')
    user_name, user_password = 'Мясо', 'Мясо123'
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys(user_name, Keys.ENTER)
    sleep(1)
    assert login.get_attribute('value') == user_name, 'Не верный логин'
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys(user_password)
    assert password.get_attribute('value') == user_password, 'Не верный пароль'
    enter_button = driver.find_element(By.CSS_SELECTOR, '.controls-BaseButton__wrapper.controls-Button__wrapper_viewMode-filled.controls-BaseButton__wrapper_captionPosition_end.controls-Button_textAlign-center.controls-Button__wrapper_filled_4xl')
    enter_button.click()
    sleep(2)

    print('Проверка правильности сайта и заголовка после авторизации на сайте')
    assert driver.current_url == fix_site, 'Не верный сайт'
    assert driver.title == 'СБИС', 'Не верный звгловок'
    # contacts = driver.find_element(By.CSS_SELECTOR, '[data-qa="Контакты"]')
    contacts_for_first_click = driver.find_element(By.CSS_SELECTOR, '[data-qa="NavigationPanels-Accordion__title"].NavigationPanels-Accordion__title.NavigationPanels-Accordion__title_level-1')
    action_chains = ActionChains(driver)
    # sleep(2)
    action_chains.click(contacts_for_first_click)
    action_chains.perform()
    sleep(2)
    contacts_for_second_click = driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle.NavigationPanels-SubMenu__title-with-separator.NavigationPanels-Accordion__prevent-default')
    action_chains.click(contacts_for_second_click)
    action_chains.perform()
    sleep(2)

    print('Проверить правильность сайта и заголовка после перехода в контакты')
    assert driver.current_url == 'https://fix-online.sbis.ru/page/dialogs', 'Не верный сайт'
    assert driver.title == 'Контакты', 'Не верный заголовок'

    print('Проверить кол-во вкладок на странице "Контакты"')
    tabs_in_contacts = driver.find_elements(By.CSS_SELECTOR, '.sabyPage-MainLayout__tabs_itemWrapper')
    assert len(tabs_in_contacts) == 4, 'Не верное количество вкладок'

    print('Проверить отображение кнопки создания диалога в шапке окна')
    message_button = driver.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')
    assert message_button.is_displayed(), 'Не отображается кнопка создания диалога'
    message_button.click()
    sleep(2)

    print('Проверить открытие окна добавления адресата в диалог')
    destination_window = driver.find_element(By.CSS_SELECTOR, '.controls-Popup.ws-float-area-show-complete')
    assert destination_window.is_displayed(), 'Окно добавления адресата не открылось'

    print('Проверить наличие строки поиска адресата')
    string_of_find = driver.find_element(By.CSS_SELECTOR, '.controls-Popup.ws-float-area-show-complete .controls-Field')
    assert string_of_find.is_displayed(), 'Строка поиска не отображается'

    print('Проверить корректность полученных результатов поиска')
    find_name = 'Мясников Георгий'
    string_of_find.send_keys(find_name)
    sleep(2)
    itog_of_found_destination = driver.find_elements(By.CSS_SELECTOR, '[class="controls-ListView__itemContent  controls-ListView__item_default-topPadding_s controls-ListView__item_default-bottomPadding_s controls-ListView__item-rightPadding_s controls-ListView__item-leftPadding_l "]')
    assert len(itog_of_found_destination) == 1, 'Найдены лишние адресаты'
    destination_name = driver.find_element(By.CSS_SELECTOR, '.ws-inline-flexbox.person-BaseInfo__titleContainer.person-BaseInfo__content')
    assert destination_name.text == find_name, 'Не верное имя адресата'
    destination_name.click()
    sleep(2)

    print('Проверить данные получателя, отображение поля ввода сообщения, корректности введенного сообщения и кнопки отправки сообщения')
    test_message = 'Привет! Это тестовый прогон'
    destination_in_message = driver.find_element(By.CSS_SELECTOR, '.ws-flexbox.ws-flex-column.msg-person-item__info-block')
    assert destination_in_message.text == find_name, 'Не верное имя адресата'
    message_field = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    assert message_field.is_displayed(), 'Не отображается поле ввода сообщения'
    message_field.send_keys(test_message)
    sleep(2)
    assert message_field.text == test_message, 'Не верный текст сообщения'
    message_sending = driver.find_element(By.CSS_SELECTOR, '.icon-BtArrow')
    assert message_sending.is_displayed(), 'Кнопка отправки сообщения не отображается'
    message_sending.click()
    sleep(2)

    print('Проверить реестр сообщений, получателя и текст сообщения')
    message_list = driver.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item')
    assert len(message_list) == 1, 'В реестре неверное кол-во сообщений'
    destination_in_message_list = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-dialogs-item__addressee"]')
    assert destination_in_message_list.text == find_name
    destination_message_text = driver.find_element(By.CSS_SELECTOR, '.msg-dialogs-item__content-inner')

    print('Проверить удаление сообщения')
    delete_message = driver.find_element(By.CSS_SELECTOR, '.msg-dialogs-item')
    sleep(2)
    action_chains = ActionChains(driver)
    action_chains.move_to_element(delete_message)
    action_chains.perform()
    sleep(2)
    delete_button = driver.find_element(By.CSS_SELECTOR, '[class="controls-Button__icon controls-BaseButton__icon controls-icon_size-m controls-icon_style-danger controls-icon icon-Erase"]')
    assert delete_button.is_displayed(), 'Нет кнопки удаления сообщения'
    delete_button.click()
    sleep(3)

    print('Проверить реестр после удаления сообщения')
    message_list = driver.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item')
    assert len(message_list) == 0, 'В реестре неверное кол-во сообщений'

finally:
    driver.quit()