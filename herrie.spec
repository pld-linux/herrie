Summary:	A command line music player
Summary(pl):	Konsolowy odtwarzacz muzyki
Name:		herrie
Version:	0.6
Release:	1
License:	BSD
Group:		Applications/Sound
Source0:	http://www.il.fontys.nl/~ed/projects/herrie/distfiles/%{name}-%{version}.tar.gz
# Source0-md5:	579231dc7bfa660cab702aef02921480
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-curses.patch
URL:		http://g-rave.nl/projects/herrie/
BuildRequires:	curl-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libao-devel
BuildRequires:	libid3tag-devel
BuildRequires:	libmad-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libvorbis-devel
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Herrie is a command line music player. It has a split-screen file
manager and playlist interface and supports a number of file formats
(MP3, Ogg Vorbis, wave, FLAC, etc).

%description -l pl
Herrie jest konsolowym odtwarzaczem muzyki. Posiada on ekran
podzielony na zarz±dcê plików oraz interfejs playlisty. Obs³uguje
wiele formatów plików (MP3, Ogg Vorbis, wave, FLAC itp).

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} -C src \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}" \
	OPTLDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} -C src/ install \
        DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc COPYING ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/%{name}.1*
