#
# TODO:
# - create some bconds for optional stuff
#
Summary:	A command line music player
Summary(hu.UTF-8):	Parancssoros zenelejátszó
Summary(pl.UTF-8):	Konsolowy odtwarzacz muzyki
Name:		herrie
Version:	2.2
Release:	6
License:	BSD
Group:		Applications/Sound
Source0:	http://herrie.info/distfiles/%{name}-%{version}.tar.bz2
# Source0-md5:	88832b10298ab89473730eb0c93b6ddf
Patch0:		%{name}-link.patch
URL:		http://herrie.info/
BuildRequires:	alsa-lib-devel
BuildRequires:	curl-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libao-devel
BuildRequires:	libid3tag-devel
BuildRequires:	libmad-devel
BuildRequires:	libmodplug-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libxspf-devel >= 1.2.0
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Herrie is a command line music player. It has a split-screen file
manager and playlist interface and supports a number of file formats
(MP3, Ogg Vorbis, wave, FLAC, etc).

%description -l hu.UTF-8
Herrie egy parancssoros zenelejátszó. Osztott képernyős fájlkezelője
és lejátszó-lista felülete van, és sokféle formátumot támogat (MP3,
Ogg Vorbis, wave, FLAC, stb.).

%description -l pl.UTF-8
Herrie jest konsolowym odtwarzaczem muzyki. Posiada on ekran
podzielony na zarządcę plików oraz interfejs playlisty. Obsługuje
wiele formatów plików (MP3, Ogg Vorbis, wave, FLAC itp).

%prep
%setup -q
%patch0 -p1

# spiff -> xspf
%{__sed} -i 's,spiff,xspf,g' `grep -r -l 'spiff' .`
%{__sed} -i 's,SPIFF,XSPF,g' `grep -r -l 'SPIFF' .`

%build
CC="%{__cc}" \
LDFLAGS="%{rpmldflags}" \
CFLAGS="%{rpmcflags}" \
./configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

:> $RPM_BUILD_ROOT%{_sysconfdir}/herrie.conf

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.conf
%doc COPYING ChangeLog README *.sample
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/%{name}.1*
