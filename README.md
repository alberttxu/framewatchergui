# framewatchergui

framewatchergui is a GUI wrapper for IMOD's framewatcher tool.

## Requirements
- IMOD 4.10.10 or higher
- If running on Windows: Cygwin and VcXsrv

## Install
Centos 7

- Install IMOD: `sudo sh -c 'curl -O http://bio3d.colorado.edu/ftp/latestIMOD/RHEL7-64_CUDA8.0/imod_4.10.31_RHEL7-64_CUDA8.0.sh && echo 'Y' | sh imod_4.10.31_RHEL7-64_CUDA8.0.sh && rm imod_4.10.31_RHEL7-64_CUDA8.0.sh'`
 - `sudo yum install -y epel-release`
- `sudo yum install -y python36-tkinter python36-pip`
- `sudo python36 -m pip install framewatchergui`

Windows

- Download the Cygwin [setup-x86_64.exe](https://cygwin.com/setup-x86_64.exe) installer
- Download this repository's [cygwin_dependencies.bat](https://raw.githack.com/alberttxu/framewatchergui/master/cygwin_install_scripts/cygwin_dependencies.bat) into the same folder.
- Double click the cygwin_dependencies.bat file to start the installer. Continue clicking next until the installation is finished.
	> If a Cygwin installation already exists at C:\cygwin64, this will add the dependencies and not overwrite any packages.
- Download and install [VcXsrv](https://sourceforge.net/projects/vcxsrv/) Windows X Server
- Start VcXsrv (Start Menu -> XLaunch -> Next -> Next -> Next -> Finish).
	> You need to start VcXsrv for your user on every boot. It is easiest to keep the X server session number to 0.0, so make sure other users have not already started VcXsrv.
- Open Cygwin terminal
- Install IMOD (4.10.31 in this case) : `curl -O http://bio3d.colorado.edu/ftp/latestIMOD/win64_CUDA8.0/imod_4.10.31_win64_CUDA8.0.sh && echo 'Y' | sh imod_4.10.31_win64_CUDA8.0.sh`
- Install framewatchergui: `python3 -m pip install framewatchergui`
- Set DISPLAY environment variable: `echo 'export DISPLAY=:0.0' >> ~/.bash_profile`


## Usage
If Align is unchecked, framewatcher will watch the Watch Directory for .mrc and .tif files and move them and their associated .pcm files to the Processed Directory.

If Align is checked, framewatcher will watch the Watch Directory for .mrc and .tif files and move them and their associated .pcm files to temporary directories for aligning. Each temporary directory should have a worker enabled.

The multiplier option for a worker increases the load to its queue when there are multiple workers aligning files in round-robin. E.g. A worker with GPU enabled can align movies 2-3x faster than CPU only workers, so it should have a multiplier of 2 (or 3).

For Options information, see the [framewatcher man page](http://bio3d.colorado.edu/imod/betaDoc/man/framewatcher.html).
