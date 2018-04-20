# Script generated with Bloom
pkgdesc="ROS - simple_message defines a simple messaging connection and protocol for communicating with an industrial robot controller. Additional handler and manager classes are included for handling connection limited systems. This package is part of the ROS-Industrial program."
url='http://ros.org/wiki/simple_message'

pkgname='ros-kinetic-simple-message'
pkgver='0.6.0_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-industrial-msgs'
'ros-kinetic-roscpp'
)

depends=('ros-kinetic-industrial-msgs'
'ros-kinetic-roscpp'
)

conflicts=()
replaces=()

_dir=simple_message
source=()
md5sums=()

prepare() {
    cp -R $startdir/simple_message $srcdir/simple_message
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

