#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jupyterlab
Version  : 3.1.4
Release  : 109
URL      : https://files.pythonhosted.org/packages/b1/64/fc16aed4f198251003b89b1a06a979366807ae2555e4388df66cbce1f091/jupyterlab-3.1.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/b1/64/fc16aed4f198251003b89b1a06a979366807ae2555e4388df66cbce1f091/jupyterlab-3.1.4.tar.gz
Summary  : JupyterLab computational environment
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause MIT
Requires: jupyterlab-bin = %{version}-%{release}
Requires: jupyterlab-data = %{version}-%{release}
Requires: jupyterlab-license = %{version}-%{release}
Requires: jupyterlab-python = %{version}-%{release}
Requires: jupyterlab-python3 = %{version}-%{release}
Requires: Jinja2
Requires: ipython
Requires: jupyter_core
Requires: jupyterlab_server
Requires: packaging
Requires: tornado
BuildRequires : Jinja2
BuildRequires : buildreq-distutils3
BuildRequires : ipython
BuildRequires : jupyter-packaging
BuildRequires : jupyterlab_server
BuildRequires : packaging
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
Requires: pypi(ipython)
Requires: pypi(jinja2)
Requires: pypi(jupyter_core)
Requires: pypi(jupyter_server)
Requires: pypi(jupyterlab_server)
Requires: pypi(nbclassic)
Requires: pypi(packaging)
Requires: pypi(tornado)

%description python3
python3 components for the jupyterlab package.


