# ------------------------------------------------------
# -------------------- mplwidget.py --------------------
# ------------------------------------------------------
from PyQt5.QtWidgets import*  # All constitutes belonging to the QtWidgets are added.

from matplotlib.backends.backend_qt5agg import FigureCanvas # FigureCanvas can be thought of as the paper (canvas) we need to draw pictures.

from matplotlib.figure import Figure

    
class MplWidget(QWidget):  # define the class named MplWidget with the same name as the Widget we are Promoting in Qt Designer,.
    
    def __init__(self, parent = None):  # The 'self' parameter is used to specify that variables (functions) defined in a class are a variable of that class so that they can be excluded from the class.

        QWidget.__init__(self, parent) # This snippet is assigned to the 'self' statement as we will need to access it outside the class (in the main.py file).
        
        self.canvas = FigureCanvas(Figure())
        
        grid_layout = QGridLayout()  # define grid layout ( QVBoxLayout )
        grid_layout.addWidget(self.canvas) # add the FigureCanvas object into this grid layout
        
        self.canvas.axes = self.canvas.figure.add_subplot(111) # define a new axes for figurecanvas
        self.setLayout(grid_layout)  # define the grid layout we created with the setLayout function to ensure that our class (the interface we will create) is the layout