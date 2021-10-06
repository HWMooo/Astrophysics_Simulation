from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavBar
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D

class MPLCanvas(FigureCanvas):
    def __init__(self):
        self.fig = Figure()
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.setupPlotAx()
        
    def setupPlotAx(self):
        self.ax = self.fig.add_subplot(111, projection="3d")
        self.ax.mouse_init()
          
class MatPlotLibWidget(QWidget):
    
    """
     self-contained QWidget class to place into a QWindow
    This class creates a matplotlib canvas with toolbar 
    to be easily inserted into a QWindow
    """
    def __init__(self, parent=None):
        super().__init__(parent)

        self.canvas = MPLCanvas()
        self.toolbar = NavBar(self.canvas, self)
        self.ax = self.canvas.ax
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(self.canvas)
        layout.addWidget(self.toolbar)
        
    def clearCanvas(self):
        self.canvas.ax.clear()

    def update(self):
        self.canvas.draw()
