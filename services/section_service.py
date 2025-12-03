from repositories.section_repository import SectionRepository
from utils.http_responses import build_response

class SectionService:
    def __init__(self):
        self.repository = SectionRepository()

    def get_sections(self, event):
        try:
            query_params = event.get('queryStringParameters') or {}
            section_id = query_params.get('id')
            name = query_params.get('name')

            if section_id:
                section = self.repository.get_section_by_id(section_id)
                if section:
                    return build_response(200, section)
                return build_response(404, {"message": "Section not found"})
            
            if name:
                section = self.repository.get_section_by_name(name)
                if section:
                    return build_response(200, section)
                return build_response(404, {"message": "Section not found"})

            sections = self.repository.get_all_sections()
            return build_response(200, sections)
        except Exception as e:
            return build_response(500, {"error": str(e)})
