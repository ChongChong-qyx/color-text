class CannotFoundQtError(Exception):
	pass

try:
	import PySide2
	del PySide2

except ModuleNotFoundError:
	error_text = ['如果要使用此功能，请先在CMD（命令提示符）输入命令 “python -m pip install PySide2 shiboken2” 以安装PySide2和shiboken2。',
		'To use this feature, enter the command "Python-m pip install PySide2 shiboken2" in CMD (command prompt) to install PySide2 and shiboken2.']
	error = CannotFoundQtError(error_text[1] + '\n' + '              ' + error_text[0])
	raise error

all_supported_controls = ['QCalendarWidget', 'QCheckBox', 'QComboBox', 'QCommandLinkButton', 'QDateEdit', 'QDateTimeEdit',
	'QBoubleSpinBox', 'QFontComboBox', 'QKeySequenceEdit', 'QLabel', 'QLineEdit', 'QPlainTextEdit', 'QPushButton',
	'QRadioButton', 'QSpinBox', 'QTextEdit', 'QTimeEdit', 'QDialogButtonBox']

def SetControlTextColor(control, color, controls="*"):
	now_style_sheet = control.styleSheet()
	control.setStyleSheet(now_style_sheet + "\n" + controls + " { color : " + str(color) + " }")
