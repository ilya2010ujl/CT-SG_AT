import time

import pytest
import element_action


class TestRequestCallForm:

    @pytest.mark.case_id(1)
    def test_validation_tooltip(self, page):
        element_action.navigation_action.open_index_page(page)
        element_action.field_action.type_text_in_field_by_name(page, field_name='Фамилия', text='34242')
        element_action.button_action.click_on_button_by_name(page, "Отправить")
        element_action.field_action.tooltip_for_field_is(page, 'Имя', 'Поле обязательно для заполнения')
        element_action.field_action.tooltip_for_field_is(page, 'Телефон', 'Поле обязательно для заполнения')
        element_action.field_action.tooltip_for_field_is(page, 'E-mail', 'Поле обязательно для заполнения')
        element_action.field_action.tooltip_for_field_is(page, 'Продукт', 'Поле обязательно для заполнения')
        element_action.field_action.tooltip_for_field_is(page, 'Комментарий', 'Поле обязательно для заполнения')
