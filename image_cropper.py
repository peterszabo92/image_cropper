
import sys
import os
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget
from dragdroplistview import DragDropListView

from PIL import Image

class Ui(QMainWindow):
      def __init__(self):
         super(Ui, self).__init__()
         # Load the .ui file

         bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
         path_to_ui = os.path.abspath(os.path.join(bundle_dir,'image_cropper.ui'))

         ui = uic.loadUi(path_to_ui, self)

         self.cropButton = ui.crop_button
         self.cropButton.setCheckable(True)
         self.cropButton.clicked.connect(self.cropImages)

         self.option4K.clicked.connect(self.resolutionButtonClicked)
         self.option2K.clicked.connect(self.resolutionButtonClicked)
         self.option1K.clicked.connect(self.resolutionButtonClicked)
         self.option4K_2K.clicked.connect(self.resolutionButtonClicked)
         self.option2K_4K.clicked.connect(self.resolutionButtonClicked)
         self.option2K_1K.clicked.connect(self.resolutionButtonClicked)
         self.option1K_2K.clicked.connect(self.resolutionButtonClicked)

         self.remove_item.clicked.connect(self.removeItem)

         self.cropWidth = ui.crop_width
         self.cropHeight = ui.crop_height

         self.fileList = ui.listWidget

         self.cropWidth.setText('0')
         self.cropHeight.setText('0')

         # Show the GUI
         self.show() 

      def resolutionButtonClicked(self):
         resolution = self.sender().text().split('x')
         self.cropWidth.setText(resolution[0])
         self.cropHeight.setText(resolution[1])

      def removeItem(self):
         self.fileList.removeSelectedItem()

      def cropImages(self):
         cropWidth = int(self.cropWidth.text())
         cropHeight = int(self.cropHeight.text())

         if cropWidth <= 0 or cropHeight <= 0: return

         imgFilePaths = self.fileList.getFiles()
         for x in range(len(imgFilePaths)): self.cropSingleImage(imgFilePaths[x], cropWidth, cropHeight)

      def cropSingleImage(self, imageFilePath, cropWidth, cropHeight):
         img = Image.open(imageFilePath)
         img_info = img.info
         imgCropped = img.crop(box = (0, 0, cropWidth, cropHeight))
         imgCropped.save(imageFilePath + '_cropped.png', **img_info)

def main():
   app = QApplication(sys.argv)
   ui = Ui()

   ui.show()
   sys.exit(app.exec())

if __name__ == '__main__':
   main()