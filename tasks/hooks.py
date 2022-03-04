from . import __version__ as app_version

app_name = "tasks"
app_title = "daily tasks"
app_publisher = "abc"
app_description = "work"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "abc"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/tasks/css/tasks.css"
# app_include_js = "/assets/tasks/js/tasks.js"

# include js, css files in header of web template
# web_include_css = "/assets/tasks/css/tasks.css"
# web_include_js = "/assets/tasks/js/tasks.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "tasks/public/scss/website"

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

# before_install = "tasks.install.before_install"
# after_install = "tasks.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "tasks.uninstall.before_uninstall"
# after_uninstall = "tasks.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "tasks.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Sales Order": {
		"on_submit": "tasks.doctype.sales_order.sales_order.send_email",
		"before_update_after_submit": "tasks.doctype.sales_order.sales_order.send_email",
		"on_cancel":"tasks.doctype.sales_order.sales_order.send_email",
		"on_trash":"tasks.doctype.sales_order.sales_order.send_email"

	}
}

#doctype_js = {
  #      "Item" : "doctype/item/item.js"
#}
# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"tasks.tasks.all"
# 	],
# 	"daily": [
# 		"tasks.tasks.daily"
# 	],
# 	"hourly": [
# 		"tasks.tasks.hourly"
# 	],
# 	"weekly": [
# 		"tasks.tasks.weekly"
# 	]
# 	"monthly": [
# 		"tasks.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "tasks.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "tasks.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "tasks.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


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
# 	"tasks.auth.validate"
# ]

