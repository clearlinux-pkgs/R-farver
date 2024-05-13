#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v10
# autospec commit: 5905be9
#
Name     : R-farver
Version  : 2.1.2
Release  : 31
URL      : https://cran.r-project.org/src/contrib/farver_2.1.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/farver_2.1.2.tar.gz
Summary  : High Performance Colour Space Manipulation
Group    : Development/Tools
License  : MIT
Requires: R-farver-lib = %{version}-%{release}
Requires: R-farver-license = %{version}-%{release}
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
using different colour spaces. As different colour spaces have
    different uses, efficient conversion between these representations are
    important. The 'farver' package provides a set of functions that gives
    access to very fast colour space conversion and comparisons
    implemented in C++, and offers speed improvements over the
    'convertColor' function in the 'grDevices' package.

%package lib
Summary: lib components for the R-farver package.
Group: Libraries
Requires: R-farver-license = %{version}-%{release}

%description lib
lib components for the R-farver package.


%package license
Summary: license components for the R-farver package.
Group: Default

%description license
license components for the R-farver package.


%prep
%setup -q -n farver
pushd ..
cp -a farver buildavx2
popd
pushd ..
cp -a farver buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1715629088

%install
export SOURCE_DATE_EPOCH=1715629088
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-farver
cp %{_builddir}/farver/LICENSE.note %{buildroot}/usr/share/package-licenses/R-farver/3da02386a01327cb8aae9ba8da15adbe40a314a0 || :
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/farver/DESCRIPTION
/usr/lib64/R/library/farver/INDEX
/usr/lib64/R/library/farver/LICENSE
/usr/lib64/R/library/farver/Meta/Rd.rds
/usr/lib64/R/library/farver/Meta/features.rds
/usr/lib64/R/library/farver/Meta/hsearch.rds
/usr/lib64/R/library/farver/Meta/links.rds
/usr/lib64/R/library/farver/Meta/nsInfo.rds
/usr/lib64/R/library/farver/Meta/package.rds
/usr/lib64/R/library/farver/NAMESPACE
/usr/lib64/R/library/farver/NEWS.md
/usr/lib64/R/library/farver/R/farver
/usr/lib64/R/library/farver/R/farver.rdb
/usr/lib64/R/library/farver/R/farver.rdx
/usr/lib64/R/library/farver/R/sysdata.rdb
/usr/lib64/R/library/farver/R/sysdata.rdx
/usr/lib64/R/library/farver/help/AnIndex
/usr/lib64/R/library/farver/help/aliases.rds
/usr/lib64/R/library/farver/help/farver.rdb
/usr/lib64/R/library/farver/help/farver.rdx
/usr/lib64/R/library/farver/help/figures/README-unnamed-chunk-4-1.png
/usr/lib64/R/library/farver/help/figures/README-unnamed-chunk-5-1.png
/usr/lib64/R/library/farver/help/figures/README-unnamed-chunk-7-1.png
/usr/lib64/R/library/farver/help/figures/README-unnamed-chunk-8-1.png
/usr/lib64/R/library/farver/help/figures/logo.png
/usr/lib64/R/library/farver/help/figures/logo.svg
/usr/lib64/R/library/farver/help/paths.rds
/usr/lib64/R/library/farver/html/00Index.html
/usr/lib64/R/library/farver/html/R.css
/usr/lib64/R/library/farver/tests/testthat.R
/usr/lib64/R/library/farver/tests/testthat/test-comparison.R
/usr/lib64/R/library/farver/tests/testthat/test-conversion.R
/usr/lib64/R/library/farver/tests/testthat/test-decoding.R
/usr/lib64/R/library/farver/tests/testthat/test-encoding.R
/usr/lib64/R/library/farver/tests/testthat/test-manip.R
/usr/lib64/R/library/farver/tests/testthat/test-names.R
/usr/lib64/R/library/farver/tests/testthat/test-non-finite.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/farver/libs/farver.so
/V4/usr/lib64/R/library/farver/libs/farver.so
/usr/lib64/R/library/farver/libs/farver.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-farver/3da02386a01327cb8aae9ba8da15adbe40a314a0
