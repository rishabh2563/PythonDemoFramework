import pytest
from selenium.webdriver.support.select import Select
from Testdata.Homepagedata import HomepageData
from Utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage


class Testtwo(BaseClass):

    def test_formsubmission(self, getdata):
        homepage = HomePage(self.driver)
        homepage.get_name(getdata["firstname"])
        homepage.get_email(getdata["email"])
        homepage.get_password(getdata["password"])
        homepage.get_checkbox()
        sel = Select(homepage.get_dropdown())
        sel.select_by_visible_text(getdata["gender"])
        homepage.get_status()
        homepage.get_dob("12/10/1996")
        homepage.get_submitbtn()
        self.driver.refresh()

    @pytest.fixture(params=HomepageData.gettestdata("Testcase2"))
    def getdata(self, request):
        return request.param
