



import matplotlib.pyplot as chart
import Chart_over_house_prices as CF

# Data for plotting
x = CF.ListX
y = CF.ListY

# Create a figure and an axes
chart.figure()
chart.plot(x, y)

# Add title and labelss
chart.title('Chart over house prices')
chart.xlabel('Years')
chart.ylabel('Price')

# Show the plot
chart.show()
