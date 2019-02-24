%define		_status		beta
%define		_pearname	HTTP_Upload
%define		subver		b4
%define		rel			1
%include	/usr/lib/rpm/macros.php
Summary:	%{_pearname} - Easy and secure managment of files submitted via HTML Forms
Summary(pl.UTF-8):	%{_pearname} - Proste i łatwe zarządzanie plikami przesyłanymi przez formularze HTML
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	0.%{subver}.%{rel}
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{subver}.tgz
# Source0-md5:	be4ca339fae538c8fbadd7b358b1356f
URL:		http://pear.php.net/package/HTTP_Upload/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-PEAR-core
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

%description -l pl.UTF-8
Ta klasa dostarcza system zaawansowanego uploadu plików z formularzy
html.

Właściwości:
- Potrafi pobrać jeden i wiele plików.
- Bezpieczne kopiowanie z katalogu tmp.
- Prosty mechanizm wykrywania prawidłowego uploadu, braku uploadu oraz
  błędu.
- Daje rozszerzone informacje o ładowanym pliku.
- Zmiana nazwy plików na kilka sposobów: tak jak jest, bezpiecznie lub
  unikalnie.
- Sprawdzanie dozwolonych rozszerzeń plików.
- Wsparcie dla wielojęzycznych komunikatów błędów.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

# must use own own dir
# interestingly it is loading from correct path already when running as
# installed package.
install -d .%{php_pear_dir}/data/%{_pearname}
mv .%{php_pear_dir}/data/*.php .%{php_pear_dir}/data/%{_pearname}

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
%{php_pear_dir}/HTTP/Upload.php
%dir %{php_pear_dir}/HTTP/Upload
%{php_pear_dir}/HTTP/Upload/Error.php
%{php_pear_dir}/HTTP/Upload/File.php
%dir %{php_pear_dir}/data/HTTP_Upload
%{php_pear_dir}/data/HTTP_Upload/en.php
%lang(da) %{php_pear_dir}/data/HTTP_Upload/da.php
%lang(de) %{php_pear_dir}/data/HTTP_Upload/de.php
%lang(es) %{php_pear_dir}/data/HTTP_Upload/es.php
%lang(et) %{php_pear_dir}/data/HTTP_Upload/et.php
%lang(fr) %{php_pear_dir}/data/HTTP_Upload/fr.php
%lang(it) %{php_pear_dir}/data/HTTP_Upload/it.php
%lang(nl) %{php_pear_dir}/data/HTTP_Upload/nl.php
%lang(pt_BR) %{php_pear_dir}/data/HTTP_Upload/pt_BR.php
%lang(ru) %{php_pear_dir}/data/HTTP_Upload/ru.php
%lang(sv) %{php_pear_dir}/data/HTTP_Upload/sv.php
