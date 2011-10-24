
%global eclipse_major   3
%global eclipse_minor   7
%global eclipse_majmin  %{eclipse_major}.%{eclipse_minor}
%global eclipse_micro   0
%global initialize      1
%global download_url    http://download.eclipse.org/technology/linuxtools/eclipse-build/3.7.x_Indigo/

# All arches line up between Eclipse and Linux kernel names except i386 -> x86
%ifarch %{ix86}
%global eclipse_arch    x86
%else
%global eclipse_arch   %{_arch}
%endif

# FIXME:  update java packaging guidelines for this.  See
# fedora-devel-java-list discussion in September 2008.
#
# Prevent brp-java-repack-jars from being run.
%define __jar_repack 0

Summary:        An open, extensible IDE
Name:           eclipse
Version:        %{eclipse_majmin}.%{eclipse_micro}
Epoch:		1
Release:        1.3
License:        EPL
Group:          Development/Java
URL:            http://www.eclipse.org/
Source0:        %{download_url}eclipse-build-5791c48513b4207ab1eec1e00bed4b2186f9aad5.tar.xz
Source1:        %{download_url}eclipse-3.7.0-I20110613-1736-src.tar.bz2
# Patch to allow xpcom.cpp to build under latest xulrunner which has removed
# a particular API and a type it depends on so we don't want to compile that
# API
Patch1:         eclipse-xpcom-h.patch

BuildRequires:  ant
BuildRequires:  rsync
BuildRequires:  jpackage-utils >= 0:1.5, make, gcc
BuildRequires:  gtk2-devel
BuildRequires:  glib2-devel
BuildRequires:  libgnome-devel
BuildRequires:  gcc-c++
BuildRequires:  nspr-devel
BuildRequires:  libxtst-devel
BuildRequires:  mesagl-devel
BuildRequires:  mesaglu-devel
BuildRequires:  cairo >= 1.0
BuildRequires:  unzip
BuildRequires:  desktop-file-utils
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  java-javadoc
BuildRequires:  libxt-devel
BuildRequires:  xulrunner-devel 
BuildRequires:  webkitgtk-devel

BuildRequires: icu4j-eclipse >= 0:4.4.2-2
BuildRequires: tomcat5-jasper-eclipse >= 5.5.31-2
BuildRequires: tomcat6-servlet-2.5-api >= 6.0.32-8
BuildRequires: tomcat6-jsp-2.1-api
BuildRequires: ant-antlr ant-apache-bcel ant-apache-log4j ant-apache-oro ant-apache-regexp ant-apache-resolver ant-commons-logging ant-apache-bsf ant-commons-net
BuildRequires: ant-javamail ant-jdepend ant-junit ant-swing ant-jsch ant-testutil ant-apache-xalan2 ant-jmf
BuildRequires: jsch >= 0:0.1.41
BuildRequires: apache-commons-el
BuildRequires: apache-commons-logging
BuildRequires: apache-commons-codec
BuildRequires: jakarta-commons-httpclient
BuildRequires: jetty >= 6.1.24-1
BuildRequires: lucene >= 2.9.4-5
BuildRequires: lucene-contrib >= 2.9.4-5
BuildRequires: junit >= 3.8.1-3jpp
BuildRequires: junit4
BuildRequires: hamcrest >= 0:1.1-9.2
BuildRequires: sat4j >= 2.3.0-1
BuildRequires: objectweb-asm >= 3.3.1-1

%description
The Eclipse platform is designed for building integrated development
environments (IDEs), server-side applications, desktop applications, and
everything in between.

%package     swt
Summary:        SWT Library for GTK+-2.0
Group:          Development/Java
# %{_libdir}/java directory owned by jpackage-utils
Requires:       jpackage-utils
Requires:       gtk2
Requires:       xulrunner 
Requires:       webkitgtk
Conflicts:      mozilla
Provides:       libswt3-gtk2 = %{epoch}:%{version}-%{release}
# The 20 is more than the currently (2008-06-25) latest 3.3.2 package
# but I want to leave some room in case we need to do an F9 update.
Obsoletes:       libswt3-gtk2 < %{epoch}:3.3.2-20

