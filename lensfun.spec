%define lib_major 0
%define lib_name %mklibname lensfun %{lib_major}
%define lib_dev %mklibname lensfun -d

Name: lensfun
Version: 0.2.6
Summary: A library to rectifying the defects introduced by your photographic equipment
Release: 1
License: GPLv3
Group: System/Libraries
URL: http://lensfun.berlios.de/
Source0: http://download.berlios.de/lensfun/%{name}-%{version}.tar.bz2
# (fc) 0.2.3-1mdv fix build on 64bits
Patch1: lensfun-0.2.3-64bits.patch
BuildRequires:	python
BuildRequires:	glib2-devel
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
BuildRequires:	cmake
BuildRequires:	doxygen
Patch0:		lensfun-0.2.6-cmake_LIB_SUFFIX.patch
Patch2:		lensfun-0.2.6-cmake_pkgconfig.patch

%description
A library to rectifying the defects introduced by your photographic equipment.

%files
%_datadir/lensfun
%_docdir/*

#------------------------------------------------------------------

%package -n	%{lib_name}
Summary: A library to rectifying the defects introduced by your photographic equipment
Group: System/Libraries
Requires: %{name}

%description -n	%{lib_name}
A library to rectifying the defects introduced by your photographic equipment.

%files -n %{lib_name}
%{_libdir}/*.so.*

#------------------------------------------------------------------

%package -n	%{lib_dev}
Summary: Development tools for programs which will use the %{name}
Group: Development/C
Requires: %{lib_name} = %{version}
Provides: %{name}-devel = %{version}-%{release}

%description -n	%{lib_dev}
This package contains the header files and .so
libraries for developing %{name}.

%files -n %{lib_dev}
%{_includedir}/%{name}/*.h*
%{_libdir}/*.so
%{_libdir}/pkgconfig/lensfun.pc

#------------------------------------------------------------------

%prep

%setup -q 
%patch0 -p1
%patch1 -p1 -b .64bits
%patch2 -p1


%build
%cmake \
  -DBUILD_DOC:BOOL=ON \
  -DBUILD_TESTS:BOOL=OFF

%make all

%install
mkdir -p %{buildroot}/%{_datadir}/doc/%{name}
make install/fast DESTDIR=%{buildroot} -C build
cp -r  docs/*.txt %{buildroot}/%{_datadir}/doc/%{name}/



