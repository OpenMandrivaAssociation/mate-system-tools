%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	MATE System Tools
Name:		mate-system-tools 
Version:	1.8.1
Release:	2
License:	GPLv2+
Group:		System/Configuration/Other
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
Patch0:		mate-system-tools-1.8.1-clang_buildfix.patch
BuildRequires:	intltool
BuildRequires:	yelp-tools
BuildRequires:	mate-common
BuildRequires:	libiw-devel
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(liboobs-1)
BuildRequires:	pkgconfig(libcaja-extension)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(polkit-gtk-mate-1)
BuildRequires:	pkgconfig(system-tools-backends-2.0)
Requires:	system-tools-backends2
Requires:	usermode

%description
Day-to-day system management on Unix systems is a chore. Even when 
you're using a friendly graphical desktop, seemingly basic tasks 
like setting the system time, changing the network setup, importing 
and exporting network shared filesystems and configuring swap partitions 
requires editing configuration files by hand, and the exact procedure 
varies between different operating systems and distributions.

The MATE System Tools solve all these problems, giving you a simple
graphical interface for each task, which uses an advanced backend to 
edit all the relevant files and apply your changes. The interface 
looks and acts in exactly the same way regardless of what platform 
you're using.

%package devel
Summary:	Pkgconfig file for %{name}
Group:		Development/Other

%description devel
This package contains the pkgconfig file for %{name}.

%prep
%setup -q
%apply_patches

%build
%configure \
	--enable-services

%make

%install
%makeinstall_std
rm -rf %buildroot/var/lib/scrollkeeper

%find_lang %{name} --with-gnome --all-name

%files -f %{name}.lang
%doc README AUTHORS COPYING HACKING NEWS ChangeLog 
%dir %_sysconfdir/%{name}
%config(noreplace) %_sysconfdir/%{name}/*.conf
%{_bindir}/mate-network-admin
%{_bindir}/mate-services-admin
%{_bindir}/mate-shares-admin
%{_bindir}/mate-time-admin
%{_bindir}/mate-users-admin
%{_libdir}/caja/extensions-2.0/libcaja-gst-shares.so
%{_datadir}/applications/mate-network.desktop
%{_datadir}/applications/mate-services.desktop
%{_datadir}/applications/mate-shares.desktop
%{_datadir}/applications/mate-time.desktop
%{_datadir}/applications/mate-users.desktop
%{_datadir}/glib-2.0/schemas/org.mate.system-tools.gschema.xml
%{_datadir}/%{name}
%{_iconsdir}/mate/*/*/*

%files devel
%_libdir/pkgconfig/mate-system-tools.pc

