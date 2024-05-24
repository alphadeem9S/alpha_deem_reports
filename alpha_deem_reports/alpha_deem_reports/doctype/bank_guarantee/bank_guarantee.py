# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt


import frappe
from frappe import _
from frappe.utils import flt, date_diff
from frappe.model.document import Document


class BankGuarantee(Document):
	def validate(self):
		if not (self.customer or self.supplier):
			frappe.throw(_("Select the customer or supplier."))

		self.validity_in_days = date_diff(self.guarantee_end_date, self.start_date)

		self.company_cover_percentage = 100 - flt(self.bank_cover_percentage)
		self.bank_cover_amount =  flt(self.amount) * (flt(self.bank_cover_percentage) * 0.01)
		self.company_cover_amount =  flt(self.amount) - flt(self.bank_cover_amount)
		self.cover_commission = flt(self.bank_cover_amount) * flt(self.cover_commission_percentage) * 0.01

	def on_submit(self):
		if not self.bank_guarantee_number:
			frappe.throw(_("Enter the Bank Guarantee Number before submittting."))
		if not self.name_of_beneficiary:
			frappe.throw(_("Enter the name of the Beneficiary before submittting."))
		if not self.bank:
			frappe.throw(_("Enter the name of the bank or lending institution before submittting."))


@frappe.whitelist()
def get_voucher_details(bank_guarantee_type: str, reference_name: str):
	if not isinstance(reference_name, str):
		raise TypeError("reference_name must be a string")

	fields_to_fetch = ["grand_total"]

	if bank_guarantee_type == "Receiving":
		doctype = "Sales Order"
		fields_to_fetch.append("customer")
		fields_to_fetch.append("project")
	else:
		doctype = "Purchase Order"
		fields_to_fetch.append("supplier")

	return frappe.db.get_value(doctype, reference_name, fields_to_fetch, as_dict=True)