# Script generated with Bloom
pkgdesc="ROS - ROS-Industrial core stack contains packages and libraries for supporing industrial systems"
url='http://ros.org/wiki/industrial_core'

pkgname='ros-kinetic-industrial-core'
pkgver='0.6.0_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-industrial-deprecated'
'ros-kinetic-industrial-msgs'
'ros-kinetic-industrial-robot-client'
'ros-kinetic-industrial-robot-simulator'
'ros-kinetic-industrial-trajectory-filters'
'ros-kinetic-industrial-utils'
'ros-kinetic-simple-message'
)

conflicts=()
replaces=()

_dir=industrial_core
source=()
md5sums=()

prepare() {
    cp -R $startdir/industrial_core $srcdir/industrial_core
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

