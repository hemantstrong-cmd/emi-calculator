# file: cma_generator.py

from dataclasses import dataclass
from typing import List, Dict
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet


@dataclass
class BaseFinancials:
    revenue: float
    expenses: float
    assets: float
    liabilities: float


@dataclass
class Assumptions:
    revenue_growth: float
    expense_growth: float


class CMAProjector:

    @staticmethod
    def project(base: BaseFinancials, assumptions: Assumptions, years: int = 5) -> List[Dict]:
        data = []
        revenue = base.revenue
        expenses = base.expenses
        assets = base.assets
        liabilities = base.liabilities

        for year in range(1, years + 1):
            revenue *= (1 + assumptions.revenue_growth)
            expenses *= (1 + assumptions.expense_growth)

            profit = revenue - expenses
            net_worth = assets - liabilities + profit

            data.append({
                "Year": f"Year {year}",
                "Revenue": round(revenue, 2),
                "Expenses": round(expenses, 2),
                "Profit": round(profit, 2),
                "Net Worth": round(net_worth, 2)
            })

        return data


class PDFGenerator:

    @staticmethod
    def generate(data: List[Dict], filename: str = "cma_report.pdf"):
        doc = SimpleDocTemplate(filename)
        styles = getSampleStyleSheet()

        elements = []
        elements.append(Paragraph("CMA Data (5-Year Projection)", styles["Title"]))

        table_data = [["Year", "Revenue", "Expenses", "Profit", "Net Worth"]]

        for row in data:
            table_data.append([
                row["Year"],
                row["Revenue"],
                row["Expenses"],
                row["Profit"],
                row["Net Worth"]
            ])

        table = Table(table_data)

        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ]))

        elements.append(table)
        doc.build(elements)


def generate_cma_report():
    base = BaseFinancials(
        revenue=500000,
        expenses=300000,
        assets=800000,
        liabilities=400000
    )

    assumptions = Assumptions(
        revenue_growth=0.10,
        expense_growth=0.08
    )

    projected_data = CMAProjector.project(base, assumptions)
    PDFGenerator.generate(projected_data)

    print("CMA PDF generated successfully.")


if __name__ == "__main__":
    generate_cma_report()
