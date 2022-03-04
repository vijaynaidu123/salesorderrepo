import frappe
from frappe.core.doctype.communication.email import make


def send_email(self,doc):
	print("print the sales order nub")
	msg="Your sales order is submited"
	msg2="Your order is canceled"
	if msg="on_submit":
		frappe.msgprint(msg)
	elif msg2="on_cancel":
		#frappe.msgprint(msg2)

	make(subject = "Email Subject", content=msg, recipients='vijay.n@promantia.com',
        send_email=True)
	#msg = """Email send successfully to Employee"""
	frappe.msgprint(msg)
	#frappe.msgprint("alert sales salesorder")


