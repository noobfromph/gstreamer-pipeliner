# gstreamer-pipeliner
The `gstreamer-pipeliner` is a tool that parses GStreamer pipelines stored in a JSON file and provides functionality to execute the pipeline.

### Setup (Fedora 35 and Up)
To set up GStreamer with Fedora OS, follow the steps below:
```bash
dnf -y update
dnf -y groupinstall "Development Tools"
dnf -y install dnf-utils

dnf -y install gtk-doc glib2 glib2-devel speex speex-devel wget pygobject3-devel cairo cairo-devel cairo-gobject cairo-gobject-devel libnotify-devel libnotify libjpeg-turbo-devel nginx pango-devel orc-devel libvorbis-devel libtheora-devel libxml2-devel openssl-devel libsoup-devel mpg123-libs webrtc-audio-processing-devel gnutls-devel libvpx-devel librsvg2-devel

dnf -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
dnf -y install python3-gobject-devel

# autoconf
wget http://ftp.gnu.org/gnu/autoconf/autoconf-2.69.tar.gz
tar xvf autoconf-2.69.tar.gz
cd autoconf-2.69
./configure
make 
make install

# automake
wget http://ftp.gnu.org/gnu/automake/automake-1.14.tar.gz
tar xvzf automake-1.14.tar.gz
cd automake-1.14
./configure
make
make install

# python3
dnf -y install python3
dnf -y install python3-pip
dnf -y install python3-devel

# nasm
cd /etc/yum.repos.d/
wget https://www.nasm.us/nasm.repo
cd /tmp/
dnf -y clean all
dnf -y install nasm

# x264
wget http://ftp.videolan.org/pub/x264/snapshots/x264-snapshot-20191217-2245-stable.tar.bz2
tar xvzf x264-snapshot-20191217-2245-stable.tar.bz2
cd x264-snapshot-20191217-2245-stable
./configure --enable-shared --enable-static --libdir=/usr/lib64
make
make install

# main gstreamer 1.14.3
export REPO_NAME=gstreamer
export GSTREAMER_VERSION=1.14.3

git clone git://anongit.freedesktop.org/git/gstreamer/$REPO_NAME
cd $REPO_NAME
git checkout tags/$GSTREAMER_VERSION
libtoolize
./autogen.sh --disable-gtk-doc --enable-introspection=yes --libdir=/usr/lib64
make
make install

export REPO_NAME=gst-plugins-base
git clone git://anongit.freedesktop.org/git/gstreamer/$REPO_NAME
cd $REPO_NAME
git checkout tags/$GSTREAMER_VERSION
libtoolize
./autogen.sh --disable-gtk-doc --enable-introspection=yes --libdir=/usr/lib64 --enable-rtmp=yes --enable-dash=yes --enable-webrtc=yes --enable-srt=yes
make
sudo make install

# gst-python
git clone git://anongit.freedesktop.org/gstreamer/gst-python
cd gst-python
git checkout tags/$GSTREAMER_VERSION
libtoolize
PYTHON=python3.6 ./autogen.sh --prefix=/usr --with-libpython-dir=/usr/lib64/ --libdir=/usr/lib64
make
make install
```

### Setup Development
To set up the development environment, follow these steps:
```bash
python -m venv env
pip install -r requirements.txt
```

### Running the Application
To run the application, use the following command:
```bash
python app.py pipes.json --exec
```
Where:
- `pipes.json` is the JSON file containing the GStreamer pipeline to process.
- `--exec` is an optional flag indicating whether to execute the generated pipeline.

### JSON input format
The json file format is as described below:
```json
{
    "pipeline": [
        {
            "elem_name": "name of element ",
            "plugin_name": "plugin name such as videotestsrc",
            "attributes": [
                {
                    "key": "such as framerate",
                    "value": "values such as 60 for 60fps"
                }
            ],
            "attach_queue": "as to attach queue for this element, you can manually attach a queue"
        }
}
```
Note: the sequence here is important.

### License
This project is licensed under the MIT License. See the LICENSE file for more information.

### Collaboration
Contributions to the project are welcome! If you would like to collaborate and improve the `gstreamer-pipeliner`, follow the steps below:

- Fork the repository on GitHub.
- Clone your forked repository to your local machine.
- Create a new branch for your feature or bug fix.
- Make your changes and commit them, providing a descriptive commit message.
- Push your changes to your forked repository.
- Submit a pull request to the main repository.
- Please ensure that your contributions adhere to the coding conventions, follow the existing project structure, and include appropriate documentation and test cases.

Thank you for your interest in collaborating on the gstreamer-pipeliner project! Together, we can make it even better.
