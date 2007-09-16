Epoch:  1

%ifarch %{ix86} x86_64
%define gcj_support     1
%else
%define gcj_support     1
%endif
%define tomcatepoch     0
%define tomcatversion   5.5.23
%define tomcatsharedir  %{_datadir}/tomcat5
%define tomcatlibdir    %{_var}/lib/tomcat5
%define firefox_version %(rpm -q mozilla-firefox --queryformat %{VERSION} 2>/dev/null)
%define firefox_dir     %(firefox-config --defines 2>/dev/null | sed -n -e 's,.*MOZ_DEFAULT_MOZILLA_FIVE_HOME=\\"\\([^\\"]*\\)\\"\\(.*\\),\\1,p')
%define section         free
%define eclipse_major   3
%define eclipse_minor   3
%define eclipse_majmin  %{eclipse_major}.%{eclipse_minor}
%define eclipse_micro   0
%define libname         libswt3

# All archs line up between Eclipse and Linux kernel names except i386 -> x86
%ifarch %{ix86}
%define eclipse_arch    x86
%else
%define eclipse_arch   %{_arch}
%endif

Summary:        An open, extensible IDE
Name:           eclipse
Version:        %{eclipse_majmin}.%{eclipse_micro}
Release:        %mkrel 0.18.3
License:        Eclipse Public License
Group:          Development/Java
URL:            http://www.eclipse.org/
Source0:        ftp://ftp.cse.buffalo.edu/pub/Eclipse/eclipse/downloads/drops/R-3.3-200706251500/eclipse-sourceBuild-srcIncluded-3.3.zip
Source1:        %{name}.script
Source2:        %{name}.desktop
Source3:        eclipse.in
Source4:        org.fedoraproject.ide.platform-3.3.0.2.zip
Source6:        %{name}.conf
Source16:       %{name}-copy-platform.sh
Source17:       efj.sh.in
Source18:       ecj.sh.in
# This file contains the types of files we'd like to extract from the jars
# when using the FileInitializer
Source19:       %{name}-filenamepatterns.txt
# cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/eclipse co equinox-incubator/org.eclipse.equinox.initializer
# tar cjf eclipse-fileinitializerapp.tar.bz2 equinox-incubator/
# (generated 2006-11-01 18:48 UTC)
Source20:       %{name}-fileinitializerapp.tar.bz2

# This needs to go upstream
Patch3:         %{name}-libupdatebuild2.patch
# Build swttools.jar
# https://bugs.eclipse.org/bugs/show_bug.cgi?id=90364
Patch4:         %{name}-swttools.patch
# This does two things:
# 1. allows the launcher to be in /usr/bin and
# 2. ensures that the OSGi configuration directory
#    (which contains the JNI .sos) is in %{_libdir}
# We should investigate whether or not this can go upstream
Patch12:        %{name}-launcher-set-install-dir-and-shared-config.patch
# Always generate debug info when building RPMs (Andrew Haley)
# This needs to be investigated for getEnv changes
Patch14:        %{name}-ecj-rpmdebuginfo.patch
# generic releng plugins that can be used to build plugins
# see this thread for details: 
# https://www.redhat.com/archives/fedora-devel-java-list/2006-April/msg00048.html
Patch15:        %{name}-pde.build-add-package-build.patch
# This tomcat stuff will change when they move to the equinox jetty provider
# https://bugs.eclipse.org/bugs/show_bug.cgi?id=98371
Patch6:         %{name}-tomcat55.patch
Patch7:         %{name}-tomcat55-build.patch
# Use ecj for gcj
Patch17:        %{name}-ecj-gcj.patch
Patch24:        %{name}-add-ppc64-sparc64-s390-s390x.patch
#https://bugs.eclipse.org/bugs/show_bug.cgi?id=198840
Patch25:       %{name}-launcher-double-free-bug.patch
#FIXME: file a bug upstream
Patch26:        %{name}-launcher-fix-java-home.patch
Patch100:       %{name}-libswt-model.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  ant
BuildRequires:  jpackage-utils >= 0:1.5, make, gcc
BuildRequires:  gnome-vfs2-devel
BuildRequires:  gtk2-devel
BuildRequires:  glib2-devel
BuildRequires:  libgnome2-devel
BuildRequires:  libgnomeui2-devel
BuildRequires:  gcc-c++
BuildRequires:  mozilla-firefox
BuildRequires:  mozilla-firefox-devel
BuildRequires:  nspr-devel
BuildRequires:  libxtst-devel
BuildRequires:  mesagl-devel
BuildRequires:  mesaglu-devel
BuildRequires:  cairo-devel >= 0:1.0
BuildRequires:  unzip
BuildRequires:  icu4j-eclipse >= 0:3.6.1
BuildRequires:  desktop-file-utils
%if %{gcj_support}
BuildRequires:  java-1.5.0-gcj-javadoc
BuildRequires:  java-gcj-compat-devel >= 0:1.0.64
%else
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  java-javadoc >= 1.6.0
BuildRequires:  libxt-devel
%endif

# https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=180642
BuildRequires: ant-antlr ant-apache-bcel ant-apache-log4j ant-apache-oro ant-apache-regexp ant-apache-resolver ant-commons-logging
BuildRequires: ant-apache-bsf ant-commons-net ant-jmf
BuildRequires: ant-javamail ant-jdepend ant-junit ant-nodeps ant-swing ant-trax ant-jsch
BuildRequires: jsch >= 0:0.1.31
BuildRequires: jakarta-commons-beanutils jakarta-commons-collections jakarta-commons-digester jakarta-commons-dbcp jakarta-commons-el jakarta-commons-fileupload jakarta-commons-launcher jakarta-commons-logging jakarta-commons-modeler jakarta-commons-pool
BuildRequires: mx4j >= 0:2.1
BuildRequires: tomcat5 >= %{tomcatepoch}:%{tomcatversion}
BuildRequires: tomcat5-jasper >= %{tomcatepoch}:%{tomcatversion}
BuildRequires: jsp
BuildRequires: tomcat5-servlet-2.4-api >= %{tomcatepoch}:%{tomcatversion}
BuildRequires: lucene
BuildRequires: lucene-demo
BuildRequires: lucene-contrib
BuildRequires: regexp 
BuildRequires: junit
BuildRequires: junit4
BuildRequires: jetty5

%description
The Eclipse Platform is designed for building integrated development
environments (IDEs) that can be used to create applications as diverse
as web sites, embedded Java(tm) programs, C++ programs, and Enterprise
JavaBeans(tm).

%package        ecj
Summary:        Eclipse Compiler for Java
Group:          Development/Java
Obsoletes:      ecj < 3.2.0
Provides:       ecj = %{epoch}:%{version}-%{release}
%if %{gcj_support}
%else
Requires:       java >= 1.6.0
%endif

%description    ecj
Eclipse compiler for Java.

%package     -n %{libname}-gtk2
Summary:        SWT Library for GTK+-2.0
Group:          Development/Java
Requires:       %mklibname mozilla-firefox %{firefox_version}

%description -n %{libname}-gtk2
SWT Library for GTK+-2.0.

%package        rcp
Summary:        Eclipse Rich Client Platform
Group:          Development/Java
Requires:       %{libname}-gtk2 = %{epoch}:%{version}-%{release}
# This file-level requirement is for the bi-arch multilib case
%if 0
Requires: %{_libdir}/%{name}/plugins/org.eclipse.swt.gtk.linux.%{eclipse_arch}_3.3.0.v3346.jar
%endif
Requires(post):     %{libname}-gtk2 = %{epoch}:%{version}-%{release}
Requires(postun):   %{libname}-gtk2 = %{epoch}:%{version}-%{release}
%if %{gcj_support}
%else
Requires:       java >= 1.6.0
%endif

%description    rcp
Eclipse Rich Client Platform

%package        cvs-client
Summary:        Eclipse CVS Client
Group:          Development/Java
Requires:       %{name}-rcp = %{epoch}:%{version}-%{release}
Requires(post):    %{name}-rcp = %{epoch}:%{version}-%{release}
Requires(postun):  %{name}-rcp = %{epoch}:%{version}-%{release}
%if %{gcj_support}
%else
Requires:       java >= 1.6.0
%endif

%description    cvs-client
Eclipse CVS Client

%package        platform
Summary:        Eclipse platform common files
Group:          Development/Java
Obsoletes:      %{name}-ui %{name}-gtk2 %{name}-scripts eclipse
Provides:       %{name}-ui = %{epoch}:%{version}-%{release}
Provides:       %{name}-scripts = %{epoch}:%{version}-%{release}
Provides:       %{name}-gtk2 = %{epoch}:%{version}-%{release}
Requires:       java >= 1.6.0
Requires:       %{name}-rcp = %{epoch}:%{version}-%{release}
Requires(post):   %{name}-rcp = %{epoch}:%{version}-%{release}
Requires(postun): %{name}-rcp = %{epoch}:%{version}-%{release}
Requires: %{libname}-gtk2 = %{epoch}:%{version}-%{release}
Requires: %mklibname mozilla-firefox %{firefox_version}
Requires: ant-antlr ant-apache-bcel ant-apache-log4j ant-apache-oro ant-apache-regexp ant-apache-resolver ant-commons-logging
Requires: ant-apache-bsf ant-commons-net ant-jmf
Requires: ant-javamail ant-jdepend ant-junit ant-nodeps ant-swing ant-trax ant-jsch
Requires: jakarta-commons-beanutils jakarta-commons-collections jakarta-commons-digester jakarta-commons-dbcp jakarta-commons-el jakarta-commons-fileupload jakarta-commons-launcher jakarta-commons-logging jakarta-commons-modeler jakarta-commons-pool
Requires: mx4j >= 0:2.1
Requires: tomcat5 >= %{tomcatepoch}:%{tomcatversion}
Requires: tomcat5-jasper >= %{tomcatepoch}:%{tomcatversion}
Requires: jsp
Requires: tomcat5-servlet-2.4-api >= %{tomcatepoch}:%{tomcatversion}
Requires: jetty5
Requires: jsch >= 0:0.1.31
Requires: lucene >= 0:1.9.1
Requires: lucene-contrib >= 0:1.9.1
Requires: lucene-demo
Requires: regexp
Requires: junit
Requires: junit4
Requires: icu4j-eclipse
# (walluck) Fedora forgets to include these
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Requires: eclipse-cvs-client
Requires: eclipse-subclipse
Requires: eclipse-changelog
Requires: eclipse-rpm-editor
# no xmlrpc3 -> no mylyn on ppc64 due to:
# https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=239123
%ifnarch ppc64 alpha
Requires: eclipse-mylyn
Requires: eclipse-mylyn-ide
Requires: eclipse-mylyn-bugzilla
Requires: eclipse-mylyn-trac
%endif

%description    platform
The Eclipse Platform is the base of all IDE plugins.  This does not include the
Java Development Tools or the Plugin Development Environment.

%package        jdt
Summary:        Eclipse Java Development Tools
Group:          Development/Java
Provides:       eclipse = %{epoch}:%{version}-%{release}
Requires:       %{name}-platform = %{epoch}:%{version}-%{release}
Requires:       %{name}-cvs-client = %{epoch}:%{version}-%{release}
Requires:       %{name}-ecj = %{epoch}:%{version}-%{release}
Requires(post):    %{name}-platform = %{epoch}:%{version}-%{release}
Requires(postun):  %{name}-platform = %{epoch}:%{version}-%{release}
Requires(post):    %{name}-ecj = %{epoch}:%{version}-%{release}
Requires(postun):  %{name}-ecj = %{epoch}:%{version}-%{release}
Requires:       junit
Requires:       junit4

