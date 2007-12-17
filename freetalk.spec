%define name freetalk
%define release		%mkrel 4

Summary:    Console jabber client	
Name:		%name
Version:	0.69
Release:	%release
Source0:	http://savannah.nongnu.org/download/%name/%name-%version.tar.bz2
Patch: freetalk-0.69-guile.patch
License:	GPL
Group:		Networking/Instant messaging
Url:		http://freetalk.nongnu.org/
BuildRequires: loudmouth-devel guile-devel
BuildRequires: ncurses-devel readline-devel
BuildRequires: gettext-devel

%description
Freetalk is a console based Jabber client. It features a readline interface 
with completion of buddy names, commands, and even ordinary English words! 

Freetalk is extensible, configurable, and scriptable through a Guile interface.

%prep
%setup -q
%patch -p1
aclocal -I m4
autoconf
automake -a -c

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
unset  $(env | grep '=@' | sed 's/=.*//') 
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


