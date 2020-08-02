"""
Add watermarks to video files.
在视频文件中添加水印。
"""

from platform import system

if system() == 'Windows':

	del system

	class FFmpegNotFoundError(Exception):
		pass

	def get_ffmpeg_exe():
		from os import getenv
		from sys import path
		from os.path import join, isfile

		exe_path = getenv("COLOR_TEXT_FFMPEG_EXE", None)
		if exe_path:
			return exe_path
		else:
			exe_path = join(path[0], 'color_text/ffmpeg.exe')
			if isfile(exe_path):
				return exe_path
			else:
				exe_path = join(path[5], 'color_text/ffmpeg.exe')
				if isfile(exe_path):
					return exe_path
				else:
					exe_path = join(path[0], 'ffmpeg.exe')
					if isfile(exe_path):
						return exe_path
					else:
						error = FFmpegNotFoundError("Unable to find FFmpeg, try reinstalling this library.\n                                   找不到FFmpeg，请尝试重新安装。")
						raise error

		del getenv
		del path
		del join

	ffmpeg_path = get_ffmpeg_exe()

	all_watermark_colors = ["red", "green", "pink", "purple", "brown", "grey", "black", "blue", "white", "orange", "yellow"]

	class ColorTextError(Exception):
		pass

	def AddWatermarksToVideoFile(video_file, output_file, show_informations=False, *args):
		"""
		Add watermarks to a video file.
		添加水印到视频文件。
		"""

		if video_file == output_file:
			error = ColorTextError("The original file has the same name as the output file.\n                                   原文件和输出文件同名。")
			raise error

		from subprocess import PIPE, run
		from os import remove
		from shutil import copy
		from os.path import isfile
		from sys import path

		if type(show_informations) != bool:
			error = ColorTextError("show_informations parameter must be bool.\n                                   show_informations参数的类型必须为bool。")
			raise error

		if show_informations:
			from os import system

		if not show_informations:
			def system(command):
				result = run(command, stdout = PIPE, stderr = PIPE, universal_newlines = True, shell = True)
				return result.stdout

		times = 0

		file_arg = args[0]

		watermark_type = file_arg['type']
		if watermark_type != 'text' and watermark_type != 'photo':
			error = ColorTextError("Invalid type.\n                                   无效的类型。")
			raise error

		pos = file_arg['pos']
		if len(pos) != 2:
			error = ColorTextError("The length of the pos parameter must be 2.\n                                   pos参数的长度必须为2。")
			raise error
		if type(pos[0]) != int or type(pos[1]) != int:
			error = ColorTextError("Numbers in pos parameter must be int.\n                                   pos参数中的数的类型必须为int。")
			raise error

		if watermark_type == "text":
			times = 1

			text = file_arg['text']
			if type(text) != str:
				error = ColorTextError("Text parameter must be str.\n                                   text参数的类型必须为str。")
				raise error

			font_size = file_arg['font_size']
			if type(font_size) != int:
				error = ColorTextError("Font_size parameter must be int.\n                                   font_size参数的类型必须为int。")
				raise error

			font_file = file_arg['font_file']
			if not isfile(font_file):
				error = ColorTextError("Font_file parameter must be a real file.\n                                   font_file参数的中的值必须为一个真实的字体文件。")
				raise error

			font_color = file_arg['font_color']
			if not font_color in all_watermark_colors:
				error = ColorTextError("Font_color parameter must be a color.\n                                   font_color参数的中的值必须为一个颜色。")
				raise error

			shadowy = file_arg['shadowy']
			if type(shadowy) != int:
				error = ColorTextError("Shadowy parameter must be int.\n                                   shadowy参数的类型必须为int。")
				raise error

			if isfile("temp_video_" + str(times) + ".mp4"):
				remove("temp_video_" + str(times) + ".mp4")
			system(ffmpeg_path + ' -i ' + video_file + ' -vf "drawtext=fontfile=' + font_file + ': ' + "'" + text +
				"'" + ':' + 'x=' + str(pos[0]) + ':' + 'y=' + str(pos[1]) + ':' + 'fontsize=' + str(font_size) + ':' + 'fontcolor=' +
				font_color + ':' + 'shadowy=' + str(shadowy) + '" ' + ("temp_video_" + str(times) + ".mp4"))

		elif watermark_type == "photo":

			photo_file = file_arg['photo_file']
			if not isfile(photo_file):
				error = ColorTextError("Photo_file parameter must be a real file.\n                                   font_file参数的中的值必须为一个真实的图片文件。")
				raise error

			if isfile("temp_video_" + str(times) + ".mp4"):
				remove("temp_video_" + str(times) + ".mp4")
			system(ffmpeg_path + ' -i ' + video_file + ' -vf "movie=' + photo_file + '[watermark];[in][watermark] overlay=main_w-overlay_w-' +
				str(pos[0]) + ':main_h-overlay_h-' + str(pos[1]) + '[out] " ' + ("temp_video_" + str(times) + ".mp4"))

		for file_arg in args[1:]:
			times += 1

			watermark_type = file_arg['type']
			if watermark_type != 'text' and watermark_type != 'photo':
				error = ColorTextError("Invalid type.\n                                   无效的类型。")
				raise error

			pos = file_arg['pos']
			if len(pos) != 2:
				error = ColorTextError("The length of the pos parameter must be 2.\n                                   pos参数的长度必须为2。")
				raise error
			if type(pos[0]) != int or type(pos[1]) != int:
				error = ColorTextError("Numbers in pos parameter must be int.\n                                   pos参数中的数的类型必须为int。")
				raise error

			if watermark_type == "text":
				text = file_arg['text']
				if type(text) != str:
					error = ColorTextError("Text parameter must be str.\n                                   text参数的类型必须为str。")
					raise error

				font_size = file_arg['font_size']
				if type(font_size) != int:
					error = ColorTextError("Font_size parameter must be int.\n                                   font_size参数的类型必须为int。")
					raise error

				font_file = file_arg['font_file']
				if not isfile(font_file):
					error = ColorTextError("Font_file parameter must be a real file.\n                                   font_file参数的中的值必须为一个真实的字体文件。")
					raise error

				font_color = file_arg['font_color']
				if not font_color in all_watermark_colors:
					error = ColorTextError("Font_color parameter must be a color.\n                                   font_color参数的中的值必须为一个颜色。")
					raise error

				shadowy = file_arg['shadowy']
				if type(shadowy) != int:
					error = ColorTextError("Shadowy parameter must be int.\n                                   shadowy参数的类型必须为int。")
					raise error

				if isfile("temp_video_" + str(times) + ".mp4"):
					remove("temp_video_" + str(times) + ".mp4")
				system(ffmpeg_path + ' -i ' + ("temp_video_" + str(times - 1) + ".mp4") + ' -vf "drawtext=fontfile=' + font_file + ': ' + "'" + text +
					"'" + ':' + 'x=' + str(pos[0]) + ':' + 'y=' + str(pos[1]) + ':' + 'fontsize=' + str(font_size) + ':' + 'fontcolor=' +
					font_color + ':' + 'shadowy=' + str(shadowy) + '" ' + ("temp_video_" + str(times) + ".mp4"))

			elif watermark_type == "photo":
				photo_file = file_arg['photo_file']
				if not isfile(photo_file):
					error = ColorTextError("Photo_file parameter must be a real file.\n                                   font_file参数的中的值必须为一个真实的图片文件。")
					raise error

				if isfile("temp_video_" + str(times) + ".mp4"):
					remove("temp_video_" + str(times) + ".mp4")
				system(ffmpeg_path + ' -i ' + ("temp_video_" + str(times - 1) + ".mp4") + ' -vf "movie=' + photo_file + '[watermark];[in][watermark] overlay=main_w-overlay_w-' +
					str(pos[0]) + ':main_h-overlay_h-' + str(pos[1]) + '[out] " ' + ("temp_video_" + str(times) + ".mp4"))

		copy("temp_video_" + str(times) + ".mp4", output_file)
		all_temp_files = list(range(1, times + 1))
		for temp_file in all_temp_files:
			remove("temp_video_" + str(temp_file) + ".mp4")

		del system, remove
		del copy
		del isfile
		del path
		del PIPE, run

	def AddTextWatermarkToVideoFile(video_file, output_file, pos, font_file, text, font_size, font_color, shadowy, show_informations=False):
		"""
		Add a text watermark to a video file.
		添加一个文字水印到视频文件。
		"""
		AddWatermarksToVideoFile(video_file, output_file, show_informations, {'type': 'text', 'pos': pos, 'font_file': font_file, 'text': text,'font_size': font_size, 'font_color': font_color, 'shadowy': shadowy})

	def AddPhotoWatermarkToVideoFile(video_file, ouput_file, pos, photo_file, show_informations=False):
		"""
		Add a photo watermark to a video file.
		添加一个图像水印到视频文件。
		"""
		AddWatermarksToVideoFile(video_file, output_file, show_informations, {'type': 'photo', 'pos': pos, 'photo_file': photo_file})

else:
	del system
