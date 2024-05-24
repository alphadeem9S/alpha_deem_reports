# Copyright (c) 2023, Smart Solutions and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.utils import flt, month_diff


def execute(filters=None):
	columns = get_columns()
	data = []

	data = frappe.db.get_all(
		"Project",
		filters=filters,
		fields=[
			"name",
			"project_name",
			"status",
			"percent_complete",
			"project_percentage",
			"expected_start_date",
			"expected_end_date",
			"customer",
			"project_amount",
			"tax_amount",
			"grand_total",
			"total_billed_amount"
		]
	)

	for project in data:
		complete = flt(project["percent_complete"], precision=2)
		project["percent_complete"] = f"{complete} %"

		project["project_duration"] = month_diff(project["expected_end_date"], project["expected_start_date"]) if project["expected_end_date"] and project["expected_start_date"] else 0

	return columns, data


def get_columns():
	return [
		{
			"fieldname": "name",
			"label": _("Project"),
			"fieldtype": "Link",
			"options": "Project",
			"width": 120,
		},
		{
			"fieldname": "project_name",
			"label": _("Project Name"),
			"fieldtype": "Data",
			"width": 200,
		},
		{
			"fieldname": "customer",
			"label": _("Customer"),
			"fieldtype": "Link",
			"options": "Customer",
			"width": 150,
		},
		{"fieldname": "status", "label": _("Status"), "fieldtype": "Data", "width": 120},
		{"fieldname": "project_amount", "label": _("Project Amount"), "fieldtype": "Currency", "width": 120},
		{"fieldname": "tax_amount", "label": _("Tax Amount"), "fieldtype": "Currency", "width": 120},
		{"fieldname": "grand_total", "label": _("Grand Total"), "fieldtype": "Currency", "width": 120},

		{"fieldname": "project_percentage", "label": _("Project Percentage"), "fieldtype": "Float", "width": 120},
		{"fieldname": "percent_complete", "label": _("Completion"), "fieldtype": "Data", "width": 120},
		{"fieldname": "total_billed_amount", "label": _("Total Billed Amount"), "fieldtype": "Currency", "width": 120},

		{"fieldname": "project_duration", "label": _("Project Duration (Month)"), "fieldtype": "Int", "width": 120},
		{
			"fieldname": "expected_start_date",
			"label": _("Start Date"),
			"fieldtype": "Date",
			"width": 120,
		},
		{"fieldname": "expected_end_date", "label": _("End Date"), "fieldtype": "Date", "width": 120},
	]