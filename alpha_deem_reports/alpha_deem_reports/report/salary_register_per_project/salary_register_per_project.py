# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt


import frappe
from frappe import _
from frappe.utils import flt

import erpnext


def execute(filters=None):
	columns, earning_types, ded_types = get_columns()
	projects = get_projects_map(filters)
 
	data = []
	for p in projects:
		row = [
			p.name,
			p.company
		]

		ss = get_salary_slips(filters, p.name)

		row.append(sum(flt(s.leave_without_pay) for s in ss))
		row.append(sum(flt(s.payment_days) for s in ss))
		
		for e in earning_types:
			total_e = 0
			for s in ss:
				for d in get_salary_details(s.name):
					if d.salary_component == e:
						total_e += d.amount
			row.append(total_e)

		row.append(sum(flt(s.gross_pay) for s in ss) )

		for d in ded_types:
			total_e = 0
			for s in ss:
				for i in get_salary_details(s.name):
					if i.salary_component == e:
						total_e += i.amount
			row.append(total_e)

		row.append( sum(flt(s.total_loan_repayment) for s in ss) )

		row.append(sum(flt(s.total_deduction) for s in ss))
		row.append(sum(flt(s.net_pay) for s in ss))
		data.append(row)

	return columns, data



def get_columns():
	columns = [
		_("Project") + ":Link/Project:180",
		_("Company") + ":Link/Company:120",
		_("Leave Without Pay") + ":Float:100",
		_("Payment Days") + ":Float:120",
	]

	salary_components = {_("Earning"): [], _("Deduction"): []}

	for component in frappe.db.sql(
		"""select distinct sd.salary_component, sc.type
		from `tabSalary Detail` sd, `tabSalary Component` sc
		where sc.name=sd.salary_component and sd.amount != 0""",
		as_dict=1,
	):
		salary_components[_(component.type)].append(component.salary_component)

	columns = (
		columns
		+ [(e + ":Currency:120") for e in salary_components[_("Earning")]]
		+ [_("Gross Pay") + ":Currency:120"]
		+ [(d + ":Currency:120") for d in salary_components[_("Deduction")]]
		+ [
			_("Loan Repayment") + ":Currency:120",
			_("Total Deduction") + ":Currency:120",
			_("Net Pay") + ":Currency:120",
		]
	)

	return columns, salary_components[_("Earning")], salary_components[_("Deduction")]


def get_salary_slips(filters, project):
	get_filters = [["company", "=", filters.get("company")], ["project", "like", project], ["start_date", ">=", filters.get("start_date")], ["end_date", "<=", filters.get("end_date")]]
	salary_slips = frappe.db.get_all("Salary Slip", filters=get_filters, fields=[
		"name",
		"leave_without_pay",
		"payment_days",
		"gross_pay",
		"total_loan_repayment",
		"total_deduction",
		"net_pay"
	])

	return salary_slips


def get_projects_map(filters):
	get_filters = {}
	if filters.get("project"):
		get_filters.update({"name": filters.get("project")})

	return frappe.db.get_all("Project", filters=get_filters, fields=["name", "company"])


def get_salary_details(ss_name):
	return frappe.db.get_all("Salary Detail", filters={"parent": ss_name}, fields=["*"])
	 

