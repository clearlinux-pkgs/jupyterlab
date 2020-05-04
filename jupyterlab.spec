#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jupyterlab
Version  : 2.1.2
Release  : 67
URL      : https://files.pythonhosted.org/packages/64/b4/65b608ca9d7a78adf403bb1dd6ca0c7b3ce2cedbe1255184b3dc88436723/jupyterlab-2.1.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/64/b4/65b608ca9d7a78adf403bb1dd6ca0c7b3ce2cedbe1255184b3dc88436723/jupyterlab-2.1.2.tar.gz
Summary  : The JupyterLab notebook server extension.
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause MIT
Requires: jupyterlab-bin = %{version}-%{release}
Requires: jupyterlab-data = %{version}-%{release}
Requires: jupyterlab-license = %{version}-%{release}
Requires: jupyterlab-python = %{version}-%{release}
Requires: jupyterlab-python3 = %{version}-%{release}
Requires: Jinja2
Requires: jupyterlab_server
Requires: notebook
Requires: tornado
BuildRequires : Jinja2
BuildRequires : buildreq-distutils3
BuildRequires : jupyterlab_server
BuildRequires : notebook
BuildRequires : tornado

%description
**[Installation](#installation)** |
**[Documentation](http://jupyterlab.readthedocs.io)** |
**[Contributing](#contributing)** |
**[License](#license)** |
**[Team](#team)** |
**[Getting help](#getting-help)** |

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
Provides: pypi(jupyterlab)
Requires: pypi(jinja2)
Requires: pypi(jupyterlab_server)
Requires: pypi(notebook)
Requires: pypi(tornado)

%description python3
python3 components for the jupyterlab package.


%prep
%setup -q -n jupyterlab-2.1.2
cd %{_builddir}/jupyterlab-2.1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588632825
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jupyterlab
cp %{_builddir}/jupyterlab-2.1.2/LICENSE %{buildroot}/usr/share/package-licenses/jupyterlab/9627fe5214679aa301dcdbb0f788b000d2cbf30e
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

%files data
%defattr(-,root,root,-)
/usr/share/jupyter/jupyter_notebook_config.d/jupyterlab.json
/usr/share/jupyter/lab/schemas/@jupyterlab/application-extension/main.json
/usr/share/jupyter/lab/schemas/@jupyterlab/application-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/application-extension/sidebar.json
/usr/share/jupyter/lab/schemas/@jupyterlab/apputils-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/apputils-extension/palette.json
/usr/share/jupyter/lab/schemas/@jupyterlab/apputils-extension/print.json
/usr/share/jupyter/lab/schemas/@jupyterlab/apputils-extension/themes.json
/usr/share/jupyter/lab/schemas/@jupyterlab/codemirror-extension/commands.json
/usr/share/jupyter/lab/schemas/@jupyterlab/codemirror-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/completer-extension/consoles.json
/usr/share/jupyter/lab/schemas/@jupyterlab/completer-extension/files.json
/usr/share/jupyter/lab/schemas/@jupyterlab/completer-extension/notebooks.json
/usr/share/jupyter/lab/schemas/@jupyterlab/completer-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/console-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/console-extension/tracker.json
/usr/share/jupyter/lab/schemas/@jupyterlab/docmanager-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/docmanager-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/documentsearch-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/documentsearch-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/extensionmanager-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/extensionmanager-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/filebrowser-extension/browser.json
/usr/share/jupyter/lab/schemas/@jupyterlab/filebrowser-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/fileeditor-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/fileeditor-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/imageviewer-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/imageviewer-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/inspector-extension/inspector.json
/usr/share/jupyter/lab/schemas/@jupyterlab/inspector-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/launcher-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/launcher-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/logconsole-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/logconsole-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/mainmenu-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/mainmenu-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/markdownviewer-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/markdownviewer-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/notebook-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/notebook-extension/tracker.json
/usr/share/jupyter/lab/schemas/@jupyterlab/settingeditor-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/settingeditor-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/shortcuts-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/shortcuts-extension/shortcuts.json
/usr/share/jupyter/lab/schemas/@jupyterlab/statusbar-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/statusbar-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/terminal-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/terminal-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/tooltip-extension/consoles.json
/usr/share/jupyter/lab/schemas/@jupyterlab/tooltip-extension/files.json
/usr/share/jupyter/lab/schemas/@jupyterlab/tooltip-extension/notebooks.json
/usr/share/jupyter/lab/schemas/@jupyterlab/tooltip-extension/package.json.orig
/usr/share/jupyter/lab/static/0cb5a5c0d251c109458c85c6afeffbaa.svg
/usr/share/jupyter/lab/static/13685372945d816a2b474fc082fd9aaa.ttf
/usr/share/jupyter/lab/static/1ab236ed440ee51810c56bd16628aef0.ttf
/usr/share/jupyter/lab/static/2.a9b3bd9391c5f5245e28.js
/usr/share/jupyter/lab/static/2.a9b3bd9391c5f5245e28.js.LICENSE.txt
/usr/share/jupyter/lab/static/261d666b0147c6c5cda07265f98b8f8c.eot
/usr/share/jupyter/lab/static/3.f941985263277afd3725.js
/usr/share/jupyter/lab/static/3.f941985263277afd3725.js.LICENSE.txt
/usr/share/jupyter/lab/static/4.ce34abf308d449caaf60.js
/usr/share/jupyter/lab/static/5.9034a259f0f5d7418c18.js
/usr/share/jupyter/lab/static/6.c52921459f39b8f8ec3d.js
/usr/share/jupyter/lab/static/89ffa3aba80d30ee0a9371b25c968bbb.svg
/usr/share/jupyter/lab/static/a0369ea57eb6d3843d6474c035111f29.eot
/usr/share/jupyter/lab/static/a06da7f0950f9dd366fc9db9d56d618a.woff2
/usr/share/jupyter/lab/static/b15db15f746f29ffa02638cb455b8ec0.woff2
/usr/share/jupyter/lab/static/bea989e82b07e9687c26fc58a4805021.woff
/usr/share/jupyter/lab/static/c1868c9545d2de1cf8488f1dadd8c9d0.eot
/usr/share/jupyter/lab/static/c20b5b7362d8d7bb7eddf94344ace33e.woff2
/usr/share/jupyter/lab/static/db78b9359171f24936b16d84f63af378.ttf
/usr/share/jupyter/lab/static/ec3cfddedb8bebd2d7a3fdf511f7c1cc.woff
/usr/share/jupyter/lab/static/ec763292e583294612f124c0b0def500.svg
/usr/share/jupyter/lab/static/f89ea91ecd1ca2db7e09baa2c4b156d1.woff
/usr/share/jupyter/lab/static/imports.css
/usr/share/jupyter/lab/static/index.html
/usr/share/jupyter/lab/static/index.out.js
/usr/share/jupyter/lab/static/main.84c2f11f976011b33c76.js
/usr/share/jupyter/lab/static/package.json
/usr/share/jupyter/lab/static/vendors~main.1ff9e1aa66854e17eccd.js
/usr/share/jupyter/lab/static/vendors~main.1ff9e1aa66854e17eccd.js.LICENSE.txt
/usr/share/jupyter/lab/themes/@jupyterlab/theme-dark-extension/index.css
/usr/share/jupyter/lab/themes/@jupyterlab/theme-dark-extension/index.js
/usr/share/jupyter/lab/themes/@jupyterlab/theme-light-extension/index.css
/usr/share/jupyter/lab/themes/@jupyterlab/theme-light-extension/index.js

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jupyterlab/9627fe5214679aa301dcdbb0f788b000d2cbf30e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
