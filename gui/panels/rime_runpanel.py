from PySide2 import QtWidgets
from PySide2.QtGui import QColor, QTextCursor
from PySide2.QtCore import Slot

from gui.panels.rime_runprogress import RunProgressWidget
from rime_manager import Manager
import sys



class RunPanelWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        #self.runPageProcessBar = QtWidgets.QProgressBar()
        self.runPageStatistics = QtWidgets.QTextEdit()
        self.runPageStatistics.setReadOnly(True)

        self.runPageRunButton = QtWidgets.QPushButton("Run")
        self.runPageRunButton.setObjectName("runButton")

        self.runPageGrid = QtWidgets.QGridLayout()
        self.runPageGrid.setObjectName("runPageLayout")
        self.runPageGrid.addWidget(self.runPageStatistics, 0, 0)
        self.runPageGrid.addWidget(self.runPageRunButton, 1, 0)
        self.runPageGrid.rowStretch(0)

        self.setLayout(self.runPageGrid)

        self.runPageRunButton.clicked.connect(self.runRime)

    def update_statistics(self):
        self.runPageStatistics.clear()

        for p in Manager.getInstance().run_params:
            if ((p == 'binary_path' and Manager.getInstance().run_params[p] == '') or
                (p == 'metadata_path' and Manager.getInstance().run_params[p] == '') or
                (p == 'rip_path' and Manager.getInstance().run_params[p] == '') or
                (p == 'output_path' and Manager.getInstance().run_params[p] == '')):
                self.runPageStatistics.setTextBackgroundColor(QColor(251,115,115))
            else:
                self.runPageStatistics.setTextBackgroundColor(QColor(255, 255, 255))

            self.runPageStatistics.append(p + ": " + str(Manager.getInstance().run_params[p]) + "\n")

    def validate_forms(self):
        if(Manager.checkNecessaryInput(Manager)):
            self.runPageRunButton.setEnabled(True)
            self.runPageRunButton.setToolTip("Start execution")
        else:
            self.runPageRunButton.setEnabled(True)
            self.runPageRunButton.setToolTip("Please set the required input/output parameters!")

    @Slot()
    def runRime(self):
        print("xxxxx")
        self.runProgressWindow = RunProgressWidget()
        print("xxxxx")
        Manager.getInstance().connectOutput(self.runProgressWindow.runProgressBox.append)
        print("xxxxx")
        self.runProgressWindow.show()
        print("xxxxx")

    @Slot(str)
    def appendToStats(self, msg):
        self.runPageStatistics.append(msg)
