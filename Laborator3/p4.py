"""
   Build and return a string that represents the corresponding XML element.
"""


def build_xml_element(tag, content, **attributes):
    # Initialize the XML element string with the opening tag
    xml_element = f"<{tag}"

    # Add attributes to the element
    for key, value in attributes.items():
        xml_element += f' {key}="{value}"'

    # Close the opening tag
    xml_element += f">{content}</{tag}>"

    return xml_element


if __name__ == "__main__":
    result = build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
    print(result)
