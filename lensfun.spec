%define lib_major 0
%define lib_name %mklibname lensfun %{lib_major}
%define lib_dev %mklibname lensfun -d

Name: lensfun
Version: 0.2.5
Summary: A library to rectifying the defects introduced by your photographic equipment
Release: %mkrel 1
License: GPLv3
Group: System/Libraries
URL: http://lensfun.berlios.de/
Source0: http://download.berlios.de/lensfun/%{name}-%{version}.tar.bz2
# (fc) 0.2.3-1mdv fix build on 64bits
Patch1: lensfun-0.2.3-64bits.patch
BuildRequires: python
BuildRequires: glib2-devel
BuildRequires: libpng-devel
BuildRequires: zlib-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
A library to rectifying the defects introduced by your photographic equipment.

%files
%defattr(-,root,root,-)
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
%defattr(-,root,root,-)
%{_libdir}/*.so.*

#------------------------------------------------------------------

%package -n	%{lib_dev}
Summary: Development tools for programs which will use the %{name}
Group: Development/C
Requires: %{lib_name} = %{version}
Provides: %{name}-devel = %{version}-%{release}

%description -n	%{lib_dev}
This package contains the header files and .so libraries for developing %{name}.

%files -n %{lib_dev}
%defattr(-,root,root,755)
%{_includedir}/*.h*
%{_libdir}/*.so
%{_libdir}/pkgconfig/lensfun.pc

#------------------------------------------------------------------

%prep

%setup -q 
%patch1 -p1 -b .64bits

%build
# We can't use macro configure
%setup_compile_flags \
	./configure \
	--prefix=%buildroot%_prefix \
	--libdir=%buildroot%_libdir \
	--sysconfdir=%buildroot%_sysconfdir

%make all

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

