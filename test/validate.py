#!/usr/bin/env python

from __future__ import print_function
from lxml import etree


if __name__ == "__main__":
    message = etree.parse("../export_message/export.message.example.xml")

    schema_doc = etree.parse("../export_message/export.message.schema.xsd")

    schema = etree.XMLSchema(schema_doc)


    schema.assertValid(message)