import frappe
@frappe.whitelist()
def item(item_code):
	item_code = frappe.form_dict.get('item_code')
	i = frappe.get_doc('Item',item_code)
	frappe.msgprint("item code is " +item_code);

	i.append('barcodes',{
    	'barcode' : item_code
	})

	i.save();
	return "sucess"
	#doc_m = frappe.get_doc("Item", source_name)
#j=frappe.db.sql("""select item_code from tabItem where item_code like %s order by item_code desc limit 1""",i)
#prefix=j[0][0]
#prefix="".join(prefix)

#frappe.msgprint("New Item Code "+new_num1+" has been generated")
#return new_num1;