%description swt
SWT Library for GTK+-2.0.

%package        rcp
Summary:        Eclipse Rich Client Platform
Group:          Development/Java
Requires:       %{name}-swt = %{epoch}:%{version}-%{release}
Requires:       icu4j-eclipse >= 0:4.4.2-2
Requires:       java >= 1.6.0

%description    rcp
Eclipse Rich Client Platform

%package        platform
Summary:        Eclipse platform common files
Group:          Development/Java
Requires:   %{name}-rcp = %{version}-%{release}
Requires: ant-antlr ant-apache-bcel ant-apache-log4j ant-apache-oro ant-apache-regexp ant-apache-resolver ant-commons-logging ant-apache-bsf ant-commons-net
Requires: ant-javamail ant-jdepend ant-junit ant-swing ant-jsch ant-testutil ant-apache-xalan2 ant-jmf
Requires: apache-commons-el 
Requires: apache-commons-logging 
Requires: apache-commons-codec
Requires: tomcat5-jasper-eclipse >= 5.5.31-2
Requires: tomcat6-servlet-2.5-api >= 6.0.32-8
Requires: tomcat6-jsp-2.1-api
Requires: jetty >= 6.1.24-1
Requires: jsch >= 0.1.41
Requires: lucene >= 2.9.4-5
Requires: lucene-contrib >= 2.9.4-5
Requires: sat4j >= 2.3.0-1
Provides: eclipse-cvs-client = %{epoch}:%{version}-%{release}
Obsoletes: eclipse-cvs-client < %{epoch}:3.3.2-20

%description    platform
The Eclipse Platform is the base of all IDE plugins.  This does not include the
Java Development Tools or the Plugin Development Environment.

%package        jdt
Summary:        Eclipse Java Development Tools
Group:          Development/Java
Requires:       %{name}-platform = %{epoch}:%{version}-%{release}
Requires:       %{name}-cvs-client = %{epoch}:%{version}-%{release}
Requires:       junit >= 3.8.1-3jpp
Requires:       junit4
Requires:       jakarta-commons-httpclient
Requires:       java-javadoc
Requires:       java-devel

%description    jdt
Eclipse Java Development Tools.  This package is required to use Eclipse for
developing software written in the Java programming language.

%package        pde
Summary:        Eclipse Plugin Development Environment
Group:          Development/Java
Provides:       eclipse = %{epoch}:%{version}-%{release}
Provides:       eclipse-sdk = %{epoch}:%{version}-%{release}
Requires:       %{name}-platform = %{epoch}:%{version}-%{release}
Requires:       %{name}-jdt = %{epoch}:%{version}-%{release}
Requires:       objectweb-asm >= 3.3.1-1
Requires:       hamcrest >= 0:1.1-9.2
# For PDE Build wrapper script + creating jars
Requires:       zip
Requires:       bash
Provides:       %{name}-pde-runtime = %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-pde-runtime < %{epoch}:3.3.2-20

%description    pde
Eclipse Plugin Development Environment.  This package is required for
developing Eclipse plugins.

%prep
%setup -q -n eclipse-build-5791c48513b4207ab1eec1e00bed4b2186f9aad5
cp %{SOURCE1} .
ant -DbuildArch=%{eclipse_arch} applyPatches
pushd build/eclipse-3.7.0-I20110613-1736-src
pushd plugins/org.eclipse.swt
pushd Eclipse\ SWT\ Mozilla/common/library/
%patch1 -p0
popd
popd

# Use our system-installed javadocs, reference only what we built, and
# don't like to osgi.org docs (FIXME:  maybe we should package them?)
sed -i -e "s|http://java.sun.com/j2se/1.4.2/docs/api|%{_datadir}/javadoc/java|" \
   -e "/osgi\.org/d" \
   -e "s|-breakiterator|;../org.eclipse.equinox.util/@dot\n;../org.eclipse.ecf.filetransfer_3.0.0.v20090302-0803.jar\n;../org.eclipse.ecf_3.0.0.v20090302-0803.jar\n-breakiterator|" \
    plugins/org.eclipse.platform.doc.isv/platformOptions.txt
