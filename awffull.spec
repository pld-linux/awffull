# TODO:
# - install flags in %{datadir}/%{name} and make config for apache
# - patch config in package and fix paths
Summary:	Web server log analysis program
Summary(pl.UTF-8):	Program do analizy logów serwera WWW
Name:		awffull
Version:	3.10.2
Release:	7
License:	GPL v3+
Group:		Applications/Networking
Source0:	http://www.stedee.id.au/files/%{name}-%{version}.tar.gz
# Source0-md5:	90c1b0137ce687d06e56c49b854d41c1
Source1:	%{name}.sysconfig
Source2:	%{name}.cron
Source3:	%{name}.crontab
Patch0:		%{name}-no_css_overwrite_warning.patch
Patch1:		%{name}-geoip.patch
Patch2:		%{name}-locale_names.patch
Patch3:		%{name}-no_verbose_trash.patch
URL:		http://www.stedee.id.au/awffull/
BuildRequires:	GeoIP-devel > 1.4.0-1
BuildRequires:	gd-devel
BuildRequires:	gettext-tools
BuildRequires:	pcre-devel
Suggests:	crondaemon
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
%patch2 -p1
%patch3 -p1
rm po/*gmo
mv -f po/{no,nb}.po
mv -f po/zh{,_CN}.po

%build
%configure
%{__make} -C po update-gmo
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/%{name},/etc/{sysconfig,cron.d},%{_sbindir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p sample.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf
install -p contrib/%{name}_history_regen.pl $RPM_BUILD_ROOT%{_sbindir}
cp -p %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/%{name}
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_sbindir}/%{name}.cron
cp -p %{SOURCE3} $RPM_BUILD_ROOT/etc/cron.d/%{name}

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
%{_mandir}/man[15]/awffull*
