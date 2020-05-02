# Ranger theme
# Tasty wine colors

from ranger.gui.colorscheme import ColorScheme
from ranger.gui.color import *

NeoPackage = {208, 209, 210, 211, 212, 213}

BPack1 = 23
BPack2 = 188
BPack3 = 73
BPack4 = 66
BPack5 = 31

NeoOrange = 208
NeoWarning = 88
NeoPurple = 140
NeoCyan = 159
NeoPink = 210

class Default(ColorScheme):
	def use(self, context):
		fg, bg, attr = default_colors

		if context.reset:
			return default_colors

		elif context.in_browser:
			if context.selected:
                                attr = reverse
			else:
				attr = normal
			if context.empty or context.error:
				bg = NeoWarning
			if context.border:
				attr = normal
				fg = black
			if context.media:
				if context.image:
					fg = 209
				else:
					fg = NeoCyan
			if context.container:
				attr |= bold
				fg = NeoCyan
			if context.directory:
				attr |= normal
				fg = BPack3
			elif context.executable and not \
					any((context.media, context.container,
						context.fifo, context.socket)):
				attr |= normal
				fg = NeoCyan
			if context.socket:
				fg = NeoCyan
			if context.fifo or context.device:
				fg = NeoCyan
				if context.device:
					attr |= bold
			if context.link:
				fg = context.good and NeoCyan or NeoPurple
			if context.tag_marker and not context.selected:
				attr |= bold
				if fg in (NeoWarning, NeoPurple):
					fg = black
				else:
					fg = red
			if not context.selected and (context.cut or context.copied):
				fg = NeoCyan
				attr |= bold
			if context.main_column:
				if context.selected:
					attr |= normal
				if context.marked:
					attr |= bold
					fg = yellow
			if context.badinfo:
				if attr & reverse:
					bg = magenta
				else:
					fg = 213

		elif context.in_titlebar:
			attr |= normal
			if context.hostname:
				attr |= bold
				fg = context.bad and NeoOrange or NeoCyan
			elif context.directory:
				fg = BPack2
			elif context.tab:
				if context.good:
					bg = 213
			elif context.link:
				fg = NeoCyan

		elif context.in_statusbar:
			if context.permissions:
				if context.good:
					fg = black
				elif context.bad:
					fg = magenta
			if context.marked:
				attr |= bold | reverse
				fg = yellow
			if context.message:
				if context.bad:
					attr |= bold
					fg = red

		if context.text:
			if context.highlight:
				attr |= reverse

		if context.in_taskview:
			if context.title:
				fg = NeoCyan

			if context.selected:
				attr |= reverse

		return fg, bg, attr
