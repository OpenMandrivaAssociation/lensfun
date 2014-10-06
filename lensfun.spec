%define major	0
%define libname %mklibname lensfun %{major}
%define libaux %mklibname auxfun %{major}
%define devname %mklibname lensfun -d

Summary:	A library to rectifying the defects introduced by your photographic equipment
Name:		lensfun
Version:	0.3.0
Release:	1
License:	GPLv3
Group:		System/Libraries
Url:		http://lensfun.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/%{name}/%{version}/%{name}-%{version}.tar.bz2
Patch0:		man-path-0.3.0.patch

BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	python
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(zlib)

%description
A library to rectifying the defects introduced by your photographic equipment.

%package -n	%{libname}
Summary:	A library to rectifying the defects introduced by your photographic equipment
Group:		System/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n	%{libname}
A library to rectifying the defects introduced by your photographic equipment.

%package -n	%{libaux}
Summary:	A library to rectifying the defects introduced by your photographic equipment
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}

%description -n	%{libaux}
A library to rectifying the defects introduced by your photographic equipment.

%package -n	%{devname}
Summary:	Development tools for programs which will use the %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libaux} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package contains the header files and .so
libraries for developing %{name}.

%prep
%setup -q
%apply_patches

%build
# failed with clang
# need investigation
# export CC=gcc
%cmake \
	-DBUILD_DOC:BOOL=ON \
%ifarch %armx
	-BUILD_FOR_SSE2=OFF \
	-BUILD_FOR_SSE=OFF \
%endif
	-DBUILD_AUXFUN=ON \
	-DBUILD_TESTS:BOOL=OFF

%make all

%install
mkdir -p %{buildroot}/%{_datadir}/doc/%{name}
make install/fast DESTDIR=%{buildroot} -C build
cp -r  docs/*.txt %{buildroot}%{_datadir}/doc/%{name}/

%files
%doc %{_docdir}/*
%{_datadir}/lensfun
%{_bindir}/g-lensfun-update-data
%{_bindir}/lensfun-add-adapter
%{_bindir}/lensfun-update-data
%{_mandir}/man1/*.*

%files -n %{libname}
%{_libdir}/liblensfun.so.%{major}*

%files -n %{libaux}
%{_libdir}/libauxfun.so.%{major}*

%files -n %{devname}
%{_includedir}/%{name}/*.h*
%{_includedir}/auxfun/*.h*
%{_libdir}/*.so
%{_libdir}/pkgconfig/lensfun.pc
