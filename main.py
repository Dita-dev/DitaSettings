import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot


# Create the Qt Application
app = QApplication(sys.argv)


# Greetings
@Slot()
def say_hello():
    print("Button clicked, Hello!")
    
# Create a button
button = QPushButton("Click me")

# Connect the button to the function
button.clicked.connect(say_hello)

# Show the button
button.show()
# Run the main Qt loop
app.exec()