Summary:	The Ultimate Packer for eXecutables
Summary(pl):	Program pakuj±cy pliki wykonywalne
Name:		upx
Version:	1.24
Release:	1
License:	GPL
Group:		Applications
Source0:	http://upx.sourceforge.net/download/%{name}-%{version}-src.tar.gz
# Source0-md5:	c7addf22766bdc9878e0a191855eec16
Patch0:		%{name}-opt.patch
Patch1:		%{name}-ucl.patch
URL:		http://upx.sourceforge.net/
BuildRequires:	glibc-static
BuildRequires:	ucl-devel >= 1.01
BuildRequires:  libstdc++-devel
Exclusivearch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UPX is an advenced executable file compressor. UPX will typically
reduce the file size of programs by around 50%-70%. Note that UPX need
decompress program file before run, what request some space on /tmp.
You shouldn't compress suid guid and some others "strategy" for
security programs. UPX need access to /proc filesystem.

%description -l pl
UPX jest zaawansowanym kompresorem plików wykonywalnych. Zazwyczaj
zmniejsza wielko¶æ programów o oko³o 50%-70%. UPX wymaga dekompresji
programu przed uruchomieniem, co wymaga trochê miejsca na /tmp. Nie
powiniene¶ nim kompresowaæ programów maj±cych suid, guid i innych
wa¿nych dla bezpieczeñstwa systemu. Do pracy wymaga dostêpu do systemu
/proc

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cd doc
%{__make} CFLAGS_O="%{rpmcflags}"
cd ../src
%{__make} \
	CFLAGS_O="%{rpmcflags}" \
	CC="%{__cxx}"
cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install doc/upx.1 $RPM_BUILD_ROOT%{_mandir}/man1
install src/upx $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS LICENSE NEWS PROJECTS README README.SRC THANKS
%attr(755,root,root) %{_bindir}/upx
%{_mandir}/man1/upx.1*