sed -i -e "s|http://java.sun.com/j2se/1.5/docs/api|%{_datadir}/javadoc/java|" \
   -e "s/win32.win32.x86/gtk.linux.%{eclipse_arch}/" \
   plugins/org.eclipse.jdt.doc.isv/jdtOptions.txt
sed -i -e "s|http://java.sun.com/j2se/1.4/docs/api|%{_datadir}/javadoc/java|" \
   -e "s/motif.linux.x86/gtk.linux.%{eclipse_arch}/" \
   plugins/org.eclipse.pde.doc.user/pdeOptions.txt \
   plugins/org.eclipse.pde.doc.user/pdeOptions.txt


# FIXME:  do this as part of eclipse-build
#
# the swt version is set to HEAD on s390x but shouldn't be
# get swt version
#SWT_MAJ_VER=$(grep maj_ver plugins/org.eclipse.swt/Eclipse\ SWT/common/library/make_common.mak | cut -f 2 -d =)
#SWT_MIN_VER=$(grep min_ver plugins/org.eclipse.swt/Eclipse\ SWT/common/library/make_common.mak | cut -f 2 -d =)
#SWT_VERSION=$SWT_MAJ_VER$SWT_MIN_VER
#swt_frag_ver=$(grep v$SWT_VERSION plugins/org.eclipse.swt.gtk.linux.x86/build.xml | sed "s:.*<.*\"\(.*\)\" />:\1:")
#swt_frag_ver_s390x=$(grep "version\.suffix\" value=" plugins/org.eclipse.swt.gtk.linux.s390x/build.xml | sed "s:.*<.*\"\(.*\)\" />:\1:")

# make sure there are no jars left
JARS=""
for j in $(find -name \*.jar); do
  if [ ! -L $j ]; then
    JARS="$JARS `echo $j`"
  fi
done
if [ ! -z "$JARS" ]; then
    echo "These jars should be deleted and symlinked to system jars: $JARS"
   #FIXME: enable  exit 1
fi

popd

%build
export JAVA_HOME=%{java_home}
ant provision.cvs

%install
ant -DdestDir=$RPM_BUILD_ROOT -Dprefix=/usr -Dmultilib=true installSDKinDropins

# We don't need icon.xpm
# https://bugs.eclipse.org/292472
rm $RPM_BUILD_ROOT/%{_libdir}/%{name}/icon.xpm

# Some directories we need
install -d -m 755 $RPM_BUILD_ROOT%{_libdir}/java

pushd $RPM_BUILD_ROOT%{_libdir}/%{name}
# Create file listings for the extracted shared libraries
echo -n "" > %{_builddir}/%{buildsubdir}/%{name}-platform.install;
for id in `ls configuration/org.eclipse.osgi/bundles`; do
  if [ "Xconfiguration" = $(echo X`find configuration/org.eclipse.osgi/bundles/$id -name libswt\*.so` | sed "s:/.*::") ]; then
    echo "%{_libdir}/%{name}/configuration/org.eclipse.osgi/bundles/$id" > %{_builddir}/%{buildsubdir}/%{name}-swt.install;
  else
    echo "%{_libdir}/%{name}/configuration/org.eclipse.osgi/bundles/$id" >> %{_builddir}/%{buildsubdir}/%{name}-platform.install;
  fi
done
popd

# Symlinks to the SWT JNI shared libraries in %%{_libdir}/eclipse
pushd $RPM_BUILD_ROOT%{_libdir}/%{name}
for lib in $(find configuration -name libswt\*.so); do
  ln -s $lib `basename $lib`
done
popd

