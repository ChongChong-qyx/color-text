class CannotFoundQtError(Exception):
	pass

try:
	import PyQt5
	del PyQt5

except ModuleNotFoundError:
	error_text = ['如果要使用此功能，请先在CMD（命令提示符）输入命令 “python -m pip install PyQt5 pyqt5-tools PyQt5-sip click python-dotenv” 以安装PyQt5、pyqt5-tools、PyQt5-sip、click和python-dotenv。',
		'To use this feature, enter the command "Python-m pip install PyQt5 pyqt5-tools pyqt5-sip click python-dotenv" in CMD (command prompt) to install PyQt5, pyqt5-tools, PyQt5-sip, click, and python-dotenv.']
	error = CannotFoundQtError(error_text[1] + '\n' + '              ' + error_text[0])
	raise error

all_supported_controls = ['QCalendarWidget', 'QCheckBox', 'QComboBox', 'QCommandLinkButton', 'QDateEdit', 'QDateTimeEdit',
	'QBoubleSpinBox', 'QFontComboBox', 'QKeySequenceEdit', 'QLabel', 'QLineEdit', 'QPlainTextEdit', 'QPushButton',
	'QRadioButton', 'QSpinBox', 'QTextEdit', 'QTimeEdit', 'QDialogButtonBox']

def SetControlTextColor(control, color, controls="*"):
	now_style_sheet = control.styleSheet()
	control.setStyleSheet(now_style_sheet + "\n" + controls + " { color : " + str(color) + " }")
