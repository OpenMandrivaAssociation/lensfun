%define major 0
%define libname %mklibname lensfun %{major}
%define devname %mklibname lensfun -d

Summary:	A library to rectifying the defects introduced by your photographic equipment
Name:		lensfun
Version:	0.3.3
Release:	3
License:	GPLv3
Group:		System/Libraries
Url:		https://github.com/lensfun/lensfun/
Source0:	https://github.com/lensfun/lensfun/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:		lensfun-0.3.3-c++20.patch

BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	python
BuildRequires:	python-docutils
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(zlib)

%description
A library to rectifying the defects introduced by your photographic equipment.

%package -n	%{libname}
Summary:	A library to rectifying the defects introduced by your photographic equipment
Group:		System/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{mklibname auxfun 0} < 0.3.1

%description -n	%{libname}
A library to rectifying the defects introduced by your photographic equipment.

%package -n	%{devname}
Summary:	Development tools for programs which will use the %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package contains the header files and .so
libraries for developing %{name}.

%prep
%autosetup -p1

%build
%cmake \
	-DBUILD_DOC:BOOL=ON \
	-DCMAKE_BUILD_TYPE:STRING=Release \
%ifarch %{x86_64}
	-DBUILD_FOR_SSE=ON -DBUILD_FOR_SSE2=ON \
%else
	-DBUILD_FOR_SSE=OFF -DBUILD_FOR_SSE2=OFF \
%endif
	-DBUILD_AUXFUN=ON \
	-DBUILD_TESTS:BOOL=OFF

%make_build all

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
%{python_sitelib}/lensfun*

%files -n %{libname}
%{_libdir}/liblensfun.so.%{major}*
%{_libdir}/liblensfun.so.1

%files -n %{devname}
%{_includedir}/%{name}/*.h*
%{_libdir}/*.so
%{_libdir}/pkgconfig/lensfun.pc
