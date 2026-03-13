import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def execute():
    # 1. Ensure custom field is correctly named and column exists
    create_custom_fields({
        "Assessment Plan": [{
            "fieldname": "custom_status",
            "fieldtype": "Select",
            "label": "Status",
            "options": "\nOpen\nClosed",
            "default": "Open",
            "insert_after": "academic_term",
            "allow_on_submit": 1,
        }]
    }, update=True)

    # 2. Update Number Card filters
    cards = ["Open Assessment Plans", "Closed Assessment Plans"]
    for card_name in cards:
        if frappe.db.exists("Number Card", card_name):
            card = frappe.get_doc("Number Card", card_name)
            # Update filters_json to use custom_status
            if card.filters_json and ('"fieldname": "status"' in card.filters_json or '"status"' in card.filters_json):
                new_filters = card.filters_json.replace('"status"', '"custom_status"')
                frappe.db.set_value("Number Card", card_name, "filters_json", new_filters)

    frappe.db.commit()
