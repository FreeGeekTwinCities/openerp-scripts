import openerplib
connection = openerplib.get_connection(hostname=app.config['ERP_HOST'], database=app.config['ERP_DB'], login=app.config['ERP_USER'], password=app.config['ERP_PASSWORD'])

employee_model = connection.get_model("hr.employee")
employees = employee_model.search_read([("active", "=", True)])

attendance_model = connection.get_model("hr.attendance")
timesheet_model = connection.get_model("hr_timesheet_sheet.sheet")
    
today = str(date.today().strftime('%Y-%m-%d'))
now = str(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))
auto_signout_hours = int(app.config['AUTO_SIGNOUT_HOURS'])

employees_signed_in = [{'id': employee['id'], 'name': employee['name']} for employee in employees if employee['state'] == 'present']