%if %{gcj_support}
Requires:       java-1.5.0-gcj-javadoc
%else
Requires:       java-javadoc >= 1.6.0
%endif
# no xmlrpc3 -> no mylyn on ppc64 due to:
# https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=239123
%ifnarch ppc64 alpha
Requires:       eclipse-mylyn-java
%endif

%description    jdt
Eclipse Java Development Tools.  This package is required to use Eclipse for
developing software written in the Java programming language.

%package        pde
Summary:        Eclipse Plugin Development Environment
Group:          Development/Java
Provides:      eclipse-sdk
# Can remove for mdv2008.1
Obsoletes:     eclipse-sdk < 1:3.3.0-0.9.1
Provides:       eclipse-pde-sdk
Obsoletes:      eclipse-pde-sdk 1:3.3.0-0.9.1
Provides:       eclipse-cvs-client-sdk
Obsoletes:      eclipse-cvs-client-sdk < 1:3.3.0-0.9.1
Provides:       eclipse-jdt-sdk
Obsoletes:      eclipse-jdt-sdk < 1:3.3.0-0.9.1
Provides:       eclipse-pde-sdk
Obsoletes:      eclipse-pde-sdk < 1:3.3.0-0.9.1
Provides:       eclipse-platform-sdk
Obsoletes:      eclipse-platform-sdk < 1:3.3.0-0.9.1
Provides:       eclipse-rcp-sdk
Obsoletes:      eclipse-rcp-sdk < 1:3.3.0-0.9.1
# end remove for mdv2008.1
Requires:       %{name}-platform = %{epoch}:%{version}-%{release}
Requires:       %{name}-jdt = %{epoch}:%{version}-%{release}
Requires:       %{name}-pde-runtime = %{epoch}:%{version}-%{release}
# no xmlrpc3 -> no mylyn on ppc64 due to:
# https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=239123
%ifnarch ppc64 alpha
Requires:       eclipse-mylyn-pde
%endif
Requires(post):    %{name}-platform = %{epoch}:%{version}-%{release}
Requires(postun):  %{name}-platform = %{epoch}:%{version}-%{release}
Requires(post):    %{name}-jdt = %{epoch}:%{version}-%{release}
Requires(postun):  %{name}-jdt = %{epoch}:%{version}-%{release}
Requires(post):    %{name}-pde-runtime = %{epoch}:%{version}-%{release}
Requires(postun):  %{name}-pde-runtime = %{epoch}:%{version}-%{release}
Requires(post):    %{name}-platform-sdk = %{epoch}:%{version}-%{release}
Requires(postun):  %{name}-platform-sdk = %{epoch}:%{version}-%{release}

%description    pde
Eclipse Plugin Development Environment.  This package is required for
developing Eclipse plugins.

%package        pde-runtime
Summary:        Eclipse Plugin Development Environment runtime plugin
Group:          Development/Java
Requires:       %{name}-jdt = %{epoch}:%{version}-%{release}
Requires:       %{name}-platform = %{epoch}:%{version}-%{release}
Requires(post):    %{name}-platform = %{epoch}:%{version}-%{release}
Requires(postun):  %{name}-platform = %{epoch}:%{version}-%{release}

%description    pde-runtime
Eclipse Plug-in Development Environment runtime plugin
(org.eclipse.pde.runtime).

%prep
%setup -q -c

# (walluck) try not forking the Jasper compiler
%{__sed} --in-place 's/fork="true"/fork="false"/' plugins/org.eclipse.help.webapp/buildJSPs.xml
sed --in-place "s/java5.home/java.home/" build.xml
%patch3 -p0
# FIXME:  investigate why we are pushd'ing here
# Build swttools.jar
pushd plugins/org.eclipse.swt.gtk.linux.x86_64
%patch4 -p0
popd

# tomcat patches
pushd plugins/org.eclipse.tomcat
%patch6 -p0
%patch7 -p0
popd
sed --in-place "s/4.1.130/%{tomcatversion}/g"           \
                features/org.eclipse.platform/build.xml \
                plugins/org.eclipse.tomcat/build.xml    \
                plugins/org.eclipse.tomcat/META-INF/MANIFEST.MF   \
                assemble.*.xml

pushd plugins/org.eclipse.jdt.core
%patch17 -p0
popd

# liblocalfile fixes
sed --in-place "s/JAVA_HOME =/#JAVA_HOME =/" plugins/org.eclipse.core.filesystem/natives/unix/linux/Makefile
sed --in-place "s/OPT_FLAGS=-O/OPT_FLAGS=-O2 -g/" plugins/org.eclipse.core.filesystem/natives/unix/linux/Makefile

# launcher patches
rm plugins/org.eclipse.platform/launchersrc.zip
pushd features/org.eclipse.equinox.executable
%patch12 -p0
%patch25 -p0
%patch26 -p0
# put the configuration directory in an arch-specific location
sed --in-place "s:/usr/lib/eclipse/configuration:%{_libdir}/%{name}/configuration:" library/eclipse.c
# make the eclipse binary relocatable
sed --in-place "s:/usr/share/eclipse:%{_datadir}/%{name}:" library/eclipse.c
# (walluck) fix JAVA_HOME
sed --in-place 's:^javaHome=""$:javaHome="%{java_home}":' library/gtk/build.sh
zip -q -9 -r ../../plugins/org.eclipse.platform/launchersrc.zip library
popd

# (walluck) Fedora has a bug here wrt the macros being used
# use our system-installed javadocs
sed --in-place "s|http://java.sun.com/j2se/1.4.2/docs/api|%{_javadocdir}/java|" \
   plugins/org.eclipse.platform.doc.isv/platformOptions.txt
sed --in-place "s|http://java.sun.com/j2se/1.5/docs/api|%{_javadocdir}/java|" \
   plugins/org.eclipse.jdt.doc.isv/jdtaptOptions.txt                     \
   plugins/org.eclipse.jdt.doc.isv/jdtOptions.txt
sed --in-place "s|http://java.sun.com/j2se/1.4/docs/api|%{_javadocdir}/java|" \
   plugins/org.eclipse.pde.doc.user/pdeOptions.txt                       \
   plugins/org.eclipse.pde.doc.user/pdeOptions

%patch14 -p0

pushd plugins/org.eclipse.pde.build
%patch15
sed --in-place "s:/usr/share/eclipse:%{_datadir}/%{name}:" templates/package-build/build.properties
popd

# FIXME this should be patched upstream with a flag to turn on and off 
# all output should be directed to stdout
# https://bugs.eclipse.org/bugs/show_bug.cgi?id=144942
find -type f -name \*.xml -exec sed --in-place -r "s/output=\".*(txt|log).*\"//g" "{}" \;

# Remove existing .sos and binary launcher
find -name \*.so | xargs rm
find features/org.eclipse.equinox.executable -type f -name eclipse | xargs rm

# Symlinks

## BEGIN ANT ##
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-antlr.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-apache-bcel.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-apache-bsf.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-apache-log4j.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-apache-oro.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-apache-regexp.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-apache-resolver.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-commons-logging.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-commons-net.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-jai.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-javamail.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-jdepend.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-jmf.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-jsch.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-junit.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-launcher.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-netrexx.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-nodeps.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-starteam.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-stylebook.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-swing.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-trax.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-weblogic.jar
# FIXME:  use build-jar-repository
# (walluck) Unlike Fedora, Mandriva ships both ant-bsf and
# (walluck) ant-commons-net, as well as ant-jmf
ln -s %{_javadir}/ant/ant-antlr.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-antlr.jar
ln -s %{_javadir}/ant/ant-apache-bcel.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-apache-bcel.jar
ln -s %{_javadir}/ant/ant-apache-bsf.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-apache-bsf.jar
ln -s %{_javadir}/ant/ant-apache-log4j.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-apache-log4j.jar
ln -s %{_javadir}/ant/ant-apache-oro.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-apache-oro.jar
ln -s %{_javadir}/ant/ant-apache-regexp.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-apache-regexp.jar
ln -s %{_javadir}/ant/ant-apache-resolver.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-apache-resolver.jar
ln -s %{_javadir}/ant/ant-commons-logging.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-commons-logging.jar
# https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=180642
# the symlinks that are commented-out are not currently shipped on Fedora
ln -s %{_javadir}/ant/ant-commons-net.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-commons-net.jar
#ln -s %{_javadir}/ant/ant-jai.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-jai.jar
ln -s %{_javadir}/ant.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant.jar
ln -s %{_javadir}/ant/ant-javamail.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-javamail.jar
ln -s %{_javadir}/ant/ant-jdepend.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-jdepend.jar
ln -s %{_javadir}/ant/ant-jmf.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-jmf.jar
ln -s %{_javadir}/ant/ant-jsch.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-jsch.jar
ln -s %{_javadir}/ant/ant-junit.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-junit.jar
ln -s %{_javadir}/ant-launcher.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-launcher.jar
#ln -s %{_javadir}/ant/ant-netrexx.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-netrexx.jar
ln -s %{_javadir}/ant/ant-nodeps.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-nodeps.jar
#ln -s %{_javadir}/ant/ant-starteam.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-starteam.jar
#ln -s %{_javadir}/ant/ant-stylebook.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-stylebook.jar
ln -s %{_javadir}/ant/ant-swing.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-swing.jar
ln -s %{_javadir}/ant/ant-trax.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-trax.jar
#ln -s %{_javadir}/ant/ant-weblogic.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-weblogic.jar
## END ANT ##

