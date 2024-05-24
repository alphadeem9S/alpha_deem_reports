from . import __version__ as app_version

app_name = "alpha_deem_reports"
app_title = "Alpha Deem Reports"
app_publisher = "Smart Solutions"
app_description = "Alpha Deem Reports"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@smartsoleg.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/alpha_deem_reports/css/alpha_deem_reports.css"
# app_include_js = "/assets/alpha_deem_reports/js/alpha_deem_reports.js"

# include js, css files in header of web template
# web_include_css = "/assets/alpha_deem_reports/css/alpha_deem_reports.css"
# web_include_js = "/assets/alpha_deem_reports/js/alpha_deem_reports.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "alpha_deem_reports/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "alpha_deem_reports.install.before_install"
# after_install = "alpha_deem_reports.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "alpha_deem_reports.uninstall.before_uninstall"
# after_uninstall = "alpha_deem_reports.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "alpha_deem_reports.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	"Project": "alpha_deem_reports.alpha_deem_reports.doctype.project.project.Project",
	"Bank Guarantee": "alpha_deem_reports.alpha_deem_reports.doctype.bank_guarantee.bank_guarantee.BankGuarantee"
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"alpha_deem_reports.tasks.all"
#	],
#	"daily": [
#		"alpha_deem_reports.tasks.daily"
#	],
#	"hourly": [
#		"alpha_deem_reports.tasks.hourly"
#	],
#	"weekly": [
#		"alpha_deem_reports.tasks.weekly"
#	]
#	"monthly": [
#		"alpha_deem_reports.tasks.monthly"
#	]
# }

# Testing
# -------

# before_tests = "alpha_deem_reports.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "alpha_deem_reports.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
override_doctype_dashboards = {
	"Project": "alpha_deem_reports.alpha_deem_reports.doctype.project.project_dashboard.get_data",
}

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Request Events
# ----------------
# before_request = ["alpha_deem_reports.utils.before_request"]
# after_request = ["alpha_deem_reports.utils.after_request"]

# Job Events
# ----------
# before_job = ["alpha_deem_reports.utils.before_job"]
# after_job = ["alpha_deem_reports.utils.after_job"]

# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"alpha_deem_reports.auth.validate"
# ]

fixtures = [
    {"dt": "Server Script", "filters": [["reference_doctype", "in", ["Journal Entry", "Delivery Note"]]]},
    {"dt": "Client Script", "filters": [["dt", "in", ["Project", "Bank Guarantee"]]]},
]