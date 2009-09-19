Summary:	A gtk2 theme with blue and grey colors
Name:		gtk2-theme-Murrine-Grey-Blue
Version:	1.0
Release:	1
License:	GPL
Group:		Themes/GTK+
Source0:	http://carme.pld-linux.org/~uzsolt/sources/Murrine-Grey-Blue.tar.bz2
# Source0-md5:	4438eefcc7c432c82b2d87a39feda0e2
Requires:	gtk2-theme-engine-murrine >= 0.90.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A gtk2 theme with blue and grey colors.

%prep
%setup -q -n Murrine-Grey-Blue

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/themes/Murrine-Grey-Blue
cp -R gtk* $RPM_BUILD_ROOT%{_datadir}/themes/Murrine-Grey-Blue

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/themes/Murrine-Grey-Blue
