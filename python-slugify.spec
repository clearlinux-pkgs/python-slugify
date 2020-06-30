#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-slugify
Version  : 4.0.1
Release  : 18
URL      : https://files.pythonhosted.org/packages/9f/42/e336f96a8b6007428df772d0d159b8eee9b2f1811593a4931150660402c0/python-slugify-4.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/9f/42/e336f96a8b6007428df772d0d159b8eee9b2f1811593a4931150660402c0/python-slugify-4.0.1.tar.gz
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
Provides: pypi(python_slugify)
Requires: pypi(text_unidecode)

%description python3
python3 components for the python-slugify package.


%prep
%setup -q -n python-slugify-4.0.1
cd %{_builddir}/python-slugify-4.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1593530900
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-slugify
cp %{_builddir}/python-slugify-4.0.1/LICENSE %{buildroot}/usr/share/package-licenses/python-slugify/39348c15454a917e7a44ef76017b198dc3834d8d
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
/usr/share/package-licenses/python-slugify/39348c15454a917e7a44ef76017b198dc3834d8d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
