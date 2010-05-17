%define version  0.1
%define release  %mkrel 1

Name:            ginkgo
Version:         %{version}
Release:         %{release}
License:         GPLv2+
Url:             http://www.mandriva.com/
Group:           Graphical desktop/KDE 
BuildRoot:       %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source0:         %name-%version.tar.bz2
Summary:         Ginkgo is a navigator for Nepomuk, the KDE semantic toolkit
BuildArch:       noarch
%description
Ginkgo is a navigator for Nepomuk, the KDE semantic toolkit

%files -f %{name}.lang
%defattr(-,root,root)
%_kde_appsdir/%name

#------------------------------------------------

%prep
%setup -q -n %name-%version

%build

%install
rm -rf %buildroot
%__mkdir -p %buildroot%_kde_appsdir/%name
cp -frv src/* %buildroot%_kde_appsdir/%name/

%find_lang %name

%clean
rm -rf %buildroot

