#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mkosi
Version  : 9
Release  : 27
URL      : https://github.com/systemd/mkosi/archive/v9/mkosi-9.tar.gz
Source0  : https://github.com/systemd/mkosi/archive/v9/mkosi-9.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: mkosi-bin = %{version}-%{release}
Requires: mkosi-license = %{version}-%{release}
Requires: mkosi-man = %{version}-%{release}
Requires: mkosi-python = %{version}-%{release}
Requires: mkosi-python3 = %{version}-%{release}
Requires: bmap-tools-bin
BuildRequires : buildreq-distutils3

%description
# mkosi - Create legacy-free OS images
A fancy wrapper around `dnf --installroot`, `debootstrap`,
`pacstrap` and `zypper` that may generate disk images with a number of
bells and whistles.

%package bin
Summary: bin components for the mkosi package.
Group: Binaries
Requires: mkosi-license = %{version}-%{release}

%description bin
bin components for the mkosi package.


%package license
Summary: license components for the mkosi package.
Group: Default

%description license
license components for the mkosi package.


%package man
Summary: man components for the mkosi package.
Group: Default

%description man
man components for the mkosi package.


%package python
Summary: python components for the mkosi package.
Group: Default
Requires: mkosi-python3 = %{version}-%{release}

%description python
python components for the mkosi package.


%package python3
Summary: python3 components for the mkosi package.
Group: Default
Requires: python3-core

%description python3
python3 components for the mkosi package.


%prep
%setup -q -n mkosi-9
cd %{_builddir}/mkosi-9

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1609883960
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
mkdir -p %{buildroot}/usr/share/package-licenses/mkosi
cp %{_builddir}/mkosi-9/LICENSE %{buildroot}/usr/share/package-licenses/mkosi/01a6b4bf79aca9b556822601186afab86e8c4fbf
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mkosi

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mkosi/01a6b4bf79aca9b556822601186afab86e8c4fbf

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/mkosi.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
