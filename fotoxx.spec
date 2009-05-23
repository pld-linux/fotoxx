Summary:	Image procesor
Summary(pl.UTF-8):	Procesor grafiki
Name:		fotoxx
Version:	6.9.2
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://kornelix.squarespace.com/storage/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	fefe87e7dac56de22c39cfba821149ec
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

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/CHANGES doc/README doc/userguide-en.html
%attr(755,root,root) /usr/local/*
