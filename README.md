# Command Listener

* MacOSX:
  * `brew install portaudio`
    * Necessary for capturing microphone input
  * `brew install automake`


* Linux (Raspberry Pi 3):
  * `sudo apt install libasound2-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg`
  * `sudo apt-get install python-pyaudio python3-pyaudio`
    * Necessary for capturing microphone input
  * `sudo apt-get install -y python python-dev python-pip build-essential swig git libpulse-dev`
  * Follow the steps [here](https://howchoo.com/g/ztbhyzfknze/how-to-install-pocketsphinx-on-a-raspberry-pi#extract-the-files-into-separate-directories)
  * `sudo apt-get install xsel xclip flac`
  * Remove line from `%(name)s=probesysfs,provider=hidinput` from `~/.kivy/config.ini`
  * Follow the steps [here](https://www.dexterindustries.com/howto/make-your-raspberry-pi-speak/)
  * Create `alias say=espeak -ven-us` inside `~/.bashrc` 

* For all OSs:
  * Install  [PocketSpinx](http://jrmeyer.github.io/asr/2016/01/09/Installing-CMU-Sphinx-on-Ubuntu.html)
  * `pip3 install -r requirements.txt`
  * `python3 main.py`
