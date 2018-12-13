# Homer Controller - Voice Command Listener

This app enables sending voice commands to [graphql-api](https://github.com/HomeIoTController/graphql-api). On that note, before installing this app please read and setup [compose](https://github.com/HomeIoTController/compose). This is mandatory for this application to work!

## Getting Started

* MacOSX setup:
  * `brew install portaudio`
    * Necessary for capturing microphone input
  * `brew install automake`


* Linux (including Raspberry Pi) setup:
  * `sudo apt install libasound2-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg`
  * `sudo apt-get install python-pyaudio python3-pyaudio`
    * Necessary for capturing microphone input
  * `sudo apt-get install -y python python-dev python-pip build-essential swig git libpulse-dev`


* For all OSs:
  * `pip3 install -r requirements.txt`
  * `python3 main.py`

## Using PocketSpinx for voice recognition

  * This project is currently using `recognizer.recognize_google(audio)`. However, you can also use `recognizer.recognize_sphinx` as an open source alternative. To do that follow the steps bellow:

    * Install [PocketSpinx](http://jrmeyer.github.io/asr/2016/01/09/Installing-CMU-Sphinx-on-Ubuntu.html)
    * Raspberry Pi only:
      * Follow the steps [here](https://howchoo.com/g/ztbhyzfknze/how-to-install-pocketsphinx-on-a-raspberry-pi#extract-the-files-into-separate-directories)
      * `sudo apt-get install xsel xclip flac`
      * Remove line from `%(name)s=probesysfs,provider=hidinput` from `~/.kivy/config.ini`
      * Follow the steps [here](https://www.dexterindustries.com/howto/make-your-raspberry-pi-speak/)
      * Create `alias say=espeak -ven-us` inside `~/.bashrc`
