Name:           ros-hydro-nodelet
Version:        1.8.6
Release:        0%{?dist}
Summary:        ROS nodelet package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/nodelet
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       libuuid-devel
Requires:       ros-hydro-bondcpp
Requires:       ros-hydro-message-runtime
Requires:       ros-hydro-pluginlib
Requires:       ros-hydro-rosconsole
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-std-msgs
Requires:       tinyxml-devel
BuildRequires:  boost-devel
BuildRequires:  libuuid-devel
BuildRequires:  ros-hydro-bondcpp
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-cmake-modules >= 0.3.2
BuildRequires:  ros-hydro-message-generation
BuildRequires:  ros-hydro-pluginlib
BuildRequires:  ros-hydro-rosconsole
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-rospy
BuildRequires:  ros-hydro-std-msgs
BuildRequires:  tinyxml-devel

%description
The nodelet package is designed to provide a way to run multiple algorithms in
the same process with zero copy transport between algorithms. This package
provides both the nodelet base class needed for implementing a nodelet, as well
as the NodeletLoader class used for instantiating nodelets.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Thu Oct 30 2014 Esteve Fernandez <esteve@osrfoundation.org> - 1.8.6-0
- Autogenerated by Bloom

* Wed Oct 29 2014 Esteve Fernandez <esteve@osrfoundation.org> - 1.8.5-0
- Autogenerated by Bloom

