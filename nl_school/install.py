import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def after_install():
    create_assessment_plan_custom_fields()


def create_assessment_plan_custom_fields():
    """Create custom fields that are required for the app to function."""
    create_custom_fields(
        {
            "Assessment Plan": [
                {
                    "fieldname": "custom_status",
                    "fieldtype": "Select",
                    "label": "Status",
                    "options": "\nOpen\nClosed",
                    "default": "Open",
                    "insert_after": "academic_term",
                    "allow_on_submit": 1,
                },
                {
                    "fieldname": "custom_exam_type",
                    "fieldtype": "Link",
                    "label": "Exam Type",
                    "options": "Exam Type",
                    "insert_after": "grading_scale",
                },
            ],
            "Student Attendance": [
                {
                    "fieldname": "custom_shift",
                    "fieldtype": "Link",
                    "label": "Shift",
                    "options": "Shift Type",
                    "insert_after": "link_nvfk",
                    "reqd": 1,
                },
                {
                    "fieldname": "custom_start_time",
                    "fieldtype": "Time",
                    "label": "Start Time",
                    "insert_after": "custom_shift",
                },
                {
                    "fieldname": "custom_end_time",
                    "fieldtype": "Time",
                    "label": "End Time",
                    "insert_after": "custom_start_time",
                },
            ],
            "Student Report Generation Tool": [
                {
                    "fieldname": "custom_teachers_comment",
                    "fieldtype": "Small Text",
                    "label": "Teachers Comment",
                    "insert_after": "assessment_terms",
                },
            ],
            "Student": [
                {
                    "fieldname": "custom_status",
                    "fieldtype": "Select",
                    "label": "Status",
                    "options": "Active\nInactive\nSuspended\nLeft",
                    "default": "Active",
                    "insert_after": "custom_student_id",
                },
                {
                    "fieldname": "custom_reason_for_exiting",
                    "fieldtype": "Select",
                    "label": "Reason For Exiting",
                    "options": "\nViolation of contract /parent hand book\nIllness or poor health \nPersonal and social reasons \nViolation of school rules by the child leading to expulsion\nRelocation\nOther(Reason for leaving)",
                    "insert_after": "leaving_certificate_number",
                },
            ],
            "Company": [
                {
                    "fieldname": "custom_rubber_stamp",
                    "fieldtype": "Attach Image",
                    "label": "Rubber Stamp",
                    "insert_after": "old_parent",
                },
            ],
            "Education Settings": [
                {
                    "fieldname": "custom_autocreate_academic_year",
                    "fieldtype": "Check",
                    "label": "Autocreate Academic Year",
                    "insert_after": "school_college_logo",
                },
                {
                    "fieldname": "custom_auto_enroll_students_yearly",
                    "fieldtype": "Check",
                    "label": "Auto Enroll Students Yearly",
                    "insert_after": "school_college_logo",
                },
            ],
        },
        update=True,
    )
