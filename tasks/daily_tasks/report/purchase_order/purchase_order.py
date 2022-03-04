# Copyright (c) 2022, abc and contributors
# For license information, please see license.txt

import frappe
#from frappe import __

def execute(filters=None):
	columns = get_columns()
	conditions=get_conditions(filters)
	data=get_data(filters,conditions)
	#columns = []
	#data = []
	return columns, data

def get_columns():
	columns = [
	{
	    'fieldname': 'company',
		'label': 'Company',
		'fieldtype': "Data",
	},
	{  
	 	'fieldname': 'supplier_group',
		'label': 'Supplier_Group',
		'fieldtype': "Link",
		'options': 'Supplier Group'
	},
	{
	    'fieldname': 'name',
		'label': 'Name',
		'fieldtype': "Data",
	},
	{
		'fieldname': 'supplier_name',
		'label': 'Supplier',
		'fieldtype': "Link",
		'options': 'Supplier'
	},
	{
		'fieldname': 'rate',
		'label': 'Rate',
		'fieldtype': "float",
	},
	{
		'fieldname': 'amount',
		'label': 'Amount',
		'fieldtype': "float",
	},
	{
		'fieldname': 'item_code',
		'label': 'Item_Code',
		'fieldtype': "Link",
		'options': 'Item'	
	}
	
	]
	return columns

def get_conditions(filters):
	print(filters.get('name'))
	conditions=""
	if filters.get("company"):
		conditions+= "and `tabPurchase Order`.company='{}'".format(filters.get('company'))
	if filters.get("supplier_group"):
		conditions+="and `tabSupplier`.supplier_group='{}'".format(filters.get('supplier_group'))
	if filters.get("name"):
		conditions+="and `tabPurchase Order`.name ='{}'".format(filters.get('name'))
	return conditions


def get_data(filters,conditions):
	query=frappe.db.sql(""" select `tabPurchase Order`.company,`tabSupplier`.supplier_group,
	`tabPurchase Order`.name,`tabSupplier`.supplier_name,
	`tabPurchase Order Item`.rate,`tabPurchase Order Item`.amount,
	`tabPurchase Order Item`.item_code from `tabPurchase Order`
	left  join `tabPurchase Order Item` on `tabPurchase Order`.name=`tabPurchase Order Item`.parent 
	left join `tabSupplier` on `tabSupplier`.supplier_name=`tabPurchase Order`.supplier where 
	`tabSupplier`.supplier_name!= '' %s""" %(conditions),as_dict=1)
	#data=frappe.db.sql(query,conditions,as_dict=True)
	return query


