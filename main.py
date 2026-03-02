from services.user_service import create_user, get_all_users
from services.order_service import create_order
from services.report_service import generate_sales_report

# Create sample user
create_user("Nishh", "nishh@email.com")

# Show users
print("Users:", get_all_users())

# Create order
create_order(1, 1500.00)

# Generate report
report = generate_sales_report()
print("Report Generated:", report)