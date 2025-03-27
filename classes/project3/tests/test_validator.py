import pytest

from classes.project3.inventory.utils.validators import int_validator


class TestIntValidator:

    def test_valid(self):
        int_validator('arg', 10,0,20, 'min msg exception', 'max msg exception')

    def test_type_error(self):
        with pytest.raises(TypeError):
            int_validator('arg', 1.5,0,20, 'min msg exception', 'max msg exception')


    def test_value_error(self):
        with pytest.raises(ValueError):
            int_validator('arg', 1,10,20, 'min msg exception', 'max msg exception')


    def test_value_error_msg(self):
        with pytest.raises(ValueError) as ex:
            int_validator('arg', 1,10,20, 'min msg exception', 'max msg exception')

        assert str(ex.value) == 'min msg exception'