import re
from xml.etree import ElementTree

BAD_SLUG_PATTERN = r"([/\\<>\s])"


def clean_fixture_field_name(field_name):
    """Effectively slugifies a fixture's field name so that we don't send
    bad XML back from the phone. Ideally, the fixture name should be
    verified as a good slug before using it.
    """
    subbed_string = re.sub(BAD_SLUG_PATTERN, '_', field_name)
    if subbed_string.startswith('xml'):
        subbed_string = subbed_string.replace('xml', '_', 1)
    return subbed_string


def is_identifier_invalid(name):
    """
    Determine if given name is an invalid XML identifier:
    - Blank
    - Contains special characters
    - Start with "xml"
    - Start with a number
    """
    if (not bool(name) or name.startswith('xml')):
        return True

    try:
        ElementTree.fromstring(u'<{} />'.format(name).encode('utf-8'))
    except ElementTree.ParseError:
        return True

    return False


def get_fields_without_attributes(fields):
    fields_without_attributes = []
    for fixture_field in fields:
        fields_without_attributes.append(fixture_field.field_name)
    return fields_without_attributes
