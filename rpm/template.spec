Name:           ros-jade-industrial-utils
Version:        0.4.3
Release:        0%{?dist}
Summary:        ROS industrial_utils package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/industrial_utils
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-roscpp
Requires:       ros-jade-urdf
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-urdf

%description
Industrial utils is a library package that captures common funcitonality for the
ROS-Industrial distribution.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Sun Feb 21 2016 Shaun Edwards <sedwards@swri.org> - 0.4.3-0
- Autogenerated by Bloom

