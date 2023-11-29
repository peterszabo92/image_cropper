import sys, os
from PyQt6.QtWidgets import QListWidgetItem, QListWidget
from PyQt6.QtCore import Qt, QMimeData, QUrl

class DragDropListView(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
             event.accept()
        else:
             event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.DropAction.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.DropAction.CopyAction)
            event.accept()

            links = []

            for url in event.mimeData().urls():
                if url.isLocalFile():
                    links.append(str(url.toLocalFile()))
                else:
                    links.append(str(url.toString()))

            self.addItems(links)
        else:
            event.ignore()

    def removeSelectedItem(self):
        listItems=self.selectedItems()
        if not listItems: return        
        for item in listItems:
            self.takeItem(self.row(item))

    def getFiles(self):
        items = []
        for x in range(self.count()):
            items.append(self.item(x).text())
        return items