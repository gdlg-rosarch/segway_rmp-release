Name:           ros-hydro-segway-rmp
Version:        0.1.2
Release:        0%{?dist}
Summary:        ROS segway_rmp package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/segway_rmp
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-geometry-msgs
Requires:       ros-hydro-libsegwayrmp
Requires:       ros-hydro-message-runtime
Requires:       ros-hydro-nav-msgs
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-serial
Requires:       ros-hydro-std-msgs
Requires:       ros-hydro-tf
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-geometry-msgs
BuildRequires:  ros-hydro-libsegwayrmp
BuildRequires:  ros-hydro-message-generation
BuildRequires:  ros-hydro-nav-msgs
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-serial
BuildRequires:  ros-hydro-std-msgs
BuildRequires:  ros-hydro-tf

%description
segway_rmp

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
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
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Sat Mar 14 2015 William Woodall <wjwwood@gmail.com> - 0.1.2-0
- Autogenerated by Bloom

