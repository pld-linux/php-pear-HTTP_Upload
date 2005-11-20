%include	/usr/lib/rpm/macros.php
%define		_class		HTTP
%define		_subclass	Upload
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Easy and secure managment of files submitted via HTML Forms
Summary(pl):	%{_pearname} - Proste i ³atwe zarz±dzanie plikami przesy³anymi przez formularze HTML
Name:		php-pear-%{_pearname}
Version:	0.9.1
Release:	4
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	fd1161202786fcba5272d2715bcda787
Patch0:		%{name}-bug-4441.patch
Patch1:		http://glen.alkohol.ee/pld/%{name}-et.patch
Patch2:		%{name}-bug-4318.patch
URL:		http://pear.php.net/package/HTTP_Upload/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class provides an advanced file uploader system for file uploads
made from html forms.

Features:
- Can handle from one file to multiple files.
- Safe file copying from tmp dir.
- Easy detecting mechanism of valid upload, missing upload or error.
- Gives extensive information about the uploaded file.
- Rename uploaded files in different ways: as it is, safe or unique.
- Validate allowed file extensions.
- Multiple languages error messages support.

In PEAR status of this package is: %{_status}.

%description -l pl
Ta klasa dostarcza system zaawansowanego uploadu plików z formularzy
html.

W³a¶ciwo¶ci:
- Potrafi pobraæ jeden i wiele plików.
- Bezpieczne kopiowanie z katalogu tmp.
- Prosty mechanizm wykrywania prawid³owego uploadu, braku uploadu oraz
  b³êdu.
- Daje rozszerzone informacje o ³adowanym pliku.
- Zmiana nazwy plików na kilka sposobów: tak jak jest, bezpiecznie lub
  unikalnie.
- Sprawdzanie dozwolonych rozszerzeñ plików.
- Wsparcie dla wielojêzycznych komunikatów b³êdów.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup
cd ./%{php_pear_dir}/%{_class}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
