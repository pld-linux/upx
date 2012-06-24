Summary:	The Ultimate Packer for eXecutables
Summary(pl):	Program pakuj�cy pliki wykonywalne
Name:		upx
Version:	2.03
Release:	1
License:	GPL
Group:		Applications
Source0:	http://upx.sourceforge.net/download/%{name}-%{version}-src.tar.gz
# Source0-md5:	a4b1da8a7ab58faf0aad7c67412d5e8e
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
UPX jest zaawansowanym kompresorem plik�w wykonywalnych. Zazwyczaj
zmniejsza wielko�� program�w o oko�o 50%-70%. UPX dekompresuje program
przed uruchomieniem, co wymaga troch� miejsca w /tmp. Nie powiniene�
nim kompresowa� program�w maj�cych suid, guid i innych wa�nych dla
bezpiecze�stwa systemu. Do pracy wymaga dost�pu do systemu /proc

%prep
%setup -q -n %{name}-%{version}-src

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
%doc BUGS LICENSE NEWS PROJECTS README README.SRC THANKS
%attr(755,root,root) %{_bindir}/upx
%{_mandir}/man1/upx.1*
