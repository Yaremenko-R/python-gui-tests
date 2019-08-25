import pytest
from fixture.application import Application
import importlib


@pytest.fixture(scope="session")
def app(request):
    testdata = request.config.getoption("--testdata")
    fixture = Application(target="C:\\FreeAddressBookPortable\\AddressBook.exe", testdata=testdata)
    request.addfinalizer(fixture.destroy)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--testdata", action="store", default="groups.xlsx")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            test_data = load_form_module(fixture[5:])
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])


def load_form_module(module):
    return importlib.import_module("data.%s" % module).test_data