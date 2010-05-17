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
Requires:        python-kde4
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

mkdir -p $RPM_BUILD_ROOT%{_datadir}/locale
#make po_files
for i in po/*.po
do
  langdir="$RPM_BUILD_ROOT%{_datadir}/locale/`basename ${i} .po`/LC_MESSAGES/"
  mkdir -p ${langdir}
  msgfmt -o ${langdir}/%name.mo ${i}
done


%find_lang %name

%clean
rm -rf %buildroot

