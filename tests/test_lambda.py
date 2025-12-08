import unittest
from unittest.mock import MagicMock, patch
from services.section_service import SectionService
from repositories.section_repository import SectionRepository

class TestSectionService(unittest.TestCase):

    def setUp(self):
        self.mock_items = [
            {
                'id': '1', 
                'title': 'Iam Alejandro Fernández', 
                'subtitle': 'Desarrollador Web, Mobile y Cloud',
                'content': 'Desarrollador con experiencia en AWS...',
                'image_url': 'https://example.com/photo.jpg',
                'buttons': [{'text': 'Ver proyectos', 'link': '/proyectos'}]
            },
            {
                'id': '2', 
                'title': 'Skills', 
                'content': 'Node.js, Python, Java...'
            }
        ]

    @patch.object(SectionRepository, 'get_all_sections')
    def test_get_all_sections_success(self, mock_get_all):
        mock_get_all.return_value = self.mock_items
        
        service = SectionService()
        response = service.get_sections({}) # Empty event
        
        self.assertEqual(response['statusCode'], 200)
        self.assertIn('Iam Alejandro Fernández', response['body'])
        self.assertIn('Skills', response['body'])

    @patch.object(SectionRepository, 'get_section_by_id')
    def test_get_section_by_id_success(self, mock_get_by_id):
        mock_get_by_id.return_value = self.mock_items[0]
        
        service = SectionService()
        event = {'queryStringParameters': {'id': '1'}}
        response = service.get_sections(event)
        
        self.assertEqual(response['statusCode'], 200)
        self.assertIn('Iam Alejandro Fernández', response['body'])
        self.assertNotIn('Skills', response['body'])

    @patch.object(SectionRepository, 'get_section_by_name')
    def test_get_section_by_name_success(self, mock_get_by_name):
        mock_get_by_name.return_value = self.mock_items[1]
        
        service = SectionService()
        event = {'queryStringParameters': {'name': 'Skills'}}
        response = service.get_sections(event)
        
        self.assertEqual(response['statusCode'], 200)
        self.assertIn('Skills', response['body'])

    @patch.object(SectionRepository, 'get_section_by_id')
    def test_get_section_by_id_not_found(self, mock_get_by_id):
        mock_get_by_id.return_value = None
        
        service = SectionService()
        event = {'queryStringParameters': {'id': '999'}}
        response = service.get_sections(event)
        
        self.assertEqual(response['statusCode'], 404)

    @patch.object(SectionRepository, 'get_all_sections')
    def test_get_sections_error(self, mock_get_all_sections):
        mock_get_all_sections.side_effect = Exception("DynamoDB Error")
        
        service = SectionService()
        response = service.get_sections({})
        
        self.assertEqual(response['statusCode'], 500)
        self.assertIn('DynamoDB Error', response['body'])

    @patch.object(SectionRepository, 'get_section_by_section')
    def test_get_section_by_section_success(self, mock_get_by_section):
        mock_get_by_section.return_value = self.mock_items[0]
        
        service = SectionService()
        event = {'queryStringParameters': {'section': 'about'}}
        response = service.get_sections(event)
        
        self.assertEqual(response['statusCode'], 200)
        self.assertIn('Iam Alejandro Fernández', response['body'])
        self.assertNotIn('Skills', response['body'])

    @patch.object(SectionRepository, 'get_section_by_section')
    def test_get_section_by_section_not_found(self, mock_get_by_section):
        mock_get_by_section.return_value = None
        
        service = SectionService()
        event = {'queryStringParameters': {'section': '999'}}
        response = service.get_sections(event)
        
        self.assertEqual(response['statusCode'], 404)

if __name__ == '__main__':
    unittest.main()