## BEGIN TOMCAT ##
rm plugins/org.eclipse.tomcat/commons-beanutils.jar
rm plugins/org.eclipse.tomcat/commons-collections.jar
rm plugins/org.eclipse.tomcat/commons-digester.jar
rm plugins/org.eclipse.tomcat/commons-logging-api.jar
rm plugins/org.eclipse.tomcat/commons-modeler.jar
rm plugins/org.eclipse.tomcat/jakarta-regexp-1.3.jar
rm plugins/org.eclipse.tomcat/servlet.jar
rm plugins/org.eclipse.tomcat/servlets-manager.jar
rm plugins/org.eclipse.tomcat/naming-common.jar
rm plugins/org.eclipse.tomcat/servlets-common.jar
rm plugins/org.eclipse.tomcat/tomcat-http11.jar
rm plugins/org.eclipse.tomcat/bootstrap.jar
rm plugins/org.eclipse.tomcat/catalina.jar
rm plugins/org.eclipse.tomcat/jasper-compiler.jar
rm plugins/org.eclipse.tomcat/jasper-runtime.jar
rm plugins/org.eclipse.tomcat/mx4j-jmx.jar
rm plugins/org.eclipse.tomcat/naming-resources.jar
rm plugins/org.eclipse.tomcat/naming-factory.jar
rm plugins/org.eclipse.tomcat/servlets-default.jar
rm plugins/org.eclipse.tomcat/servlets-invoker.jar
rm plugins/org.eclipse.tomcat/tomcat-coyote.jar
rm plugins/org.eclipse.tomcat/tomcat-util.jar
mkdir -p plugins/org.eclipse.tomcat/lib
ln -s %{tomcatsharedir}/bin/bootstrap.jar plugins/org.eclipse.tomcat/lib/bootstrap.jar
ln -s %{_javadir}/tomcat5/catalina.jar plugins/org.eclipse.tomcat/lib/catalina.jar
ln -s %{_javadir}/tomcat5/catalina-optional.jar plugins/org.eclipse.tomcat/lib/catalina-optional.jar
ln -s %{_javadir}/jasper5-compiler.jar plugins/org.eclipse.tomcat/lib/jasper-compiler.jar
ln -s %{_javadir}/jasper5-runtime.jar plugins/org.eclipse.tomcat/lib/jasper-runtime.jar
ln -s %{_javadir}/mx4j/mx4j.jar plugins/org.eclipse.tomcat/lib/mx4j.jar
ln -s %{_javadir}/mx4j/mx4j-impl.jar plugins/org.eclipse.tomcat/lib/mx4j-impl.jar
ln -s %{_javadir}/mx4j/mx4j-jmx.jar plugins/org.eclipse.tomcat/lib/mx4j-jmx.jar
ln -s %{_javadir}/tomcat5/naming-factory.jar plugins/org.eclipse.tomcat/lib/naming-factory.jar
ln -s %{_javadir}/tomcat5/naming-resources.jar plugins/org.eclipse.tomcat/lib/naming-resources.jar
ln -s %{_javadir}/tomcat5/servlets-default.jar plugins/org.eclipse.tomcat/lib/servlets-default.jar
ln -s %{_javadir}/tomcat5/servlets-invoker.jar plugins/org.eclipse.tomcat/lib/servlets-invoker.jar
ln -s %{_javadir}/tomcat5/tomcat-coyote.jar plugins/org.eclipse.tomcat/lib/tomcat-coyote.jar
ln -s %{_javadir}/tomcat5/tomcat-http.jar plugins/org.eclipse.tomcat/lib/tomcat-http.jar
ln -s %{_javadir}/tomcat5/tomcat-util.jar plugins/org.eclipse.tomcat/lib/tomcat-util.jar
build-jar-repository -s -p plugins/org.eclipse.tomcat/lib commons-beanutils
build-jar-repository -s -p plugins/org.eclipse.tomcat/lib commons-collections
build-jar-repository -s -p plugins/org.eclipse.tomcat/lib commons-dbcp
build-jar-repository -s -p plugins/org.eclipse.tomcat/lib commons-digester
build-jar-repository -s -p plugins/org.eclipse.tomcat/lib commons-digester-rss
build-jar-repository -s -p plugins/org.eclipse.tomcat/lib commons-el
build-jar-repository -s -p plugins/org.eclipse.tomcat/lib commons-fileupload
build-jar-repository -s -p plugins/org.eclipse.tomcat/lib commons-launcher
build-jar-repository -s -p plugins/org.eclipse.tomcat/lib commons-logging-api
build-jar-repository -s -p plugins/org.eclipse.tomcat/lib commons-modeler
build-jar-repository -s -p plugins/org.eclipse.tomcat/lib commons-pool
build-jar-repository -s -p plugins/org.eclipse.tomcat/lib jspapi
build-jar-repository -s -p plugins/org.eclipse.tomcat/lib regexp
build-jar-repository -s -p plugins/org.eclipse.tomcat/lib servletapi5
## END TOMCAT ##

JUNITVERSION=$(ls plugins | grep org.junit_3 | sed 's/org.junit_//')
build-jar-repository -s -p plugins/org.junit_$JUNITVERSION junit

rm plugins/org.junit4/junit.jar
ln -s %{_javadir}/junit4.jar plugins/org.junit4/junit.jar 

pushd plugins/org.eclipse.swt/Eclipse\ SWT\ PI/gtk/library
# /usr/lib -> /usr/lib64
sed --in-place "s:/usr/lib/:%{_libdir}/:g" build.sh
# (walluck) Fedora has a bug here, we should use java_home, not jvmdir
sed --in-place "s:-L\$(AWT_LIB_PATH):-L%{java_home}/jre/lib/%{_arch}:" make_linux.mak
popd

%if %{gcj_support}
find plugins -type f -name \*.xml -exec sed --in-place "s/\(<antcall target=\"build.index\".*\/>\)/<\!-- \1 -->/" "{}" \;
%endif

# the swt version is set to HEAD on ia64 but shouldn't be
# get swt version
SWT_MAJ_VER=$(grep maj_ver plugins/org.eclipse.swt/Eclipse\ SWT/common/library/make_common.mak | cut -f 2 -d =)
SWT_MIN_VER=$(grep min_ver plugins/org.eclipse.swt/Eclipse\ SWT/common/library/make_common.mak | cut -f 2 -d =)
SWT_VERSION=$SWT_MAJ_VER$SWT_MIN_VER
swt_frag_ver=$(grep v$SWT_VERSION plugins/org.eclipse.swt.gtk.linux.x86/build.xml | sed "s:.*<.*\"\(.*\)\"/>:\1:")
swt_frag_ver_ia64=$(grep "version\.suffix\" value=" plugins/org.eclipse.swt.gtk.linux.ia64/build.xml | sed "s:.*<.*\"\(.*\)\"/>:\1:")
sed --in-place "s/$swt_frag_ver_ia64/$swt_frag_ver/g" plugins/org.eclipse.swt.gtk.linux.ia64/build.xml \
                                                      assemble.org.eclipse.sdk.linux.gtk.ia64.xml \
                                                      features/org.eclipse.rcp/build.xml

# (walluck) I am not sure if this is a bug or not, but Fedora's
# (walluck) `uname -p' behaves differently from Mandriva's, so we
# (walluck) always use `uname -m' instead
pushd './plugins/org.eclipse.swt/Eclipse SWT PI/gtk/library'
%patch100 -p0
popd

# (walluck) Fedora has a bug here, we need to use the correct JAVA_HOME
%{__sed} --in-place 's,^JAVA_HOME =.*,JAVA_HOME = %{java_home},' plugins/org.eclipse.core.filesystem/natives/unix/linux/Makefile

# (anssi) JNIGenerator fails to run with
# [java] java.lang.NoClassDefFoundError: java.security.Security
# thus leaving ia64 and x86_64 with 32bit-only C source code.
# Setting fork="yes" seems to fix it. jvm is used to ensure correct
# jvm in fork mode.
%{__sed} --in-place 's,<java ,<java fork="true" jvm="%{java}" ,' plugins/org.eclipse.*/build.xml
%{__sed} --in-place 's,<java ,<java jvm="%{java}" ,' build.xml

## Nasty hack to get suppport for ppc64, sparc{,64} and alpha
%patch24 -p1
# there is only partial support for ppc64 so we have to remove this
# partial support to get the replacemnt hack to work
find -name \*ppc64\* | xargs rm -r
# remove ppc64 support from features/org.eclipse.platform.source/feature.xml
# replace ppc64 with a fake arch (ppc128) so we don't have duplicate ant targets
find -type f -name \*.xml -exec sed --in-place "s/\(rootFileslinux_gtk_\)ppc64/\1ppc128/g" "{}" \;
# remove org.eclipse.platform.source.linux.gtk.ppc64,3.2.0.v20060602-0010-gszCh-8eOaU1uKq
sed --in-place "s/,.\{38\}ppc64.*macosx/,org.eclipse.platform.source.macosx/g" features/org.eclipse.platform.source/build.xml
# replace final occurances with an existing arch
sed --in-place "s/ppc64/x86_64/g" features/org.eclipse.platform.source/build.xml
# Move all of the ia64 directories to ppc64 or sparc{,64} or alpha dirs and replace
# the ia64 strings with ppc64 etc.
%ifarch ppc64 sparc sparc64 alpha
  for f in $(find -name \*ia64\* | grep -v motif | grep -v ia64_32); do 
    mv $f $(echo $f | sed "s/ia64/%{_arch}/")
  done
  find -type f ! -name \*.java -a ! -name feature.xml -exec sed --in-place "s/ia64_32/@eye-eh-64_32@/g" "{}" \;
  find -type f ! -name \*.java -a ! -name feature.xml -exec sed --in-place "s/ia64/%{_arch}/g" "{}" \;
  find -type f ! -name \*.java -a ! -name feature.xml -exec sed --in-place "s/@eye-eh-64_32@/ia64_32/g" "{}" \;
%endif 

