%include	/usr/lib/rpm/macros.php
%define		_class		HTTP
%define		_subclass	Upload
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - Easy and secure managment of files submitted via HTML Forms
Summary(pl):	%{_class}_%{_subclass} - Proste i �atwe zarz�dzanie plikami przesy�anymi przez formularze HTML
Name:		php-pear-%{_pearname}
Version:	0.8
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class provides an advanced file uploader system for file uploads
made from html forms. Features:
- Can handle from one file to multiple files.
- Safe file copying from tmp dir.
- Easy detecting mechanism of valid upload, missing upload or error.
- Gives extensive information about the uploaded file.
- Rename uploaded files in different ways: as it is, safe or unique.
- Validate allowed file extensions.
- Multiple languages error messages support.

%description -l pl
Ta klasa dostarcza system zaawansowanego uploadu plik�w z formularzy
html. W�a�ciwo�ci:
- Potrafi pobra� jeden i wiele plik�w.
- Bezpieczne kopiowanie z katalogu tmp.
- Prosty mechanizm wykrywania prawid�owego uploadu, braku uploadu oraz
  b��du.
- Daje rozszerzone informacje o �adowanym pliku.
- Zmiana nazwy plik�w na kilka sposob�w: tak jak jest, bezpiecznie lub
  unikalnie.
- Sprawdzanie dozwolonych rozszerze� plik�w.
- Wsparcie dla wieloj�zycznych komunikat�w b��d�w.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs/*
%{php_pear_dir}/%{_class}/*.php
