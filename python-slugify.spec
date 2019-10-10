#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-slugify
Version  : 3.0.4
Release  : 11
URL      : https://files.pythonhosted.org/packages/f5/ef/c868a9ac657405f051a8a501ac5633e769c54228716b8db7f8d717977e57/python-slugify-3.0.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/f5/ef/c868a9ac657405f051a8a501ac5633e769c54228716b8db7f8d717977e57/python-slugify-3.0.4.tar.gz
Summary  : A Python Slugify application that handles Unicode
Group    : Development/Tools
License  : MIT
Requires: python-slugify-bin = %{version}-%{release}
Requires: python-slugify-license = %{version}-%{release}
Requires: python-slugify-python = %{version}-%{release}
Requires: python-slugify-python3 = %{version}-%{release}
Requires: Unidecode
Requires: text-unidecode
BuildRequires : Unidecode
BuildRequires : buildreq-distutils3
BuildRequires : text-unidecode

%description
Python Slugify
====================
**A Python slugify application that handles unicode**.

%package bin
Summary: bin components for the python-slugify package.
Group: Binaries
Requires: python-slugify-license = %{version}-%{release}

%description bin
bin components for the python-slugify package.


%package license
Summary: license components for the python-slugify package.
Group: Default

%description license
license components for the python-slugify package.


%package python
Summary: python components for the python-slugify package.
Group: Default
Requires: python-slugify-python3 = %{version}-%{release}

%description python
python components for the python-slugify package.


%package python3
Summary: python3 components for the python-slugify package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-slugify package.


%prep
%setup -q -n python-slugify-3.0.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570741969
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-slugify
cp LICENSE %{buildroot}/usr/share/package-licenses/python-slugify/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/slugify

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-slugify/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
