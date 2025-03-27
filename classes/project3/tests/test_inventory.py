import pytest
from classes.project3.inventory.model.inventory import Resource

@pytest.fixture
def resource_mock():
    return {
        'name': 'resource_name',
        'manufacturer': 'company',
        'total':20,
        'allocated':5
        }

@pytest.fixture
def resource(resource_mock):
    return Resource(**resource_mock)

def test_resource_creation():
    resource = Resource('name', 'company', 20, 5)
    assert resource.name == 'name'
    assert resource.manufacturer == 'company'
    assert resource.total == 20
    assert resource.allocated == 5


def test_resource_creation2(resource_mock, resource):
    assert resource_mock['name'] == resource.name
    assert resource_mock['manufacturer'] == resource.manufacturer
    assert resource_mock['total'] == resource.total
    assert resource_mock['allocated'] == resource.allocated


def test_value_error():
    with pytest.raises(ValueError):
        Resource('name', 'company', -20, 5)


@pytest.mark.parametrize('value', [-1,0,1000])
def test_claim_invalid(resource, value):
    with pytest.raises(ValueError):
        resource.claim(value)   