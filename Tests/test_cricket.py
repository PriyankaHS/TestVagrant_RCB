import pytest

from Pages.page_cricket import Cricket


@pytest.mark.usefixtures("setup_file")
class Test_Cricket:
    @pytest.fixture(autouse=True)
    def SetUp(self, setup_file):
        self.file = setup_file
        self.cricket = Cricket(self.file)

    # extracting the data of foreign players
    def test_cricket_player_validate(self):
        assert len(self.cricket.country_filter(country="india", not_in=True)) == 4

    # checking the role
    def test_cricket_role_validate(self):
        assert len(self.cricket.role_filter(role="Wicket-keeper")) >= 1

# In test layer, setup file is decorated with fixture and is injected with conftest set up file
# setup file is assigned to cricket is converted and called in constructor

