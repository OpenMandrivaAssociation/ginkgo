Summary:	Navigator for Nepomuk, the KDE semantic toolkit
Name:		ginkgo
Version:	0.32
Release:	14
License:	GPLv2+
Url:		https://wiki.mandriva.com/en/Ginkgo
Group:		Graphical desktop/KDE 
Source0:	%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	kde4-macros
Requires:	python-kde4
Requires:	python-mako
Requires:       oxygen-icon-theme

%description
Ginkgo is a graphical front-end for managing data semantically. Ginkgo 
lets you create and explore links between your personal data such 
as e-mails, contacts, files, Web pages. It harnesses the Nepomuk
framework.

%files -f %{name}.lang
%{_kde_appsdir}/%{name}
%{_kde_datadir}/applications/kde4/%{name}.desktop
%{_bindir}/%{name}

#------------------------------------------------

%prep
%setup -q

# Fix unreadable files
find . -perm 0600 -exec chmod 0644 '{}' \;

%build
# clean old leftover from the tarball that prevent upload
rm -Rf src/ginkgo/util/.cache

# change "Report a Bug" URL to Rosa Bugzilla
sed -i 's!https://qa.mandriva.com!http://bugs.rosalinux.ru/!' %{name}

# also change .po headers for consistency
sed -i 's!https://qa.mandriva.com/!http://bugs.rosalinux.ru/!' po/*.po

%install
mkdir -p %{buildroot}%{_kde_appsdir}/%{name}
cp -frv src/* %{buildroot}%{_kde_appsdir}/%{name}/
mkdir %{buildroot}%{_bindir}/
cp -frv %{name} %{buildroot}%{_bindir}/%{name}

mkdir -p %{buildroot}%{_datadir}/locale
#make po_files
for i in po/*.po
do
  langdir="%{buildroot}%{_datadir}/locale/`basename ${i} .po`/LC_MESSAGES/"
  mkdir -p ${langdir}
  msgfmt -o ${langdir}/%{name}.mo ${i}
done

chmod -R a+r %{buildroot}/%{_kde_appsdir}/%{name}

mkdir -p %{buildroot}%{_kde_datadir}/applications/kde4

cat > %{buildroot}%{_kde_datadir}/applications/kde4/%{name}.desktop << EOF
[Desktop Entry]
Name=Ginkgo
Comment=Ginkgo is a graphical front-end for Nepomuk
Exec=%{_bindir}/%{name}
Icon=nepomuk
Type=Application
Categories=Utility;KDE;Qt;
EOF

%find_lang %{name}

