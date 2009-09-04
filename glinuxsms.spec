# SPEC written by Julien Catalano with the great help of http://qa.mandrakesoft.com/twiki/bin/view/Main/RpmHowTo
%define name glinuxsms

%define version 0.1
%define release  %mkrel 5

%define title   Glinuxsms
%define longtitle Glinuxsms is a GNOME2 GUI/front-end for linuxsms 

Summary:        %longtitle
Name:           %name
Version:        %version
Release:        %release
License:        GPL
Group:          Communications
Url:		http://glinuxsms.sourceforge.net/

Source0:        %name-%version.tar.bz2
# Make 3 icons %name-{16,32,48}.png and then tar cjf %name-icons.tar.bz2 *png
Source1:        %name-icons.tar.bz2

BuildRoot:      %_tmppath/%name-buildroot

Buildrequires: libgnomeui2-devel
Requires: linuxsms

%description
 glinuxsms is a GNOME2 GUI/front-end for linuxsms, an interesting
 tool to send SMS to cellphones all over the world. With glinuxsms
 you just write your message and click SEND, no need to get write
 the full command on a terminal. It uses linuxsms as a backend,
 and its configuration files as well. 

The main purpose for now is to keep it simple and light. 

Why should you use it?

 If you are a GNOME user, then you may SMS message your 
 contacts with a few clicks, no need to launch a xterm 
 to write the full commands. 

%prep
%setup -q
# unpack icons:
%setup -q -T -D -a1

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
# icon
mkdir -p $RPM_BUILD_ROOT{%{_liconsdir},%{_iconsdir},%{_miconsdir}}
install -D -m 644 %{name}-48.png $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
install -D -m 644 %{name}-32.png $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -D -m 644 %{name}-16.png $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png

# Menu
# Every entry must be changed according package specfications
# Pay attention to "section" "command" and "longtitle"
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_bindir}/%{name}
Icon=%{name}
Categories=Network;
Name=%{title}
Comment=%{longtitle}
EOF

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING README INSTALL TODO AUTHORS
%_bindir/*
%{_datadir}/applications/mandriva-%name.desktop

%_miconsdir/%name.png
%_iconsdir/%name.png
%_liconsdir/%name.png

