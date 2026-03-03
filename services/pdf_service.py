from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
import matplotlib.pyplot as plt
import os


def generate_pdf(report):

    os.makedirs("outputs", exist_ok=True)

    pdf_path = "outputs/professional_report.pdf"
    chart_path = "outputs/sales_chart.png"

    # -------- Create Chart --------
    user_totals = {}

    for row in report:
        user = row["user_name"]
        amount = float(row["total_amount"])
        user_totals[user] = user_totals.get(user, 0) + amount

    plt.figure()
    plt.bar(user_totals.keys(), user_totals.values())
    plt.xlabel("User")
    plt.ylabel("Total Amount")
    plt.title("Total Sales per User")
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()

    # -------- Create PDF --------
    doc = SimpleDocTemplate(pdf_path, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()

    # Title
    elements.append(Paragraph("<b>Automated Data Analysis Report</b>", styles['Title']))
    elements.append(Spacer(1, 20))

    # Summary Section
    total_orders = len(report)
    total_revenue = sum(float(row["total_amount"]) for row in report)

    elements.append(Paragraph(f"Total Orders: {total_orders}", styles['Normal']))
    elements.append(Paragraph(f"Total Revenue: ₹ {total_revenue}", styles['Normal']))
    elements.append(Spacer(1, 20))

    # -------- Table Section --------
    table_data = [["Order ID", "User Name", "Total Amount"]]

    for row in report:
        table_data.append([
            row["order_id"],
            row["user_name"],
            float(row["total_amount"])
        ])

    table = Table(table_data, repeatRows=1)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (2, 1), (2, -1), 'RIGHT'),
    ]))

    elements.append(table)
    elements.append(PageBreak())

    # -------- Chart Section --------
    elements.append(Paragraph("<b>Sales Visualization</b>", styles['Heading2']))
    elements.append(Spacer(1, 15))
    elements.append(Image(chart_path, width=6 * inch, height=4 * inch))

    doc.build(elements)

    return pdf_path