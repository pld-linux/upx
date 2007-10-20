Summary:	The Ultimate Packer for eXecutables
Summary(pl.UTF-8):	Program pakujący pliki wykonywalne
Name:		upx
Version:	3.01
Release:	1
License:	GPL
Group:		Applications
Source0:	http://upx.sourceforge.net/download/%{name}-%{version}-src.tar.bz2
# Source0-md5:	58f3c87bf7e067ece5f7c510d4423cb8
Source1:        http://dl.sourceforge.net/sevenzip/lzma443.tar.bz2
# Source1-md5:	c4e1b467184c7cffd4371c74df2baf0f
URL:		http://upx.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRequires:	ucl-devel >= 1.01
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UPX is an advanced executable file compressor. UPX will typically
reduce the file size of programs by around 50%-70%. Note that UPX
needs to decompress the program file before run, what request some
space in /tmp. You shouldn't compress suid guid and some others
"strategic" for security programs. UPX needs access to the /proc
filesystem.

%description -l pl.UTF-8
UPX jest zaawansowanym kompresorem plików wykonywalnych. Zazwyczaj
zmniejsza wielkość programów o około 50%-70%. UPX dekompresuje program
przed uruchomieniem, co wymaga trochę miejsca w /tmp. Nie powinieneś
nim kompresować programów mających suid, guid i innych ważnych dla
bezpieczeństwa systemu. Do pracy wymaga dostępu do systemu /proc

%prep
%setup -q -n %{name}-%{version}-src -a1

%build
%{__make} -C doc
%{__make} -C src \
	CCARCH="" \
	CFLAGS_O="%{rpmcflags}" \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	UCLDIR="%{_prefix}" \
	UPX_LZMADIR="../"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install doc/upx.1 $RPM_BUILD_ROOT%{_mandir}/man1
install src/upx.out $RPM_BUILD_ROOT%{_bindir}/upx

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS LICENSE NEWS PROJECTS README README.1ST README.SRC THANKS
%attr(755,root,root) %{_bindir}/upx
%{_mandir}/man1/upx.1*
