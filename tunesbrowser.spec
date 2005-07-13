Name:		tunesbrowser
Summary:	simple music player using the DAAP protocol
Version:	0.3.0
Release:	0
License:	BSD
Group:		Applications
Source0:	http://crazney.net/programs/itunes/files/%{name}-%{version}.tar.bz2
# Source0-md5:	dacfc3f7209c3165be9a9211dfb7bf0e
URL:		http://crazney.net/programs/itunes/
BuildRequires:	gstreamer-plugins-devel
BuildRequires:	libopendaap-devel >= 0.4.0
BuildRequires:	pango-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TunesBrowser is a simple music player, capable of playing music found
on iTunes® shares. TunesBrowser can connect to iTunes applications (as
of April 29 2004) and is implemented on top of libopendaap.
TunesBrowser was written with the purpose of being a prototype
front-end for libopendaap.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tunesbrowser
%{_datadir}/tunesbrowser.glade
%{_mandir}/man1/*.gz
