%define lib_major 0
%define lib_name %mklibname lensfun %{lib_major}
%define lib_dev %mklibname lensfun -d

Name:		lensfun
Version:	0.2.6
Summary:	A library to rectifying the defects introduced by your photographic equipment
Release:	2
License:	GPLv3
Group:		System/Libraries
URL:		http://lensfun.berlios.de/
Source0:	http://download.berlios.de/lensfun/%{name}-%{version}.tar.bz2
# (fc) 0.2.3-1mdv fix build on 64bits
Patch1:		lensfun-0.2.3-64bits.patch
BuildRequires:	python
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	zlib-devel
BuildRequires:	cmake
BuildRequires:	doxygen
Patch0:		lensfun-0.2.6-cmake_LIB_SUFFIX.patch
Patch2:		lensfun-0.2.6-cmake_pkgconfig.patch

%description
A library to rectifying the defects introduced by your photographic equipment.

%files
%{_datadir}/lensfun
%{_docdir}/*

#------------------------------------------------------------------

%package -n	%{lib_name}
Summary:	A library to rectifying the defects introduced by your photographic equipment
Group:		System/Libraries
Requires:	%{name}

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
cp -r  docs/*.txt %{buildroot}%{_datadir}/doc/%{name}/

%changelog
* Tue Jul 03 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.2.6-1
+ Revision: 807964
- BR: doxygen
- BR: cmake
- version update 0.2.6

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2.5-2
+ Revision: 666070
- mass rebuild

* Fri Aug 06 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.2.5-1mdv2011.0
+ Revision: 567185
- update to 0.2.5
- drop patch0, not needed any more

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.4-2mdv2010.1
+ Revision: 523162
- rebuilt for 2010.1

* Sun Oct 18 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.2.4-1mdv2010.0
+ Revision: 458118
- Update to 0.2.4

* Sat Jul 11 2009 Frederic Crozat <fcrozat@mandriva.com> 0.2.3-1mdv2010.0
+ Revision: 394797
- Patch1: fix build on 64bits
- Release 0.2.3
- Patch0: fix linking

* Tue Jun 24 2008 Helio Chissini de Castro <helio@mandriva.com> 0.2.2b-1mdv2009.0
+ Revision: 228769
- Added missing buildrequires
- import lensfun

