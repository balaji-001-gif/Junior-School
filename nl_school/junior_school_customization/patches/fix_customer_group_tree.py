import frappe
from frappe.utils.nestedset import rebuild_tree

def execute():
    # Rebuild Customer Group tree to fix potential recursion errors
    rebuild_tree("Customer Group")
    frappe.db.commit()
