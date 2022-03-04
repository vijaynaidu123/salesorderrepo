frappe.ui.form.on('Item', {
	refresh(frm) {
		console.log("text")
		// your code here
	
	frm.add_custom_button(__('codes'), function(){
		    //frappe.new_doc('Item',true)
		    //frappe.set_route("Form", "Purchase Order")
		    //frappe.msgprint(InsertBarcode);
		
	
	//"Insert Baecode");
	
	frappe.call({
         // type:'POST',
         method:" tasks.daily_tasks.doctype.item.item",
          args:{
              'item_code' : frm.doc.item_code
          },
              async:false,
              
              callback:function(r){
                  console.log(r);
              }
      })
	})
  }
	
})