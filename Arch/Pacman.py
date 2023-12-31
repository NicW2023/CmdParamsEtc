### First check if any manual interventions are necessary here:
### https://archlinux.org/
### !!!!!!!!!!!!!!!!ADD TO A RSS!!!!!!!!!!!!!!!!!!!!!
### Also maybe install this from the AUR https://aur.archlinux.org/packages/informant


### https://wiki.archlinux.org/title/pacman
### https://wiki.archlinux.org/title/PKGBUILD
### https://wiki.archlinux.org/title/Creating_packages

#########################################################################################################
### Update all packages on the system:
#########################################################################################################
pacman -Syu

#########################################################################################################
### Querying package databases
#########################################################################################################
### Pacman queries the local package database with the -Q flag, the sync database with the -S flag and the files database with the -F flag. See pacman -S --help
### Search for packages in the database, searching both in packages' names and descriptions: 
pacman -Ss string1 string2 ...

#########################################################################################################
### view the dependency tree of a package:
#########################################################################################################
pactree package_name

### add the -r flag if you want to see the tree of things that depend on this package (the reverse of the above)


#########################################################################################################
### Cleaning the cache:
### https://wiki.archlinux.org/title/Pacman#Cleaning_the_package_cache
#########################################################################################################


#########################################################################################################
### Other commands
#########################################################################################################
### Download a package without installing it:
pacman -Sw package_name

### Install a 'local' package that is not from a remote repository (e.g. the package is from the AUR):
pacman -U /path/to/package/package_name-version.pkg.tar.zst

### To keep a copy of the local package in pacman's cache, use:
pacman -U file:///path/to/package/package_name-version.pkg.tar.zst

### Install a 'remote' package (not from a repository stated in pacman's configuration files):
pacman -U http://www.example.com/repo/example.pkg.tar.zst

### To inhibit the -S, -U and -R actions, -p can be used.
### Pacman always lists packages to be installed or removed and asks for permission before it takes action. 


#########################################################################################################
### Configuration
#########################################################################################################
### Pacman's settings are located in /etc/pacman.conf: this is the place where the user configures the program to work in the desired manner.

### Skip package from being upgraded:
### To have a specific package skipped when upgrading the system, add this line in the [options] section:
# IgnorePkg=linux
### For multiple packages use a space-separated list, or use additional IgnorePkg lines.


#########################################################################################################
### Package security
#########################################################################################################
### Pacman supports package signatures, which add an extra layer of security to the packages. The default configuration, SigLevel = Required DatabaseOptional, enables signature verification for all the packages on a global level. This can be overridden by per-repository SigLevel lines. For more details on package signing and signature verification, take a look at pacman-key. 
### https://wiki.archlinux.org/title/Pacman-key


#########################################################################################################
### Troubleshooting
#########################################################################################################
### https://wiki.archlinux.org/title/Pacman#Troubleshooting


#########################################################################################################
### Flags
#########################################################################################################
-R, --remove
## Remove package(s) from the system. Groups can also be specified to be removed, in which case every package in that group will be removed. Files belonging to the specified package will be deleted, and the database will be updated. Most configuration files will be saved with a .pacsave extension unless the --nosave option is used. See Remove Options below.

-S, --sync
## Synchronize packages. Packages are installed directly from the remote repositories, including all dependencies required to run the packages. For example, pacman -S qt will download and install qt and all the packages it depends on. If a package name exists in more than one repository, the repository can be explicitly specified to clarify the package to install: pacman -S testing/qt. You can also specify version requirements: pacman -S "bash>=3.2". Quotes are needed, otherwise the shell interprets ">" as redirection to a file. 
## Packages that provide other packages are also handled. For example, pacman -S foo will first look for a foo package. If foo is not found, packages that provide the same functionality as foo will be searched for. If any package is found, it will be installed. A selection prompt is provided if multiple packages providing foo are found.
## You can also use pacman -Su to upgrade all packages that are out-of-date. See Sync Options below. When upgrading, pacman performs version comparison to determine which packages need upgrading. This behavior operates as follows:

# Alphanumeric:
# 1.0a < 1.0b < 1.0beta < 1.0p < 1.0pre < 1.0rc < 1.0 < 1.0.a < 1.0.1
# Numeric:
# 1 < 1.0 < 1.1 < 1.1.1 < 1.2 < 2.0 < 3.0.0

-V, --version
## Display version and exit.

-h, --help
## Display syntax for the given operation. If no operation was supplied, then the general syntax is shown.


#########################################################################################################
### Transaction Options
#########################################################################################################
-p, --print
## Only print the targets instead of performing the actual operation (sync, remove or upgrade). Use --print-format to specify how targets are displayed. The default format string is "%l", which displays URLs with -S, file names with -U, and pkgname-pkgver with -R.


#########################################################################################################
### SYNC OPTIONS (APPLY TO -S)
#########################################################################################################
-i, --info
## Display information on a given sync database package. Passing two --info or -i flags will also display those packages in all repositories that depend on this package.

-s, --search <regexp>
## This will search each package in the sync databases for names or descriptions that match regexp. When you include multiple search terms, only packages with descriptions matching ALL of those terms will be returned.

-u, --sysupgrade
## Upgrades all packages that are out-of-date. Each currently-installed package will be examined and upgraded if a newer package exists. A report of all packages to upgrade will be presented, and the operation will not proceed without user confirmation. Dependencies are automatically resolved at this level and will be installed/upgraded if necessary. 
## Additional targets can also be specified manually, so that -Su foo will do a system upgrade and install/upgrade the "foo" package in the same operation.

