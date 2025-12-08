from boto3.dynamodb.conditions import Attr, Key
from config.dynamodb import table

class SectionRepository:
    def get_all_sections(self):
        try:
            response = table.scan()
            return response.get('Items', [])
        except Exception as e:
            print(f"Error fetching sections: {str(e)}")
            raise e

    def get_section_by_id(self, section_id):
        try:
            response = table.get_item(Key={'id': section_id})
            return response.get('Item')
        except Exception as e:
            print(f"Error fetching section by id {section_id}: {str(e)}")
            raise e

    def get_section_by_name(self, name):
        try:
            response = table.scan(
                FilterExpression=Attr('name').eq(name)
            )
            items = response.get('Items', [])
            return items[0] if items else None
        except Exception as e:
            print(f"Error fetching section by name {name}: {str(e)}")
            raise e

    def get_section_by_section(self, section):
        try:
            response = table.query(
                IndexName = 'section-sections',
                KeyConditionExpression = Key('section').eq(section)
            )
            return response.get('Items', [])
        except Exception as e:
            print(f"Error fetching section by id {section}: {str(e)}")
            raise e
