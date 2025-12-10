from tax import Person, TaxConfig
from utils import format_vnd, print_header, validate_income_input

def demo_interactive():
    """Interactive demo for personal income tax calculation."""
    print_header("=== TÍNH THUẾ TNCN (demo) ===")
    
    # Get user input
    name = input("Tên người lao động: ").strip()
    year = int(input("Năm tính thuế (ví dụ 2025): ").strip())
    deps = int(input("Số người phụ thuộc đã đăng ký: ").strip())

    person = Person(name, year, deps)

    # Input monthly incomes
    print("\n(ghi chú: để trống 1 tháng nhập 0 hoặc Enter)")
    for m in range(1, 13):
        s = input(f"Thu nhập tháng {m} (VNĐ, Enter->0): ")
        income = validate_income_input(s)
        person.set_month_income(m-1, income)

    # Compute taxes
    person.compute_monthly_taxes()
    summary = person.annual_reconciliation()

    # Display results
    display_results(person, summary, year, name)

def display_results(person, summary, year, name):
    """Display tax calculation results in a formatted table."""
    print_header(f"Quyết toán TNCN năm {year} - {name}")
    
    print(f"{'Tháng':>5} | {'Thu nhập':>15} | {'Thuế tạm nộp':>15}")
    print("-" * 45)
    
    for i in range(12):
        print(f"{i+1:>5} | {format_vnd(person.monthly_gross[i]):>15} | {format_vnd(person.monthly_tax_paid[i]):>15}")
    
    print("-" * 45)
    print(f"{'Tổng':>5} | {format_vnd(summary['total_gross']):>15} | {format_vnd(summary['total_paid']):>15}")
    
    print_summary_details(summary)

def print_summary_details(summary):
    """Print detailed summary of tax calculation."""
    print(f"\nThu nhập tính thuế cả năm: {format_vnd(summary['annual_taxable'])}")
    print(f"Thuế thực tế phải nộp cả năm: {format_vnd(summary['annual_tax'])}")
    
    diff = summary['difference']
    if diff > 0:
        print(f"Số đã tạm nộp lớn hơn: bạn được hoàn {format_vnd(diff)}")
    elif diff < 0:
        print(f"Bạn còn phải nộp thêm: {format_vnd(-diff)}")
    else:
        print("Bạn đã nộp đúng số thuế (không được hoàn, không phải nộp thêm).")

if __name__ == "__main__":
    demo_interactive()