# remove jdt.apt.pluggable.core, jdt.compiler.tool and org.eclipse.jdt.compiler.apt as they require a JVM that supports Java 1.6
for plugin in jdt.apt.pluggable.core jdt.compiler.tool jdt.compiler.apt; do
  version=$(grep org.eclipse.$plugin plugins/org.eclipse.$plugin/build.xml | grep condition.property | cut -d _ -f 2-3 | cut -d \" -f 1)
  sed --in-place "s/org.eclipse.$plugin:0.0.0,$version,//" features/org.eclipse.jdt/build.xml
  linenum=$(grep -no $plugin features/org.eclipse.jdt/build.xml | cut -d : -f 1)
  sed --in-place -e "$linenum,$(expr $linenum + 4)d" features/org.eclipse.jdt/build.xml
# If we're build with IcedTea then we don't want to remove the plugins from the
# feature.xml because we will build these plugins after the main build. This
# allows us to produce 1.5 bytecode for all of the SDK except for the parts that
# explicitly use Java 1.6. This enables GCJ to work with Eclipse on all platforms. 
%if ! %{gcj_support}
  linenum=$(grep -no $plugin features/org.eclipse.jdt/feature.xml | cut -d : -f 1)
  sed --in-place -e "$(expr $linenum - 1),$(expr $linenum + 5)d" features/org.eclipse.jdt/feature.xml
%endif 
  linenum=$(grep -no "dir=\"plugins/org.eclipse.$plugin" assemble.org.eclipse.sdk.linux.gtk.%{eclipse_arch}.xml | cut -d : -f 1)
  sed --in-place -e "$linenum,$(expr $linenum + 2)d" assemble.org.eclipse.sdk.linux.gtk.%{eclipse_arch}.xml
  linenum=$(grep -no "value=\"org.eclipse.$plugin" assemble.org.eclipse.sdk.linux.gtk.%{eclipse_arch}.xml | cut -d : -f 1)
  sed --in-place -e "$(expr $linenum - 2),$(expr $linenum + 1)d" assemble.org.eclipse.sdk.linux.gtk.%{eclipse_arch}.xml
done

# link to the jsch jar
rm plugins/com.jcraft.jsch_0.1.31.jar
ln -s %{_javadir}/jsch.jar plugins/com.jcraft.jsch_0.1.31.jar

# link to the icu4j stuff
rm plugins/com.ibm.icu_3.6.1.v20070417.jar
ln -s %{_datadir}/eclipse/plugins/com.ibm.icu_3.6.1.v20070417.jar plugins/com.ibm.icu_3.6.1.v20070417.jar

# link to lucene
rm plugins/org.apache.lucene_1.9.1.v200706111724.jar
ln -s %{_javadir}/lucene.jar plugins/org.apache.lucene_1.9.1.v200706111724.jar
rm plugins/org.apache.lucene.analysis_1.9.1.v200706181610.jar
ln -s %{_javadir}/lucene-contrib/lucene-analyzers.jar plugins/org.apache.lucene.analysis_1.9.1.v200706181610.jar

# link to commons-logging
rm plugins/org.apache.commons.logging_1.0.4.v200706111724.jar
ln -s %{_javadir}/commons-logging.jar plugins/org.apache.commons.logging_1.0.4.v200706111724.jar

rm plugins/javax.servlet.jsp_2.0.0.v200706191603.jar
ln -s %{_javadir}/jsp.jar plugins/javax.servlet.jsp_2.0.0.v200706191603.jar

rm plugins/javax.servlet_2.4.0.v200706111738.jar
ln -s %{_javadir}/servlet.jar plugins/javax.servlet_2.4.0.v200706111738.jar

# link to commons-el
rm plugins/org.apache.commons.el_1.0.0.v200706111724.jar
ln -s %{_javadir}/commons-el.jar plugins/org.apache.commons.el_1.0.0.v200706111724.jar

rm plugins/org.apache.jasper_5.5.17.v200706111724.jar
ln -s %{_javadir}/jasper5.jar plugins/org.apache.jasper_5.5.17.v200706111724.jar

JETTYPLUGINVERSION=$(ls plugins | grep org.mortbay.jetty_5 | sed 's/org.mortbay.jetty_//')
rm plugins/org.mortbay.jetty_$JETTYPLUGINVERSION
ln -s %{_javadir}/jetty5/jetty5.jar plugins/org.mortbay.jetty_$JETTYPLUGINVERSION

# delete included jars
# https://bugs.eclipse.org/bugs/show_bug.cgi?id=170662
rm plugins/org.eclipse.swt.win32.win32.x86/swt.jar \
   plugins/org.eclipse.swt/extra_jars/exceptions.jar \
   plugins/org.eclipse.swt.tools/swttools.jar \
   plugins/org.eclipse.osgi/osgi/osgi.cmpn.jar \
   plugins/org.eclipse.osgi/osgi/osgi.core.jar \
   plugins/org.eclipse.osgi/supplement/osgi/osgi.jar

# make sure there are no jars left
JARS=""
for j in $(find -name \*.jar); do
  if [ ! -L $j ]; then
    JARS="$JARS $j"
  fi
done
if [ ! -z "$JARS" ]; then
    echo "These jars should be deleted and symlinked to system jars: $JARS"
    exit 1
fi

tar jxf %{SOURCE20}

%build
ORIGCLASSPATH=$CLASSPATH

# Bootstrapping:
# 1. Build ecj with gcj-built ecj ("javac")
# 2. Re-build ecj with output of 1.

# 1a. compile ecj with javac
%{ant} -DcompilerArg="-encoding ISO-8859-1 -nowarn" -buildfile jdtcoresrc/compilejdtcorewithjavac.xml

%if %{gcj_support}
  # 1b. Natively-compile ecj
  %{gcj} -fPIC -fjni -findirect-dispatch -shared -Wl,-Bsymbolic \
    -o jdtcoresrc/ecj.jar.so jdtcoresrc/ecj.jar
   
  %{gcj_dbtool} -n jdtcoresrc/ecj.db 30000
  %{gcj_dbtool} -a jdtcoresrc/ecj.db jdtcoresrc/ecj.jar{,.so}

  # To ensure we're not using any pre-compiled ecj on the build system, set this
  export ANT_OPTS="-Dgnu.gcj.precompiled.db.path=`pwd`/jdtcoresrc/ecj.db"
%endif

# 2. Use this ecj to rebuild itself
export CLASSPATH=`pwd`/jdtcoresrc/ecj.jar:$ORIGCLASSPATH
%{ant} -DcompilerArg="-encoding ISO-8859-1 -nowarn" -buildfile jdtcoresrc/compilejdtcore.xml

%if %{gcj_support}
  # Natively-compile it
  %{gcj} -fPIC -fjni -findirect-dispatch -shared -Wl,-Bsymbolic \
    -o ecj.jar.so ecj.jar
  %{gcj_dbtool} -n ecj.db 30000
  %{gcj_dbtool} -a ecj.db ecj.jar{,.so}
  export ANT_OPTS="-Dgnu.gcj.precompiled.db.path=`pwd`/ecj.db"
  
  # Remove old native bits
  rm jdtcoresrc/ecj.db jdtcoresrc/ecj.jar.so
%endif

# Build the rest of Eclipse
export CLASSPATH=`pwd`/ecj.jar:$ORIGCLASSPATH
export JAVA_HOME=%{java_home}
%{ant} \
  -Dnobootstrap=true \
  -DinstallOs=linux -DinstallWs=gtk -DinstallArch=%{eclipse_arch} \
  -Dlibsconfig=true -DjavacSource=1.5 -DjavacTarget=1.5 -DcompilerArg="-encoding ISO-8859-1 -nowarn"

# build 1.6 when building with IcedTea
SDK=$(cd eclipse && pwd)
mkdir -p home
homedir=$(cd home && pwd)
LAUNCHERVERSION=$(ls $SDK/plugins | grep equinox.launcher_ | sed 's/org.eclipse.equinox.launcher_//')

%if ! %{gcj_support}
for plugin in jdt.compiler.tool jdt.compiler.apt jdt.apt.pluggable.core; do
  pushd plugins/org.eclipse.$plugin
  %{java} -cp $SDK/plugins/org.eclipse.equinox.launcher_$LAUNCHERVERSION \
       org.eclipse.core.launcher.Main                    \
       -application org.eclipse.ant.core.antRunner       \
       build.update.jar                                  \
       -vmargs -Duser.home=$homedir
  popd
done
%endif

## Build the FileInitializer application
PDEPLUGINVERSION=$(ls $SDK/plugins | grep pde.build | sed 's/org.eclipse.pde.build_//')
pushd equinox-incubator
mkdir -p build

# This can go away when package build handles plugins (not just features)
echo "<project default=\"main\"><target name=\"main\"></target></project>" > build/assemble.org.eclipse.equinox.initializer.all.xml
echo "<project default=\"main\"><target name=\"main\"></target></project>" > build/package.org.eclipse.equinox.initializer.all.xml

%{java} -cp $SDK/plugins/org.eclipse.equinox.launcher_$LAUNCHERVERSION \
     -Duser.home=$homedir                              \
      org.eclipse.core.launcher.Main \
     -application org.eclipse.ant.core.antRunner       \
     -Dtype=plugin                                    \
     -Did=org.eclipse.equinox.initializer                   \
     -DsourceDirectory=$(pwd)                          \
     -DbaseLocation=$SDK \
     -Dbuilder=$SDK/plugins/org.eclipse.pde.build_$PDEPLUGINVERSION/templates/package-build  \
     -f $SDK/plugins/org.eclipse.pde.build_$PDEPLUGINVERSION/scripts/build.xml

pushd build/plugins/org.eclipse.equinox.initializer
%{java} -cp $SDK/plugins/org.eclipse.equinox.launcher_$LAUNCHERVERSION \
     -Duser.home=$homedir                              \
      org.eclipse.core.launcher.Main \
     -application org.eclipse.ant.core.antRunner       \
     -f build.xml build.update.jar
popd
popd

%install
rm -rf $RPM_BUILD_ROOT

# Get swt version
SWT_MAJ_VER=$(grep maj_ver plugins/org.eclipse.swt/Eclipse\ SWT/common/library/make_common.mak | cut -f 2 -d =)
SWT_MIN_VER=$(grep min_ver plugins/org.eclipse.swt/Eclipse\ SWT/common/library/make_common.mak | cut -f 2 -d =)
SWT_VERSION=$SWT_MAJ_VER$SWT_MIN_VER

# Some directories we need
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/links
install -d -m 755 $RPM_BUILD_ROOT%{_libdir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins
install -d -m 755 $RPM_BUILD_ROOT%{_libdir}/%{name}/features

# Explode the resulting SDK tarball
tar -C $RPM_BUILD_ROOT%{_datadir} -zxf result/linux-gtk-%{eclipse_arch}-sdk.tar.gz
cp launchertmp/eclipse $RPM_BUILD_ROOT%{_datadir}/eclipse
%ifarch ppc64 sparc sparc64 alpha
cp features/org.eclipse.platform/gtk/eclipse.ini $RPM_BUILD_ROOT%{_datadir}/eclipse
%endif

# Install 1.6 plugins when building with IcedTea
%if ! %{gcj_support}
for plugin in jdt.apt.pluggable.core jdt.compiler.tool jdt.compiler.apt; do
  cp plugins/org.eclipse.$plugin/org.eclipse.$plugin_*.jar $RPM_BUILD_ROOT%{_datadir}/eclipse/plugins
done
%endif

# Add a compatibility symlink to startup.jar
pushd $RPM_BUILD_ROOT%{_datadir}/%{name}
LAUNCHERNAME=$(ls plugins | grep equinox.launcher_)
ln -s plugins/$LAUNCHERNAME startup.jar
popd

# Install the file initializer app
cp equinox-incubator/org.eclipse.equinox.initializer/org.eclipse.equinox.initializer_*.jar \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins

# Install the Fedora Eclipse product plugin
unzip -qq -d $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins %{SOURCE4}

# Set up an extension location and a link file for the arch-specific dir
echo "path:$RPM_BUILD_ROOT%{_libdir}" > $RPM_BUILD_ROOT%{_datadir}/%{name}/links/fragments.link
echo "name=Eclipse Platform" > $RPM_BUILD_ROOT%{_libdir}/%{name}/.eclipseextension
echo "id=org.eclipse.platform" >> $RPM_BUILD_ROOT%{_libdir}/%{name}/.eclipseextension
echo "version=%{eclipse_majmin}.%{eclipse_micro}" >> $RPM_BUILD_ROOT%{_libdir}/%{name}/.eclipseextension

# Install the platform-specific fragments in an arch-specific dir
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/*%{eclipse_arch}* $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins

# platform.source has the launcher src zip which is platform-specific
PLATFORMSOURCEVERSION=$(ls $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins | grep platform.source_ | sed 's/org.eclipse.platform.source_//')
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/org.eclipse.platform.source_$PLATFORMSOURCEVERSION \
  $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins

# help.webapp generates web.xml with Apache Jakarta Tomcat JspC. This file is
# generated differently for different archs. FIXME investigate this.
HELPWEBAPPVERSION=$(ls $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins | grep help.webapp_ | sed 's/org.eclipse.help.webapp_//')
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/org.eclipse.help.webapp_$HELPWEBAPPVERSION \
  $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins

# update.core.linux is a fragment
# FIXME: make a patch for upstream to change to swt fragment notation
UPDATECORELINUXVERSION=$(ls $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins | grep update.core.linux_ | sed 's/org.eclipse.update.core.linux_//')
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/org.eclipse.update.core.linux_$UPDATECORELINUXVERSION \
  $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins

# FIXME: there is a problem with gjdoc generating different HTML on different
# architectures.
PLATFORMDOCISVVERSION=$(ls $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins | grep platform.doc.isv_ | sed 's/org.eclipse.platform.doc.isv_//')
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/org.eclipse.platform.doc.isv_$PLATFORMDOCISVVERSION \
  $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins
# ppc64 is problematic with these two
JDTDOCISVVERSION=$(ls $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins | grep jdt.doc.isv_ | sed 's/org.eclipse.jdt.doc.isv_//')
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/org.eclipse.jdt.doc.isv_$JDTDOCISVVERSION \
  $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins
PDEDOCUSERVERSION=$(ls $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins | grep pde.doc.user_ | sed 's/org.eclipse.pde.doc.user_//')
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/org.eclipse.pde.doc.user_$PDEDOCUSERVERSION \
  $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins

# Adding support for ppc64 and sparc{64} makes the rcp feature 
# have multilib conflicts
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/features/org.eclipse.rcp_* \
  $RPM_BUILD_ROOT%{_libdir}/%{name}/features

# FIXME: investigate why it doesn't work to set this -- configuration data is
# always written to /usr/share/eclipse/configuration, even with
#     -Dosgi.sharedConfiguration.area=$RPM_BUILD_ROOT%{_libdir}/%{name}/configuration
# Note (2006-12-05):  upon looking at this again, we (bkonrath, overholt) don't
# know what we're doing with $libdir_path :)  It requires some investigation.
# 
# Extract .so files
# https://bugs.eclipse.org/bugs/show_bug.cgi?id=90535
pushd $RPM_BUILD_ROOT
datadir_path=$(echo %{_datadir}/%{name} | sed -e 's/^\///')
libdir_path=$(echo %{_libdir}/%{name} | sed -e 's/^\///')
java -Dosgi.sharedConfiguration.area=$libdir_path/configuration \
     -cp $datadir_path/startup.jar \
     org.eclipse.core.launcher.Main \
     -consolelog \
     -application org.eclipse.equinox.initializer.configInitializer \
     -fileInitializer %{SOURCE19}
popd

# Make proper links file
echo "path:/usr/lib" > $RPM_BUILD_ROOT%{_datadir}/%{name}/links/fragments.link
echo "path:/usr/lib64" > $RPM_BUILD_ROOT%{_datadir}/%{name}/links/fragments64.link

# Install config.ini to an arch dependent location and remove the unnecessary
# configuration data
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/configuration $RPM_BUILD_ROOT%{_libdir}/%{name}
rm -r $RPM_BUILD_ROOT%{_libdir}/%{name}/configuration/org.eclipse.update
rm -r $RPM_BUILD_ROOT%{_libdir}/%{name}/configuration/org.eclipse.core.runtime
rm -r $RPM_BUILD_ROOT%{_libdir}/%{name}/configuration/org.eclipse.equinox.app

# Set eclipse.product to org.fedoraproject.ide.platform 
sed --in-place "s/plugins\/org.eclipse.platform/plugins\/org.fedoraproject.ide.platform/" \
  $RPM_BUILD_ROOT%{_libdir}/%{name}/configuration/config.ini
sed --in-place "s/eclipse.product=org.eclipse.sdk.ide/eclipse.product=org.fedoraproject.ide.platform.product/" \
  $RPM_BUILD_ROOT%{_libdir}/%{name}/configuration/config.ini

# Install the launcher so
LAUNCHERFRAGVERSION=$(ls $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins | grep equinox.launcher.gtk.linux.%{eclipse_arch}_ | sed "s/.*equinox.launcher.gtk.linux.*_//")
cp launchertmp/library/gtk/eclipse_*.so \
$RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/org.eclipse.equinox.launcher.gtk.linux.%{eclipse_arch}_$LAUNCHERFRAGVERSION

# Install the Eclipse binary wrapper
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/eclipse $RPM_BUILD_ROOT%{_libdir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
# (walluck) Fedora has a bug here, they want to use the binary
# (walluck) only, but then we lose the ability to configure it
%if 1
cp %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/eclipse
sed --in-place "s|@LIBDIR@|%{_libdir}|g" $RPM_BUILD_ROOT%{_bindir}/eclipse
ECLIPSELIBSUFFIX=$(ls $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/org.eclipse.equinox.launcher.gtk.linux*/*.so | sed "s/.*.launcher.gtk.linux.//")
sed --in-place "s|@ECLIPSELIBSUFFIX@|$ECLIPSELIBSUFFIX|" $RPM_BUILD_ROOT%{_bindir}/eclipse
%else
%{__perl} -pe \
  's|/usr/lib/eclipse/|%{_libdir}/%{name}/|g ;
   s|/etc/|%{_sysconfdir}/|g ;
   s|/usr/bin/|%{_bindir}/|g ;
   s|/usr/lib/|%{_libdir}/|g ;
   s|\@FIREFOX_DIR\@|%{firefox_dir}|g' \
  %{SOURCE1} > $RPM_BUILD_ROOT%{_bindir}/eclipse
chmod a+x $RPM_BUILD_ROOT%{_bindir}/eclipse
%endif

# Ensure the shared libraries have the correct permissions
pushd $RPM_BUILD_ROOT%{_libdir}/%{name} 
for lib in `find configuration -name \*.so`; do
   chmod 755 $lib
done

%if 0
# http://qa.mandriva.com/show_bug.cgi?id=21682
%{__rm} -r %{buildroot}%{_libdir}/%{name}/configuration/org.eclipse.osgi
%endif

# Create file listings for the extracted shared libraries
# (walluck) Fedora has a bug here, they forget to create this file
echo -n "" > %{_builddir}/%{buildsubdir}/%{libname}-gtk2.install;
echo -n "" > %{_builddir}/%{buildsubdir}/%{name}-platform.install;
for id in `ls configuration/org.eclipse.osgi/bundles`; do
  if [ "Xconfiguration" = $(echo X`find configuration/org.eclipse.osgi/bundles/$id -name libswt\*.so` | sed "s:/.*::") ]; then
    echo "%{_libdir}/%{name}/configuration/org.eclipse.osgi/bundles/$id" > %{_builddir}/%{buildsubdir}/%{libname}-gtk2.install;
  else
    echo "%{_libdir}/%{name}/configuration/org.eclipse.osgi/bundles/$id" >> %{_builddir}/%{buildsubdir}/%{name}-platform.install;
  fi
done 
popd

# Install symlinks to the SWT JNI shared libraries in /usr/lib/eclipse
pushd $RPM_BUILD_ROOT%{_libdir}/%{name}
for lib in $(find configuration -name libswt\*.so); do  
  ln -s %{_libdir}/%{name}/$lib `basename $lib`
done
popd

# (anssi) Other software depending on swt-gtk-3.2.jar load these too, so
# put them back in %{_libdir} too.
pushd $RPM_BUILD_ROOT%{_libdir}
for lib in $(find %{name}/configuration -name libswt\*.so); do
  ln -s %{_libdir}/$lib `basename $lib`
done
popd

# (anssi) Other software depends on swt-gtk-3.2.jar too, so put it in
# jnidir which is for arch-dependent jars.
# Install the SWT jar symlinks in jnidir
SWTJARVERSION=$(grep v$SWT_VERSION plugins/org.eclipse.swt.gtk.linux.%{eclipse_arch}/build.xml | sed "s:.*<.*\"\(.*\)\"/>:\1:")
install -d -m755 $RPM_BUILD_ROOT%{_jnidir}
pushd $RPM_BUILD_ROOT%{_jnidir}
ln -s %{_libdir}/%{name}/plugins/org.eclipse.swt.gtk.linux.%{eclipse_arch}_$SWTJARVERSION.jar swt-gtk-%{eclipse_majmin}.%{eclipse_micro}.jar
ln -s swt-gtk-%{eclipse_majmin}.%{eclipse_micro}.jar swt-gtk-%{eclipse_majmin}.jar
popd

# Install the eclipse-ecj.jar symlink for java-1.4.2-gcj-compat's "javac"
JDTCORESUFFIX=$(ls $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins | grep jdt.core_ | sed "s/org.eclipse.jdt.core_//")
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
ln -s %{_datadir}/%{name}/plugins/org.eclipse.jdt.core_$JDTCORESUFFIX $RPM_BUILD_ROOT%{_javadir}/eclipse-ecj.jar
ln -s %{_javadir}/eclipse-ecj.jar $RPM_BUILD_ROOT%{_javadir}/jdtcore.jar
# (walluck) Fedora doesn't do this, but I think we need it for
# (walluck) JPackage compatibility
ln -s %{_javadir}/eclipse-ecj.jar $RPM_BUILD_ROOT%{_javadir}/ecj.jar

# FIXME: get rid of this by putting logic in package build to know what version
#        of pde.build it's using
# Install a versionless pde.build
pushd $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/
ln -s org.eclipse.pde.build_* org.eclipse.pde.build
popd

# Icons
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
ln -s %{_datadir}/%{name}/plugins/org.fedoraproject.ide.platform/eclipse48.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
ln -s %{_datadir}/%{name}/plugins/org.fedoraproject.ide.platform/eclipse32.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps
ln -s ../../../../%{name}/plugins/org.fedoraproject.ide.platform/eclipse.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pixmaps
ln -s %{_datadir}/icons/hicolor/48x48/apps/%{name}.png $RPM_BUILD_ROOT%{_datadir}/pixmaps
%ifarch %{ix86} x86_64
# Remove unused icon.xpm
# see https://bugs.eclipse.org/bugs/show_bug.cgi?id=86848
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/icon.xpm
%endif

# Install the efj wrapper script 
install -p -D -m0755 %{SOURCE17} $RPM_BUILD_ROOT%{_bindir}/efj
%{__sed} --in-place -e "s:startup.jar:%{_datadir}/%{name}/startup.jar:;" -e "s:@gccsuffix@:$(readlink -f %{java} | %{__sed} 's,^.*gij,,'):;" %{buildroot}%{_bindir}/efj

# Install the ecj wrapper script
install -p -D -m0755 %{SOURCE18} $RPM_BUILD_ROOT%{_bindir}/ecj
%{__sed} --in-place -e "s:@JAVADIR@:%{_javadir}:;" -e "s:@gccsuffix@:$(readlink -f %{java} | %{__sed} 's,^.*gij,,'):;" %{buildroot}%{_bindir}/ecj

# A sanity check.
desktop-file-validate %{SOURCE2}

# freedesktop.org menu entry
install -p -D -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

# Create a script that can be used to make a symlink tree of the
# eclipse platform.
cp %{SOURCE16} copy-platform
(
  cd $RPM_BUILD_ROOT%{_datadir}/%{name}
  ls -d * | egrep -v '^(plugins|features|links|about_files)$'
  ls -d plugins/* features/* links/*
) |
sed -e's/^\(.*\)$/\1 \1/' -e's,^,ln -s $eclipse/,' >> copy-platform

mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/buildscripts
cp copy-platform $RPM_BUILD_ROOT%{_datadir}/%{name}/buildscripts

pushd $RPM_BUILD_ROOT%{_datadir}/%{name}
## BEGIN ANT ##
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-antlr.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-apache-bcel.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-apache-bsf.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-apache-log4j.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-apache-oro.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-apache-regexp.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-apache-resolver.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-commons-logging.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-commons-net.jar
#rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-jai.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-javamail.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-jdepend.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-jmf.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-jsch.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-junit.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-launcher.jar
#rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-netrexx.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-nodeps.jar
#rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-starteam.jar
#rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-stylebook.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-swing.jar
rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-trax.jar
#rm plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-weblogic.jar
# FIXME:  use build-jar-repository
# (walluck) Unlike Fedora, Mandriva ships both ant-bsf and
# (walluck) ant-commons-net, as well as ant-jmf
ln -s %{_javadir}/ant/ant-antlr.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-antlr.jar
ln -s %{_javadir}/ant/ant-apache-bcel.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-apache-bcel.jar
ln -s %{_javadir}/ant/ant-apache-bsf.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-apache-bsf.jar
ln -s %{_javadir}/ant/ant-apache-log4j.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-apache-log4j.jar
ln -s %{_javadir}/ant/ant-apache-oro.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-apache-oro.jar
ln -s %{_javadir}/ant/ant-apache-regexp.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-apache-regexp.jar
ln -s %{_javadir}/ant/ant-apache-resolver.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-apache-resolver.jar
ln -s %{_javadir}/ant/ant-commons-logging.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-commons-logging.jar
# https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=180642
# the symlinks that are commented-out are not currently shipped on Fedora
ln -s %{_javadir}/ant/ant-commons-net.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-commons-net.jar
#ln -s %{_javadir}/ant/ant-jai.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-jai.jar
ln -s %{_javadir}/ant.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant.jar
ln -s %{_javadir}/ant/ant-javamail.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-javamail.jar
ln -s %{_javadir}/ant/ant-jdepend.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-jdepend.jar
ln -s %{_javadir}/ant/ant-jmf.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-jmf.jar
ln -s %{_javadir}/ant/ant-jsch.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-jsch.jar
ln -s %{_javadir}/ant/ant-junit.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-junit.jar
ln -s %{_javadir}/ant-launcher.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-launcher.jar
#ln -s %{_javadir}/ant/ant-netrexx.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-netrexx.jar
ln -s %{_javadir}/ant/ant-nodeps.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-nodeps.jar
#ln -s %{_javadir}/ant/ant-starteam.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-starteam.jar
#ln -s %{_javadir}/ant/ant-stylebook.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-stylebook.jar
ln -s %{_javadir}/ant/ant-swing.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-swing.jar
ln -s %{_javadir}/ant/ant-trax.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-trax.jar
#ln -s %{_javadir}/ant/ant-weblogic.jar plugins/org.apache.ant_1.7.0.v200706080842/lib/ant-weblogic.jar
## END ANT ##

## BEGIN TOMCAT ##
TOMCATPLUGINVERSION=$(ls plugins | grep tomcat | sed 's/org.eclipse.tomcat_//')
mkdir -p plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib
ln -s %{tomcatsharedir}/bin/bootstrap.jar plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib/bootstrap.jar
ln -s %{_javadir}/tomcat5/catalina.jar plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib/catalina.jar
ln -s %{_javadir}/tomcat5/catalina-optional.jar plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib/catalina-optional.jar
ln -s %{_javadir}/jasper5-compiler.jar plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib/jasper-compiler.jar
ln -s %{_javadir}/jasper5-runtime.jar plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib/jasper-runtime.jar
ln -s %{_javadir}/mx4j/mx4j.jar plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib/mx4j.jar
ln -s %{_javadir}/mx4j/mx4j-impl.jar plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib/mx4j-impl.jar
ln -s %{_javadir}/mx4j/mx4j-jmx.jar plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib/mx4j-jmx.jar
ln -s %{_javadir}/tomcat5/naming-factory.jar plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib/naming-factory.jar
ln -s %{_javadir}/tomcat5/naming-resources.jar plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib/naming-resources.jar
ln -s %{_javadir}/tomcat5/servlets-default.jar plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib/servlets-default.jar
ln -s %{_javadir}/tomcat5/servlets-invoker.jar plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib/servlets-invoker.jar
ln -s %{_javadir}/tomcat5/tomcat-coyote.jar plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib/tomcat-coyote.jar
ln -s %{_javadir}/tomcat5/tomcat-http.jar plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib/tomcat-http.jar
ln -s %{_javadir}/tomcat5/tomcat-util.jar plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib/tomcat-util.jar
build-jar-repository -s -p plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib commons-beanutils
build-jar-repository -s -p plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib commons-collections
build-jar-repository -s -p plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib commons-dbcp
build-jar-repository -s -p plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib commons-digester
build-jar-repository -s -p plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib commons-digester-rss
build-jar-repository -s -p plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib commons-el
build-jar-repository -s -p plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib commons-fileupload
build-jar-repository -s -p plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib commons-launcher
build-jar-repository -s -p plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib commons-logging-api
build-jar-repository -s -p plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib commons-modeler
build-jar-repository -s -p plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib commons-pool
build-jar-repository -s -p plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib jspapi
build-jar-repository -s -p plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib regexp
build-jar-repository -s -p plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib servletapi5
## END TOMCAT ##

JETTYPLUGINVERSION=$(ls plugins | grep org.mortbay.jetty_5 | sed 's/org.mortbay.jetty_//')
rm plugins/org.mortbay.jetty_$JETTYPLUGINVERSION
ln -s %{_javadir}/jetty5/jetty5.jar plugins/org.mortbay.jetty_$JETTYPLUGINVERSION

build-jar-repository -s -p plugins/org.junit_* junit

rm plugins/org.junit4_4.3.1/junit.jar
ln -s %{_javadir}/junit4.jar plugins/org.junit4_4.3.1/junit.jar

# link to the jsch jar
rm plugins/com.jcraft.jsch_0.1.31.jar
ln -s %{_javadir}/jsch.jar plugins/com.jcraft.jsch_0.1.31.jar

# link to the icu4j stuff
rm plugins/com.ibm.icu_3.6.1.v20070417.jar

# link to lucene
rm plugins/org.apache.lucene_1.9.1.v200706111724.jar
ln -s %{_javadir}/lucene.jar plugins/org.apache.lucene_1.9.1.v200706111724.jar
rm plugins/org.apache.lucene.analysis_1.9.1.v200706181610.jar
ln -s %{_javadir}/lucene-contrib/lucene-analyzers.jar plugins/org.apache.lucene.analysis_1.9.1.v200706181610.jar

# link to commons-logging
rm plugins/org.apache.commons.logging_1.0.4.v200706111724.jar
ln -s %{_javadir}/commons-logging.jar plugins/org.apache.commons.logging_1.0.4.v200706111724.jar

# link to commons-el
rm plugins/org.apache.commons.el_1.0.0.v200706111724.jar
ln -s %{_javadir}/commons-el.jar plugins/org.apache.commons.el_1.0.0.v200706111724.jar

popd

# (walluck) I am not sure why this supposedly works on Fedora and
# (walluck) fails on Mandriva before even one iteration.
%if 0
# Ensure that the zip files are the same across all builds.
# This is needed to make these package multilib compatible.
# FIXME: this needs to be re-written as a separate program
# warning: big hack!
mkdir -p ${RPM_BUILD_ROOT}/tmp
for zip in `find ${RPM_BUILD_ROOT}%{_datadir}/%{name} -type f -name \*.zip -o -type f -name \*.jar`; do
  # unpack every zip, set the date of the files and directories and repack the zip
  ZIPNAME=`basename $zip`
  TMPDIR=`mktemp -d -p ${RPM_BUILD_ROOT}/tmp $ZIPNAME.tmpdir.XXXXXXXXXX` 
  ZIPDIR=`mktemp -d -p ${RPM_BUILD_ROOT}/tmp $ZIPNAME.zipdir.XXXXXXXXXX`        
  
  pushd $TMPDIR 
  unzip -qq -o $zip
  rm -f $zip    

  # check if there are jars or zips inside the zip or jar
  zipsinside=`find $TMPDIR -type f -name \*.zip -o -name \*.jar`
  if [ -n "$zipsinside" ]; then
     for zip2 in $zipsinside; do
       # unpack every zip, set the date of the files and directories and repack the zip
       ZIPNAME2=`basename $zip2`
       TMPDIR2=`mktemp -d -p ${RPM_BUILD_ROOT}/tmp $ZIPNAME2.tmpdir.XXXXXXXXXX`
       ZIPDIR2=`mktemp -d -p ${RPM_BUILD_ROOT}/tmp $ZIPNAME2.zipdir.XXXXXXXXXX`

       pushd $TMPDIR2
       unzip -qq -o $zip2
       rm -f $zip2

       # create the directories first
       for d in `find -type d | LC_ALL=C sort`; do
         mkdir -p $ZIPDIR2/$d
       done
       # move the contents over to the a new directory in order and set the times. 
       for f in `find -type f | LC_ALL=C sort`; do
         cp $f $ZIPDIR2/$f
         touch --date="1980-01-01 UTC" $ZIPDIR2/$f
       done
       popd

       # Set the times of the directories.
       touch --date="1980-01-01 UTC" `find $ZIPDIR2 -type d`

       # make the new zip
       pushd $ZIPDIR2
       find -type f -print | LC_ALL=C sort | /usr/bin/zip -q -X -9 $zip2 -@
       popd

       # Cleanup.
       rm -rf $TMPDIR2
       rm -rf $ZIPDIR2
     done
  fi 
  
  # now on to the original zip or jar.
  # create the directories first
  for d in `find -type d | LC_ALL=C sort`; do
    mkdir -p $ZIPDIR/$d
  done 
  # move the contents over to the a new directory in order and set the times. 
  for f in `find -type f | LC_ALL=C sort`; do 
    cp $f $ZIPDIR/$f
    touch --date="1980-01-01 UTC" $ZIPDIR/$f
  done
  popd

  # Set the times of the directories.
  touch --date="1980-01-01 UTC" `find $ZIPDIR -type d`

  # make the new zip
  pushd $ZIPDIR
  find -type f -print | LC_ALL=C sort | /usr/bin/zip -q -X -9 $zip -@
  popd

  # Cleanup.
  rm -rf $TMPDIR
  rm -rf $ZIPDIR
done
rm -rf ${RPM_BUILD_ROOT}/tmp
%endif

# (walluck) Fedora doesn't do this, but we have to link in our
# (walluck) own scripts
pushd plugins/org.apache.ant_*/bin
for i in ant antRun; do
  test -e $i && %{__rm} $i && %{__ln_s} %{_bindir}/$i $i || exit 1
done
popd

# (walluck) Fedora has some problem here, but (1) Mandriva doesn't
# (walluck) automatically compile .py files (they probably should)
# (walluck) and (2) I don't understand why only this file would
# (walluck) create the multilib conflict
%if 0
pushd $RPM_BUILD_ROOT%{_datadir}/%{name}
# remove this python script so that it is not aot compiled, thus avoiding a
# multilib conflict
ANTPLUGINVERSION=$(ls plugins | grep org.apache.ant_ | sed 's/org.apache.ant_//')
rm plugins/org.apache.ant_$ANTPLUGINVERSION/bin/runant.py
%endif

# FIXME: (walluck) Our ui.ide directory doesn't have a version
# FIXME: (walluck) after it---so UIIDEPLUGINVERSION is empty
%if %{gcj_support}
# exclude org.eclipse.ui.ide to work around
# https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=175547
UIIDEPLUGINVERSION=$(ls plugins | grep ui.ide_ | sed 's/org.eclipse.ui.ide_//')
if [ -n "$UIIDEPLUGINVERSION" ]; then
%ifnarch ia64
%{_bindir}/aot-compile-rpm --exclude %{_datadir}/%{name}/plugins/org.eclipse.ui.ide_$UIIDEPLUGINVERSION
%else
OSGIPLUGINVERSION=$(ls plugins | grep osgi_ | sed 's/org.eclipse.osgi_//')
%{_bindir}/aot-compile-rpm --exclude %{_datadir}/%{name}/plugins/org.eclipse.ui.ide_$UIIDEPLUGINVERSION \
                --exclude %{_datadir}/%{name}/plugins/org.eclipse.osgi_$OSGIPLUGINVERSION
%endif
else
%{_bindir}/aot-compile-rpm
fi

rm %{buildroot}%{_libdir}/gcj/eclipse/org.eclipse.ui.ide*

%endif
%if 0
popd
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post platform
%if %{gcj_support}
%{update_gcjdb}
%endif
%{update_desktop_database}
%update_icon_cache hicolor

%postun platform
%if %{gcj_support}
%{clean_gcjdb}
%endif
%{update_desktop_database}
%update_icon_cache hicolor

%if %{gcj_support}
%post ecj
%{update_gcjdb}

%postun ecj
%{clean_gcjdb}

%post -n %{libname}-gtk2
%{update_gcjdb}

%postun -n %{libname}-gtk2
%{clean_gcjdb}

%post rcp
%{update_gcjdb}

%postun rcp
%{clean_gcjdb}

%post jdt
%{update_gcjdb}

%postun jdt
%{clean_gcjdb}

%post pde
%{update_gcjdb}

%postun pde
%{clean_gcjdb}

%post pde-runtime
%{update_gcjdb}

%postun pde-runtime
%{clean_gcjdb}
%endif

%files ecj
%defattr(-,root,root)
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/org.eclipse.jdt.core_*
%{_javadir}/ecj.jar
%{_javadir}/eclipse-ecj.jar
%{_javadir}/jdtcore.jar
%{_bindir}/ecj
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/org.eclipse.jdt.core_*
%endif

%files -n %{libname}-gtk2 -f %{libname}-gtk2.install
%defattr(-,root,root)
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_libdir}/libswt-*.so
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/libswt-*.so
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/configuration
%if 1
%dir %{_libdir}/%{name}/configuration/org.eclipse.osgi
%dir %{_libdir}/%{name}/configuration/org.eclipse.osgi/bundles
%endif
%{_datadir}/%{name}/plugins/org.eclipse.swt_*
%{_libdir}/%{name}/plugins/org.eclipse.swt.gtk.linux.%{eclipse_arch}_*
# FIXME: do we need to build?
#%{_libdir}/%{name}/libcairo-swt.so
%{_jnidir}/swt-gtk*.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/org.eclipse.swt.gtk.linux.%{eclipse_arch}_*
%endif

%files rcp
%defattr(-,root,root)
%dir %{_datadir}/%{name}/features
%dir %{_libdir}/%{name}/features
%{_libdir}/%{name}/configuration/org.eclipse.osgi/.bundledata*
%{_libdir}/%{name}/configuration/org.eclipse.osgi/.lazy*
%{_libdir}/%{name}/configuration/org.eclipse.osgi/.manager
%{_libdir}/%{name}/configuration/org.eclipse.osgi/.state*
%{_libdir}/%{name}/configuration/config.ini
%{_libdir}/%{name}/.eclipseextension
%{_datadir}/%{name}/.eclipseproduct
%{_datadir}/%{name}/notice.html
%{_datadir}/%{name}/epl-v10.html
%{_datadir}/%{name}/links
%{_datadir}/%{name}/startup.jar
%ifarch %{ix86} x86_64
%{_datadir}/%{name}/about.html
%endif
%ifarch x86_64
%{_datadir}/%{name}/about_files
%endif
%{_datadir}/%{name}/readme
%{_libdir}/%{name}/features/org.eclipse.rcp_*
%{_datadir}/%{name}/plugins/org.eclipse.core.commands_*
%{_datadir}/%{name}/plugins/org.eclipse.core.contenttype_*
%{_datadir}/%{name}/plugins/org.eclipse.core.databinding_*
%{_datadir}/%{name}/plugins/org.eclipse.core.databinding.beans_*
%{_datadir}/%{name}/plugins/org.eclipse.core.expressions_*
%{_datadir}/%{name}/plugins/org.eclipse.core.jobs_*
%{_datadir}/%{name}/plugins/org.eclipse.core.runtime_*
%{_datadir}/%{name}/plugins/org.eclipse.core.runtime.compatibility.auth_*
%{_datadir}/%{name}/plugins/org.eclipse.equinox.app_*
%{_datadir}/%{name}/plugins/org.eclipse.equinox.common_*
%{_datadir}/%{name}/plugins/org.eclipse.equinox.launcher_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.launcher.gtk.linux.%{eclipse_arch}_*
%{_datadir}/%{name}/plugins/org.eclipse.equinox.preferences_*
%{_datadir}/%{name}/plugins/org.eclipse.equinox.registry_*
%{_datadir}/%{name}/plugins/org.eclipse.help_*
%{_datadir}/%{name}/plugins/org.eclipse.jface_*
%{_datadir}/%{name}/plugins/org.eclipse.jface.databinding_*
%{_datadir}/%{name}/plugins/org.eclipse.osgi_*
%{_datadir}/%{name}/plugins/org.eclipse.rcp_*
%{_datadir}/%{name}/plugins/org.eclipse.swt_*
%{_datadir}/%{name}/plugins/org.eclipse.ui_*
%{_datadir}/%{name}/plugins/org.eclipse.ui.workbench_*
%{_datadir}/%{name}/plugins/org.eclipse.update.configurator_*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/org.eclipse.update.configurator_*
%ifnarch ia64
%{_libdir}/gcj/%{name}/org.eclipse.osgi_*
%endif
%{_libdir}/gcj/%{name}/org.eclipse.equinox.registry_*
%{_libdir}/gcj/%{name}/org.eclipse.equinox.launcher_*
%{_libdir}/gcj/%{name}/org.eclipse.equinox.app_*
%{_libdir}/gcj/%{name}/org.eclipse.jface_*
%{_libdir}/gcj/%{name}/org.eclipse.jface.databinding_*
%{_libdir}/gcj/%{name}/org.eclipse.core.commands_*
%{_libdir}/gcj/%{name}/org.eclipse.core.runtime.compatibility.auth_*
%{_libdir}/gcj/%{name}/org.eclipse.ui.workbench_*
%{_libdir}/gcj/%{name}/org.eclipse.core.jobs_*
%{_libdir}/gcj/%{name}/org.eclipse.ui_*
%{_libdir}/gcj/%{name}/org.eclipse.core.runtime_*
%{_libdir}/gcj/%{name}/org.eclipse.equinox.preferences_*
%{_libdir}/gcj/%{name}/org.eclipse.core.expressions_*
%{_libdir}/gcj/%{name}/org.eclipse.equinox.common_*
%{_libdir}/gcj/%{name}/org.eclipse.help_*
%{_libdir}/gcj/%{name}/org.eclipse.core.contenttype_*
%{_libdir}/gcj/%{name}/org.eclipse.core.databinding_*
%{_libdir}/gcj/%{name}/org.eclipse.core.databinding.beans_*
%endif

%files cvs-client
%{_datadir}/%{name}/plugins/org.eclipse.team.cvs.core_*
%{_datadir}/%{name}/plugins/org.eclipse.cvs_*
%{_datadir}/%{name}/plugins/org.eclipse.team.cvs.ssh2_*
%{_datadir}/%{name}/plugins/org.eclipse.team.cvs.ssh_*
%{_datadir}/%{name}/plugins/org.eclipse.team.cvs.ui_*
%{_datadir}/%{name}/features/org.eclipse.cvs_*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/org.eclipse.team.cvs.core_*
%{_libdir}/gcj/%{name}/org.eclipse.team.cvs.ssh_*
%{_libdir}/gcj/%{name}/org.eclipse.team.cvs.ssh2_*
%{_libdir}/gcj/%{name}/org.eclipse.team.cvs.ui_*
%endif

%files platform -f %{name}-platform.install
%defattr(-,root,root)
%attr(0755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}/eclipse.ini
%{_libdir}/%{name}/eclipse
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/icons/*/*/apps/*
%{_datadir}/%{name}/features/org.eclipse.platform_*
%{_datadir}/%{name}/plugins/com.jcraft.jsch_*
%{_datadir}/%{name}/plugins/javax.servlet_*
%{_datadir}/%{name}/plugins/javax.servlet.jsp_*
%{_datadir}/%{name}/plugins/org.apache.ant_*
%{_datadir}/%{name}/plugins/org.apache.commons.el_*
%{_datadir}/%{name}/plugins/org.apache.commons.logging_*
%{_datadir}/%{name}/plugins/org.apache.jasper_*
%{_datadir}/%{name}/plugins/org.apache.lucene_*
%{_datadir}/%{name}/plugins/org.apache.lucene.analysis_*
%{_datadir}/%{name}/plugins/org.eclipse.ant.core_*
%{_datadir}/%{name}/plugins/org.eclipse.compare_*
%{_datadir}/%{name}/plugins/org.eclipse.core.boot_*
%{_datadir}/%{name}/plugins/org.eclipse.core.filebuffers_*
%{_datadir}/%{name}/plugins/org.eclipse.core.filesystem_*
%{_datadir}/%{name}/plugins/org.fedoraproject.ide.platform
%ifarch %{ix86} x86_64 ppc
%{_libdir}/%{name}/plugins/org.eclipse.core.filesystem.linux.%{eclipse_arch}_*
%endif
%{_datadir}/%{name}/plugins/org.eclipse.core.net_*
%{_datadir}/%{name}/plugins/org.eclipse.core.resources_*
%{_datadir}/%{name}/plugins/org.eclipse.core.resources.compatibility_*
%{_datadir}/%{name}/plugins/org.eclipse.core.runtime.compatibility_*
%{_datadir}/%{name}/plugins/org.eclipse.core.runtime.compatibility.registry_*
%{_datadir}/%{name}/plugins/org.eclipse.core.variables_*
%{_datadir}/%{name}/plugins/org.eclipse.debug.core_*
%{_datadir}/%{name}/plugins/org.eclipse.debug.ui_*
%{_datadir}/%{name}/plugins/org.eclipse.equinox.http.jetty_*
%{_datadir}/%{name}/plugins/org.eclipse.equinox.http.registry_*
%{_datadir}/%{name}/plugins/org.eclipse.equinox.http.servlet_*
%{_datadir}/%{name}/plugins/org.eclipse.equinox.jsp.jasper_*
%{_datadir}/%{name}/plugins/org.eclipse.equinox.jsp.jasper.registry_*
%{_datadir}/%{name}/plugins/org.eclipse.help.appserver_*
%{_datadir}/%{name}/plugins/org.eclipse.help.base_*
%{_datadir}/%{name}/plugins/org.eclipse.help.ui_*
%{_libdir}/%{name}/plugins/org.eclipse.help.webapp_*
%{_datadir}/%{name}/plugins/org.eclipse.jface.text_*
%{_datadir}/%{name}/plugins/org.eclipse.jsch.core_*
%{_datadir}/%{name}/plugins/org.eclipse.jsch.ui_*
%{_datadir}/%{name}/plugins/org.eclipse.ltk.core.refactoring_*
%{_datadir}/%{name}/plugins/org.eclipse.ltk.ui.refactoring_*
%{_datadir}/%{name}/plugins/org.eclipse.osgi.services_*
%{_datadir}/%{name}/plugins/org.eclipse.osgi.util_*
%{_datadir}/%{name}/plugins/org.eclipse.platform_*
%{_datadir}/%{name}/plugins/org.eclipse.platform.doc.user_*
%{_datadir}/%{name}/plugins/org.eclipse.search_*
%{_datadir}/%{name}/plugins/org.eclipse.team.core_*
%{_datadir}/%{name}/plugins/org.eclipse.team.ui_*
%{_datadir}/%{name}/plugins/org.eclipse.text_*
%{_datadir}/%{name}/plugins/org.eclipse.tomcat_*
%{_datadir}/%{name}/plugins/org.eclipse.ui.browser_*
%{_datadir}/%{name}/plugins/org.eclipse.ui.cheatsheets_*
%{_datadir}/%{name}/plugins/org.eclipse.ui.console_*
%{_datadir}/%{name}/plugins/org.eclipse.ui.editors_*
%{_datadir}/%{name}/plugins/org.eclipse.ui.externaltools_*
%{_datadir}/%{name}/plugins/org.eclipse.ui.forms_*
%{_datadir}/%{name}/plugins/org.eclipse.ui.ide_*
%{_datadir}/%{name}/plugins/org.eclipse.ui.ide.application_*
%{_datadir}/%{name}/plugins/org.eclipse.ui.intro_*
%{_datadir}/%{name}/plugins/org.eclipse.ui.intro.universal_*
%{_datadir}/%{name}/plugins/org.eclipse.ui.navigator_*
%{_datadir}/%{name}/plugins/org.eclipse.ui.navigator.resources_*
%{_datadir}/%{name}/plugins/org.eclipse.ui.net_*
%{_datadir}/%{name}/plugins/org.eclipse.ui.presentations.r21_*
%{_datadir}/%{name}/plugins/org.eclipse.ui.views_*
%{_datadir}/%{name}/plugins/org.eclipse.ui.views.properties.tabbed_*
%{_datadir}/%{name}/plugins/org.eclipse.ui.workbench.compatibility_*
%{_datadir}/%{name}/plugins/org.eclipse.ui.workbench.texteditor_*
%{_datadir}/%{name}/plugins/org.eclipse.update.core_*
%{_libdir}/%{name}/plugins/org.eclipse.update.core.linux_*
%{_datadir}/%{name}/plugins/org.eclipse.update.scheduler_*
%{_datadir}/%{name}/plugins/org.eclipse.update.ui_*
%{_datadir}/%{name}/plugins/org.mortbay.jetty_*
%{_datadir}/%{name}/plugins/org.eclipse.equinox.initializer_*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/javax.servlet_*
%{_libdir}/gcj/%{name}/javax.servlet.jsp_*
%{_libdir}/gcj/%{name}/org.apache.jasper_*
%{_libdir}/gcj/%{name}/org.eclipse.ant.core_*
%{_libdir}/gcj/%{name}/org.eclipse.compare_*
%{_libdir}/gcj/%{name}/org.eclipse.core.filebuffers_*
%{_libdir}/gcj/%{name}/org.eclipse.core.filesystem_*
%{_libdir}/gcj/%{name}/org.eclipse.core.net_*
%{_libdir}/gcj/%{name}/org.eclipse.core.resources_*
%{_libdir}/gcj/%{name}/org.eclipse.core.resources.compatibility_*
%{_libdir}/gcj/%{name}/org.eclipse.core.runtime.compatibility_*
%{_libdir}/gcj/%{name}/org.eclipse.core.variables_*
%{_libdir}/gcj/%{name}/org.eclipse.debug.core_*
%{_libdir}/gcj/%{name}/org.eclipse.debug.ui_*
%{_libdir}/gcj/%{name}/org.eclipse.equinox.http.jetty_*
%{_libdir}/gcj/%{name}/org.eclipse.equinox.http.servlet_*
%{_libdir}/gcj/%{name}/org.eclipse.equinox.jsp.jasper_*
%{_libdir}/gcj/%{name}/org.eclipse.equinox.jsp.jasper.registry_*
%{_libdir}/gcj/%{name}/org.eclipse.help.appserver_*
%{_libdir}/gcj/%{name}/org.eclipse.help.base_*
%{_libdir}/gcj/%{name}/org.eclipse.help.ui_*
%{_libdir}/gcj/%{name}/org.eclipse.help.webapp_*
%{_libdir}/gcj/%{name}/org.eclipse.jface.text_*
%{_libdir}/gcj/%{name}/org.eclipse.jsch.core_*
%{_libdir}/gcj/%{name}/org.eclipse.jsch.ui_*
%{_libdir}/gcj/%{name}/org.eclipse.ltk.core.refactoring_*
%{_libdir}/gcj/%{name}/org.eclipse.ltk.ui.refactoring_*
%{_libdir}/gcj/%{name}/org.eclipse.osgi.services_*
%{_libdir}/gcj/%{name}/org.eclipse.osgi.util_*
%{_libdir}/gcj/%{name}/org.eclipse.search_*
%{_libdir}/gcj/%{name}/org.eclipse.team.core_*
%{_libdir}/gcj/%{name}/org.eclipse.team.ui_*
%{_libdir}/gcj/%{name}/org.eclipse.text_*
%{_libdir}/gcj/%{name}/org.eclipse.ui.browser_*
%{_libdir}/gcj/%{name}/org.eclipse.ui.cheatsheets_*
%{_libdir}/gcj/%{name}/org.eclipse.ui.console_*
%{_libdir}/gcj/%{name}/org.eclipse.ui.editors_*
%{_libdir}/gcj/%{name}/org.eclipse.ui.externaltools_*
%{_libdir}/gcj/%{name}/org.eclipse.ui.forms_*
# FIXME
#%{_libdir}/gcj/%{name}/org.eclipse.ui.ide.application_*
%{_libdir}/gcj/%{name}/org.eclipse.ui.intro_*
%{_libdir}/gcj/%{name}/org.eclipse.ui.navigator_*
%{_libdir}/gcj/%{name}/org.eclipse.ui.navigator.resources_*
%{_libdir}/gcj/%{name}/org.eclipse.ui.net_*
%{_libdir}/gcj/%{name}/org.eclipse.ui.presentations.r21_*
%{_libdir}/gcj/%{name}/org.eclipse.ui.views_*
%{_libdir}/gcj/%{name}/org.eclipse.ui.views.properties.tabbed_*
%{_libdir}/gcj/%{name}/org.eclipse.ui.workbench.texteditor_*
%{_libdir}/gcj/%{name}/org.eclipse.update.core_*
%{_libdir}/gcj/%{name}/org.eclipse.update.scheduler_*
%{_libdir}/gcj/%{name}/org.eclipse.update.ui_*
%{_libdir}/gcj/%{name}/compatibility.*
%{_libdir}/gcj/%{name}/org.eclipse.equinox.http.registry_*
%{_libdir}/gcj/%{name}/org.eclipse.equinox.initializer_*
%{_libdir}/gcj/%{name}/platform.jar.*
%{_libdir}/gcj/%{name}/runtime_registry_compatibility.jar.*
%{_libdir}/gcj/%{name}/tomcatwrapper.jar.*
%{_libdir}/gcj/%{name}/universal.jar.*
%endif

%files jdt
%defattr(-,root,root)
%{_bindir}/efj
%{_datadir}/%{name}/features/org.eclipse.jdt_*
%{_datadir}/%{name}/plugins/org.eclipse.ant.ui_*
%{_datadir}/%{name}/plugins/org.junit_*
%{_datadir}/%{name}/plugins/org.eclipse.jdt.junit_*
%{_datadir}/%{name}/plugins/org.eclipse.jdt.doc.user_*
%{_datadir}/%{name}/plugins/org.eclipse.jdt.apt.core_*
%{_datadir}/%{name}/plugins/org.eclipse.jdt.ui_*
%{_datadir}/%{name}/plugins/org.eclipse.jdt.debug_*
%{_datadir}/%{name}/plugins/org.eclipse.jdt.junit4.runtime_*
%{_datadir}/%{name}/plugins/org.junit4_*
%{_datadir}/%{name}/plugins/org.eclipse.jdt_*
%{_datadir}/%{name}/plugins/org.eclipse.jdt.launching_*
%{_datadir}/%{name}/plugins/org.eclipse.jdt.core.manipulation_*
%{_datadir}/%{name}/plugins/org.eclipse.jdt.apt.ui_*
%{_datadir}/%{name}/plugins/org.eclipse.jdt.junit.runtime_*
%{_datadir}/%{name}/plugins/org.eclipse.jdt.debug.ui_*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/org.eclipse.ant.ui_*
%{_libdir}/gcj/%{name}/org.eclipse.jdt.apt.core_*
%{_libdir}/gcj/%{name}/org.eclipse.jdt.ui_*
%{_libdir}/gcj/%{name}/org.eclipse.jdt.junit4.runtime_*
%{_libdir}/gcj/%{name}/org.eclipse.jdt.junit.runtime_*
%{_libdir}/gcj/%{name}/org.eclipse.jdt.junit_*
%{_libdir}/gcj/%{name}/org.eclipse.jdt.launching_*
%{_libdir}/gcj/%{name}/org.eclipse.jdt.core.manipulation_*
%{_libdir}/gcj/%{name}/org.eclipse.jdt.apt.ui_*
%{_libdir}/gcj/%{name}/org.eclipse.jdt.debug.ui_*
%{_libdir}/gcj/%{name}/jdimodel.jar.*
%{_libdir}/gcj/%{name}/jdi.jar.*
%else
%{_datadir}/%{name}/plugins/org.eclipse.jdt.apt.pluggable.core_*
%{_datadir}/%{name}/plugins/org.eclipse.jdt.compiler.apt_*
%{_datadir}/%{name}/plugins/org.eclipse.jdt.compiler.tool_*
%endif

%files pde
%defattr(-,root,root)
%{_datadir}/%{name}/features/org.eclipse.sdk_*
%{_datadir}/%{name}/features/org.eclipse.pde_*
%{_datadir}/%{name}/features/org.eclipse.pde.source_*
%{_libdir}/%{name}/plugins/org.eclipse.pde.doc.user_*
%{_datadir}/%{name}/plugins/org.eclipse.pde.build_*
%{_datadir}/%{name}/plugins/org.eclipse.pde.build
%{_datadir}/%{name}/plugins/org.eclipse.pde_*
%{_datadir}/%{name}/plugins/org.eclipse.pde.core_*
%{_datadir}/%{name}/plugins/org.eclipse.pde.junit.runtime_*
%{_datadir}/%{name}/plugins/org.eclipse.pde.ui_*
%{_datadir}/%{name}/plugins/org.eclipse.pde.ui.templates_*
%{_datadir}/%{name}/features/org.eclipse.rcp.source_*
%{_libdir}/%{name}/plugins/org.eclipse.rcp.source.linux.gtk.%{eclipse_arch}*
%{_datadir}/%{name}/plugins/org.eclipse.rcp.source_*
%{_datadir}/%{name}/plugins/org.eclipse.pde.source_*
%{_datadir}/%{name}/features/org.eclipse.cvs.source_*
%{_datadir}/%{name}/plugins/org.eclipse.cvs.source_*
%{_datadir}/%{name}/plugins/org.eclipse.sdk_*
%{_datadir}/%{name}/features/org.eclipse.jdt.source_*
%{_libdir}/%{name}/plugins/org.eclipse.jdt.doc.isv_*
%{_datadir}/%{name}/plugins/org.eclipse.jdt.source_*
%{_datadir}/%{name}/plugins/org.junit.source_*
%{_datadir}/%{name}/features/org.eclipse.platform.source_*
%{_datadir}/%{name}/plugins/javax.servlet.jsp.source_*
%{_datadir}/%{name}/plugins/javax.servlet.source_*
%{_datadir}/%{name}/plugins/org.apache.ant.source_*
%{_datadir}/%{name}/plugins/org.apache.commons.el.source_*
%{_datadir}/%{name}/plugins/org.apache.commons.logging.source_*
%{_datadir}/%{name}/plugins/org.apache.jasper.source_*
%{_datadir}/%{name}/plugins/org.apache.lucene.analysis.source_*
%{_datadir}/%{name}/plugins/org.apache.lucene.source_*
%{_libdir}/%{name}/plugins/org.eclipse.platform.doc.isv_*
%{_libdir}/%{name}/plugins/org.eclipse.platform.source_*
%{_libdir}/%{name}/plugins/org.eclipse.platform.source.linux.gtk.%{eclipse_arch}_*
%{_datadir}/%{name}/plugins/org.mortbay.jetty.source_*
%{_datadir}/%{name}/buildscripts
%if %{gcj_support}
%{_libdir}/gcj/%{name}/org.eclipse.pde_*
%{_libdir}/gcj/%{name}/org.eclipse.pde.core_*
%{_libdir}/gcj/%{name}/org.eclipse.pde.junit.runtime_*
%{_libdir}/gcj/%{name}/org.eclipse.pde.ui_*
%{_libdir}/gcj/%{name}/org.eclipse.pde.ui.templates_*
%{_libdir}/gcj/%{name}/org.eclipse.platform.doc.isv_*
%{_libdir}/gcj/%{name}/pdebuild.jar*
%{_libdir}/gcj/%{name}/pdebuild-ant.jar*
%endif

%files pde-runtime
%defattr(-,root,root)
%{_datadir}/%{name}/plugins/org.eclipse.pde.runtime_*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/org.eclipse.pde.runtime_*
%endif
