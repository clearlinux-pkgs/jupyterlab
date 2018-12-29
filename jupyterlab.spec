#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jupyterlab
Version  : 0.35.4
Release  : 41
URL      : https://files.pythonhosted.org/packages/39/4f/e8f51e797e6c4a580551141a9cc9ef38235d0cc3b1920d8bb3bacb58c927/jupyterlab-0.35.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/39/4f/e8f51e797e6c4a580551141a9cc9ef38235d0cc3b1920d8bb3bacb58c927/jupyterlab-0.35.4.tar.gz
Summary  : The JupyterLab notebook server extension.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: jupyterlab-bin = %{version}-%{release}
Requires: jupyterlab-data = %{version}-%{release}
Requires: jupyterlab-license = %{version}-%{release}
Requires: jupyterlab-python = %{version}-%{release}
Requires: jupyterlab-python3 = %{version}-%{release}
Requires: jupyterlab_server
Requires: notebook
BuildRequires : buildreq-distutils3
BuildRequires : jupyterlab_server
BuildRequires : notebook

%description
An extensible, comprehensive Jupyter web application.

%package bin
Summary: bin components for the jupyterlab package.
Group: Binaries
Requires: jupyterlab-data = %{version}-%{release}
Requires: jupyterlab-license = %{version}-%{release}

%description bin
bin components for the jupyterlab package.


%package data
Summary: data components for the jupyterlab package.
Group: Data

%description data
data components for the jupyterlab package.


%package license
Summary: license components for the jupyterlab package.
Group: Default

%description license
license components for the jupyterlab package.


%package python
Summary: python components for the jupyterlab package.
Group: Default
Requires: jupyterlab-python3 = %{version}-%{release}

%description python
python components for the jupyterlab package.


%package python3
Summary: python3 components for the jupyterlab package.
Group: Default
Requires: python3-core

%description python3
python3 components for the jupyterlab package.


%prep
%setup -q -n jupyterlab-0.35.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541348103
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jupyterlab
cp LICENSE %{buildroot}/usr/share/package-licenses/jupyterlab/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
mkdir -p  %{buildroot}/usr/share/jupyter/
mv %{buildroot}/usr/etc/jupyter/jupyter_notebook_config.d %{buildroot}/usr/share/jupyter/
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jlpm
/usr/bin/jupyter-lab
/usr/bin/jupyter-labextension
/usr/bin/jupyter-labhub

%files data
%defattr(-,root,root,-)
/usr/share/jupyter/jupyter_notebook_config.d/jupyterlab.json
/usr/share/jupyter/lab/schemas/@jupyterlab/application-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/application-extension/sidebar.json
/usr/share/jupyter/lab/schemas/@jupyterlab/apputils-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/apputils-extension/themes.json
/usr/share/jupyter/lab/schemas/@jupyterlab/codemirror-extension/commands.json
/usr/share/jupyter/lab/schemas/@jupyterlab/codemirror-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/docmanager-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/docmanager-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/extensionmanager-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/extensionmanager-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/fileeditor-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/fileeditor-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/notebook-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/notebook-extension/tracker.json
/usr/share/jupyter/lab/schemas/@jupyterlab/shortcuts-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/shortcuts-extension/plugin.json
/usr/share/jupyter/lab/static/0.8655c60128912e3ea900.js
/usr/share/jupyter/lab/static/0.8655c60128912e3ea900.js.map
/usr/share/jupyter/lab/static/3.41f272f8c07719e6ad4f.js
/usr/share/jupyter/lab/static/3.41f272f8c07719e6ad4f.js.map
/usr/share/jupyter/lab/static/674f50d287a8c48dc19ba404d20fe713.eot
/usr/share/jupyter/lab/static/912ec66d7572ff821749319396470bde.svg
/usr/share/jupyter/lab/static/af7ae505a9eed503f8b8e6982036873e.woff2
/usr/share/jupyter/lab/static/b06871f281fee6b241d60582ae9369b9.ttf
/usr/share/jupyter/lab/static/fee66e712a8a08eef5805a46892932ad.woff
/usr/share/jupyter/lab/static/index.html
/usr/share/jupyter/lab/static/index.out.js
/usr/share/jupyter/lab/static/main.13de647526d0a582493b.js
/usr/share/jupyter/lab/static/main.13de647526d0a582493b.js.map
/usr/share/jupyter/lab/static/package.json
/usr/share/jupyter/lab/static/vega.0adc8a452b66056a4f6e.js
/usr/share/jupyter/lab/static/vega.0adc8a452b66056a4f6e.js.map
/usr/share/jupyter/lab/static/vendors~main.10079ad9676c70f28097.js
/usr/share/jupyter/lab/static/vendors~main.10079ad9676c70f28097.js.map
/usr/share/jupyter/lab/static/vendors~vega.c717f56039d7217b5baa.js
/usr/share/jupyter/lab/static/vendors~vega.c717f56039d7217b5baa.js.map
/usr/share/jupyter/lab/themes/@jupyterlab/theme-dark-extension/674f50d287a8c48dc19ba404d20fe713.eot
/usr/share/jupyter/lab/themes/@jupyterlab/theme-dark-extension/af7ae505a9eed503f8b8e6982036873e.woff2
/usr/share/jupyter/lab/themes/@jupyterlab/theme-dark-extension/b06871f281fee6b241d60582ae9369b9.ttf
/usr/share/jupyter/lab/themes/@jupyterlab/theme-dark-extension/embed.css
/usr/share/jupyter/lab/themes/@jupyterlab/theme-dark-extension/fee66e712a8a08eef5805a46892932ad.woff
/usr/share/jupyter/lab/themes/@jupyterlab/theme-dark-extension/index.css
/usr/share/jupyter/lab/themes/@jupyterlab/theme-dark-extension/package.json.orig
/usr/share/jupyter/lab/themes/@jupyterlab/theme-light-extension/674f50d287a8c48dc19ba404d20fe713.eot
/usr/share/jupyter/lab/themes/@jupyterlab/theme-light-extension/af7ae505a9eed503f8b8e6982036873e.woff2
/usr/share/jupyter/lab/themes/@jupyterlab/theme-light-extension/b06871f281fee6b241d60582ae9369b9.ttf
/usr/share/jupyter/lab/themes/@jupyterlab/theme-light-extension/embed.css
/usr/share/jupyter/lab/themes/@jupyterlab/theme-light-extension/fee66e712a8a08eef5805a46892932ad.woff
/usr/share/jupyter/lab/themes/@jupyterlab/theme-light-extension/index.css
/usr/share/jupyter/lab/themes/@jupyterlab/theme-light-extension/package.json.orig

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jupyterlab/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
