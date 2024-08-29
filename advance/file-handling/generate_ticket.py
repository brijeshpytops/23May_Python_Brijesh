from fpdf import FPDF
from datetime import datetime

# Create instance of FPDF class
pdf = FPDF()

# Add a page
pdf.add_page()

# Set font
pdf.set_font("Arial", "B", 16)

# Add a cell
pdf.cell(200, 10, txt="Bus Ticket", ln=True, align='C')

# Add ticket details
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt=f"Ticket Number: BT123456", ln=True, align='L')
pdf.cell(200, 10, txt=f"Passenger Name: John Doe", ln=True, align='L')
pdf.cell(200, 10, txt=f"Bus Number: 42A", ln=True, align='L')
pdf.cell(200, 10, txt=f"Departure: New York, NY", ln=True, align='L')
pdf.cell(200, 10, txt=f"Destination: Washington, DC", ln=True, align='L')
pdf.cell(200, 10, txt=f"Date of Journey: {datetime.now().strftime('%Y-%m-%d')}", ln=True, align='L')
pdf.cell(200, 10, txt=f"Departure Time: 10:00 AM", ln=True, align='L')
pdf.cell(200, 10, txt=f"Seat Number: 12B", ln=True, align='L')
pdf.cell(200, 10, txt=f"Price: $50.00", ln=True, align='L')

# Optional: Add some extra design
pdf.line(10, 50, 200, 50)

# Save the pdf with name .pdf
pdf.output("bus_ticket.pdf")

print("Bus ticket generated successfully!")
