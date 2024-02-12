import sys
import base64
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PySide6.QtWebEngineWidgets import QWebEngineView
from jinja2 import Template
from datetime import datetime
import Resource_rc

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def save_pdf(self, InvoiceNumber: str, Item_dictionary: dict, TotalAmount: float):
        # Convert Item_dictionary to required format
        items = []
        for key, value in Item_dictionary.items():
            quantity, unit_price, name = value
            amount = round(quantity * unit_price, 2)
            items.append({
                'name': name,
                'quantity': quantity,
                'unit_price': str(unit_price),
                'amount': str(amount)
            })

        # Your dynamic data
        data = {
            'date': datetime.now().strftime('%B %d, %Y'),
            'time': datetime.now().strftime('%H:%M:%S'),
            'invoice_number': InvoiceNumber,
            'items': items,
            'total': TotalAmount
        }

        # Read the HTML template
        with open('invoice_template.html', 'r') as file:
            template_content = file.read()

        # Read the image file and convert it to base64
        with open("Resource/img/icon.png", 'rb') as img_file:
            img_data = img_file.read()
            img_base64 = base64.b64encode(img_data).decode('utf-8')

        # Add base64-encoded image data to the data dictionary
        data['logo'] = f"data:image/png;base64,{img_base64}"

        # Create a Jinja2 template
        template = Template(template_content)

        # Render the template with dynamic data
        html_content = template.render(data)

        # Create a QWebEngineView to render HTML content
        webview = QWebEngineView()
        webview.setHtml(html_content)

        def on_load_finished(result):
            # Once the page is loaded, print it to a PDF file
            save_path, _ = QFileDialog.getSaveFileName(self, "Save PDF", "invoice.pdf", "PDF Files (*.pdf)")
            if save_path:
                webview.page().printToPdf(save_path)

        # Connect to the loadFinished signal to trigger saving PDF when the page is loaded
        webview.page().loadFinished.connect(on_load_finished)
