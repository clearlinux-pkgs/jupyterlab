#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jupyterlab
Version  : 0.34.12
Release  : 34
URL      : https://files.pythonhosted.org/packages/38/cb/1b3fe08b58765e11abbbfaa9acfaa8629404236bf9c0f43c1e7b17b56fb4/jupyterlab-0.34.12.tar.gz
Source0  : https://files.pythonhosted.org/packages/38/cb/1b3fe08b58765e11abbbfaa9acfaa8629404236bf9c0f43c1e7b17b56fb4/jupyterlab-0.34.12.tar.gz
Summary  : The JupyterLab notebook server extension.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: jupyterlab-bin
Requires: jupyterlab-python3
Requires: jupyterlab-license
Requires: jupyterlab-data
Requires: jupyterlab-python
Requires: jupyterlab_launcher
Requires: notebook
BuildRequires : buildreq-distutils3
BuildRequires : jupyterlab_launcher
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
%setup -q -n jupyterlab-0.34.12

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1537636769
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/jupyterlab
cp LICENSE %{buildroot}/usr/share/doc/jupyterlab/LICENSE
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
/usr/share/jupyter/lab/schemas/@jupyterlab/apputils-extension/package.json
/usr/share/jupyter/lab/schemas/@jupyterlab/apputils-extension/themes.json
/usr/share/jupyter/lab/schemas/@jupyterlab/codemirror-extension/commands.json
/usr/share/jupyter/lab/schemas/@jupyterlab/codemirror-extension/package.json
/usr/share/jupyter/lab/schemas/@jupyterlab/docmanager-extension/package.json
/usr/share/jupyter/lab/schemas/@jupyterlab/docmanager-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/extensionmanager-extension/package.json
/usr/share/jupyter/lab/schemas/@jupyterlab/extensionmanager-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/fileeditor-extension/package.json
/usr/share/jupyter/lab/schemas/@jupyterlab/fileeditor-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/notebook-extension/package.json
/usr/share/jupyter/lab/schemas/@jupyterlab/notebook-extension/tracker.json
/usr/share/jupyter/lab/schemas/@jupyterlab/shortcuts-extension/package.json
/usr/share/jupyter/lab/schemas/@jupyterlab/shortcuts-extension/plugin.json
/usr/share/jupyter/lab/static/0.8655c60128912e3ea900.js
/usr/share/jupyter/lab/static/0.8655c60128912e3ea900.js.map
/usr/share/jupyter/lab/static/3.41f272f8c07719e6ad4f.js
/usr/share/jupyter/lab/static/3.41f272f8c07719e6ad4f.js.map
/usr/share/jupyter/lab/static/674f50d287a8c48dc19ba404d20fe713.eot
/usr/share/jupyter/lab/static/912ec66d7572ff821749319396470bde.svg
/usr/share/jupyter/lab/static/af7ae505a9eed503f8b8e6982036873e.woff2
/usr/share/jupyter/lab/static/b06871f281fee6b241d60582ae9369b9.ttf
/usr/share/jupyter/lab/static/error.html
/usr/share/jupyter/lab/static/fee66e712a8a08eef5805a46892932ad.woff
/usr/share/jupyter/lab/static/index.html
/usr/share/jupyter/lab/static/index.out.js
/usr/share/jupyter/lab/static/main.4dabccaa6191334b21b3.js
/usr/share/jupyter/lab/static/main.4dabccaa6191334b21b3.js.map
/usr/share/jupyter/lab/static/package.json
/usr/share/jupyter/lab/static/vega.9cff6aa9bc603daa8752.js
/usr/share/jupyter/lab/static/vega.9cff6aa9bc603daa8752.js.map
/usr/share/jupyter/lab/static/vendors~main.9426d747af44253aafe1.js
/usr/share/jupyter/lab/static/vendors~main.9426d747af44253aafe1.js.map
/usr/share/jupyter/lab/static/vendors~vega.a85114bab00108ec904d.js
/usr/share/jupyter/lab/static/vendors~vega.a85114bab00108ec904d.js.map
/usr/share/jupyter/lab/themes/@jupyterlab/theme-dark-extension/674f50d287a8c48dc19ba404d20fe713.eot
/usr/share/jupyter/lab/themes/@jupyterlab/theme-dark-extension/af7ae505a9eed503f8b8e6982036873e.woff2
/usr/share/jupyter/lab/themes/@jupyterlab/theme-dark-extension/b06871f281fee6b241d60582ae9369b9.ttf
/usr/share/jupyter/lab/themes/@jupyterlab/theme-dark-extension/embed.css
/usr/share/jupyter/lab/themes/@jupyterlab/theme-dark-extension/fee66e712a8a08eef5805a46892932ad.woff
/usr/share/jupyter/lab/themes/@jupyterlab/theme-dark-extension/index.css
/usr/share/jupyter/lab/themes/@jupyterlab/theme-dark-extension/package.json
/usr/share/jupyter/lab/themes/@jupyterlab/theme-light-extension/674f50d287a8c48dc19ba404d20fe713.eot
/usr/share/jupyter/lab/themes/@jupyterlab/theme-light-extension/af7ae505a9eed503f8b8e6982036873e.woff2
/usr/share/jupyter/lab/themes/@jupyterlab/theme-light-extension/b06871f281fee6b241d60582ae9369b9.ttf
/usr/share/jupyter/lab/themes/@jupyterlab/theme-light-extension/embed.css
/usr/share/jupyter/lab/themes/@jupyterlab/theme-light-extension/fee66e712a8a08eef5805a46892932ad.woff
/usr/share/jupyter/lab/themes/@jupyterlab/theme-light-extension/index.css
/usr/share/jupyter/lab/themes/@jupyterlab/theme-light-extension/package.json

%files license
%defattr(-,root,root,-)
/usr/share/doc/jupyterlab/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