%prep
%setup -q -n jupyterlab-3.1.4
cd %{_builddir}/jupyterlab-3.1.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1628212354
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jupyterlab
cp %{_builddir}/jupyterlab-3.1.4/LICENSE %{buildroot}/usr/share/package-licenses/jupyterlab/fa62fa6d531b94e755b914b3291c8541ce40f411
cp %{_builddir}/jupyterlab-3.1.4/jupyterlab/static/1036.78d136acb6f2b00042ef.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/jupyterlab/01ebbe688c25d738b9ee0e2de8113f7351c88e7a
cp %{_builddir}/jupyterlab-3.1.4/jupyterlab/static/3935.640625791c067ed14c45.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/jupyterlab/10645e5e81c59dc0f14b79252005ea68d42f1ba7
cp %{_builddir}/jupyterlab-3.1.4/jupyterlab/static/7294.51bceb31ba4dfd026d8a.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/jupyterlab/0036998e52f1b6442c90b9ea6df602bef0294cc5
cp %{_builddir}/jupyterlab-3.1.4/jupyterlab/static/jlab_core.86360d749a1ef5f29afb.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/jupyterlab/7f822fe9341af8f82ad1b0c69aba957822a377cf
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
mkdir -p  %{buildroot}/usr/share/jupyter/
mv %{buildroot}/usr/etc/jupyter/jupyter_notebook_config.d %{buildroot}/usr/share/jupyter/
mv %{buildroot}/usr/etc/jupyter/jupyter_server_config.d/jupyterlab.json  %{buildroot}/usr/share/jupyter/
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
/usr/share/jupyter/jupyterlab.json
/usr/share/jupyter/lab/schemas/@jupyterlab/application-extension/commands.json
/usr/share/jupyter/lab/schemas/@jupyterlab/application-extension/context-menu.json
/usr/share/jupyter/lab/schemas/@jupyterlab/application-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/application-extension/sidebar.json
/usr/share/jupyter/lab/schemas/@jupyterlab/apputils-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/apputils-extension/palette.json
/usr/share/jupyter/lab/schemas/@jupyterlab/apputils-extension/print.json
/usr/share/jupyter/lab/schemas/@jupyterlab/apputils-extension/themes.json
/usr/share/jupyter/lab/schemas/@jupyterlab/apputils-extension/workspaces.json
/usr/share/jupyter/lab/schemas/@jupyterlab/codemirror-extension/commands.json
/usr/share/jupyter/lab/schemas/@jupyterlab/codemirror-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/completer-extension/consoles.json
/usr/share/jupyter/lab/schemas/@jupyterlab/completer-extension/files.json
/usr/share/jupyter/lab/schemas/@jupyterlab/completer-extension/notebooks.json
/usr/share/jupyter/lab/schemas/@jupyterlab/completer-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/console-extension/foreign.json
/usr/share/jupyter/lab/schemas/@jupyterlab/console-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/console-extension/tracker.json
/usr/share/jupyter/lab/schemas/@jupyterlab/debugger-extension/main.json
/usr/share/jupyter/lab/schemas/@jupyterlab/debugger-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/docmanager-extension/download.json
/usr/share/jupyter/lab/schemas/@jupyterlab/docmanager-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/docmanager-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/documentsearch-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/documentsearch-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/extensionmanager-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/extensionmanager-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/filebrowser-extension/browser.json
/usr/share/jupyter/lab/schemas/@jupyterlab/filebrowser-extension/download.json
/usr/share/jupyter/lab/schemas/@jupyterlab/filebrowser-extension/open-browser-tab.json
/usr/share/jupyter/lab/schemas/@jupyterlab/filebrowser-extension/open-with.json
/usr/share/jupyter/lab/schemas/@jupyterlab/filebrowser-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/fileeditor-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/fileeditor-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/help-extension/about.json
/usr/share/jupyter/lab/schemas/@jupyterlab/help-extension/jupyter-forum.json
/usr/share/jupyter/lab/schemas/@jupyterlab/help-extension/launch-classic.json
/usr/share/jupyter/lab/schemas/@jupyterlab/help-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/hub-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/hub-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/imageviewer-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/imageviewer-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/inspector-extension/consoles.json
/usr/share/jupyter/lab/schemas/@jupyterlab/inspector-extension/inspector.json
/usr/share/jupyter/lab/schemas/@jupyterlab/inspector-extension/notebooks.json
/usr/share/jupyter/lab/schemas/@jupyterlab/inspector-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/launcher-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/launcher-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/logconsole-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/logconsole-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/mainmenu-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/mainmenu-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/markdownviewer-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/markdownviewer-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/notebook-extension/export.json
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
/usr/share/jupyter/lab/schemas/@jupyterlab/toc-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/toc-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/tooltip-extension/consoles.json
/usr/share/jupyter/lab/schemas/@jupyterlab/tooltip-extension/files.json
/usr/share/jupyter/lab/schemas/@jupyterlab/tooltip-extension/notebooks.json
/usr/share/jupyter/lab/schemas/@jupyterlab/tooltip-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/translation-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/translation-extension/plugin.json
/usr/share/jupyter/lab/static/1033.f56962890956fc6e6596.js
/usr/share/jupyter/lab/static/1036.78d136acb6f2b00042ef.js
/usr/share/jupyter/lab/static/1036.78d136acb6f2b00042ef.js.LICENSE.txt
/usr/share/jupyter/lab/static/1044.f66ea94ed607a9489d3a.js
/usr/share/jupyter/lab/static/1057.0961f79a52dd75b037e0.js
/usr/share/jupyter/lab/static/1231.fcdcebbdb2f6c490f0ea.js
/usr/share/jupyter/lab/static/1249.d0e24983cd0b70b76d69.js
/usr/share/jupyter/lab/static/126.59a3d537b056def67aa5.js
/usr/share/jupyter/lab/static/1281.c8e3a63a622546f8ee6f.js
/usr/share/jupyter/lab/static/1281.c8e3a63a622546f8ee6f.js.LICENSE.txt
/usr/share/jupyter/lab/static/1358.5d13bafd71e17aa4c0e6.js
/usr/share/jupyter/lab/static/1397.21c555d9e8e96d6972db.js
/usr/share/jupyter/lab/static/1551f4f60c37af51121f106501f69b80.woff2
/usr/share/jupyter/lab/static/1641.97513f8430dd3c24ec9d.js
/usr/share/jupyter/lab/static/1842.cb2f50d386b934e25119.js
/usr/share/jupyter/lab/static/1902.97901b600062212ba07e.js
/usr/share/jupyter/lab/static/1902.97901b600062212ba07e.js.LICENSE.txt
/usr/share/jupyter/lab/static/198.e15a7b1d2f1f38f9a142.js
/usr/share/jupyter/lab/static/2249.5301371302de97c11554.js
/usr/share/jupyter/lab/static/2285773e6b4b172f07d9b777c81b0775.woff
/usr/share/jupyter/lab/static/2349.035dcfd299d7bdfce6be.js
/usr/share/jupyter/lab/static/2353.a4348113388a2d11db7c.js
/usr/share/jupyter/lab/static/2356.427f2c5234c276b88282.js
/usr/share/jupyter/lab/static/23f19bb08961f37aaf692ff943823453.eot
/usr/share/jupyter/lab/static/2440.609ba553d3400d47c2a3.js
/usr/share/jupyter/lab/static/2585.48f9a557a77852d31366.js
/usr/share/jupyter/lab/static/2719.a4c135a609b3114581f8.js
/usr/share/jupyter/lab/static/2745.d2df00240676d406848a.js
/usr/share/jupyter/lab/static/2990.40aa207ec66b19433515.js
/usr/share/jupyter/lab/static/2f517e09eb2ca6650ff5bec5a95157ab.svg
/usr/share/jupyter/lab/static/3087.16f7189699ef924a7898.js
/usr/share/jupyter/lab/static/3122.786ec5c194bcf8aafd70.js
/usr/share/jupyter/lab/static/3236.3ea21c9c2b9d2fbb2834.js
/usr/share/jupyter/lab/static/3373.36520bb7c6ebf9c7a54b.js
/usr/share/jupyter/lab/static/3387.d6796545e04bc1d097b1.js
/usr/share/jupyter/lab/static/3443.244b16e1f75413de5fcf.js
/usr/share/jupyter/lab/static/3496.ef3a40fd9ba495356b85.js
/usr/share/jupyter/lab/static/3531.9f6f6751d363447e432d.js
/usr/share/jupyter/lab/static/3532.d86d02abab8c4da138ae.js
/usr/share/jupyter/lab/static/3664.3fe3a38a433bb41c1ef4.js
/usr/share/jupyter/lab/static/3791.6330ee75804e23855e77.js
/usr/share/jupyter/lab/static/3935.640625791c067ed14c45.js
/usr/share/jupyter/lab/static/3935.640625791c067ed14c45.js.LICENSE.txt
/usr/share/jupyter/lab/static/3992.11b6eb40d448a4cbc6dd.js
/usr/share/jupyter/lab/static/406.388a951ae4fc1290eeb2.js
/usr/share/jupyter/lab/static/4155.1eeaff1a19a1e7668778.js
/usr/share/jupyter/lab/static/4402.d33399d17f42e6fcc872.js
/usr/share/jupyter/lab/static/4429.fa7e08d5a51ece1132ad.js
/usr/share/jupyter/lab/static/45.b4bea0990972c48c6da5.js
/usr/share/jupyter/lab/static/4570.84ba6f203ea3ad3d3277.js
/usr/share/jupyter/lab/static/4631.cc296069ce9e45625659.js
/usr/share/jupyter/lab/static/4689f52cc96215721344e51e5831eec1.svg
/usr/share/jupyter/lab/static/4894.139073df71b0c7becda6.js
/usr/share/jupyter/lab/static/491974d108fe4002b2aaf7ffc48249a0.ttf
/usr/share/jupyter/lab/static/5065.8c52fec5bcea620c6ee1.js
/usr/share/jupyter/lab/static/5223.06a607f82bb11e2aa34e.js
/usr/share/jupyter/lab/static/527940b104eb2ea366c8630f3f038603.ttf
/usr/share/jupyter/lab/static/5289.7b1e862d3be9afbfc7c5.js
/usr/share/jupyter/lab/static/5383.633f0a616b4efd1e34da.js
/usr/share/jupyter/lab/static/5505.747cfc6514478b38afed.js
/usr/share/jupyter/lab/static/5557.7a10e41f352c0305ef44.js
/usr/share/jupyter/lab/static/5619.f9eb67cb5068c2e3970a.js
/usr/share/jupyter/lab/static/6005.47574fe04d61d792e7e5.js
/usr/share/jupyter/lab/static/6218.4a61b4d0d89f8214406a.js
/usr/share/jupyter/lab/static/6284.5cf706782d87844d6a59.js
/usr/share/jupyter/lab/static/6284.5cf706782d87844d6a59.js.LICENSE.txt
/usr/share/jupyter/lab/static/6504.47fc81a89eb572553dee.js
/usr/share/jupyter/lab/static/6509.bedc7e84cd4ecd2bbdd1.js
/usr/share/jupyter/lab/static/6550.57d0bf1a4ceb80622d5f.js
/usr/share/jupyter/lab/static/6598.4d5b99bca79b4538064e.js
/usr/share/jupyter/lab/static/6700.1559a2ad210fd059979c.js
/usr/share/jupyter/lab/static/6777.353a82bc4b04905726a1.js
/usr/share/jupyter/lab/static/6952.65d216710b0566c9f140.js
/usr/share/jupyter/lab/static/6962.a7ea24db6db11bfe850c.js
/usr/share/jupyter/lab/static/6975.98ea1f9df4ad633d193c.js
/usr/share/jupyter/lab/static/6989.95b2425ad41316961fc0.js
/usr/share/jupyter/lab/static/7034.7a81075010d7fa682844.js
/usr/share/jupyter/lab/static/7050.e3a02d1529d34b693246.js
/usr/share/jupyter/lab/static/7084.f9acf2277b9558ae9404.js
/usr/share/jupyter/lab/static/714.db04278404689f9f8301.js
/usr/share/jupyter/lab/static/7289.8ada08bee3a4019bf9f7.js
/usr/share/jupyter/lab/static/7294.51bceb31ba4dfd026d8a.js
/usr/share/jupyter/lab/static/7294.51bceb31ba4dfd026d8a.js.LICENSE.txt
/usr/share/jupyter/lab/static/7300.5bc8fe7c10a01ac12d89.js
/usr/share/jupyter/lab/static/7463.f42390c32a9ae5b6c9ca.js
/usr/share/jupyter/lab/static/7656.cd17f4d8f04439ef21e3.js
/usr/share/jupyter/lab/static/7717.80cd3b11b84c17e824ef.js
/usr/share/jupyter/lab/static/77206a6bb316fa0aded5083cc57f92b9.eot
/usr/share/jupyter/lab/static/7755.8455ad923057278e037c.js
/usr/share/jupyter/lab/static/7788.b08f528f0574331868cb.js
/usr/share/jupyter/lab/static/7900.4ef12034ce0674957ea9.js
/usr/share/jupyter/lab/static/7a3337626410ca2f40718481c755640f.woff2
/usr/share/jupyter/lab/static/7a8b4f130182d19a2d7c67d80c090397.svg
/usr/share/jupyter/lab/static/8012.836c0fabcf29c625d9b6.js
/usr/share/jupyter/lab/static/8059.70dd042ae540be428633.js
/usr/share/jupyter/lab/static/807.a92c471538fbd2781859.js
/usr/share/jupyter/lab/static/807.a92c471538fbd2781859.js.LICENSE.txt
/usr/share/jupyter/lab/static/8102.142ea2a7489890aee1c8.js
/usr/share/jupyter/lab/static/8173.b3cdc88dcb401955d50e.js
/usr/share/jupyter/lab/static/8428.5dc1d59ead7c13c795d3.js
/usr/share/jupyter/lab/static/8523.3b447e19b31b169cec83.js
/usr/share/jupyter/lab/static/8580.ae160e5f8d93ffa44939.js
/usr/share/jupyter/lab/static/8657.41f77c6604e1a43ca99d.js
/usr/share/jupyter/lab/static/870.0c629929becd044ad803.js
/usr/share/jupyter/lab/static/8708.3da078f864f97588e13c.js
/usr/share/jupyter/lab/static/8819.a9c0ce7bc485056bd13b.js
/usr/share/jupyter/lab/static/8823.8acbb4e77088286eae22.js
/usr/share/jupyter/lab/static/8834.f0c3708f7a22bad721fc.js
/usr/share/jupyter/lab/static/8843.ccaee176da9fc302b0fe.js
/usr/share/jupyter/lab/static/900.788903a7c6a016f721c8.js
/usr/share/jupyter/lab/static/901.8541b1f92d42629470b9.js
/usr/share/jupyter/lab/static/9039.13ff1db29928c97d34d7.js
/usr/share/jupyter/lab/static/9109.c4c4e0de8cb6f0e36fd9.js
/usr/share/jupyter/lab/static/911.7d289642557a8018cbaa.js
/usr/share/jupyter/lab/static/911.7d289642557a8018cbaa.js.LICENSE.txt
/usr/share/jupyter/lab/static/9116.e6fad6d44f9a453fdd98.js
/usr/share/jupyter/lab/static/9316.94ffcc340c232f89fd25.js
/usr/share/jupyter/lab/static/9473.f06fc507e84cb272835e.js
/usr/share/jupyter/lab/static/9473.f06fc507e84cb272835e.js.LICENSE.txt
/usr/share/jupyter/lab/static/96.e42d92544a8c06a3b8db.js
/usr/share/jupyter/lab/static/9684.7ceb6b4bf54ec007564d.js
/usr/share/jupyter/lab/static/9795.3491c2c7bd9eb56acd87.js
/usr/share/jupyter/lab/static/9845.ad1652428cae2f16e588.js
/usr/share/jupyter/lab/static/9866.779782167c00cc754a41.js
/usr/share/jupyter/lab/static/9912.af43b50d4932349294ec.js
/usr/share/jupyter/lab/static/9bbb245e67a133f6e486d8d2545e14a5.eot
/usr/share/jupyter/lab/static/bb58e57c48a3e911f15fa834ff00d44a.woff
/usr/share/jupyter/lab/static/be9ee23c0c6390141475d519c2c5fb8f.ttf
/usr/share/jupyter/lab/static/bootstrap.js
/usr/share/jupyter/lab/static/build_log.json
/usr/share/jupyter/lab/static/d878b0a6a1144760244ff0665888404c.woff2
/usr/share/jupyter/lab/static/eeccf4f66002c6f2ba24d3d22f2434c2.woff
/usr/share/jupyter/lab/static/index.html
/usr/share/jupyter/lab/static/index.out.js
/usr/share/jupyter/lab/static/jlab_core.86360d749a1ef5f29afb.js
/usr/share/jupyter/lab/static/jlab_core.86360d749a1ef5f29afb.js.LICENSE.txt
/usr/share/jupyter/lab/static/main.42ca50cc20782d886960.js
/usr/share/jupyter/lab/static/package.json
/usr/share/jupyter/lab/static/style.js
/usr/share/jupyter/lab/static/third-party-licenses.json
/usr/share/jupyter/lab/themes/@jupyterlab/theme-dark-extension/index.css
/usr/share/jupyter/lab/themes/@jupyterlab/theme-dark-extension/index.js
/usr/share/jupyter/lab/themes/@jupyterlab/theme-light-extension/index.css
/usr/share/jupyter/lab/themes/@jupyterlab/theme-light-extension/index.js

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jupyterlab/0036998e52f1b6442c90b9ea6df602bef0294cc5
/usr/share/package-licenses/jupyterlab/01ebbe688c25d738b9ee0e2de8113f7351c88e7a
/usr/share/package-licenses/jupyterlab/10645e5e81c59dc0f14b79252005ea68d42f1ba7
/usr/share/package-licenses/jupyterlab/7f822fe9341af8f82ad1b0c69aba957822a377cf
/usr/share/package-licenses/jupyterlab/fa62fa6d531b94e755b914b3291c8541ce40f411

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
