Summary:	The Ultimate Packer for eXecutables
Summary(pl.UTF-8):	Program pakujący pliki wykonywalne
Name:		upx
Version:	4.2.4
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	https://github.com/upx/upx/releases/download/v%{version}/%{name}-%{version}-src.tar.xz
# Source0-md5:	e00bd2fef36a86e8916a4b61d6807e2b
URL:		https://upx.github.io
BuildRequires:	cmake >= 3.8
BuildRequires:	libstdc++-devel >= 6:8
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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
przed uruchomieniem, co wymaga trochę miejsca w /tmp. Nie należy nim
kompresować programów mających suid, guid oraz innych ważnych dla
bezpieczeństwa systemu. Do pracy wymaga dostępu do systemu plików
/proc.

%prep
%setup -q -n %{name}-%{version}-src

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/BUGS.txt LICENSE NEWS README README.SRC doc/THANKS.txt
%attr(755,root,root) %{_bindir}/upx
%{_mandir}/man1/upx.1*
