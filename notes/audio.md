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
# The play music statement takes a filename that is interpreted as an audio file to play.
    play music "illurock.ogg"

# When changing music, one can supply a fadeout and a fadein clause,
# which are used to fade out the old music and fade in the new music.
    play music "illurock.ogg" fadeout 1.0 fadein 1.0
    
# The queue music statement plays an audio file after the current file finishes playing.
    queue music "next_track.opus"
    queue music ["song1.ogg", "song2.ogg"]
    
# Music can be stopped with the stop music statement, which can also optionally take a fadeout clause.
    stop music

# Sound effects can be played with the play sound statement. Unlike music, sound effects do not loop.
    play sound "effect.ogg"

# The loop clause causes the music to loop, while noloop causes it to play only once.

# A specified duration of silence can played using a filename like "<silence 3.0>",
# where 3.0 is the number of seconds of silence that is desired.
# This can be used to delay the start of a sound file.
    play audio [ "<silence .5>", "boom.opus" ]
```

<br>
<br>

### Main Menu Music
```renpy
define config.main_menu_music = None
```