# Temporary fix until https://bugs.eclipse.org/294877 is resolved
sed -i "s|-Xms40m|-Xms128m|g" $RPM_BUILD_ROOT/%{_sysconfdir}/eclipse.ini
sed -i "s|-Xmx384m|-Xmx512m|g" $RPM_BUILD_ROOT/%{_sysconfdir}/eclipse.ini
echo "-Dorg.eclipse.swt.browser.UseWebKitGTK=true" >> $RPM_BUILD_ROOT/%{_sysconfdir}/eclipse.ini
echo "-XX:CompileCommand=exclude,org/eclipse/core/internal/dtree/DataTreeNode,forwardDeltaWith" >> $RPM_BUILD_ROOT/%{_sysconfdir}/eclipse.ini
echo "-XX:CompileCommand=exclude,org/eclipse/jdt/internal/compiler/lookup/ParameterizedMethodBinding,<init>" >> $RPM_BUILD_ROOT/%{_sysconfdir}/eclipse.ini
echo "-XX:CompileCommand=exclude,org/eclipse/cdt/internal/core/dom/parser/cpp/semantics/CPPTemplates,instantiateTemplate" >> $RPM_BUILD_ROOT/%{_sysconfdir}/eclipse.ini
echo "-XX:CompileCommand=exclude,org/eclipse/cdt/internal/core/pdom/dom/cpp/PDOMCPPLinkage,addBinding" >> $RPM_BUILD_ROOT/%{_sysconfdir}/eclipse.ini
echo "-XX:CompileCommand=exclude,org/python/pydev/editor/codecompletion/revisited/PythonPathHelper,isValidSourceFile" >> $RPM_BUILD_ROOT/%{_sysconfdir}/eclipse.ini
echo "-XX:CompileCommand=exclude,org/python/pydev/ui/filetypes/FileTypesPreferencesPage,getDottedValidSourceFiles" >> $RPM_BUILD_ROOT/%{_sysconfdir}/eclipse.ini

# SWT JAR symlink in libdir
pushd $RPM_BUILD_ROOT%{_libdir}/%{name}
ln -s ../%{name}/swt.jar ../java/swt.jar
popd

# A sanity check.
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

