# Problem Statement:
# Create a base class Report with a method generate(). Derive PDFReport, ExcelReport,
# and HTMLReport. Override generate() in each class. Write a function that accepts any
# report object and calls generate().

class Report:
    def generate(self):
        pass


class PDFReport(Report):
    def generate(self):
        print("Generating PDF report")


class ExcelReport(Report):
    def generate(self):
        print("Generating Excel report")


class HTMLReport(Report):
    def generate(self):
        print("Generating HTML report")


def create_report(report):
    report.generate()


reports = [PDFReport(), ExcelReport(), HTMLReport()]

for report in reports:
    create_report(report)
