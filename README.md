# Plex Anime Scanner

The scanner will choose the following from the folders and file names:

- Anime name
- Anime year
- Season number
- Episode number

## Folder Structure

- Root Folder (the folder that is added as root folder in the **Plex library**)
    - Anime Name (example: **Bleach**)
        - Season 1 (example: **Bleach.S01.1080p.BluRay.DTS.x264-GROUP**)
            - Episode 01 (example: **Bleach.001.1080p.BluRay.DTS.x264-GROUP.mkv**)
            - Episode 02 (example: **Bleach.002.1080p.BluRay.DTS.x264-GROUP.mkv**)
            - Episode 03
            - ...
        - Season 2 (example: **Bleach.S02.1080p.BluRay.DTS.x264-GROUP**)
            - Episode 28 (example: **Bleach.028.1080p.BluRay.DTS.x264-GROUP.mkv**)
            - Episode 29 
            - ...
        - Season 3 (example: **Bleach.S03.1080p.BluRay.DTS.x264-GROUP**)
            - Episode 56 (example: **Bleach.056.1080p.BluRay.DTS.x264-GROUP.mkv**)
            - ...
        - ...
    - ...
    
Note: The scanner will look only 2 levels down, so you need to respect the above folder structure.

### Seasons

The scanner will look on the name of the folder and it will pick up the season number. In order to match correctly the season number, you need to specify it using the following patterns:

- Bleach.**S01**.1080p.BluRay.DTS.x264-GROUP.mkv

Note: Use S01, **not S1**

### Episodes

The scanner will look on the name of the files and it will pick up the episode number. In order to match correctly the season number, you need to specify it using the following patterns:

- Bleach.**009**.1080p.BluRay.DTS.x264-GROUP.mkv
- Bleach.**09**.1080p.BluRay.DTS.x264-GROUP.mkv
- Bleach.**9**.1080p.BluRay.DTS.x264-GROUP.mkv
- Bleach.**EP009**.1080p.BluRay.DTS.x264-GROUP.mkv
- Bleach.**EP09**.1080p.BluRay.DTS.x264-GROUP.mkv
- Bleach.**EP9**.1080p.BluRay.DTS.x264-GROUP.mkv
- [GROUP] Bleach - **009** [8DC34F4C].avi

Note: If you are using something like this Bleach.**1x09**.1080p.BluRay.DTS.x264-GROUP.mkv it will not work.
Note: 

## AniDB Metadata 

The name of the episodes, description, ratting etc will be taken from AniDB using [Hama.bundle](https://github.com/StancuFlorin/Hama.bundle) plugin. This plugin was developed by [ZeroQI](https://github.com/ZeroQI/Hama.bundle) initially, but I did few tweaks in order to support the folder structure I wanted. So you need to use the forked version.

# Installation

- Download [Anime Scanner.py](https://raw.githubusercontent.com/StancuFlorin/Plex-Anime-Scanner/master/Anime%20Scanner.py)
- Save into ``[...]/Plex/Library/Application Support/Plex Media Server/Scanners/Series/Anime Scanner.py`` Note: "Scanners" and "Series" folder are not created by default and will need creating.
- Once the scanner is installed correctly, when creating a library you can select the custom scanner, otherwise the drop-down selection list is not shown.
- Install [Hama.bundle](https://github.com/StancuFlorin/Hama.bundle) plugin. The one developed my me, not the original one for the moment.

# The Result

[https://imgur.com/a/WgaNW](https://imgur.com/a/WgaNW)