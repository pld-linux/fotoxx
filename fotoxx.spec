Summary:	Image procesor
Summary(pl.UTF-8):	Procesor grafiki
Name:		fotoxx
Version:	8.3
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://kornelix.squarespace.com/storage/downloads/%{name}-%{version}.tar.gz
Patch0:		%{name}-Makefile.patch
# Source0-md5:	e5c7563306b904187765d7fa15727268
URL:		http://kornelix.squarespace.com/fotoxx
BuildRequires:	FreeImage-devel
BuildRequires:	perl-Image-ExifTool
BuildRequires:	ufraw
BuildRequires:	xdg-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fotoxx is a free open-source Linux program for improving image files
made with a digital camera.

Appart from standard operations it allows to:
  - generate thumbnails
  - fix red-eyes
  - fix perspective
  - make panoramas and HDR images

%description -l pl.UTF-8
Fotoxxm to wolne oprogramowanie open-source umożliwiające manipulacje
grafiką.

Oprócz standardowej obróbki zdjęć, umożliwia min.:
  - generowanie miniaturek
  - usuwanie efektu czerwonych oczu
  - tworzenie zdjęć panoramicznych
  - generowanie zdjęć HDR

%prep
%setup -q
%patch0

%build
%{__make} \
	CFLAGS="%{rpmcflags} -Wall -c `pkg-config --cflags gtk+-2.0`" \
	PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{CHANGES,README,toolbar-en.jpeg,userguide-*.html}
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
