
# qt audio monitor

This is a minimal-case example how to get continuous PCM data from the sound card. A preliminary SWHEar class is included which can self-detect likely input devices. To manually define an input device, set it when SWHEar() is called. In most cases it will work right out of the box. If you're playing music and no microphone is detected, it will use the sound mapper and graph the audio being played.

![demo](demo.gif)