# Create a script that can be used to make a symlink tree of the
# eclipse platform.
cp -p pdebuild/eclipse-copy-platform.sh copy-platform
(
  cd $RPM_BUILD_ROOT%{_libdir}/%{name}
  ls -d * | grep -E -v '^(plugins|features|about_files|dropins)$'
  ls -d plugins/* features/*
) |
sed -e's,^\(.*\),[ ! -e \1 ] \&\& ln -s $eclipse/\1 \1,' >> copy-platform
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}/buildscripts
mv copy-platform $RPM_BUILD_ROOT%{_libdir}/%{name}/buildscripts
copyPlatform=$RPM_BUILD_ROOT%{_libdir}/%{name}/buildscripts/copy-platform

# This symlink is actually provided by the icu4j-eclipse package
# We need to remove this *after* copy-platform creation otherwise
# copy-platform gets generated wrong.
rm $RPM_BUILD_ROOT/%{_libdir}/%{name}/plugins/com.ibm.icu_*.jar

pushd $RPM_BUILD_ROOT%{_libdir}/%{name}
for p in $(ls -d dropins/jdt/plugins/*); do
    plugin=$(basename $p)
    echo $p | sed -e"s,^\(.*\),[ ! -e plugins/$plugin ] \&\& ln -s \$eclipse/\1 plugins/$plugin," >> $copyPlatform
done
for p in $(ls -d dropins/sdk/plugins/*); do
    plugin=$(basename $p)
    echo $p | sed -e"s,^\(.*\),[ ! -e plugins/$plugin ] \&\& ln -s \$eclipse/\1 plugins/$plugin," >> $copyPlatform
done
popd

# Install the PDE Build wrapper script.
install -p -D -m0755 pdebuild/eclipse-pdebuild.sh \
  $RPM_BUILD_ROOT%{_libdir}/%{name}/buildscripts/pdebuild
PDEBUILDVERSION=$(ls $RPM_BUILD_ROOT%{_libdir}/%{name}/dropins/sdk/plugins \
  | grep org.eclipse.pde.build_ | \
  sed 's/org.eclipse.pde.build_//')
sed -i "s/@PDEBUILDVERSION@/$PDEBUILDVERSION/g" \
  $RPM_BUILD_ROOT%{_libdir}/%{name}/buildscripts/pdebuild

%post platform
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache -q %{_datadir}/icons/hicolor
fi

%postun platform
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache -q %{_datadir}/icons/hicolor
fi

%if %{initialize}
%files swt -f %{name}-swt.install
%else
%files swt
%endif
%defattr(-,root,root)
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%if %{initialize}
%dir %{_libdir}/%{name}/libswt-*.so
%dir %{_libdir}/%{name}/configuration
%dir %{_libdir}/%{name}/configuration/org.eclipse.osgi
%dir %{_libdir}/%{name}/configuration/org.eclipse.osgi/bundles
%endif
%{_libdir}/%{name}/notice.html
%{_libdir}/%{name}/epl-v10.html
%{_libdir}/%{name}/plugins/org.eclipse.swt_*
%{_libdir}/%{name}/plugins/org.eclipse.swt.gtk.linux.%{eclipse_arch}_*
%{_libdir}/%{name}/swt-gtk*.jar
%{_libdir}/%{name}/swt.jar
%{_libdir}/java/swt.jar

%files rcp
%defattr(-,root,root)
%dir %{_libdir}/%{name}/features
%dir %{_datadir}/%{name}
%if %{initialize}
%{_libdir}/%{name}/configuration/org.eclipse.osgi/.bundledata*
%{_libdir}/%{name}/configuration/org.eclipse.osgi/.lazy*
%{_libdir}/%{name}/configuration/org.eclipse.osgi/.manager
%{_libdir}/%{name}/configuration/org.eclipse.osgi/.state*
%endif
%dir %{_libdir}/%{name}/configuration
%config %{_libdir}/%{name}/configuration/config.ini
%config %{_libdir}/%{name}/configuration/org.eclipse.equinox.simpleconfigurator/bundles.info
%dir %{_libdir}/%{name}/configuration/org.eclipse.equinox.simpleconfigurator
%ifnarch ppc ppc64
%{_libdir}/%{name}/about.html
%endif
%ifarch x86_64
%{_libdir}/%{name}/about_files
%endif
%{_libdir}/%{name}/readme
%{_libdir}/%{name}/features/org.eclipse.rcp_*
%{_libdir}/%{name}/plugins/org.eclipse.core.commands_*
%{_libdir}/%{name}/plugins/org.eclipse.core.contenttype_*
%{_libdir}/%{name}/plugins/org.eclipse.core.databinding_*
%{_libdir}/%{name}/plugins/org.eclipse.core.databinding.beans_*
%{_libdir}/%{name}/plugins/org.eclipse.core.databinding.observable_*
%{_libdir}/%{name}/plugins/org.eclipse.core.databinding.property_*
%{_libdir}/%{name}/plugins/org.eclipse.core.expressions_*
%{_libdir}/%{name}/plugins/org.eclipse.core.jobs_*
%{_libdir}/%{name}/plugins/org.eclipse.core.runtime_*
%{_libdir}/%{name}/plugins/org.eclipse.core.runtime.compatibility.auth_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.app_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.common_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.launcher_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.launcher.gtk.linux.%{eclipse_arch}_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.preferences_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.registry_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.util_*
%{_libdir}/%{name}/plugins/org.eclipse.help_*
%{_libdir}/%{name}/plugins/org.eclipse.jface_*
%{_libdir}/%{name}/plugins/org.eclipse.jface.databinding_*
%{_libdir}/%{name}/plugins/org.eclipse.osgi_*
%{_libdir}/%{name}/plugins/org.eclipse.rcp_*
%{_libdir}/%{name}/plugins/org.eclipse.ui_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.workbench_*
%{_libdir}/%{name}/plugins/org.eclipse.update.configurator_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.simpleconfigurator_*

%if %{initialize}
%files platform -f %{name}-platform.install
%else
%files platform
%endif
%defattr(-,root,root)
%attr(0755,root,root) %{_bindir}/%{name}
%{_libdir}/%{name}/.eclipseproduct
%config %{_libdir}/%{name}/eclipse.ini
%config %{_sysconfdir}/eclipse.ini
%ifnarch ppc ppc64
%{_libdir}/%{name}/about_files
%endif
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/icons/*/*/apps/*
%{_libdir}/%{name}/eclipse
%dir %{_libdir}/%{name}/dropins
%dir %{_datadir}/%{name}/dropins
%{_libdir}/%{name}/features/org.eclipse.platform_*
%{_libdir}/%{name}/plugins/com.jcraft.jsch_*
%{_libdir}/%{name}/plugins/javax.servlet_*
%{_libdir}/%{name}/plugins/javax.servlet.jsp_*
%{_libdir}/%{name}/plugins/org.apache.ant_*
%{_libdir}/%{name}/plugins/org.apache.commons.el_*
%{_libdir}/%{name}/plugins/org.apache.commons.logging_*
%{_libdir}/%{name}/plugins/org.apache.lucene_*
%{_libdir}/%{name}/plugins/org.apache.lucene.core_*
%{_libdir}/%{name}/plugins/org.apache.lucene.analysis_*
%{_libdir}/%{name}/plugins/org.eclipse.ant.core_*
%{_libdir}/%{name}/plugins/org.eclipse.compare_*
%{_libdir}/%{name}/plugins/org.eclipse.compare.core_*
%{_libdir}/%{name}/plugins/org.eclipse.core.boot_*
%{_libdir}/%{name}/plugins/org.eclipse.core.externaltools_*
%{_libdir}/%{name}/plugins/org.eclipse.core.filebuffers_*
%{_libdir}/%{name}/plugins/org.eclipse.core.filesystem_*
%{_libdir}/%{name}/plugins/org.eclipse.core.filesystem.linux.%{eclipse_arch}_*
%{_libdir}/%{name}/plugins/org.eclipse.core.net_*
%{_libdir}/%{name}/plugins/org.eclipse.core.net.linux.*
%ifarch %{ix86}
%{_libdir}/%{name}/plugins/org.eclipse.update.core.linux_*
%endif
%{_libdir}/%{name}/plugins/org.eclipse.core.resources_*
%{_libdir}/%{name}/plugins/org.eclipse.core.runtime.compatibility_*
%{_libdir}/%{name}/plugins/org.eclipse.core.runtime.compatibility.registry_*
%{_libdir}/%{name}/plugins/org.eclipse.core.variables_*
%{_libdir}/%{name}/plugins/org.eclipse.debug.core_*
%{_libdir}/%{name}/plugins/org.eclipse.debug.ui_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.ds_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.event_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.http.jetty_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.http.registry_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.http.servlet_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.jsp.jasper_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.jsp.jasper.registry_*
%{_libdir}/%{name}/plugins/org.eclipse.help.appserver_*
%{_libdir}/%{name}/plugins/org.eclipse.help.base_*
%{_libdir}/%{name}/plugins/org.eclipse.help.ui_*
%{_libdir}/%{name}/plugins/org.eclipse.help.webapp_*
%{_libdir}/%{name}/plugins/org.eclipse.jface.text_*
%{_libdir}/%{name}/plugins/org.eclipse.jsch.core_*
%{_libdir}/%{name}/plugins/org.eclipse.jsch.ui_*
%{_libdir}/%{name}/plugins/org.eclipse.ltk.core.refactoring_*
%{_libdir}/%{name}/plugins/org.eclipse.ltk.ui.refactoring_*
%{_libdir}/%{name}/plugins/org.eclipse.osgi.services_*
%{_libdir}/%{name}/plugins/org.eclipse.osgi.util_*
%{_libdir}/%{name}/plugins/org.eclipse.platform_*
%{_libdir}/%{name}/plugins/org.eclipse.platform.doc.user_*
%{_libdir}/%{name}/plugins/org.eclipse.search_*
%{_libdir}/%{name}/plugins/org.eclipse.team.core_*
%{_libdir}/%{name}/plugins/org.eclipse.team.ui_*
%{_libdir}/%{name}/plugins/org.eclipse.text_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.browser_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.cheatsheets_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.console_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.editors_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.externaltools_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.forms_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.ide_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.ide.application_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.intro_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.intro.universal_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.navigator_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.navigator.resources_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.net_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.presentations.r21_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.views_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.views.properties.tabbed_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.workbench.compatibility_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.workbench.texteditor_*
%{_libdir}/%{name}/plugins/org.eclipse.update.core_*
%{_libdir}/%{name}/plugins/org.eclipse.update.scheduler_*
%{_libdir}/%{name}/plugins/org.eclipse.update.ui_*
%{_libdir}/%{name}/plugins/org.mortbay.jetty.util_*
%{_libdir}/%{name}/plugins/org.mortbay.jetty.server_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.initializer_*
%{_libdir}/%{name}/plugins/org.eclipse.team.cvs.core_*
%{_libdir}/%{name}/plugins/org.eclipse.cvs_*
%{_libdir}/%{name}/plugins/org.eclipse.team.cvs.ssh2_*
%{_libdir}/%{name}/plugins/org.eclipse.team.cvs.ui_*
%{_libdir}/%{name}/features/org.eclipse.cvs_*
%{_libdir}/%{name}/features/org.eclipse.help_*
%{_libdir}/%{name}/plugins/org.apache.jasper_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.frameworkadmin_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.frameworkadmin.equinox_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.simpleconfigurator.manipulator_*
%{_libdir}/%{name}/features/org.eclipse.equinox.p2.core.feature_*
%{_libdir}/%{name}/features/org.eclipse.equinox.p2.extras.feature_*
%{_libdir}/%{name}/features/org.eclipse.equinox.p2.rcp.feature_*
%{_libdir}/%{name}/features/org.eclipse.equinox.p2.user.ui_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.director_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.core_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.engine_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.jarprocessor_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.metadata_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.metadata.repository_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.artifact.repository_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.touchpoint.eclipse_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.touchpoint.natives_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.console_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.ql_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.operations_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.transport.ecf_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.ui_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.ui.importexport_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.ui.sdk_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.ui.sdk.scheduler_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.updatechecker_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.garbagecollector_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.directorywatcher_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.publisher_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.publisher.eclipse_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.repository_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.repository.tools_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.reconciler.dropins_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.updatesite_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.security_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.security.ui_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.extensionlocation_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.director.app_*
%{_libdir}/%{name}/plugins/org.eclipse.ecf.provider.filetransfer_*
%{_libdir}/%{name}/plugins/org.eclipse.ecf.provider.filetransfer.httpclient_*
%{_libdir}/%{name}/plugins/org.eclipse.ecf.provider.filetransfer.httpclient.ssl_*
%{_libdir}/%{name}/plugins/org.eclipse.ecf.provider.filetransfer.ssl_*
%{_libdir}/%{name}/plugins/org.eclipse.ecf.ssl_*
%{_libdir}/%{name}/plugins/org.eclipse.ecf_*
%{_libdir}/%{name}/plugins/org.eclipse.ecf.filetransfer_*
%{_libdir}/%{name}/plugins/org.eclipse.ecf.identity_*
%{_libdir}/%{name}/plugins/org.apache.commons.codec_*
%{_libdir}/%{name}/plugins/org.apache.commons.httpclient_*
%{_libdir}/%{name}/plugins/org.sat4j.core_*
%{_libdir}/%{name}/plugins/org.sat4j.pb_*
# Put this in -platform since we're putting the p2 stuff here
%{_libdir}/%{name}/artifacts.xml
# FIXME: should we ship content.xml for the platform?
#%{_libdir}/%{name}/metadata
%{_libdir}/%{name}/p2

%files jdt
%defattr(-,root,root)
%{_bindir}/efj
%{_libdir}/%{name}/dropins/jdt

%files pde
%defattr(-,root,root)
%{_libdir}/%{name}/buildscripts
%{_libdir}/%{name}/dropins/sdk

