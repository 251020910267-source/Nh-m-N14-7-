from dataclasses import dataclass, field
from typing import List, Tuple

@dataclass
class TaxConfig:
    personal_deduction_monthly: int = 11_000_000   # VND/tháng
    dependent_deduction_monthly: int = 4_400_000   # VND/người/tháng
    # monthly tax brackets: list of (upper_bound, rate) in VND and decimal
    monthly_brackets: List[Tuple[int or None, float]] = field(default_factory=lambda: [
        (5_000_000, 0.05),
        (10_000_000, 0.10),
        (18_000_000, 0.15),
        (32_000_000, 0.20),
        (52_000_000, 0.25),
        (80_000_000, 0.30),
        (None, 0.35),
    ])

    def annual_brackets(self):
        """Return the same brackets scaled to yearly (multiply bounds by 12)."""
        ab = []
        for upper, rate in self.monthly_brackets:
            ab.append((None if upper is None else upper * 12, rate))
        return ab

def compute_progressive_tax(taxable: int, brackets: List[Tuple[int or None, float]]) -> int:
    """
    Compute tax on 'taxable' (VND) using progressive brackets.
    Returns rounded-to-VND tax (int).
    """
    if taxable <= 0:
        return 0
    tax = 0.0
    lower = 0
    for upper, rate in brackets:
        if upper is None:
            portion = taxable - lower
            if portion > 0:
                tax += portion * rate
            break
        else:
            if taxable > upper:
                portion = upper - lower
                if portion > 0:
                    tax += portion * rate
                lower = upper
            else:
                portion = taxable - lower
                if portion > 0:
                    tax += portion * rate
                break
    return int(round(tax))

@dataclass
class Person:
    name: str
    tax_year: int
    dependents: int
    config: TaxConfig = field(default_factory=TaxConfig)
    monthly_gross: List[int] = field(default_factory=lambda: [0]*12)
    monthly_tax_paid: List[int] = field(default_factory=lambda: [0]*12)

    def set_month_income(self, month_index: int, income: int):
        self.monthly_gross[month_index] = income

    def compute_monthly_taxes(self):
        """Compute tax for each month (tạm nộp) using monthly taxable income."""
        pd = self.config.personal_deduction_monthly
        dd = self.config.dependent_deduction_monthly * self.dependents
        for i in range(12):
            gross = self.monthly_gross[i]
            taxable = gross - pd - dd
            if taxable < 0:
                taxable = 0
            tax = compute_progressive_tax(taxable, self.config.monthly_brackets)
            self.monthly_tax_paid[i] = tax

    def annual_reconciliation(self):
        """Compute annual taxable income and actual annual tax; return summary."""
        total_gross = sum(self.monthly_gross)
        annual_pd = self.config.personal_deduction_monthly * 12
        annual_dd = self.config.dependent_deduction_monthly * 12 * self.dependents
        annual_taxable = total_gross - annual_pd - annual_dd
        if annual_taxable < 0:
            annual_taxable = 0
        annual_tax = compute_progressive_tax(annual_taxable, self.config.annual_brackets())
        total_paid = sum(self.monthly_tax_paid)
        # positive means paid more -> refund; negative means owe more
        difference = total_paid - annual_tax
        return {
            "total_gross": total_gross,
            "annual_taxable": annual_taxable,
            "annual_tax": annual_tax,
            "total_paid": total_paid,
            "difference": difference
        }