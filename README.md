# refcon

[restricted-functions](https://github.com/donno2048/restricted-functions)'s Debian package

You can either download or build the package.

## Download

Go to the [Releases section](https://github.com/donno2048/refcon/releases)

## Build

In the _refcon_ directory run:

```sh
sudo apt update
sudo apt install build-essential git python3-pip -y
bash build.sh
sudo chmod 755 DEBIAN/
cd ..
sudo dpkg-deb --build refcon/
rm -rf refcon/usr
```

A new _recon.deb_ will be created in the parent directory of _refcon_

## Install

```sh
sudo dpkg -i refcon.deb
```

## Run

```sh
refcon
```
