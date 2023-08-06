from base.colors import colors
from base.elements.base_element import BaseElement


class InputField(BaseElement):

    def enter_value(self, value):
        self._find()
        self.element.send_keys(value)
        assert self.element.get_attribute(
            'value') == str(
            value), f'Incorrect text in field. Expected "{value}", actually "{self.element.get_attribute("value")}".'

    def clear(self):
        self._find()
        self.element.clear()
        assert self.element.get_attribute('value') == '', f'Field is not empty.'

    def placeholder_equals(self, expected_value):
        self._find()
        assert self.element.get_attribute(
            'placeholder') == expected_value, f'Incorrect placeholder of the field. Expected "{expected_value}", \
                actually "{self.element.get_attribute("placeholder")}"'

    def border_color_equals(self, color):
        self._find()
        if self.element.value_of_css_property('border'):
            assert self.element.value_of_css_property('border-color') == colors[color], \
                f'Incorrect border color. Expected "{colors[color]}", actually "{self.element.value_of_css_property("border-color")}"'
        elif self.element.value_of_css_property('border-bottom'):
            assert self.element.value_of_css_property('border-color-bottom') == colors[color], f'Incorrect border color. \
                    Expected "{colors[color]}", actually "{self.element.value_of_css_property("border-color-bottom")}"'
