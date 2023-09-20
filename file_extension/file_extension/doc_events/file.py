import frappe

def validate(doc,method):
    try:
        file_extension = doc.file_url.split('.')[-1].lower()
        extension = frappe.db.get_list("File Extension", filters={"name1": file_extension})
        frappe.log_error("extension", extension) 
        if not extension:
            frappe.throw('Only pdf and jpg files are allowed.')
    except Exception as e:
        frappe.log_error(title=("extension"), message=e, traceback=True)





