#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jupyterlab
Version  : 2.2.2
Release  : 73
URL      : https://files.pythonhosted.org/packages/1b/6f/970535cc7ba86688f61c8361fff043daec529f9e31badd8d43fe8e6a7f48/jupyterlab-2.2.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/1b/6f/970535cc7ba86688f61c8361fff043daec529f9e31badd8d43fe8e6a7f48/jupyterlab-2.2.2.tar.gz
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
%setup -q -n jupyterlab-2.2.2
cd %{_builddir}/jupyterlab-2.2.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1595895313
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
cp %{_builddir}/'jupyterlab-2.2.2/jupyterlab/static/vendors~main.aee10a0dbdadee16025a.js.LICENSE.txt' %{buildroot}/usr/share/package-licenses/jupyterlab/fc09f3614486bf83f4ebc4bb6a9876721d513c83
cp %{_builddir}/jupyterlab-2.2.2/LICENSE %{buildroot}/usr/share/package-licenses/jupyterlab/9627fe5214679aa301dcdbb0f788b000d2cbf30e
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
/usr/share/jupyter/lab/static/03ba7cb710104df27f1c9c46d64bee4e.svg
/usr/share/jupyter/lab/static/05b53beb21e3ef13d28244545977152d.woff
/usr/share/jupyter/lab/static/085b1dd8427dbeff10bd55410915a3f6.ttf
/usr/share/jupyter/lab/static/0fabb6606be4c45acfeedd115d0caca4.eot
/usr/share/jupyter/lab/static/10.ef933be28c7284465d48.js
/usr/share/jupyter/lab/static/11.7491225c4f0b26eb4a4a.js
/usr/share/jupyter/lab/static/12.4f1b1ddb0ad2b2dfd08c.js
/usr/share/jupyter/lab/static/13.7d10ed489bee28ffc039.js
/usr/share/jupyter/lab/static/14.a189b26d59494d01bfac.js
/usr/share/jupyter/lab/static/15.910c183c59db56d83c69.js
/usr/share/jupyter/lab/static/16.cc0d5b330b302cd1c1ad.js
/usr/share/jupyter/lab/static/17.c423c5d0a3b13167667b.js
/usr/share/jupyter/lab/static/18.e61e08ca5c4d0210ee45.js
/usr/share/jupyter/lab/static/19.388d594565c771ecbb3f.js
/usr/share/jupyter/lab/static/1a78af4105d4d56e6c34f76dc70bf1bc.ttf
/usr/share/jupyter/lab/static/2.9ccb7977a199a4a50689.js
/usr/share/jupyter/lab/static/2.9ccb7977a199a4a50689.js.LICENSE.txt
/usr/share/jupyter/lab/static/20.a1b307dd3c83424c7c0a.js
/usr/share/jupyter/lab/static/21.8bce2228df27d0706635.js
/usr/share/jupyter/lab/static/22.1c2664d60aec888a2923.js
/usr/share/jupyter/lab/static/23.dfbe949aa7ebd98721a3.js
/usr/share/jupyter/lab/static/24.54aad87961103d4c1393.js
/usr/share/jupyter/lab/static/25.bb9a7b884714ca64fa01.js
/usr/share/jupyter/lab/static/26.d0d2118a45d34d76ceee.js
/usr/share/jupyter/lab/static/27.20773573f8bad05f818b.js
/usr/share/jupyter/lab/static/28.f068ce4ec3f9eec27e0c.js
/usr/share/jupyter/lab/static/29.1c9dd340a512ed716998.js
/usr/share/jupyter/lab/static/3.f56ee5822ed7ab141e07.js
/usr/share/jupyter/lab/static/3.f56ee5822ed7ab141e07.js.LICENSE.txt
/usr/share/jupyter/lab/static/30.f02743df8502a328e59c.js
/usr/share/jupyter/lab/static/31.2734bfadb56a6f9ec935.js
/usr/share/jupyter/lab/static/32.62db02d6c5dba8e2016c.js
/usr/share/jupyter/lab/static/33.29921b636d356969ca26.js
/usr/share/jupyter/lab/static/34.46e3cca1ee52b1c126bc.js
/usr/share/jupyter/lab/static/35.3daf71f2f0c77b51c289.js
/usr/share/jupyter/lab/static/36.345d1e75e17128b20907.js
/usr/share/jupyter/lab/static/37.c36abc989a343a3229c5.js
/usr/share/jupyter/lab/static/38.ddef681e01deca09a1c8.js
/usr/share/jupyter/lab/static/39.375b298fa627a954649a.js
/usr/share/jupyter/lab/static/3a3398a6ef60fc64eacf45665958342e.woff2
/usr/share/jupyter/lab/static/4.69406a7d6939b46f4e98.js
/usr/share/jupyter/lab/static/40.954ce180c146f51772f0.js
/usr/share/jupyter/lab/static/41.44aefdeda08d233f8440.js
/usr/share/jupyter/lab/static/42.eb66349f8f6c9473501e.js
/usr/share/jupyter/lab/static/43.49329850adce8409ca28.js
/usr/share/jupyter/lab/static/44.42b289f0f5b853b5f29d.js
/usr/share/jupyter/lab/static/45.71e4ffb537472e75277a.js
/usr/share/jupyter/lab/static/46.eebb11d0fd47366db202.js
/usr/share/jupyter/lab/static/47.03195b8b16e6aee96eb0.js
/usr/share/jupyter/lab/static/48.2ee8c7b1445d7aa157f3.js
/usr/share/jupyter/lab/static/49.c25a20109b66ef356298.js
/usr/share/jupyter/lab/static/5.6b76a47b601eabbaa500.js
/usr/share/jupyter/lab/static/50.fa1bdc2d63136718e968.js
/usr/share/jupyter/lab/static/51.1d937dbcb7607382269d.js
/usr/share/jupyter/lab/static/52.9ed00644069dae2925bc.js
/usr/share/jupyter/lab/static/53.8b97690a74b772f669ef.js
/usr/share/jupyter/lab/static/54.bf4d64fbae9cfa744b2b.js
/usr/share/jupyter/lab/static/55.e211178e45d575ff278b.js
/usr/share/jupyter/lab/static/56.049eed1172637adb1ad8.js
/usr/share/jupyter/lab/static/57.2a1c93de3050dd642e34.js
/usr/share/jupyter/lab/static/58.c1e1660b34b24d8535bf.js
/usr/share/jupyter/lab/static/59.5ce32adc84b63b842190.js
/usr/share/jupyter/lab/static/6.6b78e05cd6cd282639ec.js
/usr/share/jupyter/lab/static/60.ce3a66f59430ce183398.js
/usr/share/jupyter/lab/static/61.d88f348e7d2ef94207a9.js
/usr/share/jupyter/lab/static/62.1d99286978adaea88882.js
/usr/share/jupyter/lab/static/63.18bd1a36bf89d7c6d03f.js
/usr/share/jupyter/lab/static/64.c6687f6d3de36d300f74.js
/usr/share/jupyter/lab/static/65.9be1c6eed573c5e102e2.js
/usr/share/jupyter/lab/static/66.9aae5e1eb21b040f8a88.js
/usr/share/jupyter/lab/static/67.831bad69df3d31355c1e.js
/usr/share/jupyter/lab/static/68.12b5dc64b500397cfe0c.js
/usr/share/jupyter/lab/static/69.c8e080e7bdd317c4d7f8.js
/usr/share/jupyter/lab/static/7.03498734f218ea9500ec.js
/usr/share/jupyter/lab/static/781e85bb50c8e8301c30de56b31b1f04.ttf
/usr/share/jupyter/lab/static/8.5d00a68b1a61b43ff9b3.js
/usr/share/jupyter/lab/static/89bd2e38475e441a5cd70f663f921d61.eot
/usr/share/jupyter/lab/static/9.11dea408b667532f5560.js
/usr/share/jupyter/lab/static/ad3a7c0d77e09602f4ab73db3660ffd8.eot
/usr/share/jupyter/lab/static/c500da19d776384ba69573ae6fe274e7.woff2
/usr/share/jupyter/lab/static/cac68c831145804808381a7032fdc7c2.woff2
/usr/share/jupyter/lab/static/ccfdb9dc442be0c629d331e94497428b.svg
/usr/share/jupyter/lab/static/dc0bd022735ed218df547742a1b2f172.woff
/usr/share/jupyter/lab/static/e75dfd904d366a2560c63c23cfc98ef8.svg
/usr/share/jupyter/lab/static/ee09ad7553b8ad3d81150d609d5341a0.woff
/usr/share/jupyter/lab/static/imports.css
/usr/share/jupyter/lab/static/index.html
/usr/share/jupyter/lab/static/index.out.js
/usr/share/jupyter/lab/static/main.52ca548de46eee7458c0.js
/usr/share/jupyter/lab/static/package.json
/usr/share/jupyter/lab/static/vendors~main.aee10a0dbdadee16025a.js
/usr/share/jupyter/lab/static/vendors~main.aee10a0dbdadee16025a.js.LICENSE.txt
/usr/share/jupyter/lab/themes/@jupyterlab/theme-dark-extension/index.css
/usr/share/jupyter/lab/themes/@jupyterlab/theme-dark-extension/index.js
/usr/share/jupyter/lab/themes/@jupyterlab/theme-light-extension/index.css
/usr/share/jupyter/lab/themes/@jupyterlab/theme-light-extension/index.js

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jupyterlab/9627fe5214679aa301dcdbb0f788b000d2cbf30e
/usr/share/package-licenses/jupyterlab/fc09f3614486bf83f4ebc4bb6a9876721d513c83

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
