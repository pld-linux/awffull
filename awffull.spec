Summary:	Web server log analysis program
Summary(pl):	Program do analizy logów serwera WWW
Name:		awffull
Version:	3.7.1
Release:	1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://www.stedee.id.au/files/%{name}-%{version}.tar.gz
# Source0-md5:	f1cf872a64780b9b83432840d6da18a0
Source1:	%{name}.sysconfig
Source2:	%{name}.cron
Source3:	%{name}.crontab
URL:		http://www.stedee.id.au/awffull/
BuildRequires:	GeoIP-devel > 1.4.0-1
BuildRequires:	gd-devel
BuildRequires:	gettext-devel
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
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/{%{name},sysconfig,cron.d},%{_sbindir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install sample.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf
install %{name}_history_regen.pl %{_sbindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}
install %{SOURCE2} $RPM_BUILD_ROOT%{_sbindir}/%{name}.cron
install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/cron.d/%{name}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog *README* TODO
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/cron.d/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
%attr(2755,root,stats) %dir %{_sysconfdir}/%{name}
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_sbindir}/%{name}.cron
%attr(755,root,root) %{_sbindir}/%{name}_history_regen.pl
%{_mandir}/man1/awffull*
