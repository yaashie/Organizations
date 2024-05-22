import unittest
from unittest.mock import MagicMock, create_autospec
from sqlalchemy.orm import Session
from Organizations.model.organization_model import OrganizationBase, ListOrganization
from Organizations.repository.organization_repository import Repository


class TestOrganizationRepository(unittest.TestCase):

    def setUp(self) -> None:
        self.mock_db_session = create_autospec(Session, instance=True)

    def test_organizations_read_repo(self) -> None:
        self.mock_db_session.query.return_value.all.return_value = [ListOrganization(id=1, name='Collance')]
        result = Repository.organizations_read_repo(self.mock_db_session)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].id, 1) #type: ignore
        self.assertEqual(result[0].name, 'Collance') #type: ignore

    def test_organization_create_repo(self) -> None:
        new_org = OrganizationBase(name='CCMG')
        self.mock_db_session.add = MagicMock()
        self.mock_db_session.commit = MagicMock()
        self.mock_db_session.refresh = MagicMock()
        created_org = Repository.organization_create_repo(self.mock_db_session, new_org) #type: ignore
        self.mock_db_session.add.assert_called_with(new_org)
        self.mock_db_session.commit.assert_called_once()
        self.mock_db_session.refresh.assert_called_with(new_org)
        self.assertEqual(created_org, new_org)


if __name__ == '__main__':
    unittest.main()
