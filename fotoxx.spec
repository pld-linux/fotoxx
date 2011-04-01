Summary:	Image procesor
Summary(pl.UTF-8):	Procesor grafiki
Name:		fotoxx
Version:	11.04
Release:	1
License:	GPL v3
Group:		Applications
Source0:	http://kornelix.squarespace.com/storage/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	535f78b5000ee117b2c91c1bee94145e
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-desktop.patch
URL:		http://kornelix.squarespace.com/fotoxx
BuildRequires:	FreeImage-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libstdc++-devel
BuildRequires:	perl-Image-ExifTool
BuildRequires:	pkgconfig
BuildRequires:	ufraw
BuildRequires:	xdg-utils
Suggests:	perl-Image-ExifTool
Suggests:	ufraw
Suggests:	xdg-utils
Obsoletes:	fotox
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
#%patch0 -p1
#%patch1 -p1

%build
%{__make} \
	CXX="%{__cxx}" \
	OPTCFLAGS="%{rpmcflags}" \
	OPTLDFLAGS="%{rpmldflags}" \
	DOCDIR=%{_docdir}/%{name}-%{version} \
	PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

install -d $RPM_BUILD_ROOT%{_mandir}/man1/
cp desktop $RPM_BUILD_ROOT%{_desktopdir}/kornelix-%{name}.desktop
cp doc/%{name}.man $RPM_BUILD_ROOT%{_mandir}/man1/fotoxx.1

%{__make} install \
	PREFIX=%{_prefix} \
	DOCDIR=%{_docdir}/%{name}-%{version} \
	DESKTOP=$RPM_BUILD_ROOT%{_desktopdir}/kornelix-%{name}.desktop \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{CHANGES,README,TRANSLATIONS,userguide-en.html}
#%lang(es) %doc doc/userguide-es.html
#%lang(fr) %doc doc/userguide-fr.html
#%lang(gl) %doc doc/userguide-gl.html
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/icons
%dir %{_datadir}/%{name}/locales
%lang(de) %{_datadir}/%{name}/locales/de
%lang(es) %{_datadir}/%{name}/locales/es
%lang(fr) %{_datadir}/%{name}/locales/fr
%lang(gl) %{_datadir}/%{name}/locales/gl
%lang(it) %{_datadir}/%{name}/locales/it
%lang(zh_CN) %{_datadir}/%{name}/locales/zh_CN
%{_desktopdir}/kornelix-%{name}.desktop
%{_mandir}/man1/*.1*
