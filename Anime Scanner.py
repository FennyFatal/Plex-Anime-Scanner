import VideoFiles, Utils, Media, Stack
import re, os, inspect, logging

LOG_PATH = os.path.abspath(os.path.join(os.path.dirname(inspect.getfile(inspect.currentframe())), "..", "..", "Logs"))
logging.basicConfig(filename=os.path.join(LOG_PATH, 'Anime Scanner.log'), level=logging.DEBUG)

regexSeason = '(?P<show>.*?)[\._\- ]+[sS](?P<season>[0-9]{2})'             # S08
regexEpisode = '(?P<show>.*?)[\._\- EP]+(?P<episode>[0-9]+)[\._\- ]+'      # 160 or EP160

def Scan(path, files, mediaList, subdirs):

	VideoFiles.Scan(path, files, mediaList, subdirs)
	paths = Utils.SplitPath(path)

	logging.debug("---------------------------------------------------") 
	logging.debug("Paths: %s" % paths)
	
	if len(paths) == 2:
		pathAnime = paths[0]
		pathSeason = paths[1]
		(animeName, animeYear) = VideoFiles.CleanName(pathAnime)
		logging.debug("Anime Name: %s" % animeName) 
		logging.debug("Anime Year: %s" % animeYear)
		
		seasonNumberMatch = re.search(regexSeason, pathSeason, re.IGNORECASE)
		if seasonNumberMatch:
			seasonNumber = seasonNumberMatch.group('season')
			logging.debug("Season Number: %s" % seasonNumber)
		else:
			seasonNumber = 1
			
		for file in files:
			episodeNumberMatch = re.search(regexEpisode, file, re.IGNORECASE)
			if episodeNumberMatch:
				episodeNumber = episodeNumberMatch.group('episode')
				logging.debug("File: %s" % file)
				logging.debug("Episode Number: %s" % episodeNumber)
				anime = Media.Episode(animeName, seasonNumber, episodeNumber, None, animeYear)
				anime.parts.append(file)
				mediaList.append(anime)
				
	Stack.Scan(path, files, mediaList, subdirs)