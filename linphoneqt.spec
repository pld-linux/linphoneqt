#
# Conditional build:
%bcond_without	dbus	# single instance handling using DBus

Summary:	Free VoIP and video softphone based on SIP protocol
Summary(pl.UTF-8):	Wolnodostępne oprogramowanie do VoIP i połączeń wideo oparte na protokole SIP
Name:		linphoneqt
Version:	4.1.1
Release:	0.1
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	https://linphone.org/releases/sources/linphoneqt/%{name}-%{version}.tar.gz
# Source0-md5:	0cf77a6e823a09ea765316ce536674cd
Patch0:		%{name}-use-pkgconfig.patch
URL:		https://linphone.org/
BuildRequires:	Qt5Concurrent-devel >= 5.9
BuildRequires:	Qt5Core-devel >= 5.9
%{?with_dbus:BuildRequires:	Qt5DBus-devel >= 5.9}
BuildRequires:	Qt5Gui-devel >= 5.9
BuildRequires:	Qt5Network-devel >= 5.9
BuildRequires:	Qt5Quick-devel >= 5.9
BuildRequires:	Qt5Quick-controls2-devel >= 5.9
BuildRequires:	Qt5Svg-devel >= 5.9
BuildRequires:	Qt5Test-devel >= 5.9
#BuildRequires:	Qt5TextToSpeech-devel >= 5.9
BuildRequires:	Qt5Widgets-devel >= 5.9
BuildRequires:	bctoolbox-devel
BuildRequires:	belcard-devel
BuildRequires:	cmake >= 3.1
BuildRequires:	linphone-devel
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	qt5-build >= 5.9
BuildRequires:	qt5-linguist >= 5.9
Requires:	Qt5Concurrent >= 5.9
Requires:	Qt5Core >= 5.9
%{?with_dbus:Requires:	Qt5DBus >= 5.9}
Requires:	Qt5Gui >= 5.9
Requires:	Qt5Network >= 5.9
Requires:	Qt5Quick >= 5.9
Requires:	Qt5Quick-controls2 >= 5.9
Requires:	Qt5Svg >= 5.9
Requires:	Qt5Test >= 5.9
#Requires:	Qt5TextToSpeech >= 5.9
Requires:	Qt5Widgets >= 5.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Free VoIP and video softphone based on SIP protocol.

%description -l pl.UTF-8
Wolnodostępne oprogramowanie do VoIP i połączeń wideo oparte na
protokole SIP.

%prep
%setup -q
%patch0 -p1

%build
install -d build
cd build
%cmake .. \
	%{?with_dbus:-DENABLE_DBUS=ON}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md README.md
%attr(755,root,root) %{_bindir}/linphone
%attr(755,root,root) %{_bindir}/linphone-tester
%{_datadir}/linphone
%{_desktopdir}/linphone.desktop
%{_iconsdir}/hicolor/scalable/apps/linphone_logo.svg
