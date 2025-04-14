import reports

# Generar reportes de ventas y gastos usando funciones del módulo
sales_report = reports.generate_sales_report('Octobre', 10000)
expense_report = reports.generate_expenses_report('Octubre', 5000)

print(sales_report)
print(expense_report)