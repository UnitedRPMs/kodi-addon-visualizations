#!/bin/bash

# New PVR add-ons repository for Kodi: https://github.com/notspiff

tag_name_waveform=master
tag_name_fishbmc=master
tag_name_spectrum=master
tag_name_shadertoy=master
tag_name_projectm=master
tag_name_goom=master
tag_name_starburst=""
tag_name_vsxu=master

set -x

tmp=$(mktemp -d)

trap cleanup EXIT
cleanup() {
    set +e
    [ -z "$tmp" -o ! -d "$tmp" ] || rm -rf "$tmp"
}

unset CDPATH
pwd=$(pwd)
date=$(date +%Y%m%d)
package=kodi-addon-visualizations
branch=master
name=kodi-addon-visualizations
version=18

pushd ${tmp}
mkdir -p ${name}/
pushd ${name}
git clone -b ${tag_name_waveform} --depth 1 https://github.com/notspiff/visualization.waveform.git
git clone -b ${tag_name_spectrum} --depth 1 https://github.com/notspiff/visualization.spectrum.git
git clone -b ${tag_name_shadertoy} --depth 1 https://github.com/notspiff/visualization.shadertoy.git
git clone -b ${tag_name_goom} --depth 1 https://github.com/notspiff/visualization.goom.git
git clone -b ${tag_name_fishbmc} --depth 1 https://github.com/notspiff/visualization.fishbmc.git
git clone -b ${tag_name_projectm} --depth 1 https://github.com/notspiff/visualization.projectm.git
git clone -b ${tag_name_vsxu} --depth 1 https://github.com/notspiff/visualization.vsxu.git
git clone --depth 1 https://github.com/notspiff/visualization.starburst.git
popd
tar Jcf "$pwd"/${name}-${version}-${date}.tar.xz ${package}
popd
