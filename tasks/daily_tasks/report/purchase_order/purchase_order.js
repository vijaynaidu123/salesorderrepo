// Copyright (c) 2022, abc and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["purchase order"] = {
        "filters": [
        {
                'fieldname': 'company',
                'label': __('Company'),
                'fieldtype': 'Link',
                'options': 'Company',
                'reqd': 1
        },
        {
                'fieldname': 'supplier_group',
                'label': __('Supplier_Group'),
                'fieldtype': 'Link',
                'options': 'Supplier Group'
        },
        {
                'fieldname': 'name',
                'label': __('Purchase_Order'),
                'fieldtype': 'Link',
                'options': 'Purchase Order',
                'get_query': () =>{
                        return {
                                filters: { "docstatus": 1 }
                                }
                        }
        }

        ]
};
