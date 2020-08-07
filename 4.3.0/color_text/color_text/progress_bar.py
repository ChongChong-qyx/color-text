class ProgressBarError(Exception):
	pass

class ProgressBarStyle():

	def __init__(self):
		from platform import system
		self.block_amount = None
		self.text = None
		if system() == 'Windows':
			self.color = None
		self.edge = None
		self.blocks = None
		del system

	def __bool__(self):
		return True if self.block_amount or self.text or self.color or self.edge else False

	def set_text(self, text):
		self.text = text

	def set_block_amount(self, block_amount):
		self.block_amount = block_amount

	def set_color(self, color):
		from platform import system
		if system() == 'Windows':
			self.color = color
		del system

	def set_edge(self, edge):
		self.edge = edge

	def set_blocks(self, blocks):
		self.blocks = blocks

class ProgressBar():

	def __init__(self):
		from platform import system
		self.block_amount = 0
		self.style = None
		self.text = ''
		if system() == 'Windows':
			self.color = 0x07
		self.edge = '|'
		self.blocks = 0

	def __bool__(self):
		return False if block_amount == 0 else True

	def set_style(self, style):
		if style.block_amount:
			set_block_amount(style.block_amount)
		if style.text:
			set_text(style.text)
		if style.color and system() == 'Windows':
			set_color(style.color)
		if style.edge:
			set_edge(style.edge)
		if style.blocks:
			set_blocks(style.blocks)

	def set_text(self, text):
		self.text = text

	def set_block_amount(self, block_amount):
		self.block_amount = block_amount

	def set_color(self, color):
		if system() == 'Windows':
			self.color = color

	def set_edge(self, edge):
		self.edge = edge

	def set_blocks(self, blocks):
		self.blocks = blocks

	def show(self):
		if system() == 'Windows':
			from .output import PrintOtherColorText

		if self.blocks > self.block_amount:
			raise ProgressBarError("blocks to show is greater tan block amount\n                  要显示的方块大于方块的数量")
		self.output_text = edge + ('█' * blocks) + ('  ' * (block_amount - blocks)) + edge + ' ' + text

		if system() == 'Windows':
			PrintOtherColorText(self.output_text, color=self.color, end='\n')
		else:
			print(self.output_text)

		if system() == 'Windows':
			del PrintOtherColorText

	def update(self):
		if system() == 'Windows':
			from .output import PrintOtherColorText

		if self.blocks > self.block_amount:
			raise ProgressBarError("blocks to show is greater tan block amount\n                  要显示的方块大于方块的数量")
		self.output_text = edge + ('█' * blocks) + ('  ' * (block_amount - blocks)) + edge + ' ' + text

		if system() == 'Windows':
			PrintOtherColorText(self.output_text, color=self.color, end='\n')
		else:
			print(self.output_text)

		if system() == 'Windows':
			del PrintOtherColorText
