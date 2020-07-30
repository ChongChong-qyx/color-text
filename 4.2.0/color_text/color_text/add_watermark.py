"""
Add watermarks to video files.
在视频文件中添加水印。
"""

from platform import system

if system() == 'Windows':

	del system

	def AddWatermarksToVideoFile(video_file, output_file, *args):
		"""
		Add watermarks to a video file.
		添加水印到视频文件。
		"""

		from os import system
		from shutil import copy as copy_file
		from sys import path as now_path

		print(args)

		times = 0

		file_arg = args[0]

		type = file_arg['type']
		pos = file_arg['pos']

		if type == "text":
			times = 1

			text = file_arg['text']
			font_size = file_arg['font_size']
			font_file = file_arg['font_file']
			font_color = file_arg['font_color']
			shadowy = file_arg['shadowy']

			system(r'.\ffmpeg.exe -i ' + video_file + ' -vf "drawtext=fontfile=' + font_file + ': ' + "'" + text +
				"'" + ':' + 'x=' + str(pos[0]) + ':' + 'y=' + str(pos[1]) + ':' + 'fontsize=' + str(font_size) + ':' + 'fontcolor=' +
				font_color + ':' + 'shadowy=' + str(shadowy) + '" ' + ("temp_video_" + str(times) + ".mp4"))

		elif type == "photo":
			photo_file = file_arg['photo_file']

			system(r'.\ffmpeg.exe -i ' + video_file + ' -vf "movie=' + photo_file + '[watermark];[in][watermark] overlay=main_w-overlay_w-' +
				str(pos[0]) + ':main_h-overlay_h-' + str(pos[1]) + '[out] " ' + ("temp_video_" + str(times) + ".mp4"))

		for file_arg in args[1:]:
			times += 1

			type = file_arg['type']
			pos = file_arg['pos']

			if type == "text":
				text = file_arg['text']
				font_size = file_arg['font_size']
				font_file = file_arg['font_file']
				font_color = file_arg['font_color']
				shadowy = file_arg['shadowy']

				system(r'.\ffmpeg.exe -i ' + ("temp_video_" + str(times - 1) + ".mp4") + ' -vf "drawtext=fontfile=' + font_file + ': ' + "'" + text +
					"'" + ':' + 'x=' + str(pos[0]) + ':' + 'y=' + str(pos[1]) + ':' + 'fontsize=' + str(font_size) + ':' + 'fontcolor=' +
					font_color + ':' + 'shadowy=' + str(shadowy) + '" ' + ("temp_video_" + str(times) + ".mp4"))

			elif type == "photo":
				photo_file = file_arg['photo_file']

				system(r'.\ffmpeg.exe -i ' + ("temp_video_" + str(times - 1) + ".mp4") + ' -vf "movie=' + photo_file + '[watermark];[in][watermark] overlay=main_w-overlay_w-' +
					str(pos[0]) + ':main_h-overlay_h-' + str(pos[1]) + '[out] " ' + ("temp_video_" + str(times) + ".mp4"))

		del system

	AddWatermarksToVideoFile('a.avi', 'a.mp4', {'type': 'text', 'pos': (10, 10), 'font_file': "simhei.ttf", 'text': "我是着急", 'font_size': 50, 'font_color': "white", 'shadowy': 3},
		{'type': 'photo', 'pos': (20, 20), 'photo_file': 'a.png'})

else:
	del system
