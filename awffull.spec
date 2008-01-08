# TODO:
# - install flags in %{datadir}/%{name} and make config for apache
# - patch config in package and fix paths
Summary:	Web server log analysis program
Summary(pl.UTF-8):	Program do analizy logów serwera WWW
Name:		awffull
Version:	3.8.2
Release:	1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://www.stedee.id.au/files/%{name}-%{version}.tar.gz
# Source0-md5:	24c972e1feefb223f0a8d4528dabe8c4
Source1:	%{name}.sysconfig
Source2:	%{name}.cron
Source3:	%{name}.crontab
Patch0:		%{name}-no_css_overwrite_warning.patch
Patch1:		%{name}-geoip.patch 
URL:		http://www.stedee.id.au/awffull/
BuildRequires:	GeoIP-devel > 1.4.0-1
BuildRequires:	gd-devel
BuildRequires:	gettext-devel
BuildRequires:	pcre-devel
Suggests:	dnshistory
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AWFFull is a Web server log analysis program, forked from Webalizer.
It adds a number of new features and improvements, such as extended
frontpage history, resizable graphs, and a few more pie charts.

%description -l pl.UTF-8
AWFFull to program do analizy logów serwer WWW wywodzący się z
Webalizera. Dodaje wiele nowych możliwości i ulepszeń, takich jak
rozszerzona historia strony głównej, skalowalne wykresy i nieco więcej
wykresów kołowych.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/%{name},/etc/{sysconfig,cron.d},%{_sbindir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install sample.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf
install contrib/%{name}_history_regen.pl $RPM_BUILD_ROOT%{_sbindir}
install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/%{name}
install %{SOURCE2} $RPM_BUILD_ROOT%{_sbindir}/%{name}.cron
install %{SOURCE3} $RPM_BUILD_ROOT/etc/cron.d/%{name}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog *README* TODO flags
%attr(2755,root,stats) %dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/cron.d/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_sbindir}/%{name}.cron
%attr(755,root,root) %{_sbindir}/%{name}_history_regen.pl
%{_mandir}/man1/awffull*
