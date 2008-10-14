Summary:	Image procesor
Summary(pl.UTF-8):	Procesor grafiki
Name:		fotoxx
Version:	5.4.1
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://kornelix.squarespace.com/storage/fotoxx/%{name}-%{version}.tar.gz
# Source0-md5:	383b3bce8310fe5fba0b49a83467ddfd
URL:		http://kornelix.squarespace.com/fotoxx
#BuildRequires:	-
#Requires:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fotoxx is a free open-source Linux program for improving image files made
with a digital camera.

%description -l pl.UTF-8
Fotoxxm to wolne oprogramowanie open-source umożliwiające manipulacje grafiką.

Oprócz standardowej obróbki zdjęć, umożliwia min.:
  - generowanie miniaturek
  - usuwanie efektu czerwonych oczu
  - tworzenie zdjęć panoramicznych
  - generowanie zdjęć HDR

%prep
%setup -q -n %{name}

%build
make

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/CHANGES doc/README doc/userguide-en.html
#%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) /usr/local/*
