Summary:	Amharic dictionary for aspell
Summary(pl.UTF-8):   Słownik amharski dla aspella
Name:		aspell-am
Version:	0.03
%define	subv	1
Release:	1
License:	Public Domain
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/am/aspell6-am-%{version}-%{subv}.tar.bz2
# Source0-md5:	7e28708b53bd4bc3008dfb04237413ac
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Amharic dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik amharski (lista słów) dla aspella.

%prep
%setup -q -n aspell6-am-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README doc/STATUS
%{_libdir}/aspell/*
%{_datadir}/aspell/*
