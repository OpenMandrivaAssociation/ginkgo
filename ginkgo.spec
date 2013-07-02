Summary:	Navigator for Nepomuk, the KDE semantic toolkit
Name:		ginkgo
Version:	0.32
Release:	3
License:	GPLv2+
Url:		http://wiki.mandriva.com/en/Ginkgo
Group:		Graphical desktop/KDE 
Source0:	%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	kde4-macros
Requires:	python-kde4
Requires:	python-mako

%description
Ginkgo is a graphical front-end for managing data semantically. Ginkgo 
lets you create and explore links between your personal data such 
as e-mails, contacts, files, Web pages. It harnesses the Nepomuk
framework.

%files -f %{name}.lang
%{_kde_appsdir}/%{name}
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
  msgfmt -o ${langdir}/%name.mo ${i}
done

%find_lang %{name}

