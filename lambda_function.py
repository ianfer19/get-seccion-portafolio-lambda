from services.section_service import SectionService

def lambda_handler(event, context):
    service = SectionService()
    return service.get_sections(event)
