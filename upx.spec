Summary:	The Ultimate Packer for eXecutables
Summary(pl):	Program pakuj�cy pliki wykonywalne
Name:		upx
Version:	1.25
Release:	1
License:	GPL
Group:		Applications
Source0:	http://upx.sourceforge.net/download/%{name}-%{version}-src.tar.gz
# Source0-md5:	6f20a62999a46a1864652454b3c8a5d8
URL:		http://upx.sourceforge.net/
BuildRequires:	glibc-static
BuildRequires:	libstdc++-devel
BuildRequires:	ucl-devel >= 1.01
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UPX is an advenced executable file compressor. UPX will typically
reduce the file size of programs by around 50%-70%. Note that UPX need
decompress program file before run, what request some space on /tmp.
You shouldn't compress suid guid and some others "strategy" for
security programs. UPX need access to /proc filesystem.

%description -l pl
UPX jest zaawansowanym kompresorem plik�w wykonywalnych. Zazwyczaj
zmniejsza wielko�� program�w o oko�o 50%-70%. UPX wymaga dekompresji
programu przed uruchomieniem, co wymaga troch� miejsca na /tmp. Nie
powiniene� nim kompresowa� program�w maj�cych suid, guid i innych
wa�nych dla bezpiecze�stwa systemu. Do pracy wymaga dost�pu do systemu
/proc

%prep
%setup -q

%build
%{__make} -C doc
%{__make} -C src \
	CCARCH="" \
	CFLAGS_O="%{rpmcflags}" \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	UCLDIR="%{_prefix}"

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
