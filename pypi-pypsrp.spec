#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pypsrp
Version  : 0.8.1
Release  : 13
URL      : https://files.pythonhosted.org/packages/57/da/3d9295972c20624c79843c1c14cf06fc6b0575ba786c1f72d6ca5bc5b9d5/pypsrp-0.8.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/57/da/3d9295972c20624c79843c1c14cf06fc6b0575ba786c1f72d6ca5bc5b9d5/pypsrp-0.8.1.tar.gz
Summary  : PowerShell Remoting Protocol and WinRM for Python
Group    : Development/Tools
License  : MIT
Requires: pypi-pypsrp-license = %{version}-%{release}
Requires: pypi-pypsrp-python = %{version}-%{release}
Requires: pypi-pypsrp-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cryptography)
BuildRequires : pypi(pyspnego)
BuildRequires : pypi(requests)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)

%description
# pypsrp - Python PowerShell Remoting Protocol Client library
[![Test workflow](https://github.com/jborean93/pypsrp/actions/workflows/ci.yml/badge.svg)](https://github.com/jborean93/pypsrp/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/jborean93/pypsrp/branch/master/graph/badge.svg)](https://codecov.io/gh/jborean93/pypsrp)
[![PyPI version](https://badge.fury.io/py/pypsrp.svg)](https://badge.fury.io/py/pypsrp)

%package license
Summary: license components for the pypi-pypsrp package.
Group: Default

%description license
license components for the pypi-pypsrp package.


%package python
Summary: python components for the pypi-pypsrp package.
Group: Default
Requires: pypi-pypsrp-python3 = %{version}-%{release}

%description python
python components for the pypi-pypsrp package.


%package python3
Summary: python3 components for the pypi-pypsrp package.
Group: Default
Requires: python3-core
Provides: pypi(pypsrp)
Requires: pypi(cryptography)
Requires: pypi(pyspnego)
Requires: pypi(requests)

%description python3
python3 components for the pypi-pypsrp package.


%prep
%setup -q -n pypsrp-0.8.1
cd %{_builddir}/pypsrp-0.8.1
pushd ..
cp -a pypsrp-0.8.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656399622
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pypsrp
cp %{_builddir}/pypsrp-0.8.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pypsrp/3feb94e218ec9cc73b84cf413325044398ed1ebb
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pypsrp/3feb94e218ec9cc73b84cf413325044398ed1ebb

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
