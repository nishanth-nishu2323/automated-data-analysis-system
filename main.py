from services.user_service import create_user, get_all_users
from services.order_service import create_order
from services.report_service import generate_sales_report
from services.pdf_service import generate_pdf

# Create sample user
create_user("nishanth", "nishanthnishu893@gmail.com")

# Show users
print("Users:", get_all_users())

# Create order
create_order(1, 1500.00)

# Generate report
report = generate_sales_report()
print("Report Generated:", report)

# ✅ Generate PDF
pdf_path = generate_pdf(report)
print("PDF saved at:", pdf_path)