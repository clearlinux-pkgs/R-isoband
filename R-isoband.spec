#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-isoband
Version  : 0.2.7
Release  : 37
URL      : https://cran.r-project.org/src/contrib/isoband_0.2.7.tar.gz
Source0  : https://cran.r-project.org/src/contrib/isoband_0.2.7.tar.gz
Summary  : Generate Isolines and Isobands from Regularly Spaced Elevation
Group    : Development/Tools
License  : MIT
Requires: R-isoband-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
A fast C++ implementation to generate contour lines (isolines) and contour
polygons (isobands) from regularly spaced grids containing elevation data.

%package lib
Summary: lib components for the R-isoband package.
Group: Libraries

%description lib
lib components for the R-isoband package.


%prep
%setup -q -n isoband
cd %{_builddir}/isoband

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1671560464

%install
export SOURCE_DATE_EPOCH=1671560464
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
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/isoband/DESCRIPTION
/usr/lib64/R/library/isoband/INDEX
/usr/lib64/R/library/isoband/LICENSE
/usr/lib64/R/library/isoband/Meta/Rd.rds
/usr/lib64/R/library/isoband/Meta/features.rds
/usr/lib64/R/library/isoband/Meta/hsearch.rds
/usr/lib64/R/library/isoband/Meta/links.rds
/usr/lib64/R/library/isoband/Meta/nsInfo.rds
/usr/lib64/R/library/isoband/Meta/package.rds
/usr/lib64/R/library/isoband/Meta/vignette.rds
/usr/lib64/R/library/isoband/NAMESPACE
/usr/lib64/R/library/isoband/NEWS.md
/usr/lib64/R/library/isoband/R/isoband
/usr/lib64/R/library/isoband/R/isoband.rdb
/usr/lib64/R/library/isoband/R/isoband.rdx
/usr/lib64/R/library/isoband/doc/index.html
/usr/lib64/R/library/isoband/doc/isoband1.R
/usr/lib64/R/library/isoband/doc/isoband1.Rmd
/usr/lib64/R/library/isoband/doc/isoband1.html
/usr/lib64/R/library/isoband/doc/isoband3.R
/usr/lib64/R/library/isoband/doc/isoband3.Rmd
/usr/lib64/R/library/isoband/doc/isoband3.html
/usr/lib64/R/library/isoband/extdata/ocean-cat.jpg
/usr/lib64/R/library/isoband/help/AnIndex
/usr/lib64/R/library/isoband/help/aliases.rds
/usr/lib64/R/library/isoband/help/figures/README-basic-example-plot-1.png
/usr/lib64/R/library/isoband/help/figures/README-volcano-1.png
/usr/lib64/R/library/isoband/help/figures/logo.png
/usr/lib64/R/library/isoband/help/isoband.rdb
/usr/lib64/R/library/isoband/help/isoband.rdx
/usr/lib64/R/library/isoband/help/paths.rds
/usr/lib64/R/library/isoband/html/00Index.html
/usr/lib64/R/library/isoband/html/R.css
/usr/lib64/R/library/isoband/tests/testthat.R
/usr/lib64/R/library/isoband/tests/testthat/test-clip-lines.R
/usr/lib64/R/library/isoband/tests/testthat/test-cpp.R
/usr/lib64/R/library/isoband/tests/testthat/test-iso-to-sfg.R
/usr/lib64/R/library/isoband/tests/testthat/test-isobands.R
/usr/lib64/R/library/isoband/tests/testthat/test-isolines-grob.R
/usr/lib64/R/library/isoband/tests/testthat/test-isolines.R
/usr/lib64/R/library/isoband/tests/testthat/test-label-placer.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/isoband/libs/isoband.so
/usr/lib64/R/library/isoband/libs/isoband.so.avx2
/usr/lib64/R/library/isoband/libs/isoband.so.avx512
