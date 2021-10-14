#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jupyterlab
Version  : 3.2.0
Release  : 121
URL      : https://files.pythonhosted.org/packages/ff/40/3a42d14494c8acccf3d66945ed347dd34984f079d11dcd9d97bfe3e6eec1/jupyterlab-3.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ff/40/3a42d14494c8acccf3d66945ed347dd34984f079d11dcd9d97bfe3e6eec1/jupyterlab-3.2.0.tar.gz
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
%setup -q -n jupyterlab-3.2.0
cd %{_builddir}/jupyterlab-3.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1634220267
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
cp %{_builddir}/jupyterlab-3.2.0/LICENSE %{buildroot}/usr/share/package-licenses/jupyterlab/fa62fa6d531b94e755b914b3291c8541ce40f411
cp %{_builddir}/jupyterlab-3.2.0/jupyterlab/static/1036.f2d455e7057498f51450.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/jupyterlab/01ebbe688c25d738b9ee0e2de8113f7351c88e7a
cp %{_builddir}/jupyterlab-3.2.0/jupyterlab/static/3935.e00facce2e55a4af6e62.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/jupyterlab/10645e5e81c59dc0f14b79252005ea68d42f1ba7
cp %{_builddir}/jupyterlab-3.2.0/jupyterlab/static/4008.d04a6dae56794e5c0c01.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/jupyterlab/0656099c1cf5c72718c57eb920abcffa02df0a93
cp %{_builddir}/jupyterlab-3.2.0/jupyterlab/static/7294.46e9d2dfa68082780e97.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/jupyterlab/0036998e52f1b6442c90b9ea6df602bef0294cc5
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
/usr/share/jupyter/lab/static/1033.fc4792a37de5b414eb76.js
/usr/share/jupyter/lab/static/1036.f2d455e7057498f51450.js
/usr/share/jupyter/lab/static/1036.f2d455e7057498f51450.js.LICENSE.txt
/usr/share/jupyter/lab/static/1044.cc317acf830cc023fa71.js
/usr/share/jupyter/lab/static/1057.1a1aee857cdaddbae1d3.js
/usr/share/jupyter/lab/static/1249.39ca2df011ac8354b8d2.js
/usr/share/jupyter/lab/static/126.616fc3d7db93ff9c6147.js
/usr/share/jupyter/lab/static/1281.6c7687aa3b273aeb96c9.js
/usr/share/jupyter/lab/static/1281.6c7687aa3b273aeb96c9.js.LICENSE.txt
/usr/share/jupyter/lab/static/1358.9ab4f57e8227ce75f427.js
/usr/share/jupyter/lab/static/1397.199db33aee6e03236e52.js
/usr/share/jupyter/lab/static/1435.479c2bcb65b99708f8c8.js
/usr/share/jupyter/lab/static/1842.dfe3826e1c2b423f512b.js
/usr/share/jupyter/lab/static/1902.84e773fc133a804e6fdf.js
/usr/share/jupyter/lab/static/1902.84e773fc133a804e6fdf.js.LICENSE.txt
/usr/share/jupyter/lab/static/198.2df510abafd627028024.js
/usr/share/jupyter/lab/static/2249.87250ae90a7024b068bb.js
/usr/share/jupyter/lab/static/2349.72a47e6a9018699e4a68.js
/usr/share/jupyter/lab/static/2353.076b641f97c08caa6313.js
/usr/share/jupyter/lab/static/2356.c9bf98121a496f51eb7e.js
/usr/share/jupyter/lab/static/2440.b1cec08f1bbdf244e2bb.js
/usr/share/jupyter/lab/static/2585.4d374708a4df1d35065d.js
/usr/share/jupyter/lab/static/2719.f0b62700d12f05ae9649.js
/usr/share/jupyter/lab/static/3087.06efd084edba2bea6ea1.js
/usr/share/jupyter/lab/static/3122.054a692dbc69a99ed3ed.js
/usr/share/jupyter/lab/static/3236.4fabf963498daeeb9624.js
/usr/share/jupyter/lab/static/3373.87c4d914a3416b1c5721.js
/usr/share/jupyter/lab/static/3387.11d04d63d2d440a1d5ae.js
/usr/share/jupyter/lab/static/3443.91fa218fa5c07f172458.js
/usr/share/jupyter/lab/static/3496.ecb0e7fcc54191234ae6.js
/usr/share/jupyter/lab/static/3502.f10e0eff0f52839fdfe8.js
/usr/share/jupyter/lab/static/3531.3e64d7e7d4022b90a3fb.js
/usr/share/jupyter/lab/static/3532.8ad8590fcfb05584223d.js
/usr/share/jupyter/lab/static/3664.9ecb606ca1ef93528614.js
/usr/share/jupyter/lab/static/373c04fd2418f5c77eea49d514731058f1907a94ff3b4e5d7c3e5767e8b53d8b.eot
/usr/share/jupyter/lab/static/3791.a4df9987c8514d0fe2aa.js
/usr/share/jupyter/lab/static/3935.e00facce2e55a4af6e62.js
/usr/share/jupyter/lab/static/3935.e00facce2e55a4af6e62.js.LICENSE.txt
/usr/share/jupyter/lab/static/3992.ccdaac9a0ccf19e97b03.js
/usr/share/jupyter/lab/static/3f6d3488cf65374f6f676c315340b0ac2be832bd55240c809448e36ef9b96326.woff
/usr/share/jupyter/lab/static/4008.d04a6dae56794e5c0c01.js
/usr/share/jupyter/lab/static/4008.d04a6dae56794e5c0c01.js.LICENSE.txt
/usr/share/jupyter/lab/static/406.7f8f75bd5a703ead1204.js
/usr/share/jupyter/lab/static/4151.c3dc0e633a876895c62c.js
/usr/share/jupyter/lab/static/4155.784ca1752696680bf373.js
/usr/share/jupyter/lab/static/4402.08c436761ad8a7622036.js
/usr/share/jupyter/lab/static/4429.9d0e9af89b4ab5bf2a29.js
/usr/share/jupyter/lab/static/45.f45f7b326032c86466f3.js
/usr/share/jupyter/lab/static/4570.44c948d7eae0f307f23c.js
/usr/share/jupyter/lab/static/4631.96a143e70f005fef7b59.js
/usr/share/jupyter/lab/static/4894.ed3bc916bbae38aaa626.js
/usr/share/jupyter/lab/static/501.d89ba9dcaa9f1f057bce.js
/usr/share/jupyter/lab/static/5065.49dd76cb64fd444f785f.js
/usr/share/jupyter/lab/static/5223.eaf592e37768e4dfbaab.js
/usr/share/jupyter/lab/static/5289.06e656d778bbaf9d85d1.js
/usr/share/jupyter/lab/static/5383.3274b1ff40ac15dbec20.js
/usr/share/jupyter/lab/static/5505.76d2302be5ddf2097231.js
/usr/share/jupyter/lab/static/5557.e303a957666aec22dae7.js
/usr/share/jupyter/lab/static/5619.014242ae0c63e5eeb6f0.js
/usr/share/jupyter/lab/static/6005.b05660078bb36ac30a33.js
/usr/share/jupyter/lab/static/6218.fb40e9a5fd9375a66441.js
/usr/share/jupyter/lab/static/6504.875dc1ab785a80f3e2b4.js
/usr/share/jupyter/lab/static/6550.401dc12fba6ab1f39a4e.js
/usr/share/jupyter/lab/static/6598.a49a6893ec76ed211968.js
/usr/share/jupyter/lab/static/6700.9bfbe77418dd01d623dd.js
/usr/share/jupyter/lab/static/6777.c2b9b409dcba3da7bc8c.js
/usr/share/jupyter/lab/static/6952.f87181edcb1cb535e471.js
/usr/share/jupyter/lab/static/6962.4836c2781f37e9e2d280.js
/usr/share/jupyter/lab/static/6975.795736b7131db5292d75.js
/usr/share/jupyter/lab/static/6989.be562031a3cede6836ed.js
/usr/share/jupyter/lab/static/7034.58ee0efd8755c3cdd8df.js
/usr/share/jupyter/lab/static/7050.6541a5f5da07ef27c300.js
/usr/share/jupyter/lab/static/7084.8cbd74268350b25b03e6.js
/usr/share/jupyter/lab/static/714.d38baae8faccca175d4b.js
/usr/share/jupyter/lab/static/7289.783c5df35524bd45f11f.js
/usr/share/jupyter/lab/static/7294.46e9d2dfa68082780e97.js
/usr/share/jupyter/lab/static/7294.46e9d2dfa68082780e97.js.LICENSE.txt
/usr/share/jupyter/lab/static/7300.7270d65ce1fae9bd1358.js
/usr/share/jupyter/lab/static/7463.03e0b25a008fae3aae30.js
/usr/share/jupyter/lab/static/7616.d412fb880534d79eb96c.js
/usr/share/jupyter/lab/static/7717.2b27fcb99c344e4b9d40.js
/usr/share/jupyter/lab/static/7730.7e3a9fb140d2d55a51fc.js
/usr/share/jupyter/lab/static/7755.d506a1d9dadf30b1e490.js
/usr/share/jupyter/lab/static/7788.4c184cb541f210c8bc43.js
/usr/share/jupyter/lab/static/7796.859ee194ae317ac438a7.js
/usr/share/jupyter/lab/static/7900.ab5d2266efbf4d05617a.js
/usr/share/jupyter/lab/static/79d088064beb3826054fb88165416235897a856ca952fca1498b1c59b16aaa48.eot
/usr/share/jupyter/lab/static/8012.a9cf2489653884713b4e.js
/usr/share/jupyter/lab/static/8059.517928ce6bb26abfabdb.js
/usr/share/jupyter/lab/static/807.82e58879e543e9b439e0.js
/usr/share/jupyter/lab/static/807.82e58879e543e9b439e0.js.LICENSE.txt
/usr/share/jupyter/lab/static/8086.1dfabaac37d971e2cc4c.js
/usr/share/jupyter/lab/static/8102.efa6f6453160dbef37b9.js
/usr/share/jupyter/lab/static/8173.278d0f34ea05d1505957.js
/usr/share/jupyter/lab/static/8428.aff78782985d5f07cc52.js
/usr/share/jupyter/lab/static/8523.19e282b47887f6ede8ed.js
/usr/share/jupyter/lab/static/8580.c1c50f01a90ab89cf153.js
/usr/share/jupyter/lab/static/8657.57bdea0d16734b128eba.js
/usr/share/jupyter/lab/static/870.2183ee85952d5577c068.js
/usr/share/jupyter/lab/static/8708.3e5f3610a837e4ed3ad9.js
/usr/share/jupyter/lab/static/8819.5d33b8aeb78081088611.js
/usr/share/jupyter/lab/static/8834.1970934133d2b6aea3ab.js
/usr/share/jupyter/lab/static/8843.8ece4c51cb8881166d22.js
/usr/share/jupyter/lab/static/8ea8791754915a898a3100e63e32978a6d1763be6df8e73a39d3a90d691cdeef.woff2
/usr/share/jupyter/lab/static/900.ad826f4cc78f1034e673.js
/usr/share/jupyter/lab/static/901.1506a53425327a39a35b.js
/usr/share/jupyter/lab/static/9039.c83eaf34fc167b58dfe6.js
/usr/share/jupyter/lab/static/9109.6b7c91dcb6d2ca14f22f.js
/usr/share/jupyter/lab/static/911.0c08f040896753efc653.js
/usr/share/jupyter/lab/static/911.0c08f040896753efc653.js.LICENSE.txt
/usr/share/jupyter/lab/static/9316.557136953e766eb6a369.js
/usr/share/jupyter/lab/static/9427.8b24bea4001504fd78a9.js
/usr/share/jupyter/lab/static/9473.f6adb1fcd9ac2f6ab565.js
/usr/share/jupyter/lab/static/9473.f6adb1fcd9ac2f6ab565.js.LICENSE.txt
/usr/share/jupyter/lab/static/96.81ba4375d8fcdfc1b0c9.js
/usr/share/jupyter/lab/static/9674eb1bd5504717903837093a67668ea88f2ed006d91367d0d4b7aa1f9211fc.svg
/usr/share/jupyter/lab/static/9834b82ad26e2a37583d22676a12dd2eb0fe7c80356a2114d0db1aa8b3899537.woff2
/usr/share/jupyter/lab/static/9845.890f96834ee755346181.js
/usr/share/jupyter/lab/static/9866.a88fba53129feac2ca0a.js
/usr/share/jupyter/lab/static/a3b9817780214caf01e8aec20bcdc2305a1ff34a15fae81ecd0923df9cd5cd0a.svg
/usr/share/jupyter/lab/static/af6397503fcefbd613976c21ad5c1e37298c18bbe07d096db03ccd3af6e05ba8.ttf
/usr/share/jupyter/lab/static/be0a084962d8066884f7fe9bd27ec16e51f5a93b72a502c92c5a24dc87eb2ebc.svg
/usr/share/jupyter/lab/static/bootstrap.js
/usr/share/jupyter/lab/static/build_log.json
/usr/share/jupyter/lab/static/cb9e9e693192413cde2b1f21c1dc1d44b6fe7b27cc2b458e8b359d18f9ff8f4e.woff
/usr/share/jupyter/lab/static/cda59d6efffa685830fd95b55f64ae9cb51279cd34b2410b69f84c7ec30157d9.ttf
/usr/share/jupyter/lab/static/e4299464e7b012968eed63ac2db1c9509f56bca409ef9f71f2926a8c3c80b2a9.eot
/usr/share/jupyter/lab/static/e42a88444448ac3d60549cc7c1ff2c8a9cac721034c073d80a14a44e79730cca.woff2
/usr/share/jupyter/lab/static/e8711bbb871afd8e9dea60e16d30f00c7e4837bbc9807065017475b849fa2313.ttf
/usr/share/jupyter/lab/static/f9217f66874b0c01cd8c10b6a295dbc4f609acb6f5adc41c37da46641b57eb02.woff
/usr/share/jupyter/lab/static/index.html
/usr/share/jupyter/lab/static/index.out.js
/usr/share/jupyter/lab/static/jlab_core.55f78d087c08cdbd9752.js
/usr/share/jupyter/lab/static/jlab_core.55f78d087c08cdbd9752.js.LICENSE.txt
/usr/share/jupyter/lab/static/main.e196f10133dff99acd9e.js
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
/usr/share/package-licenses/jupyterlab/0656099c1cf5c72718c57eb920abcffa02df0a93
/usr/share/package-licenses/jupyterlab/10645e5e81c59dc0f14b79252005ea68d42f1ba7
/usr/share/package-licenses/jupyterlab/fa62fa6d531b94e755b914b3291c8541ce40f411

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
