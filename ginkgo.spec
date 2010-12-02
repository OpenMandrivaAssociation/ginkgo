%define version  0.31
%define release  %mkrel 2

Name:            ginkgo
Version:         %{version}
Release:         %{release}
License:         GPLv2+
Url:             http://wiki.mandriva.com/en/Ginkgo
Group:           Graphical desktop/KDE 
BuildRoot:       %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source0:         %name-%version.tar.bz2
Summary:         Ginkgo is a navigator for Nepomuk, the KDE semantic toolkit
BuildRequires:   kde4-macros
Requires:        python-kde4
Requires:        python-mako
Requires:        nepomuk-scribo
BuildArch:       noarch
%description
Ginkgo is a graphical front-end for managing data semantically. Ginkgo 
lets you create and explore links between your personal data such 
as e-mails, contacts, files, Web pages. It harnesses the Nepomuk
framework.

%files -f %{name}.lang
%defattr(-,root,root)
%_kde_appsdir/%name
%_bindir/%name

#------------------------------------------------

%prep
%setup -q -n %name-%version

%build

%install
rm -rf %buildroot
%__mkdir -p %buildroot%_kde_appsdir/%name
cp -frv src/* %buildroot%_kde_appsdir/%name/
%__mkdir %buildroot%_bindir/
cp -frv %name %buildroot%_bindir/%name

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

