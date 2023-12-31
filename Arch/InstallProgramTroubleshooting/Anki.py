### https://wiki.archlinux.org/title/Anki


### install the bin version:
yay -S anki-bin
### https://aur.archlinux.org/packages/anki-bin
### installed the optional packages: lame mpv

### terminal is normally set to use anaconda to run python scripts, to python-installer was missing from anaconda when I had already had it installed with pacman.
### Disable anaconda base environment from starting automatically:
### https://bobbyhadz.com/blog/deactivate-and-disable-anaconda-base-environment
conda config --set auto_activate_base false
### installation via yay should now work after a restart of terminal:
yay -S anki-bin
### re-enable anaconda:
conda config --set auto_activate_base true

### this method seems way cleaner than editing the conda commands in .bashrc...
### Otherwise also this option: https://stackoverflow.com/questions/54429210/how-do-i-prevent-conda-from-activating-the-base-environment-by-default

addons:
### Review Heatmap
1771074083

### Image Occlusion Enhanced
1374772155