-y, --refresh
## Download a fresh copy of the master package database from the server(s) defined in pacman.conf(5). This should typically be used each time you use --sysupgrade or -u. Passing two --refresh or -y flags will force a refresh of all package databases, even if they appear to be up-to-date.



#########################################################################################################
### Bonus commands
#########################################################################################################
### To list all packages no longer required as dependencies (orphans):
pacman -Qdt

### To list all packages explicitly installed and not required as dependencies:
pacman -Qet

### To display extensive information about a given package:
pacman -Si package_name

### To remove a package and its dependencies which are not required by any other installed package:
pacman -Rs _package_name_

### To check which packages depend on a given package:
pacman -Qi qt
pacman -Sii qt

### To list packages not installed from the main repos(ie AUR or pkgbuild), use:
pacman -Qm


#########################################################################################################
### Valid pgp keys (from PKGBUILD page)
#########################################################################################################
### An array of PGP fingerprints. If used, makepkg will only accept signatures from the keys listed here and will ignore the trust values from the keyring. If the source file was signed with a subkey, makepkg will still use the primary key for comparison.

### Only full fingerprints are accepted. They must be uppercase and must not contain whitespace characters. 
### Use the below to find out the fingerprint of the appropriate key.
gpg --list-keys --fingerprint KEYID



#########################################################################################################
### Add color?
#########################################################################################################
### edit /etc/pacman.conf to uncomment or add:
Color
ILoveCandy
ParallelDownloads = 5




Programs
sudo pacman -S keepass keepassxc vlc alsa-utils alsa-plugins alsa-firmware sof-firmware


### To install wine, first unable multilib:
### uncomment the [multilib] section in /etc/pacman.conf: (both lines)
"""
[multilib]
Include = /etc/pacman.d/mirrorlist
""""

sudo vim /etc/pacman.conf
sudo pacman -Syu
sudo pacman -S wine wine-gecko wine-mono
### optional dependencies:
lib32-giflib lib32-gnutls lib32-v4l-utils lib32-libpulse lib32-alsa-lib lib32-libxcomposite lib32-libxinerama lib32-opencl-icd-loader lib32-gst-plugins-base-libs lib32-sdl2 cups dosbox

sudo pacman -S obs-studio texlive freecad sane simple-scan kicad kicad-library kicad-library-3d notepadqq flameshot
optional for above programs: libva-intel-driver libva-mesa-driver sndio v4l2loopback-dkms graphviz openscad mathjax2 grim jre-openjdk keepassxc rclone xclip libreoffice-fresh-it hunspell hunspell-en_us hunspell-en_gb hunspell-it jre8-openjdk libreoffice-extension-texmaths libreoffice-extension-writer2latex gstreamer gstreamer-docs gst-libav libde265 linux-firmware-qlogic udftools xfsprogs

sudo pacman -S enchant mythes-en ttf-liberation ttf-bitstream-vera pkgstats adobe-source-sans-pro-fonts gst-plugins-good ttf-droid ttf-dejavu aspell-en icedtea-web gst-libav ttf-ubuntu-font-family ttf-anonymous-pro languagetool libmythes noto-fonts-emoji kimageformats


sudo pacman -S asunder lib32-glibc
yay -S makemkv kio-gdrive kdiff3 ffmpegthumbnailer libreoffice-extension-languagetool gst-plugin-openh264 mkinitcpio-firmware informant qdirstat-bin heifthumbnailer resvg raw-thumbnailer xnviewmp video-compare
sudo usermod -a -G informant username # add user to informant group to afoid estra sudos
### https://github.com/bradford-smith94/informant

### Add colors to terminal:
### https://averagelinuxuser.com/linux-terminal-color/
### Note, I only changed the local ~/.bashrc by copying only the part of the downloaded bashrc related to colors into the ~/.bashrc I was already using (they had other commands in theirs too...). I also copied the COLORS_DIR file into /etc/


### https://apps.kde.org/dolphin/
### KDE KIO for gdrive: # https://community.kde.org/KDE_KIO_Worker_for_Google_Drive_Integration
### Usage: Open the Network folder in Dolphin and click on "Google Drive".
### You can use the command line as well:
# kioclient5 exec gdrive:/
### https://www.reddit.com/r/kde/comments/5yadyw/dolphin_google_drive_integration/


### Automatic cleaning the package cache
### if you download updates very often quite soon you will discover that your package cache directory is unacceptably large. For example, my package cache folder exceeded 1G after 2 weeks already.
### Check the size of your package cache:
du -sh /var/cache/pacman/pkg/

### You can clean it manually from time to time, but it is better to automate such a thing. That is possible with the paccache script that will clean it weekly by removing old packages and keeping 3 the most recent version of each package in case you need to downgrade some packages.
### paccache is a part of pacman contributed scripts, so install them:
sudo pacman -S pacman-contrib

### And activate the paccache timer:
sudo systemctl enable paccache.timer
### Now, paccache will check your package cache directory and clean it if necessary every week.

### There are also other more efficient ways to run it. For example, you can run paccache automatically after every system update, but it requires setting up a hook. I think weekly cleaning is fine for a new Arch Linux user.



### Set up firewall (https://averagelinuxuser.com/arch-linux-after-install/)
### I have a dedicated post on the Linux firewall where you can learn why and how to use the Linux firewall.
### https://averagelinuxuser.com/linux-firewall/
### I usually recommend UFW uncomplicated firewall. Install it:
sudo pacman -S ufw
### Enable:
sudo ufw enable
### Check its status.
sudo ufw status verbose
### It should be active and the default settings are fine for most users.
### Enable its autostart with the system:
sudo systemctl enable ufw.service
### And you have firewall protection.



