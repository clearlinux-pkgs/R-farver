#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-farver
Version  : 2.1.1
Release  : 29
URL      : https://cran.r-project.org/src/contrib/farver_2.1.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/farver_2.1.1.tar.gz
Summary  : High Performance Colour Space Manipulation
Group    : Development/Tools
License  : MIT
Requires: R-farver-lib = %{version}-%{release}
BuildRequires : buildreq-R

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

%description lib
lib components for the R-farver package.


%prep
%setup -q -c -n farver
cd %{_builddir}/farver

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657151598

%install
export SOURCE_DATE_EPOCH=1657151598
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library farver
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library farver
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library farver
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc farver || :


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
/usr/lib64/R/library/farver/libs/farver.so
/usr/lib64/R/library/farver/libs/farver.so.avx2
/usr/lib64/R/library/farver/libs/farver.so.avx512
