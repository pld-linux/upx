Summary:	The Ultimate Packer for eXecutables
Summary(pl):	Program pakuj�cy pliki wykonywalne
Name:		upx
Version:	1.02
Release:	1
License:	GPL
Group:		Applications
Group(de):	Applikationen
Group(pl):	Aplikacje
Source0:	http://wildsau.idv.uni-linz.ac.at/mfx/download/upx/%{name}-%{version}-src.tar.gz
URL:		http://upx.tsx.org
BuildRequires: ucl-devel
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

cd doc
%{__make}
cd ../src
%{__make} 
cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install doc/upx.1 $RPM_BUILD_ROOT%{_mandir}/man1
install src/upx $RPM_BUILD_ROOT%{_bindir}

gzip -9nf BUGS LICENSE NEWS PROJECTS README README.SRC THANKS 

%post   
%postun 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/upx
%{_mandir}/man1/upx.1*
%doc {BUGS,LICENSE,NEWS,PROJECTS,README,README.SRC,THANKS}.gz
