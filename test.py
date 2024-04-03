from bokeh.plotting import figure
from bokeh.embed import file_html
from bokeh.resources import CDN
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys

# Create a Bokeh plot
plot = figure()
plot.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5])

# Export the plot to HTML
html = file_html(plot, CDN, "my plot")

# Create a PyQt application
app = QApplication(sys.argv)

# Create a QWebEngineView widget
web = QWebEngineView()

# Load the Bokeh plot into the widget
web.setHtml(html)
web.show()

# Start the PyQt application
sys.exit(app.exec_())