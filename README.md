### Intro 
Exj is intended to simplify the maintenance of a workout journal.

It is not bound to any particular sports or activity and tries to be 
flexible enough to serve as a substitute for the pen and paper, yet providing
some additional conveniences and automation.

With the current version of the program, it should be possible to store
a sequence of training sessions and exercises you perform. Besides, the 
functionality should be sufficient for creating and following simple
cyclic training programs.

Common gym exercises are supported out of the box, other types can be added if necessary.

The journal is saved as a JSON file which can be edited in an ordinary text
editor and easily converted to other formats of your choice.

### Installation
Exj is written using [Kivy](https://kivy.org/#home) library, which is necessary to run the program.

On **Debian GNU/Linux**:
```bash
sudo apt-get install python2-kivy
git clone https://github.com/noooway/exj /your-folder/
cd /your-folder/exj
python main.py
```

On **Android** device:  
Currently, there is no precompiled package exists, and the simplest way to run the program
is by using [Kivy Launcher](https://play.google.com/store/apps/details?id=org.kivy.pygame&hl=ru).

1. Install [Kivy Launcher](https://play.google.com/store/apps/details?id=org.kivy.pygame&hl=ru) from Google Play.
2. Locate `kivy` folder on your device ( e.g. `/storage/emulated/0/kivy` ).
3. [Download Exj sources](https://github.com/noooway/exj/archive/master.zip), unpack them, and move the `exj-master` folder into `kivy` folder (some archivers create intermediate folder while unpacking; the directory containing source code is necessary).  
4. Run Kivy Launcher and select "exj". 