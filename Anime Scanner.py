import VideoFiles, Utils, Media, Stack
import re, os, inspect, logging

LOG_PATH = os.path.abspath(os.path.join(os.path.dirname(inspect.getfile(inspect.currentframe())), "..", "..", "Logs"))
logging.basicConfig(filename=os.path.join(LOG_PATH, 'Anime Scanner.log'), level=logging.DEBUG)

regexSeason = '(?P<show>.*?)[S](?P<season>[0-9]{2})'  # S08
regexEpisode = '(?P<show>.*?)(E|EP|Episodul|Special|OVA)?[\._\- ]*(?P<episode>(?<!v)[0-9]+)[v\._\- ]+'  # 160 or EP160 or Special.02
regexMovie = '(?P<show>.*?)(Movie|M)[\._\- ]*(?P<movie>[0-9]+)[\._\- ]+'  # Movie.03 or Movie03 or M.03 or M03


def getAnime(pathAnime):
    (animeName, animeYear) = VideoFiles.CleanName(pathAnime)
    logging.debug("Anime Name: %s" % animeName)
    logging.debug("Anime Year: %s" % animeYear)
    return (animeName, animeYear)


def getSeason(pathSeason):
    seasonNumberMatch = re.search(regexSeason, pathSeason, re.IGNORECASE)
    if seasonNumberMatch:
        seasonNumber = seasonNumberMatch.group('season')
    else:
        seasonNumber = 1

    logging.debug("Season Number: %s" % seasonNumber)
    return seasonNumber


def findEpisodes(animeName, animeYear, seasonNumber, files, mediaList):
    for filePath in files:
        file = os.path.basename(filePath)
        episodeNumberMatch = re.search(regexEpisode, file, re.IGNORECASE)
        movieNumberMatch = re.search(regexMovie, file, re.IGNORECASE)
        if movieNumberMatch:
            movieNumber = movieNumberMatch.group('movie')
            logging.debug("File: %s" % filePath)
            logging.debug("Movie Number: %s" % movieNumber)
            anime = Media.Movie(animeName + ' Movie ' + movieNumber, None)
            anime.parts.append(filePath)
            mediaList.append(anime)
        elif episodeNumberMatch:
            episodeNumber = episodeNumberMatch.group('episode')
            logging.debug("File: %s" % filePath)
            logging.debug("Episode Number: %s" % episodeNumber)
            anime = Media.Episode(animeName, seasonNumber, episodeNumber, None, animeYear)
            anime.parts.append(filePath)
            mediaList.append(anime)


def Scan(path, files, mediaList, subdirs):
    VideoFiles.Scan(path, files, mediaList, subdirs)
    paths = Utils.SplitPath(path)

    logging.debug("---------------------------------------------------")
    logging.debug("Paths: %s" % paths)

    if len(paths) == 1 and len(paths[0]) > 0:
        pathAnime = paths[0]
        (animeName, animeYear) = getAnime(pathAnime)
        findEpisodes(animeName, animeYear, 1, files, mediaList)

    elif len(paths) == 2:
        pathAnime = paths[0]
        (animeName, animeYear) = getAnime(pathAnime)

        pathSeason = paths[1]
        seasonNumber = getSeason(pathSeason)
        findEpisodes(animeName, animeYear, seasonNumber, files, mediaList)

    Stack.Scan(path, files, mediaList, subdirs)
