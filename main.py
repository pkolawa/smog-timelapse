#!/usr/bin/python

###

###


import subprocess, math, time
# import drawText, everyPicture,
from useDatabase import UseDatabase


class SmogTimelapse:
	def __init__(self):
		is_resolution_set = False
		is_time_set = False
		is_interval_set = False
		is_filename_set = False
		is_movie_set = False
		is_fps_set = False
		is_zip_set = False
		is_subtitles_set = False
		# drawer = new DrawText()
		# pictures = new EveryPicture()
		myDatabase = UseDatabase()

		while is_resolution_set == False:
			chosen_width = int(input("Set pictures width: "))
			chosen_height = int(input("Set pictures height: "))
			chosen_width = str(chosen_width)
			chosen_height = str(chosen_height)
			is_resolution_set = True


		while is_time_set == False:
			chosen_time = input("Set timelapse time (in seconds): ")
			chosen_time = int(chosen_time) * 1000
			while is_interval_set == False:
				chosen_interval = int(input("Set interval time (in seconds): "))
				chosen_interval = int(chosen_interval) * 1000
				divideable = chosen_time % chosen_interval
				if(chosen_interval < chosen_time and divideable == 0):
					is_interval_set = True
				elif chosen_interval >= chosen_time:
					print("Set interval is higher or equal to timelapse time")
				elif divideable != 0:
					print("Set interval to integer (in miliseconds) multipied by another integer and equal to timelapse time")
			is_time_set = True



		while is_filename_set == False:
			chosen_filename = str(input("Set the filename: \n"))
			is_filename_set = True

		while is_subtitles_set == False:
			subtitles_required = int(input("Would you like to print data on frames?\n 1.Yes\n 2.No"))
			if subtitles_required == 1:
				subtitles_required = True
				is_subtitles_set = True
			elif subtitles_required == 2:
				subtitles_required = False
				is_subtitles_set = True
			else:
				print("Wrong answer. Please, choose again.")

		while is_movie_set == False:
			movie_required = int(input("Would you like to make a movie from pictures?\n 1.Yes\n 2.No\n"))
			if movie_required == 1:
				movie_required = True
				all_frames = chosen_time / chosen_interval
				while is_fps_set == False:
					movie_fps = int(input("Set movie fps (you'll have "+str(all_frames)+" pictures): "))
					divideable = all_frames % movie_fps
					if (movie_fps < all_frames and divideable == 0):
						is_fps_set = True
					else:
						print("Something went wrong. Set fps one more time")
				is_movie_set = True
			elif movie_required == 2:
				movie_required = False
				is_movie_set = True
			else:
				print("Wrong answer. Please, choose again.")

		while is_zip_set == False:
			zip_required = int(input("Would you like to make a ZIP archive from source?\n 1.Yes\n 2.No\n"))
			if zip_required == 1:
				zip_required = True
				is_zip_set = True
			elif zip_required == 2:
				zip_required = False
				is_zip_set = True
			else:
				print("Wrong answer. Please, choose again.")

		chosen_time = str(chosen_time)
		chosen_interval = str(chosen_interval)
		chosen_filename = str(chosen_filename)

		subprocess.call(["mkdir", chosen_filename])
		for now in range(0,int(chosen_time),int(chosen_interval)):
			timestamp_str = int(time.time())
			subprocess.call(["raspistill", "-rot", "180", "-w", str(chosen_width), "-h", str(chosen_height), "-t", str(1000), "-p", "0:0:1:1", "-op", "0", "-o", str(chosen_filename)+"/"+str(timestamp_str)+".jpg"])
			myDatabase.insertData(chosen_filename, timestamp_str)
			sleep_time = int(chosen_interval) - 1000
			sleep_time = sleep_time / 1000
			time.sleep(sleep_time)

		if subtitles_required == True:
			photos = myDatabase.getTimelapse(chosen_filename)
			print(photos)

		if movie_required == True:
			half_fps = math.floor(movie_fps / 2)
			half_fps = str(half_fps)
			movie_fps = str(movie_fps)
			subprocess.call(["avconv", "-r", movie_fps, "-i", chosen_filename+"/"+chosen_filename+"_%04d.jpg", "-r", movie_fps, "-vcodec", "libx264", "-crf", "1", "-g", half_fps, chosen_filename+"/"+chosen_filename+".mp4"])
		if zip_required == True:
			subprocess.call(["tar", "cvzf", chosen_filename+".tar.gz", chosen_filename+"/"])
			subprocess.call(["rm", "-r", chosen_filename+"/"])

SmogTimelapse()
