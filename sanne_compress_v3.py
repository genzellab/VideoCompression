import os

#videos_path="/home/samanta/bebinca/objectspace/mouse/Catastrophic_Interference";
# videos_path="/mnt/genzel/Rat/OS/OS_rat_ephys/cheese videos_rat3+4";
#videos_path="/home/adrian/Documents/test_compression";
#videos_path="/media/adrian/GL04_RAT_HOMER/RAT_OS_RGS14/RGS14_Batch8_9_cOD48h/Batch9";
videos_path="/media/adrian/My Passport/ephys/rat6/Rat_OS_Ephys_Rat6_SD2_OD_19-20_02_2018"; #"/home/adrian/Downloads/ai4";
videos_format=".avi";#".mp4" #".webm";#".avi"


def find_downsampled():
  all = []
  for root, dirs, files in os.walk(videos_path):
      for file in files:
          if file.endswith(videos_format):
            if 'downsampled' in file:
              all.append(os.path.join(root, file))
  return all
            
def find_finished_total():  
  total = 0
  finished = 0
  for root, dirs, files in os.walk(videos_path):
      for file in files:
          if file.endswith(videos_format):
            if 'downsampled' not in file:
              total += 1
              #file_z = file.replace('.', 'downsampled.')
              file_z = file.replace(videos_format, 'downsampled' + videos_format)
              if os.path.join(root, file_z) in all:
                finished += 1
  return finished, total

def downsample_stuff(all, finished, total):
  for root, dirs, files in os.walk(videos_path):
      for file in files:
          if file.endswith(videos_format):
            old_file = os.path.join(root, file)
            already_in = False      
            if 'downsampled' not in file:
              file_z = file.replace('.', 'downsampled.')
              if os.path.join(root, file_z) in all:
                  already_in = True
                  #print(os.path.join(root, file))
              if already_in is False:
                  old_file = os.path.join(root, file)
                  file_l = file.split('.')
                  file_l[1] = 'downsampled'
                  file_l.append(videos_format) #might need the change from " to ' in the video format string.
                  file = ''.join(file_l)
                  new_file =  os.path.join(root, file)
                  #ffmpeg -i {old_file} -filter:v scale=-1:256 -c:a copy {new_file}
                  # os.system("ffmpeg -r 30 -i {old_file} -filter:v scale=-1:256 -c:a copy {new_file}".format(old_file=old_file, new_file=new_file)) #Original
                  os.system('ffmpeg -r 30 -i "{old_file}" -filter:v scale=-1:256 -c:a copy "{new_file}"'.format(old_file=old_file, new_file=new_file))
                  #os.system("ffmpeg -r 30 -i {old_file} -filter:v 'scale=-1:1440,pad=ceil(iw/2)*2:ih' -c:a copy {new_file}".format(old_file=old_file, new_file=new_file))
                  #os.system("ffmpeg -r 30 -i {old_file} -filter:v 'scale=-1:2160,pad=ceil(iw/2)*2:ih' -c:a copy {new_file}".format(old_file=old_file, new_file=new_file))
                  #os.system("ffmpeg -r 30 -i {old_file} -filter:v 'scale=-1:4320,pad=ceil(iw/2)*2:ih' -c:a copy {new_file}".format(old_file=old_file, new_file=new_file))
                  finished += 1
                  print(total, '/', finished)
                  #os.remove(old_file)
              #if already_in is True:
                  #os.remove(old_file)
# %%
all = find_downsampled()
finished, total = find_finished_total()
downsample_stuff(all, finished,total)
print(total, '/', finished)
print(total, '/', len(all))
# everything downsampled is "done" so -- all = done
# everything not downsampled is to do -- so create list with that
# everything everything is all avi videos -- so create list with that

# total = all non downsampled videos
# all = all downsampled videos
# finished = all already downsampled videos
