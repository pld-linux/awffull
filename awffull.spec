Summary:	Web server log analysis program
Summary(pl):	Program do analizy logów serwera WWW
Name:		awffull
Version:	3.4.1
Release:	0.1
License:	GPL
Group:		Applications/Networking
Source0:	http://www.stedee.id.au/files/%{name}-%{version}.tar.gz
# Source0-md5:	9b1ff7694d62f42dcf44832a7e163ce5
URL:		http://www.stedee.id.au/awffull
BuildRequires:	gd-devel
BuildRequires:	pcre-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AWFFull is a Web server log analysis program, forked from Webalizer.
It adds a number of new features and improvements, such as extended
frontpage history, resizable graphs, and a few more pie charts.

%description -l pl
AWFFull to program do analizy logów serwer WWW wywodz±cy siê z
Webalizera. Dodaje wiele nowych mo¿liwo¶ci i ulepszeñ, takich jak
rozszerzona historia strony g³ównej, skalowalne wykresy i nieco wiêcej
wykresów ko³owych.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog COPYING INSTALL README TODO
%attr(755,root,root) %{_bindir}/awffull
%{_mandir}/man1/awffull*
