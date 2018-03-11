%define libname %mklibname %{name}-extension
%define devname %mklibname -d %{name}-extension

Summary:	Caja extension for customizing the context menu
Name:		caja-actions
Version:	1.8.3
Release:	1
Group:		Graphical desktop/Other
License:	GPLv2+ and LGPLv2+
Url:		https://github.com/NiceandGently/caja-actions
Source0:	https://github.com/raveit65/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:	mate-common
BuildRequires:	itstool
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libcaja-extension)
BuildRequires:	pkgconfig(libgtop-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(sm) >= 1.0
BuildRequires:	pkgconfig(unique-3.0)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	yelp-tools

Requires:	%{libname} = %{version}-%{release}

%description
Caja-actions is an extension for Caja file manager which allows the user to
add arbitrary program to be launched through the Caja file manager popup
menu of selected files.

%files -f %{name}.lang
%{_bindir}/caja-actions-run
%{_bindir}/caja-actions-config-tool
%{_bindir}/caja-actions-new
%{_bindir}/caja-actions-print
%{_libexecdir}/caja-actions/
%{_datadir}/caja-actions/
%{_datadir}/icons/hicolor/*/apps/caja-actions.*
%{_datadir}/applications/cact.desktop

#---------------------------------------------------------------------------

%package -n %{name}-docs
Summary:	Documentations for %{name}
Group:		Graphical desktop/Other
BuildArch:	noarch

%description -n %{name}-docs
This package contains the documentation for %{name}

%files -n %{name}-docs
%doc AUTHORS ChangeLog NEWS README
%{_docdir}/caja-actions/html/
%{_docdir}/caja-actions/pdf/
%{_docdir}/caja-actions/objects-hierarchy.odg
%{_docdir}/caja-actions/AUTHORS
%{_docdir}/caja-actions/ChangeLog
%{_docdir}/caja-actions/NEWS
%{_docdir}/caja-actions/README
%{_docdir}/caja-actions/COPYING
%{_docdir}/caja-actions/COPYING-DOCS

#---------------------------------------------------------------------------

%package -n %{libname}
Summary:	Libraries for %{name}
Group:		System/Libraries

%description -n %{libname}
This package contains the shared libraries used by %{name}.

%files -n %{libname}
%{_libdir}/caja-actions/
%{_libdir}/caja/extensions-2.0/libcaja-actions-menu.so
%{_libdir}/caja/extensions-2.0/libcaja-actions-tracker.so

#---------------------------------------------------------------------------

%package -n %{devname}
Summary:	Libraries and include files for developing with %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains headers and shared libraries needed for development
with caja-actions.

%files -n %{devname}
%{_includedir}/caja-actions/
%{_datadir}/gtk-doc/html/caja-actions-3/

#---------------------------------------------------------------------------

%prep
%setup -q

%build
#NOCONFIGURE=1 ./autogen.sh
%configure \
	--enable-gtk-doc \
	--enable-html-manuals \
	--enable-deprecated \
	%{nil}
%make

%install
%makeinstall_std

# clean docs dirs
rm -f %{buildroot}%{_docdir}/%{name}/INSTALL
rm -f %{buildroot}%{_docdir}/%{name}/ChangeLog-2008
rm -f %{buildroot}%{_docdir}/%{name}/ChangeLog-2009
rm -f %{buildroot}%{_docdir}/%{name}/ChangeLog-2010
rm -f %{buildroot}%{_docdir}/%{name}/ChangeLog-2011
rm -f %{buildroot}%{_docdir}/%{name}/ChangeLog-2012
rm -f %{buildroot}%{_docdir}/%{name}/MAINTAINERS

# locales
%find_lang %{name} --with-gnome --all-name

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/cact.desktop

