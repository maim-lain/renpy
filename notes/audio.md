# Audio

<br>

## Formats
- Opus
- Ogg Vorbis
- MP3
- WAV (uncompressed PCM only)

<br>
<br>

## Playing Audio
```renpy
# Use the file name, Automatically loops
play music "illurock.ogg"


# Sound effects do not loop
play sound "effect.ogg"


# Fade out old audio, fade in new audio
play music "illurock.ogg" fadeout 1.0 fadein 1.0


# Stop music
stop music fadeout 1.0


# Queue music
queue music "next_track.opus"
queue music ["song1.ogg", "song2.ogg"]


# Don't loop music
play music "illurock.ogg" noloop


# A specified duration of silence can played using a filename like "<silence 3.0>",
# where 3.0 is the number of seconds of silence that is desired.
# This can be used to delay the start of a sound file.
play audio ["<silence .5>", "boom.opus"]
```

<br>
<br>

### Main Menu Music
```renpy
define config.main_menu_music = None
```
