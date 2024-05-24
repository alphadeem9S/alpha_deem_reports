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
			"customer",
			"total_billed_amount",
			"total_account_estimated_cost",
			"total_account_budget",
			"total_account_variance",
			"per_gross_margin",
			"gross_margin"
		]
	)

	for project in data:
		per_margin = flt(project["per_gross_margin"], precision=2)
		project["per_gross_margin"] = f"{per_margin} %"

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
		{"fieldname": "status", "label": _("Status"), "fieldtype": "Data", "width": 100},
		{"fieldname": "total_account_estimated_cost", "label": _("Total Estimated Cost"), "fieldtype": "Currency", "width": 130},
		{"fieldname": "total_account_budget", "label": _("Total Budget"), "fieldtype": "Currency", "width": 130},
		{"fieldname": "total_account_variance", "label": _("Variance"), "fieldtype": "Currency", "width": 130},

		{"fieldname": "total_billed_amount", "label": _("Total Billed Amount"), "fieldtype": "Currency", "width": 130},
		{"fieldname": "gross_margin", "label": _("Gross Margin"), "fieldtype": "Currency", "width": 130},

		{"fieldname": "per_gross_margin", "label": _("Gross Margin %"), "fieldtype": "Data", "width": 130}
	]