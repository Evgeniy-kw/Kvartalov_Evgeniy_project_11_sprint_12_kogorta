import data
import sender_stand_request


# Меняем значения в параметре "name" в теле запроса для создани набора
def get_kit_body(name):
    current_body = data.CREATE_KIT.copy()
    current_body["name"] = name
    return current_body


# Позитивные проверки
def positive_assert(name):
    kit_body_positive = get_kit_body(name)
    kit_response_positive = sender_stand_request.post_new_client_kit(kit_body_positive, data.AUTH_TOKEN)
    assert kit_response_positive.json()["name"] == name
    assert kit_response_positive.status_code == 201


# Негативные проверки с заполненным полем "name"
def negative_assert_with_name(name):
    kit_body_negative = get_kit_body(name)
    kit_response_negative = sender_stand_request.post_new_client_kit(kit_body_negative, data.AUTH_TOKEN)
    assert kit_response_negative.status_code == 400


# Негативные проверки с не заполненным полем "name"
def negative_assert_no_name(kit_body):
    kit_response_negative_no_name = sender_stand_request.post_new_client_kit(kit_body, data.AUTH_TOKEN)
    assert kit_response_negative_no_name.status_code == 400


# Позитивные тесты создания набора

# Проверка с параметром "name" - 1 символ
def test_create_kit_1_symbol_in_name_get_success_response():
    positive_assert("a")


# Проверка с параметром "name" - 511 символов
def test_create_kit_511_symbols_in_name_get_success_response():
    positive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


# Проверка с параметром "name" - буквы английского алфавита
def test_create_kit_english_letters_in_name_get_success_response():
    positive_assert("QWErty")


# Проверка с параметром "name" - буквы русского алфавита
def test_create_kit_russian_letters_in_name_get_success_response():
    positive_assert("Мария")


# Проверка с параметром "name" - спец. символы
def test_create_kit_has_special_symbols_in_name_get_success_response():
    positive_assert("\"№%@\",")


# Проверка с параметром "name" - пробелы внутри
def test_create_kit_has_space_in_name_get_success_response():
    positive_assert("Человек и КО")


# Проверка с параметром "name" - цифры
def test_create_kit_has_number_in_name_get_success_response():
    positive_assert("123")


# Негативные проверки

# Проверка с параметром "name" - пустой ввод
def test_create_kit_empty_name_get_error_response():
    negative_assert_with_name("")


# Проверка с параметром "name" - 512 символов
def test_create_kit_512_symbols_in_name_get_error_response():
    negative_assert_with_name("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


# Проверка с отсутствием параметра "name"
def test_create_kit_no_name_get_error_response():
    current_kit_body_negative_no_name = data.CREATE_KIT.copy()
    current_kit_body_negative_no_name.pop("name")
    negative_assert_no_name(current_kit_body_negative_no_name)


# Проверка с параметром "name" - число
def test_create_kit_numeric_type_name_get_error_response():
    negative_assert_with_name(123)
    
