%define		snap 20050917
#
Summary:	The Ultimate Packer for eXecutables
Summary(pl):	Program pakuj±cy pliki wykonywalne
Name:		upx
Version:	1.93
Release:	0.%{snap}.1
License:	GPL
Group:		Applications
#Source0:	http://upx.sourceforge.net/download/%{name}-%{version}-src.tar.gz
Source0:	%{name}-%{version}-%{snap}.tar.bz2
# Source0-md5:	a38535c32fa979ff7c79ca753b9024fa
URL:		http://upx.sourceforge.net/
BuildRequires:	glibc-static
BuildRequires:	libstdc++-devel
BuildRequires:	ucl-devel >= 1.01
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UPX is an advanced executable file compressor. UPX will typically
reduce the file size of programs by around 50%-70%. Note that UPX
needs to decompress the program file before run, what request some
space in /tmp. You shouldn't compress suid guid and some others
"strategic" for security programs. UPX needs access to the /proc
filesystem.

%description -l pl
UPX jest zaawansowanym kompresorem plików wykonywalnych. Zazwyczaj
zmniejsza wielko¶æ programów o oko³o 50%-70%. UPX dekompresuje program
przed uruchomieniem, co wymaga trochê miejsca w /tmp. Nie powiniene¶
nim kompresowaæ programów maj±cych suid, guid i innych wa¿nych dla
bezpieczeñstwa systemu. Do pracy wymaga dostêpu do systemu /proc

%prep
%setup -q -n %{name}-%{version}-%{snap}

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
install src/upx.out $RPM_BUILD_ROOT%{_bindir}/upx

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS LICENSE NEWS PROJECTS README README.SRC THANKS TODO
%attr(755,root,root) %{_bindir}/upx
%{_mandir}/man1/upx.1*
