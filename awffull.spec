Summary:	Web server log analysis program
Name:		awffull
Version:	3.4.1
Release:	0.1
License:	GPL
Group:		Applications/Networking
URL:		http://www.stedee.id.au/awffull
Source0:	http://www.stedee.id.au/files/%{name}-%{version}.tar.gz
# Source0-md5:	9b1ff7694d62f42dcf44832a7e163ce5
BuildRequires:	gd-devel
BuildRequires:	pcre-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AWFFull is a Web server log analysis program, forked from Webalizer.
It adds a number of new features and improvements, such as extended
frontpage history, resizable graphs, and a few more pie charts.

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
