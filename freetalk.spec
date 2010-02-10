%define name freetalk
%define release		%mkrel 3

Summary:    Console jabber client	
Name:		%name
Version:	3.2
Release:	%release
Source0:	http://savannah.nongnu.org/download/%name/%name-%version.tar.bz2
Patch0:		freetalk-3.2-glibc210.patch
Patch1:		freetalk-3.2-link.patch
License:	GPLv2+
Group:		Networking/Instant messaging
Url:		http://freetalk.nongnu.org/
BuildRequires: loudmouth-devel
BuildRequires: guile-devel
BuildRequires: ncurses-devel
BuildRequires: readline-devel
BuildRequires: gettext-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Freetalk is a console based Jabber client. It features a readline interface 
with completion of buddy names, commands, and even ordinary English words! 

Freetalk is extensible, configurable, and scriptable through a Guile interface.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
%configure2_5x
# /home/misc/rpm/BUILD/freetalk-0.69/doc//version.texi:33: Unknown command `locale'.
# makeinfo: Removing output file `freetalk.info' due to errors; use --force to preserve.
# make[1]: *** [freetalk.info] Error 1
# make[1]: Leaving directory `/home/misc/rpm/BUILD/freetalk-0.69/doc'
# [misc@n1 ~] $ grep locale /home/misc/rpm/BUILD/freetalk-0.69/doc//version.texi
# G_FILENAME_ENCODING=@locale
#
# so we need to remove this 
#unset  $(env | grep '=@' | sed 's/=.*//') 
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%find_lang %{name} 
%clean
rm -rf $RPM_BUILD_ROOT

%post
%_install_info %name.info

%postun
%_remove_install_info %name.info

%files -f %{name}.lang
%defattr(-,root,root) 
%doc NEWS README ChangeLog AUTHORS examples 
%_bindir/*
%_datadir/%name/
%attr(755,root,root) %_datadir/%name/extensions/first-time-run.sh
%_mandir/man1/*
%_infodir/*
