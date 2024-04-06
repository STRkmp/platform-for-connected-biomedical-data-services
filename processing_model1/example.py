from reportlab.pdfgen import canvas
from io import BytesIO


def create_pdf(file):
    packet = BytesIO()
    can = canvas.Canvas(packet)
    can.drawString(100, 100, "Hello world")
    can.save()
    packet.seek(0)
    output_file = BytesIO(packet.getvalue())
    output_file.name = 'Result.pdf'
    return output_file
