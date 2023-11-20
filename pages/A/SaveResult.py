
from reportlab.pdfgen import canvas
from io import BytesIO
def save_as_pdf(result_text, user_input_values):
    # Create a PDF document
    buffer = BytesIO()
    c = canvas.Canvas(buffer)

    # Add result text to the PDF
    c.setFont("Times-Roman", 12)
    c.drawString(10, 800, "Result:")
    c.drawString(10, 780, result_text)

    # Add user input values to the PDF
    c.setFont("Times-Roman", 12)
    c.drawString(10, 750, "User Inputted Values:")
    y_position = 730
    for key, value in user_input_values.items():
        c.drawString(20, y_position, f"{key}: {value}")
        y_position -= 20

    # Save the PDF
    c.save()

    # Move the buffer position to the beginning to read the content
    buffer.seek(0)

    return buffer
